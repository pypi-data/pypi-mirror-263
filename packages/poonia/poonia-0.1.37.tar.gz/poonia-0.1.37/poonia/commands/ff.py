#!/usr/bin/env python3
import base64
import contextlib
import datetime
import functools
import io
import json
import locale
import math
import operator
import os
import pathlib
import re
import subprocess
import sys
import tempfile
import time
import urllib
import uuid
import xml
import itertools
import collections
from contextlib import contextmanager
from functools import reduce
import concurrent.futures

import click


class Utils(object):
    @staticmethod
    def where(program):
        import os
        import sys

        if sys.platform == "win32" and not program.lower().endswith(".exe"):
            program += ".exe"

        def is_exe(fpath):
            return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

        fpath, fname = os.path.split(program)
        if fpath:
            if is_exe(program):
                return program
        else:
            for path in os.environ["PATH"].split(os.pathsep):
                path = path.strip('"')
                exe_file = os.path.join(path, program)
                if is_exe(exe_file):
                    return exe_file
        return None

    @classmethod
    def require_exe(cls, exe):
        if not cls.where(exe):
            click.secho("error: cannot find executable '%s'" %
                        exe, fg='red', bold=True, err=True)
            sys.exit(1)

    @staticmethod
    def parallel(lst, func, progressbar=None, show_pos=False, max_workers=None):
        max_workers = max_workers or os.cpu_count() or 4
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers or os.cpu_count() or 4) as executor:
            with contextlib.ExitStack() as c:
                if max_workers == 1:
                    items = map(lambda x: (x, func(x)), lst)
                else:
                    items = executor.map(lambda x: (x, func(x)), lst)
                if progressbar:
                    item_count = None
                    try:
                        item_count = len(lst)
                    except:
                        pass
                    items = c.enter_context(click.progressbar(items, length=item_count, label=progressbar, show_pos=show_pos, file=sys.stderr))
                for item in items:
                    yield item


def natural_sort_key(s, _nsre=re.compile('([0-9]+)')):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(_nsre, s)]


@click.group(help="FFMPEG helpers")
def ff():
    Utils.require_exe('ffmpeg')
    Utils.require_exe('ffprobe')


def group_by(key, seq):
    return dict(reduce(lambda grp, val: grp[key(val)].append(val) or grp, seq, collections.defaultdict(list)))


def get_in(obj, *keys):
    for k in keys:
        v = None
        try:
            v = operator.itemgetter(k)(obj)
        except (TypeError, KeyError):
            pass
        if v is None:
            return None
        obj = v
    return obj


def sget_in(obj, *keys):
    r = get_in(obj, *keys)
    if r is None:
        return ''
    return str(r)


def re_find_all_groups(regexp, s):
    return [m.groupdict() for m in re.finditer(regexp, s)]


def parse_stream_filters(filter, default_action='-'):
    filters = re_find_all_groups(
        r'(?P<type>[vas])(?P<action>\+|\-)(?P<text>[^+\s]+)', filter)
    filters = group_by(operator.itemgetter('type'), filters)

    actions_per_type = {t: set(f['action'] for f in fs)
                        for t, fs in filters.items()}
    if any(1 for _, a in actions_per_type.items() if len(a) > 1):
        click.secho(
            'You can use only one filter action type (+ or -) per stream type!', fg='red', err=True)
        sys.exit(1)
    actions_per_type = {t: list(f)[0] for t, f in actions_per_type.items()}

    def _filter(stream_type, *identifiers):
        stream_type_id = stream_type[:1]
        action = actions_per_type.get(stream_type_id, default_action)
        if action == '-':
            for f in filters.get(stream_type_id, []):
                if f['text'] in identifiers:
                    return False
            return True
        else:
            for f in filters.get(stream_type_id, []):
                if f['text'] in identifiers:
                    return True
            return False
    return _filter


def parse_default_filters(filter):
    filters = re_find_all_groups(r'(?P<type>[vas])\!(?P<text>\w+)', filter)
    filters = group_by(operator.itemgetter('type'), filters)
    type_index = {}

    def _filter(stream_type, language, index):
        stream_type_id = stream_type[:1]
        if stream_type_id in type_index:
            return type_index[stream_type_id] == index
        for f in filters.get(stream_type_id, []):
            if f['text'] == language:
                type_index[stream_type_id] = index
                return True
        return False
    return _filter


def sizeof_fmt(num, suffix='B'):
    num = float(num)
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


class FFPROBE(object):
    FFPROBE_CMD = 'ffprobe -hide_banner -loglevel fatal -show_error -show_format -show_streams -show_programs -show_chapters -show_private_data -print_format json --'

    @classmethod
    def probe_file(cls, filename):
        try:
            filename = filename.encode(locale.getpreferredencoding())
            r = subprocess.check_output(
                cls.FFPROBE_CMD.split(' ') + [filename], stderr=subprocess.STDOUT)
            return json.loads(r.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            return {'error': str(e.output)}
        return {}

    @classmethod
    def contains_video_audio(cls, filename):
        probe = cls.probe_file(filename)
        streams = get_in(probe, 'streams') or []
        return any(s for s in streams if s.get('codec_type') == 'video'),\
            any(s for s in streams if s.get('codec_type') == 'audio')

    MEDIA_EXTENSIONS = {'.aac', '.alac', '.aif', '.aifc', '.aiff', '.dsf', '.flac', '.mka', '.mkv',
                        '.ape', '.mp3', '.mp4', '.m4a', '.m4b', '.m4v', '.mpc', '.ogg', '.opus', '.wma', '.wv', '.wav'}

    @classmethod
    def is_media_file(cls, filename):
        _, ext = os.path.splitext(filename)
        return ext.lower() in cls.MEDIA_EXTENSIONS

    @classmethod
    def get_tags(cls, filename):
        probe = cls.probe_file(filename)
        tags = probe.get('format', {}).get('tags', {})
        return {k.lower(): v for k, v in tags.items()}

    @classmethod
    def get_framerate(cls, filename):
        def parse_frame_rate(framerate):
            matches = re.findall(r'^(\d+)/(\d+)$', framerate)
            if not matches:
                return None
            a, b = matches[0]
            if int(b) == 0:
                return 0
            return int(a) / float(b)

        probe = cls.probe_file(filename)
        fps = [get_in(stream, 'r_frame_rate')
               for stream in get_in(probe, 'streams')]
        fps = [parse_frame_rate(f) for f in fps]
        fps = [f for f in fps if f]
        return fps[0] if fps else None


def safe_filename(s):
    s = re.sub(r'(\w)(: +)', r'\1 - ', s)
    for c in '/\\:':
        s = s.replace(c, '-')
    s = s.replace('"', "'")
    for c in '?<>|*':
        s = s.replace(c, '_')
    return s.strip()


def escape_cmd(s):
    return "'%s'" % s if ' ' in s else s


def format_seconds(s):
    d = '%.2f' % (s % 1)
    return time.strftime(r'%H:%M:%S', time.gmtime(s)) + d.lstrip('0')


extract_formats = {
    'hdmv_pgs_subtitle': 'sup',
    'subrip': 'srt',
    'aac': 'aac',
    'opus': 'opus'
}


def escape_video_filter_param(s):
    return s.replace('[', r'\[').replace(']', r'\]')


def find_external_subtitles(filename):
    from pprint import pprint
    pprint(filename)


@ff.command(help='FFMPEG stream operations')
@click.argument('input', nargs=-1, type=click.Path(exists=True))
@click.option('-f', '--filters', default='', help='Filter streams by language (eg. "s+eng a-ger")')
@click.option('--print', 'print_', is_flag=True, help='Print ffmpeg commands')
@click.option('--apply', is_flag=True, help='Run conversion')
@click.option('--hardsub', is_flag=True, help='Run conversion')
@click.option('--force-stereo', is_flag=True, help="Convert 5.1 audio streams to stereo")
@click.option('-c:a', 'acodec', type=click.Choice(['mp3', 'aac', 'opus']), help="Audio codec")
@click.option('-b:a', 'abitrate', type=str, help="Audio bitrate", default='96k')
@click.option('-c:v', 'vcodec', type=click.Choice(['hevc', 'avc']), help="Video codec")
@click.option('--width', type=int, help="Resize video to specified width")
@click.option('-b:v', 'vbitrate', type=str, help="Video bitrate", default='')
@click.option('--crf', default=28, help='Sets quality when converting video')
@click.option('-hw', '--hardware', is_flag=True, help='Use hardware video encoding')
@click.option('-extsub', '--external-subtitles', is_flag=True, help='Find subtitles in external file')
def sel(input, filters, print_, apply, hardsub, force_stereo, acodec, abitrate, vcodec, vbitrate, width, crf, hardware, external_subtitles):
    # from pprint import pprint; pprint(input)
    # files = [f for f in os.listdir(input) if os.path.isfile(f) and not f.startswith('.')] if os.path.isdir(input) else [input]
    files = [f for f in input]
    output = []

    for f in files:
        if external_subtitles:
            find_external_subtitles(f)

        stream_filter = parse_stream_filters(filters)
        default_filter = parse_default_filters(filters)
        hw_cli = []
        if hardware:
            if sys.platform.startswith('linux'):
                hw_cli = ['-hwaccel', 'auto']
            elif sys.platform.startswith('windows') or sys.latform == 'cygwin':
                hw_cli = ['-hwaccel', 'dxva2']
        cmd = ['ffmpeg'] + hw_cli
        cmd += ['-i', f, '-c', 'copy']

        probe = FFPROBE.probe_file(f)
        if not print_:
            click.secho(f, bold=True, nl=False)
            click.secho(' (%s)' % sizeof_fmt(
                get_in(probe, 'format', 'size') or 0), fg='yellow')
        if not get_in(probe, 'streams'):
            continue

        streams = []
        default_streams = collections.defaultdict(dict)
        input_stream_counter = collections.defaultdict(lambda: -1)
        for s in get_in(probe, 'streams'):
            # video, audio, subtitle, attachment
            s_type = get_in(s, 'codec_type')
            s_lang = sget_in(s, 'tags', 'language')
            s_index = get_in(s, 'index')
            input_stream_counter[s_type] += 1
            s_index_type = input_stream_counter[s_type]
            s_default = bool(get_in(s, 'disposition', 'default'))

            keep = stream_filter(
                s_type, *filter(bool, [s_lang, get_in(s, 'channel_layout')]))
            mark_default = default_filter(
                s_type, s_lang, s_index) if keep else False
            streams.append([s, keep, mark_default, s_index_type])
            if mark_default:
                default_streams[s_type][True] = s_index
            if s_default and not mark_default:
                default_streams[s_type][False] = s_index
        to_undefault = [s[False] for _, s in default_streams.items() if s.get(
            True) and s.get(False)]

        output_stream_counter = collections.defaultdict(lambda: -1)
        vfilter = []
        if width:
            vfilter += ['scale=%i:trunc(ow/a/2)*2' % width]
        for s, keep, mark_default, s_index_type in streams:
            s_type = get_in(s, 'codec_type')
            s_info = ''
            if s_type == 'video':
                s_info = '%sx%s' % (get_in(s, 'width'), get_in(s, 'height'))
            elif s_type == 'audio':
                s_info = '%s' % (get_in(s, 'channel_layout'),)
            if get_in(s, 'disposition', 'default'):
                s_info = (s_info + ' default').strip()
            s_index = get_in(s, 'index')
            s_codec = get_in(s, 'codec_name')
            s_lang = sget_in(s, 'tags', 'language')
            unmark_default = s_index in to_undefault

            t = ('  ' if keep else ' -') + \
                '%i %s %s %s %s' % (s_index, s_type, s_codec, s_info, s_lang)
            if not print_:
                click.secho(t, fg=('white' if keep else 'red'), nl=False)
                if mark_default:
                    click.secho(' + DEFAULT', fg='green')
                elif unmark_default:
                    click.secho(' - DEFAULT', fg='red')
                else:
                    click.echo()
            if keep:
                if not (hardsub and mark_default and s_type == 'subtitle'):
                    cmd += ['-map', '0:%i' % s_index]
                output_stream_counter[s_type] += 1
                if force_stereo and s_type == 'audio' and get_in(s, 'channel_layout') not in ('stereo', 'mono'):
                    cmd += [
                        '-filter:a:%i' % output_stream_counter[s_type],
                        'pan=stereo|FL < 1.0*FL + 0.707*FC + 0.707*BL|FR < 1.0*FR + 0.707*FC + 0.707*BR'
                    ] if get_in(s, 'channel_layout') == '5.1' else [
                        '-ac:a:%i' % output_stream_counter[s_type],
                        '2'
                    ]
                    cmd += [
                        '-c:a:%i' % output_stream_counter[s_type], acodec or 'aac',
                        '-b:a:%i' % output_stream_counter[s_type], abitrate
                    ]
                elif acodec:
                    cmd += [
                        '-c:a:%i' % output_stream_counter[s_type], acodec or 'aac',
                        '-b:a:%i' % output_stream_counter[s_type], abitrate
                    ]
                if s_type == 'video' and vcodec:
                    cmd += [
                        '-c:v', 'hevc_videotoolbox' if vcodec == 'hevc' else 'h264_videotoolbox' if (
                            hardware and sys.platform == 'darwin') else 'libx265' if vcodec == 'hevc' else 'libx264',
                        '-preset', 'fast'
                    ]
                    cmd += ['-b:v', '%s' %
                            vbitrate] if vbitrate else ['-crf', '%d' % crf]
                if unmark_default:
                    cmd += [
                        '-disposition:%s:%i' % (s_type[0],
                                                output_stream_counter[s_type]), '0'
                    ]
                elif hardsub and mark_default and s_type == 'subtitle':
                    vfilter += [
                        'subtitles=%s:si=%i' % (
                            escape_video_filter_param(f), s_index_type)
                    ]
                elif mark_default:
                    cmd += [
                        '-disposition:%s:%i' % (s_type[0],
                                                output_stream_counter[s_type]), 'default'
                    ]
        base, ext = os.path.splitext(f)
        if vfilter:
            cmd += ['-vf', ', '.join(vfilter)]
        cmd += ['out__%s%s' % (base, ext)]

        output_command = ' '.join((escape_cmd(c) for c in cmd))
        output += [output_command]
        if print_:
            click.echo(output_command)

    if apply:
        click.confirm('Do you want to continue?', abort=True)
        for cmd in output:
            os.system(cmd)


@contextmanager
def temp_with_content(content, dir=None, suffix=None):
    fd, path = tempfile.mkstemp(dir=dir, suffix=suffix)
    try:
        with os.fdopen(fd, 'wb') as tmp:
            tmp.write(content.encode('utf-8'))
            tmp.flush()
        yield path
    finally:
        os.remove(path)


def random_name(ext='.bin'):
    return uuid.uuid4().hex + ext


@ff.command(help='Edit metadata')
@click.argument('input', type=click.Path(exists=True, dir_okay=False, readable=True))
@click.argument('output', type=click.Path(exists=False, dir_okay=False, writable=True), required=False)
def meta(input, output=None):
    meta = subprocess.check_output([
        'ffmpeg', '-i', input, '-f', 'ffmetadata', '-'
    ], stderr=None)
    replace_input_file = output is None
    _, input_ext = os.path.splitext(input)
    output = output or random_name(input_ext)

    has_video, has_audio = FFPROBE.contains_video_audio(input)
    if not (has_video or has_audio):
        click.echo('error: file contains no streams')
        sys.exit(1)
    mapping = [] + (['-map', '1:v'] if has_video else []) + \
        (['-map', '1:a'] if has_audio else [])

    edited_meta = click.edit(meta.decode('utf-8'))
    if edited_meta is not None:
        with temp_with_content(edited_meta) as meta_file:
            click.secho(meta_file, fg='green', bold=True)
            subprocess.check_output([
                'ffmpeg', '-i', meta_file, '-i', input, '-map_metadata', '0'] + mapping + ['-codec', 'copy', output
                                                                                           ], stderr=None)
        if replace_input_file:
            os.remove(input)
            os.rename(output, input)

class FFMPEGMeta(object):
    @classmethod
    def read(cls, filename):
        meta = subprocess.check_output([
            'ffmpeg', '-i', filename, '-f', 'ffmetadata', '-'
        ], stderr=subprocess.PIPE)
        return cls.parse(meta.decode('utf-8'))

    @staticmethod
    def parse(s):
        if not s.startswith(';FFMETADATA1\n'):
            return None
        out = [collections.OrderedDict()]
        append_next_line = False
        for x in s.split('\n')[1:]:
            if append_next_line:
                if not x.endswith('\\'):
                    append_next_line = False
                else:
                    x = x[:-1]
                next(reversed(out[-1].values())).append(x.replace('\\=', '='))
            else:
                if x == '[CHAPTER]':
                    out.append(collections.OrderedDict())
                elif '=' in x:
                    if x.endswith('\\'):
                        append_next_line = True
                        x = x[:-1]
                    key, val = x.split('=', 1)
                    out[-1][key] = [val.replace('\\=', '=')]
        for ch in out:
            for k, v in ch.items():
                ch[k] = '\n'.join(v)
        return out
    
    @staticmethod
    def milliseconds_to_timestamp(milliseconds):
        seconds, milliseconds = divmod(milliseconds, 1000)
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02d}:{seconds:02d}:{milliseconds/(1000/75):.0f}"

    @classmethod
    def to_cue(cls, meta, filename):
        common = meta[0]
        out = []
        if 'artist' in common:
            artist = common.get("artist").replace('"', "''")
            out += [f'PERFORMER "{artist}"']
        if 'album' in common or 'title' in common:
            title = common.get('album') or common.get('title').replace('"', "''")
            out += [f'TITLE "{title}"']
        out += [f'FILE "{filename}" WAVE']
        for n, ch in enumerate(meta[1:], 1):
            out += [f'  TRACK {n:02d} AUDIO']
            if 'title' in ch:
                title = ch["title"].replace('"', "''")
                out += [f'    TITLE "{title}"']
            if ch.get('TIMEBASE') == '1/1000':
               out += [f'    INDEX 01 {cls.milliseconds_to_timestamp(int(ch.get("START")))}']
        return '\n'.join(out)

    @staticmethod
    def to_str(meta):
        def escape_val(k, v):
            vlines = list(e.replace('=', '\\=') for e in v.split('\n'))
            vlines = list(f'{e}\\' for e in vlines[:-1]) + vlines[-1:]
            vlines = [f'{k}={e}' for e in vlines[:1]] + vlines[1:]
            return vlines
        lines = [';FFMETADATA1']
        if meta:
            for k, v in meta[0].items():
                if v:
                    lines += escape_val(k, v)
            for chapter in meta[1:]:
                lines.append('[CHAPTER]')
                for k, v in chapter.items():
                    if v:
                        lines += escape_val(k, v)
        return '\n'.join(lines)


@ff.command(help='Change tag in multiple files')
@click.argument('tag', nargs=1, required=True)
@click.argument('input', type=click.Path(exists=True, dir_okay=False, readable=True), nargs=-1)
@click.option('--from-tag', help='if value is empty take from another tag')
@click.option('--from-filename', is_flag=True, help='if value is empty take filename')
@click.option('--replace-if-empty', help='if value is empty take this value')
@click.option('--force-replace', help='take this value')
@click.option('--yes', '-y', help='do not ask for confirmation')
def tag(tag, input, from_tag, from_filename, replace_if_empty, force_replace, yes):
    def analyse(filename):
        has_video, has_audio = FFPROBE.contains_video_audio(filename)
        if not (has_video or has_audio):
            click.echo(f"error: file '{filename}' has no streams", err=True)
            sys.exit(1)
        meta = subprocess.check_output([
            'ffmpeg', '-i', filename, '-f', 'ffmetadata', '-'
        ], stderr=subprocess.PIPE)
        decoded = FFMPEGMeta.parse(meta.decode('utf-8'))
        return has_video, has_audio, decoded

    input_data = {}
    for filename, (has_video, has_audio, decoded) in Utils.parallel(input, analyse, progressbar='reading files', show_pos=True, max_workers=(1 if not yes else None)):
        original_tag = decoded[0].get(tag, '')
        v = original_tag
        if not v and from_tag:
            v = decoded[0].get(from_tag, '')
        if not v and from_filename:
            name, _ = os.path.splitext(os.path.basename(filename))
            v = name
        if not v and replace_if_empty:
            v = replace_if_empty
        if force_replace:
            v = force_replace
        input_data[filename] = (decoded, original_tag, v, has_video, has_audio)

    lines = []
    for filename, (_, _, val, _, _) in input_data.items():
        lines.append(f"={filename}")
        lines.append(val)
    lines = '\n'.join(lines)
    changed = click.edit(lines)
    if not changed:
        sys.exit()

    fn = ''
    changes = {}
    for line in changed.rstrip().split('\n'):
        if line.startswith('='):
            fn = line[1:]
        else:
            changes[fn] = f"{changes.get(fn)}\n{line}" if fn in changes else line
    changes = {k:(input_data[k][1], v) for k,v in changes.items() if k in input_data and input_data[k][1] != v}

    for fn, (old_tag, new_tag) in changes.items():
        click.echo(f'{fn}: ', err=True, nl=False)
        click.secho(f'{old_tag}', err=True, nl=False, fg='bright_red')
        click.echo(' -> ', err=True, nl=False)
        click.secho(f'{new_tag}', err=True, fg='bright_green')

    if not yes:
        click.confirm('\ndo you want to continue')
    for filename, (old_tag, new_tag) in changes.items():
        meta, _, _, has_video, has_audio = input_data[filename]
        _, input_ext = os.path.splitext(filename)
        mapping = [] + (['-map', '1:v'] if has_video else []) + \
            (['-map', '1:a'] if has_audio else [])
        meta[0][tag] = new_tag
        edited_meta = FFMPEGMeta.to_str(meta)
        click.secho(filename, fg='green', bold=True)
        output = random_name(input_ext)
        with temp_with_content(edited_meta) as meta_file:
            subprocess.check_output([
                'ffmpeg', '-i', meta_file, '-i', filename, '-map_metadata', '0'] + mapping + ['-codec', 'copy', output], stderr=subprocess.PIPE)
        os.remove(filename)
        os.rename(output, filename)


@ff.command(help='Make cue from chapters')
@click.argument('input', type=click.Path(exists=True, dir_okay=False, readable=True))
def cue(input):
    meta = FFMPEGMeta.read(input)
    if not meta:
        sys.exit(1)
    click.echo(FFMPEGMeta.to_cue(meta, filename=os.path.basename(input)))

def find_first_file(rootdir, names):
    to_find = set(e.lower() for e in names)
    candidates = []
    for subdir, _, files in os.walk(rootdir):
        candidates += list((f.lower(), os.path.join(subdir, f)) for f in files if f.lower() in to_find)
    candidates.sort(key=lambda e: e[1].count(os.path.sep))
    for n in names:
        found = next((path for (f, path) in candidates if f == n.lower()), None)
        if found:
            return found

@ff.command(help='Merge audio files')
@click.argument('input', type=click.Path(exists=True, dir_okay=False, readable=True), nargs=-1, required=True)
@click.option('--output', '-o', type=click.Path(exists=False, dir_okay=False, writable=True))
def merge(input, output):
    def get_meta(filename):
        meta = FFPROBE.probe_file(filename)
        duration = float(meta['streams'][0]['duration'])
        chapters = meta.get('chapters', [])
        tags = meta.get('format', {}).get('tags', {})
        tags = {
            'artist': tags.get('artist'),
            'title': tags.get('title'),
            'date': tags.get('date')
        }
        return duration, chapters, tags
    
    common_dir = os.path.commonpath(os.path.abspath(f) for f in input)
    basedir = os.path.basename(common_dir)
    if not output:
        output = f'_{basedir}.m4a'
    output_dir, output_file = os.path.dirname(output), os.path.basename(output)
    nochap_output = os.path.join(output_dir, f'nochap_{output_file}')
    cover = find_first_file(common_dir, [f'{n}.{e}' for n in ['cover', 'front', 'folder'] for e in ['jpg', 'jpeg', 'png']])
    concat_file = ''
    chapter_file = ''
    escape = lambda s: s.replace("'", "'\\''")
    start = 0.0
    artist, date, album = None, None, None
    for fn, (duration, chapters, tags) in Utils.parallel(sorted(input, key=natural_sort_key), get_meta):
        if artist is None:
            artist = tags.get('artist')
        if date is None:
            date = tags.get('date')
        if album is None:
            album = tags.get('album')
        concat_file += f"file '{escape(fn)}'\n"
        end = start + duration
        base, _ = os.path.splitext(os.path.basename(fn))
        title = tags.get('title') or base
        chapter_file += f"[CHAPTER]\nTIMEBASE=1/1000\nSTART={start*1000:.0f}\nEND={end*1000:.0f}\ntitle={title}\n"
        start = end
    album = album or basedir
    meta_file = f''';FFMETADATA
album={album}
artist={artist}
date={date}
{chapter_file}'''

    with temp_with_content(concat_file, dir='.', suffix='.txt') as f:
        subprocess.check_output([
            'ffmpeg', '-hide_banner', '-f', 'concat', '-safe', '0', '-i', f, '-map', '0:a', '-c', 'copy', nochap_output
        ])

    input_args, map_args, disp_args = [], [], []
    if cover:
        click.secho(f"\nfound cover art: '{cover}'\n", err=True, fg='bright_green')
        input_args = ['-i', cover]
        map_args = ['-map', '2']
        disp_args = ['-disposition:v', 'attached_pic']
    with temp_with_content(meta_file, dir='.', suffix='.txt') as f:
        subprocess.check_output([
            'ffmpeg', '-hide_banner', '-vn', '-i', nochap_output, '-i', f, *input_args, '-map', '0', *map_args, '-map_metadata', '1', '-c', 'copy', *disp_args, output
        ])
    os.remove(nochap_output)

@ff.command(help='Rename folder based on media tags of files it contains')
@click.argument('directories', type=click.Path(exists=True), nargs=-1)
@click.option('-t', '--template', default=r'%artist% [%year%] - %album%', help='name template', show_default=True)
@click.option('--tags', is_flag=True, help='Show available tags')
@click.option('--apply', is_flag=True, help='Apply changes')
def foldertag(directories, template, tags, apply):

    def common_keys(d1, d2):
        return dict(set(d1.items()).intersection(set(d2.items())))

    def format_str(tpl, kv):
        def sub(m):
            k = m.group(1).lower()
            if k not in kv:
                raise Exception(
                    "'%s' not found in source tags. Could not interpolate the template '%s'" % (k, tpl))
            return kv[k]
        return re.sub('%(.+?)%', sub, tpl)

    def print_tags(d):
        for k, v in d.items():
            click.secho(k, nl=False, fg='yellow')
            click.echo(": '%s'" % v)

    def add_custom_tags(d):
        if d.get('date', None):
            m = re.findall(r'(\d{4})', d.get('date'))
            if m:
                d['year'] = m[0]
        if d.get('album_artist', None) and not d.get('artist', None):
            d['artist'] = d['album_artist']

    def show_rename_msg(src, dst, apply=False):
        click.secho("'%s'" % src, bold=True, fg='green', nl=False)
        click.secho(
            " has been renamed to " if apply else ' will be renamed to ', nl=False)
        click.secho("'%s'" % dst, fg='green', bold=True)

    for directory in directories:
        directory = os.path.normpath(directory)
        if not os.path.isdir(directory):
            click.secho("'%s' is not a directory" % directory, fg='red')
            continue
        # files = [os.path.join(directory, f) for f in os.listdir(directory)]
        files = [os.path.join(dp, f)
                 for dp, dn, fn in os.walk(directory) for f in fn]
        files = [f for f in files if os.path.isfile(
            f) and FFPROBE.is_media_file(f)]
        file_tags = []
        for f in files:
            try:
                file_tags.append(FFPROBE.get_tags(f))
            except Exception as e:
                click.secho("'%s': " % f, fg='yellow', nl=False)
                click.secho(str(e), fg='red')
                continue
        if not file_tags:
            click.secho("'%s' contains no music files" % directory, fg='red')
            continue
        common_tags = reduce(common_keys, file_tags)
        add_custom_tags(common_tags)
        if tags:
            print_tags(common_tags)
            click.echo()

        basename = os.path.basename(directory)
        try:
            target_name = safe_filename(format_str(template, common_tags))
        except Exception as e:
            click.secho("'%s': " % directory, fg='yellow', nl=False)
            click.secho(str(e), fg='red')
            continue
        if basename == target_name:
            click.secho("'%s'" % basename, bold=True, fg='green', nl=False)
            click.secho(" adheres to provided template")
            continue
        show_rename_msg(basename, target_name, apply)
        if apply:
            os.rename(directory, target_name)


@ff.command(help='Extract embedded subtitles from a movie file')
@click.argument('fn', type=click.Path(dir_okay=False, resolve_path=True))
@click.option('--lang', 'language', default=None)
@click.option('--encoding', 'encoding', default='windows-1250')
@click.option('-f', '--first', is_flag=True, default=False)
def subextract(fn, language, encoding, first):
    def get_languages(fn):
        cmd = ['ffmpeg', '-i', fn]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        output, error = p.communicate()
        return re.findall(r'Stream #(\d+:\d+)\(?(\w*?)\)?: Subtitle: (\w+)', str(error), flags=re.S)

    langs = get_languages(fn)
    if not (language or first):
        if langs:
            return click.echo('\n'.join('#%s: language "%s" format "%s"' % a for a in langs))
        else:
            return click.secho('no subtitles found', fg='red', bold=True)
    lang = [a for a in langs if a[1] == language or first]
    if not lang:
        return click.secho('no subtitles in selected language', fg='red', bold=True)
    lang = lang[0]
    sfn = os.path.splitext(fn)[0] + '.' + \
        ('srt' if lang[2] == 'subrip' else lang[2])
    click.echo('saving %s subtitles to "%s"' % (lang[1], sfn))
    subprocess.Popen(['ffmpeg', '-i', fn, '-map', lang[0],
                      '-c', 'copy', sfn]).communicate()


class Subtitle(object):
    @staticmethod
    def parse_mpl(content):
        time_re = r'\[(\d+)\]'
        out = []
        for start, end, text in re.findall(r'^%s%s(.+)$' % (time_re, time_re), content, re.MULTILINE):
            start = int(start)/10.
            end = int(end)/10.
            out.append((start, end, text.replace('|', '\n')),)
        return out

    @staticmethod
    def parse_subrip(content, fps=23.976):
        time_re = r'\{(\d+)\}'
        out = []
        for start, end, text in re.findall(r'^%s%s(.+)$' % (time_re, time_re), content, re.MULTILINE):
            start = int(start)/fps
            end = int(end)/fps
            out.append((start, end, text.replace('|', '\n')),)
        return out

    @staticmethod
    def parse_srt(content):
        def from_srt_time(s):
            parts = [float(x.replace(',', '.')) for x in s.split(':')][::-1]
            s = parts[0] + parts[1] * 60 + parts[2] * 3600
            return s

        time_re = r'(\d+:\d+:\d+,\d+)'
        out = []
        for line in re.split('\n\n', content):
            if not line:
                continue
            m = re.findall(r'%s --> %s\n(.+)' %
                           (time_re, time_re), line, re.DOTALL)
            if not m:
                continue
            start, end, text = m[0]
            start = from_srt_time(start)
            end = from_srt_time(end)
            text = text.strip()
            out.append((start, end, text),)
        return out

    @staticmethod
    def parse(content):
        return Subtitle.parse_srt(content) or \
            Subtitle.parse_subrip(content) or \
            Subtitle.parse_mpl(content)

    @staticmethod
    def emit_srt(lines):
        def to_srt_time(seconds):
            hours, remainder = divmod(seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            s = ('%06.3f' % seconds).replace('.', ',')
            return '%02.0f:%02.0f:%s' % (hours, minutes, s)

        for i, [start, end, text] in enumerate(lines, 1):
            click.echo(
                '%d\n%s --> %s\n%s\n' % (i, to_srt_time(start), to_srt_time(end), text))

    @staticmethod
    def strip_markup(lines):
        out = []
        for start, end, text in lines:
            text = re.sub(r'\</?[\w]+?\>', '', text)
            text = '\n'.join(x.strip() for x in text.split('\n'))
            out.append((start, end, text))
        return out


@ff.command(help='Convert subtitle formats to srt')
@click.argument('fn', type=click.Path(dir_okay=False, resolve_path=True))
@click.option('--encoding', 'encoding', default='utf-8')
@click.option('--strip', is_flag=True)
def subconvert(fn, encoding, strip):
    _, ext = os.path.splitext(fn)
    if ext in {'.txt', '.srt'}:
        content = ''
        with open(fn, encoding=encoding) as f:
            content = f.read()
        parsed = Subtitle.parse(content)
        if strip:
            parsed = Subtitle.strip_markup(parsed)
        Subtitle.emit_srt(parsed)
    else:
        x = FFPROBE.get_framerate(fn)
        click.secho(x, nl=True, fg='yellow', bold=True)


@ff.command(help='Audiobook tool')
@click.argument('input', type=click.Path(exists=True, dir_okay=False, readable=True), nargs=-1)
@click.option('--cover', type=click.Path(exists=True, dir_okay=False, readable=True))
@click.option('--metadata', type=click.Choice(['full', 'no-chapters', 'none']), default='full')
@click.option('--bitrate', '-b', default='24k')
def book(input, cover, metadata, bitrate):
    # ffmpeg -i INPUT -f ffmetadata FFMETADATAFILE
    # ffmpeg -i INPUT -i FFMETADATAFILE -map_metadata 1 -codec copy OUTPUT
    def sizeof_fmt(num, suffix='B'):
        num = float(num)
        for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
            if abs(num) < 1024.0:
                return "%3.1f%s%s" % (num, unit, suffix)
            num /= 1024.0
        return "%.1f%s%s" % (num, 'Yi', suffix)

    def read_audio(fn):
        r = subprocess.check_output(
            ['ffmpeg', '-i', fn, '-f', 'u16le', '-ar', '48000', '-ac', '1', '-'], stderr=None)
        return bytes(r)

    probes = [FFPROBE.ffprobe(f) for f in input]
    # click.echo(probes)

    if not probes:
        click.secho('No files to process!', fg='red', err=True)
        sys.exit(1)

    title = sget_in(probes[0], 'format', 'tags', 'title')
    artist = sget_in(probes[0], 'format', 'tags', 'artist')
    album_artist = sget_in(probes[0], 'format', 'tags', 'album_artist')
    album = sget_in(probes[0], 'format', 'tags', 'album')

    durations = [float(get_in(p, 'format', 'duration')) for p in probes]
    chapter_marks = [sum(durations[:i]) for i in range(len(durations))]
    chapters = []
    for i, p in enumerate(probes):
        duration = float(get_in(p, 'format', 'duration'))

        click.secho('%s ' % sget_in(p, 'format', 'filename'),
                    bold=True, nl=False)
        click.secho('%s ' % format_seconds(duration), fg='yellow', nl=False)
        click.secho('%s ' % sizeof_fmt(
            get_in(p, 'format', 'size')), fg='cyan', nl=False)

        if metadata == 'full':
            chapter = ('Chapter %d' % (i+1), format_seconds(chapter_marks[i]))
            chapters += [chapter]
            click.echo('[%s | %s]' % chapter, nl=False)
        click.echo()

    click.confirm('Do you want to continue?', abort=True)

    pcm_filename = '__output.pcm'
    metadata_filename = '__metadata_ogg.txt'
    ogg_filename = '__ogg.opus'
    output_filename = '_book.mka'

    if metadata != 'none':
        with open(metadata_filename, 'wb') as f:
            f.write(''';FFMETADATA1
title=%s
artist=%s
album_artist=%s
album=%s
''' % (title, artist, album_artist, album))
            if metadata == 'full':
                for i, ch in enumerate(chapters, 1):
                    f.write('CHAPTER%02d=%s\n' % (i, ch[1]))
                    f.write('CHAPTER%02dNAME=%s\n' % (i, ch[0]))

    with open(pcm_filename, 'wb') as f:
        for i, p in enumerate(probes):
            x = read_audio(sget_in(p, 'format', 'filename'))
            f.write(x)

    subprocess.check_output([
        'ffmpeg', '-f', 'u16le', '-ar', '48000', '-ac', '1',
        '-i', pcm_filename
    ] + (['-i', metadata_filename, '-map_metadata', '1'] if metadata != 'none' else []) + [
        '-b:a', bitrate, '-c:a', 'libopus', ogg_filename
    ], stderr=None)

    subprocess.check_output([
        'ffmpeg', '-i', ogg_filename
    ] + ([
        '-attach', cover, '-metadata:s', 'mimetype=image/jpeg', '-metadata:s', 'filename=book-cover.jpg'
    ] if cover else []) + ['-c:a', 'copy', output_filename], stderr=None)


def extract_cover(fn, probe):
    streams = get_in(probe, 'streams')
    covers = [s for s in streams if get_in(s, 'codec_name') == 'mjpeg']
    if not covers:
        return None
    cover = covers[0]
    r = subprocess.check_output([
        'ffmpeg',
        '-hide_banner',
        '-loglevel', 'panic',
        '-i', fn,
        '-map', '0:%s' % sget_in(cover, 'index'),
        '-vframes', '1',
        '-vf', 'scale=w=400:h=400:force_original_aspect_ratio=decrease',
        '-c:v', 'mjpeg',
        '-q:v', '10',
        '-f', 'image2pipe',
        '-'
    ], stderr=None)
    return 'data:image/jpeg;base64,' + base64.b64encode(bytes(r)).decode('ascii')


def gen_rss(title, description, self_url, episodes):
    items = []
    for e in episodes:
        link = urllib.parse.urljoin(self_url, urllib.request.pathname2url(e['filename']))
        item = ''
        item += '<item>\n'
        item += '  <guid>%s</guid>\n' % link
        item += '  <link>%s</link>\n' % link
        item += '  <title>%s</title>\n' % xml.sax.saxutils.escape(e['title'])
        item += '  <description>%s</description>\n' % xml.sax.saxutils.escape(
            e['description'])
        item += '  <pubDate>%s</pubDate>\n' % e['rssdate']
        item += '  <enclosure url="%s" type="audio/mp4a-latm" length="%s"/>\n' % (
            link, e['size'])
        # item += '  <itunes:image href="%s" />\n' % e['cover']
        item += '  <itunes:duration>%d</itunes:duration>\n' % e['duration']
        item += '</item>'
        items.append(item)

    items = '\n'.join(items)
    return '''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
  <channel>
    <atom:link href="%s" rel="self" type="application/rss+xml" />
    <title>%s</title>
    <description>%s</description>
    <link>http://example.com/</link>
    %s
   </channel>
</rss>
''' % (self_url or '', title, description, items)


AUDIO_EXTENSIONS = {
    '.aac': 'audio/aac',
    '.alac': 'audio/mp4',
    '.flac': 'audio/flac',
    '.mp3': 'audio/mpeg',
    '.mp4': 'audio/mp4',
    '.m4a': 'audio/mp4a-latm',
    '.ogg': 'audio/ogg',
    '.opus': 'audio/ogg'
}


@ff.command(help='Generate podcast RSS from audio files in directory')
@click.argument('input', type=click.Path(exists=True), default='.')
@click.option('--title', '-t', type=str, default='My Podcast', help='podcast title')
@click.option('--description', '-d', type=str, default='...', help='podcast description')
@click.option('--url', type=str, help='RSS file URL')
def podcastrss(input, title, description, url):
    def is_audio_file(fn):
        _, ext = os.path.splitext(fn)
        return ext.lower() in AUDIO_EXTENSIONS

    def findall(regexp, s):
        return [m.groupdict() for m in re.finditer(regexp, s)]

    def first_sentence(s):
        return re.findall(r'^(.*?)(?:\.|$|\n)', s or '')[0]

    files = [f for f in os.listdir(input) if os.path.isfile(
        f) and not f.startswith('.')] if os.path.isdir(input) else [input]
    files = [f for f in files if is_audio_file(f)]
    episodes = []

    for f in files:
        probe = FFPROBE.ffprobe(f)
        tags = get_in(probe, 'format', 'tags')

        stat = pathlib.Path(f).stat()

        def dtformat(dt, format): return time.strftime(
            format, time.localtime(time.mktime(dt.timetuple())))

        def statformat(stattime, format): return time.strftime(
            format, time.localtime(stattime))

        tag_date = sget_in(tags, 'date')
        file_date = statformat(stat.st_mtime, '%Y%m%d')
        date = tag_date or file_date

        rssdate = dtformat(datetime.datetime.strptime(
            date, '%Y%m%d'), "%a, %d %b %Y %H:%M:%S %z")
        if tag_date == file_date:
            rssdate = statformat(stat.st_mtime, "%a, %d %b %Y %H:%M:%S %z")

        episodes.append({
            'filename': f,
            'title': sget_in(tags, 'title'),
            'description': first_sentence(sget_in(tags, 'description') or sget_in(tags, 'comment')),
            'date': tag_date or file_date,
            'rssdate': rssdate,
            'duration': int(float(get_in(probe, 'format', 'duration') or 0)),
            'size': stat.st_size
        })
    episodes.sort(key=lambda e: e['date'], reverse=True)
    for e in episodes:
        click.secho(e['filename'], fg='green', bold=True, file=sys.stderr)
        click.secho('title=%(title)s\ndescription=%(description)s\ndate=%(date)s' %
                    e, fg='yellow', file=sys.stderr)
    click.echo(gen_rss(title, description, url, episodes))


@ff.command(help='Get duration of media files')
@click.argument('directory', type=click.Path(exists=True), default='.')
def duration(directory):
    def escape_csv(s):
        if '"' in s or "," in s:
            return '"%s"' % s.replace('"', '""')
        return s

    files = sorted(f for f in os.listdir(directory) if os.path.isfile(f))
    output = []
    total_duration = 0.0
    total_size = 0
    for f in files:
        probe = FFPROBE.probe_file(f)
        size = int(get_in(probe, 'format', 'size') or 0)
        duration = float(get_in(probe, 'format', 'duration') or 0)
        if not size:
            continue
        output.append([
            click.format_filename(f),
            format_seconds(duration),
            sizeof_fmt(size),
            size/duration/1000*8 if duration > 0 else 0
        ])

        total_duration += duration
        total_size += size

    click.echo("filename,duration,size,bitrate")
    for line in output:
        click.echo('%s,%s,%s,%.1f kbps' %
                   (escape_csv(line[0]), line[1], line[2], line[3]))
    click.echo('-- total --,%s,%s,%.1f kbps' % (
        format_seconds(total_duration),
        sizeof_fmt(total_size),
        total_size/total_duration/1000*8 if total_duration > 0 else 0
    ))

class Photo(object):
    @staticmethod
    def identify_size(filename):
        cmd = ['identify', '-format', '%wx%h', filename]
        ret = subprocess.check_output(cmd)
        w, h = ret.decode('utf-8').split('x')
        return int(w), int(h)

    @staticmethod
    def largest_fitting(lst, target, margin=0):
        current_size, n = margin, 0
        for e in lst:
            if current_size + e + margin > target:
                break
            current_size += e + margin
            n += 1
        return n

    @classmethod
    def best_fit(cls, image_size, target_size, margin=0):
        max_cols = int(target_size[0] // min(image_size))
        best_n, best_arr = -1, None
        for rotated in [0, max_cols, *range(1, max_cols)] if image_size[0] != image_size[1] else [0]:
            nonrotated = max_cols - rotated
            sizes = list(image_size if not x else image_size[::-1] for x in [0] * nonrotated + [1] * rotated)
            cols = n = current_width = 0
            for s in sizes:
                if (current_width + s[0] + margin * (cols + 2)) > target_size[0]:
                    break
                current_width += s[0]
                cols += 1
                n += cls.largest_fitting(itertools.repeat(s[1]), target_size[1], margin=margin)
            if n > best_n:
                best_n, best_arr = n, sizes[:cols]
        return best_arr, best_n

    @classmethod
    @functools.lru_cache(2)
    def read_resized(cls, filename, rect):
        orig_x, orig_y = cls.identify_size(filename)
        rotate_cmd = []
        if (orig_x > orig_y and rect[0] < rect[1]) or (orig_x < orig_y and rect[0] > rect[1]):
            rotate_cmd = ['-rotate', '90']
        rect_formatted = f'{rect[0]}x{rect[1]}'
        cmd = ['convert', filename, '-colorspace', 'LAB', *rotate_cmd, '-resize', f'{rect_formatted}^', '-gravity', 'center', '-crop', f'{rect_formatted}+0+0', '+repage', '-colorspace', 'sRGB', 'png:-']
        image_data = subprocess.check_output(cmd)
        from PIL import Image
        image = Image.open(io.BytesIO(image_data))
        return image


def ratio(ratio):
    w, h = ratio.split('x')
    return float(w), float(h)

def reorder(lst):
    count = collections.OrderedDict()
    for e in lst:
        count[e] = count.get(e, 0) + 1
    for k, v in count.items():
        for _ in range(v):
            yield k

@ff.command(help='Arrange photos', name='print')
@click.argument('files', type=click.Path(exists=True, file_okay=True, dir_okay=False), nargs=-1, required=True)
@click.option('--size', default='35x45', type=ratio, help='photo size', show_default=True)
@click.option('--target', default='152x102', type=ratio, help='target print size', show_default=True)
@click.option('--dpi', type=int, default=600, show_default=True)
@click.option('--margin', type=int, default=1, show_default=True)
@click.option('--output', '-o', type=click.Path(writable=True), required=True)
def print_photo(files, size, target, dpi, margin, output):
    if os.path.exists(output):
        click.echo(f"error: file '{output}' already exists", err=True)
        sys.exit(1)
    from PIL import Image
    pixels_per_mm = dpi / 25.4
    target_px = round(target[0] * pixels_per_mm), round(target[1] * pixels_per_mm)
    photo_px = math.ceil(size[0] * pixels_per_mm), math.ceil(size[1] * pixels_per_mm)
    margin_px = math.ceil(margin * pixels_per_mm)

    best_arrangement, n = Photo.best_fit(image_size=photo_px, target_size=target_px, margin=margin_px)
    flip = False
    flipped = Photo.best_fit(image_size=photo_px, target_size=target_px[::-1], margin=margin_px)
    if flipped[1] > n:
        target_px = target_px[::-1]
        best_arrangement, n = flipped[0], flipped[1]
        flip = True

    photos = reorder(itertools.islice(itertools.cycle(files), n))
    im = Image.new("RGB", target_px, (255, 255, 255))
    margin_x = (target_px[0] - sum(e[0] for e in best_arrangement)) // (len(best_arrangement)+1)
    x = margin_x
    with click.progressbar(length=n, label='Resizing', file=sys.stderr) as bar:
        for col in best_arrangement:
            rows = (target_px[1] - margin_px) // (col[1] + margin_px)
            margin_y = (target_px[1] - rows * col[1]) // (rows + 1)
            y = margin_y
            for row in range(rows):
                f = next(photos)
                bar.update(1)
                image = Photo.read_resized(f, col)
                im.paste(image, (x, y))
                y += image.height + margin_y
            x += col[0] + margin_x

    if flip:
        im = im.transpose(Image.ROTATE_90)

    click.echo('Saving ', nl=False, err=True)
    click.secho(output, fg='bright_green', err=True, bold=True)
    im.save(output, quality=95, subsampling=0, dpi=(dpi,dpi))


if __name__ == '__main__':
    ff()
