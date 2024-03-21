import datetime
import fnmatch
import gc
import math
import os
import os.path
import re
import stat
import subprocess
import sys
import termios
import time
from decimal import Decimal
from getpass import getuser
from grp import getgrgid
from pwd import getpwuid
from socket import getfqdn, gethostname
from time import localtime, sleep
from typing import Iterator

from glxshell.lib.path import exists, expanduser
from glxshell.lib.stat import S_ISDIR, S_ISLNK, S_ISREG


APPLICATION_AUTHORS = ["Tuuuux"]
APPLICATION_DESCRIPTION = ""
APPLICATION_LICENSE = "License WTFPL v2"
APPLICATION_NAME = "glxsh"
APPLICATION_VERSION = "0.2.5"
APPLICATION_PATCH_LEVEL = "a1"
APPLICATION_WARRANTY = "Copyright (C) 2020-2022 Galaxie Shell Project.\nLicense WTFPL Version 2, December 2004 <http://www.wtfpl.net/about/>.\nThis is free software: you are free to change and redistribute it.\nThere is NO WARRANTY, to the extent permitted by law.\n"

def error_code_to_text(code):
    error_code = {
        1: "Operation not permitted",
        2: "No such file or directory",
        3: "No such process",
        4: "Interrupted system call",
        5: "I/O error",
        6: "No such device or address",
        7: "Argument list too long",
        8: "Exec format error",
        9: "Bad file number",
        10: "No child processes",
        11: "Try again",
        12: "Out of memory",
        13: "Permission denied",
        14: "Bad address",
        15: "Block device required",
        16: "Device or resource busy",
        17: "File exists",
        18: "Cross-device link",
        19: "No such device",
        20: "Not a directory",
        21: "Is a directory",
        22: "Invalid argument",
        23: "File table overflow",
        24: "Too many open files",
        25: "Not a typewriter",
        26: "Text file busy",
        27: "File too large",
        28: "No space left on device",
        29: "Illegal seek",
        30: "Read-only file system",
        31: "Too many links",
        32: "Broken pipe",
        33: "Math argument out of domain of func",
        34: "Math result not representable",
        39: "Directory not empty",
        97: "Address family not supported by protocol",
        104: "Connection timed out",
        110: "Connection timed out",
        115: "Operation now in progress",
    }
    try:
        return error_code[code]
    except KeyError:
        return "%s" % code

def size_of(size, suffix="B") -> str:
    for unit in ("", "K", "M", "G", "T", "P", "E", "Z", "Y"):
        if size < 1024:
            return "{size:.2f}{unit}{suffix}".format(
                size=size, unit=unit, suffix=suffix
            )
        size /= 1024
    return "{size:.2f}".format(size=size)

def get_bold_text(text):
    if sys.stdout.isatty():
        return "\x1b[1m%s\x1b[0m" % text
    return "%s" % text

class Xlator(dict):
    def _make_regex(self):
        return re.compile("|".join(map(re.escape, self.keys())))

    def __call__(self, match):
        return self[match.group(0)]

    def xlat(self, text):
        return self._make_regex().sub(self, text)

def quoted_split(s):
    def strip_quotes(s):
        if s and ((s[0] == '"') or (s[0] == "'")) and (s[0] == s[(-1)]):
            return s[1:(-1)]
        return s
    return [
        strip_quotes(p).replace('\\"', '"').replace("\\'", "'")
        for p in re.findall(
            "(?:[^\"\\s]*\"(?:\\\\.|[^\"])*\"[^\"\\s]*)+|(?:[^\\'\\s]*\\'(?:\\\\.|[^\\'])*\\'[^\\'\\s]*)+|[^\\s]+",
            s,
        )
    ]

def humanized_size(num, suffix="B", si=False):
    if si:
        units = ["", "K", "M", "G", "T", "P", "E", "Z"]
        last_unit = "Y"
        div = 1000.0
    else:
        units = ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]
        last_unit = "Yi"
        div = 1024.0
    for unit in units:
        if abs(num) < div:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= div
    return "%.1f%s%s" % (num, last_unit, suffix)


sep = "/"

def normcase(path):
    return path

def normpath(path):
    if path == "":
        return "."
    initial_slashes = path.startswith(sep)
    if (
        initial_slashes
        and path.startswith((sep * 2))
        and (not path.startswith((sep * 3)))
    ):
        initial_slashes = 2
    new_comps = []
    for comp in path.split(sep):
        if comp in {"", "."}:
            continue
        if (
            (comp != "..")
            or ((not initial_slashes) and (not new_comps))
            or (new_comps and (new_comps[(-1)] == ".."))
        ):
            new_comps.append(comp)
        elif new_comps:
            new_comps.pop()
    path = sep.join(new_comps)
    if initial_slashes:
        path = (sep * initial_slashes) + path
    return path or "."

def getcwd():
    return os.getcwd()

def abspath(path):
    if not isabs(path):
        return normpath(joinpath(getcwd(), path))
    return normpath(path)

def joinpath(*args):
    res = ""
    for a in args:
        if (not res) or a.startswith(sep):
            res = a
        else:
            res += sep + a
    return res.replace((sep * 2), sep)

def split(path):
    if path == "":
        return ("", "")
    r = path.rsplit(sep, 1)
    if len(r) == 1:
        return ("", path)
    head = r[0]
    if not head:
        head = sep
    return (head, r[1])

def splitext(path):
    r = path.rsplit(".", 1)
    if len(r) == 1:
        return (path, "")
    if not r[0]:
        return (path, "")
    return (r[0], ("." + r[1]))

def splitdrive(path):
    return ("", path)

def dirname(path):
    if (not path) or (sep not in path):
        return "."
    if path in (sep, (sep * 2), (sep * 3)):
        return sep
    r = normpath(path).rsplit(sep, 1)
    head = ""
    if len(r) > 1:
        if r[0]:
            head = r[0]
        else:
            head = sep
    if sep not in head:
        return "."
    return head

def basename(string=None, suffix=None):
    if not string:
        return "."
    if string in (sep, (sep * 2), (sep * 3)):
        return sep
    if sep not in string:
        return string
    if suffix:
        return normpath(string).split(sep)[(-1)].replace(suffix, "")
    return normpath(string).split(sep)[(-1)]

def exists(path):
    try:
        os.stat(path)
    except OSError:
        return False
    return True

def lexists(path):
    try:
        return os.access(path, os.F_OK) and os.readlink(path)
    except OSError:
        return False

def isfile(path):
    try:
        return S_ISREG(os.stat(path)[0])
    except (OSError, ArithmeticError):
        return False

def isdir(path):
    try:
        return S_ISDIR(os.stat(path)[0])
    except (OSError, ArithmeticError):
        return False

def islink(path):
    try:
        return S_ISLNK(os.lstat(path)[0])
    except (OSError, ArithmeticError):
        return False

def isabs(path):
    return path.startswith(sep)

def realpath(filename, *, strict=False):
    filename = os.fspath(filename)
    (path, _) = _joinrealpath(filename[:0], filename, strict, {})
    return abspath(path)

def _joinrealpath(path, rest, strict, seen):
    curdir = "."
    pardir = ".."
    if isabs(rest):
        rest = rest[1:]
        path = sep
    while rest:
        (name, _, rest) = rest.partition(sep)
        if (not name) or (name == curdir):
            continue
        if name == pardir:
            if path:
                (path, name) = split(path)
                if name == pardir:
                    path = joinpath(path, pardir, pardir)
            else:
                path = pardir
            continue
        newpath = joinpath(path, name)
        try:
            st = os.lstat(newpath)
        except OSError:
            if strict:
                raise
            is_link = False
        else:
            is_link = S_ISLNK(st.st_mode)
        if not is_link:
            path = newpath
            continue
        if newpath in seen:
            path = seen[newpath]
            if path is not None:
                continue
            if strict:
                os.stat(newpath)
            else:
                return (joinpath(newpath, rest), False)
        seen[newpath] = None
        (path, ok) = _joinrealpath(path, os.readlink(newpath), strict, seen)
        if not ok:
            return (joinpath(path, rest), False)
        seen[newpath] = path
    return (path, True)

def expanduser(s):
    if (s == "~") or s.startswith(("~" + sep)):
        h = os.getenv("HOME")
        return h + s[1:]
    if s[0] == "~":
        return ((sep + "home") + sep) + s[1:]
    return s

def commonprefix(m):
    if not m:
        return ""
    s1 = min(m)
    s2 = max(m)
    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i]
    return s1

def relpath(path, start=None):
    if not path:
        raise ValueError("no path specified")
    curdir = "."
    pardir = ".."
    if start is None:
        start = curdir
    start_list = [x for x in abspath(start).split(sep) if x]
    path_list = [x for x in abspath(path).split(sep) if x]
    i = len(commonprefix([start_list, path_list]))
    rel_list = ([pardir] * (len(start_list) - i)) + path_list[i:]
    if not rel_list:
        return curdir
    return joinpath(*rel_list)


__all__ = ["parse_date", "ParseError", "UTC", "FixedOffset"]
ISO8601_REGEX = re.compile(
    "\n    (?P<year>[0-9]{4})\n    (\n        (\n            (-(?P<monthdash>[0-9]{1,2}))\n            |\n            (?P<month>[0-9]{2})\n            (?!$)  # Don't allow YYYYMM\n        )\n        (\n            (\n                (-(?P<daydash>[0-9]{1,2}))\n                |\n                (?P<day>[0-9]{2})\n            )\n            (\n                (\n                    (?P<separator>[ T])\n                    (?P<hour>[0-9]{2})\n                    (:{0,1}(?P<minute>[0-9]{2})){0,1}\n                    (\n                        :{0,1}(?P<second>[0-9]{1,2})\n                        ([.,](?P<second_fraction>[0-9]+)){0,1}\n                    ){0,1}\n                    (?P<timezone>\n                        Z\n                        |\n                        (\n                            (?P<tz_sign>[-+])\n                            (?P<tz_hour>[0-9]{2})\n                            :{0,1}\n                            (?P<tz_minute>[0-9]{2}){0,1}\n                        )\n                    ){0,1}\n                ){0,1}\n            )\n        ){0,1}  # YYYY-MM\n    ){0,1}  # YYYY only\n    $\n    ",
    re.VERBOSE,
)

class ParseError(ValueError):
    pass

UTC = datetime.timezone.utc

def FixedOffset(
    offset_hours: float, offset_minutes: float, name: str
) -> datetime.timezone:
    return datetime.timezone(
        datetime.timedelta(hours=offset_hours, minutes=offset_minutes), name
    )

def parse_timezone(
    matches: dict[(str, str)], default_timezone=UTC
) -> datetime.timezone:
    tz = matches.get("timezone", None)
    if tz == "Z":
        return UTC
    if tz is None:
        return default_timezone
    sign = matches.get("tz_sign", None)
    hours = int(matches.get("tz_hour", 0))
    minutes = int(matches.get("tz_minute", 0))
    description = f"{sign}{hours:02d}:{minutes:02d}"
    if sign == "-":
        hours = -hours
        minutes = -minutes
    return FixedOffset(hours, minutes, description)

def parse_date(datestring: str, default_timezone=UTC) -> datetime.datetime:
    try:
        m = ISO8601_REGEX.match(datestring)
    except Exception as e:
        raise ParseError(e) from e
    if not m:
        raise ParseError(f"Unable to parse date string {datestring!r}")
    groups: dict[(str, str)] = {
        k: v for (k, v) in m.groupdict().items() if (v is not None)
    }
    try:
        return datetime.datetime(
            year=int(groups.get("year", 0)),
            month=int(groups.get("month", groups.get("monthdash", 1))),
            day=int(groups.get("day", groups.get("daydash", 1))),
            hour=int(groups.get("hour", 0)),
            minute=int(groups.get("minute", 0)),
            second=int(groups.get("second", 0)),
            microsecond=int(
                (
                    Decimal(f"0.{groups.get('second_fraction', 0)}")
                    * Decimal("1000000.0")
                )
            ),
            tzinfo=parse_timezone(groups, default_timezone=default_timezone),
        )
    except Exception as e:
        raise ParseError(e) from e

def is_iso8601(datestring: str) -> bool:
    try:
        m = ISO8601_REGEX.match(datestring)
        return bool(m)
    except Exception as e:
        raise ParseError(e) from e


def glob(pathname):
    return list(iglob(pathname))

def iglob(pathname):
    if not has_magic(pathname):
        if os.path.lexists(pathname):
            (yield pathname)
        return
    (dirname, basename) = os.path.split(pathname)
    if not dirname:
        (yield from glob1(None, basename))
        return
    if (dirname != pathname) and has_magic(dirname):
        dirs = iglob(dirname)
    else:
        dirs = [dirname]
    if has_magic(basename):
        glob_in_dir = glob1
    else:
        glob_in_dir = glob0
    for dirname in dirs:
        for name in glob_in_dir(dirname, basename):
            (yield os.path.join(dirname, name))

def glob1(dirname, pattern):
    if not dirname:
        if isinstance(pattern, bytes):
            dirname = bytes(os.curdir, "ASCII")
        else:
            dirname = os.curdir
    try:
        names = os.listdir(dirname)
    except os.error:
        return []
    if not _ishidden(pattern):
        names = [x for x in names if (not _ishidden(x))]
    return fnmatch.filter(names, pattern)

def glob0(dirname, basename):
    if not basename:
        if os.path.isdir(dirname):
            return [basename]
    elif os.path.lexists(os.path.join(dirname, basename)):
        return [basename]
    return []

magic_check = re.compile("[*?[]")
magic_check_bytes = re.compile(b"[*?[]")

def has_magic(s):
    if isinstance(s, bytes):
        match = magic_check_bytes.search(s)
    else:
        match = magic_check.search(s)
    return match is not None

def _ishidden(path):
    return path[0] in (".", b"."[0])

ST_MODE = 0
ST_INO = 1
ST_DEV = 2
ST_NLINK = 3
ST_UID = 4
ST_GID = 5
ST_SIZE = 6
ST_ATIME = 7
ST_MTIME = 8
ST_CTIME = 9

def S_IMODE(mode):
    return mode & 4095

def S_IFMT(mode):
    return mode & 61440

S_IFDIR = 16384
S_IFCHR = 8192
S_IFBLK = 24576
S_IFREG = 32768
S_IFIFO = 4096
S_IFLNK = 40960
S_IFSOCK = 49152

def S_ISDIR(mode):
    return S_IFMT(mode) == S_IFDIR

def S_ISCHR(mode):
    return S_IFMT(mode) == S_IFCHR

def S_ISBLK(mode):
    return S_IFMT(mode) == S_IFBLK

def S_ISREG(mode):
    return S_IFMT(mode) == S_IFREG

def S_ISFIFO(mode):
    return S_IFMT(mode) == S_IFIFO

def S_ISLNK(mode):
    return S_IFMT(mode) == S_IFLNK

def S_ISSOCK(mode):
    return S_IFMT(mode) == S_IFSOCK

S_ISUID = 2048
S_ISGID = 1024
S_ENFMT = S_ISGID
S_ISVTX = 512
S_IREAD = 256
S_IWRITE = 128
S_IEXEC = 64
S_IRWXU = 448
S_IRUSR = 256
S_IWUSR = 128
S_IXUSR = 64
S_IRWXG = 56
S_IRGRP = 32
S_IWGRP = 16
S_IXGRP = 8
S_IRWXO = 7
S_IROTH = 4
S_IWOTH = 2
S_IXOTH = 1
UF_NODUMP = 1
UF_IMMUTABLE = 2
UF_APPEND = 4
UF_OPAQUE = 8
UF_NOUNLINK = 16
UF_COMPRESSED = 32
UF_HIDDEN = 32768
SF_ARCHIVED = 65536
SF_IMMUTABLE = 131072
SF_APPEND = 262144
SF_NOUNLINK = 1048576
SF_SNAPSHOT = 2097152
_filemode_table = (
    (
        (S_IFLNK, "l"),
        (S_IFREG, "-"),
        (S_IFBLK, "b"),
        (S_IFDIR, "d"),
        (S_IFCHR, "c"),
        (S_IFIFO, "p"),
    ),
    ((S_IRUSR, "r"),),
    ((S_IWUSR, "w"),),
    (((S_IXUSR | S_ISUID), "s"), (S_ISUID, "S"), (S_IXUSR, "x")),
    ((S_IRGRP, "r"),),
    ((S_IWGRP, "w"),),
    (((S_IXGRP | S_ISGID), "s"), (S_ISGID, "S"), (S_IXGRP, "x")),
    ((S_IROTH, "r"),),
    ((S_IWOTH, "w"),),
    (((S_IXOTH | S_ISVTX), "t"), (S_ISVTX, "T"), (S_IXOTH, "x")),
)

def filemode(mode):
    perm = []
    for table in _filemode_table:
        for bit, char in table:
            if (mode & bit) == bit:
                perm.append(char)
                break
        else:
            perm.append("-")
    return "".join(perm)


__all__ = ["TextWrapper", "wrap", "fill", "dedent", "indent", "shorten"]
_whitespace = "\t\n\x0b\x0c\r "

class TextWrapper:
    unicode_whitespace_trans = {}
    uspace = ord(" ")
    for x in _whitespace:
        unicode_whitespace_trans[ord(x)] = uspace
    wordsep_re = re.compile(
        "(\\s+|[^\\s\\w]*\\w+[^0-9\\W]-(?=\\w+[^0-9\\W])|(?<=[\\w\\!\\\"\\'\\&\\.\\,\\?])-{2,}(?=\\w))"
    )
    wordsep_simple_re = re.compile("(\\s+)")
    sentence_end_re = re.compile("[a-z][\\.\\!\\?][\\\"\\']?\\Z")

    def __init__(
        self,
        width=None,
        initial_indent="",
        subsequent_indent="",
        expand_tabs=True,
        replace_whitespace=True,
        fix_sentence_endings=False,
        break_long_words=True,
        drop_whitespace=True,
        break_on_hyphens=True,
        tabsize=8,
        *,
        max_lines=None,
        placeholder=" [...]"
    ):
        if width is None:
            width = 70
        self.width = width
        self.initial_indent = initial_indent
        self.subsequent_indent = subsequent_indent
        self.expand_tabs = expand_tabs
        self.replace_whitespace = replace_whitespace
        self.fix_sentence_endings = fix_sentence_endings
        self.break_long_words = break_long_words
        self.drop_whitespace = drop_whitespace
        self.break_on_hyphens = break_on_hyphens
        self.tabsize = tabsize
        self.max_lines = max_lines
        self.placeholder = placeholder

    def _munge_whitespace(self, text):
        if self.expand_tabs:
            text = text.expandtabs(self.tabsize)
        if self.replace_whitespace:
            text = text.translate(self.unicode_whitespace_trans)
        return text

    def _split(self, text):
        if self.break_on_hyphens is True:
            chunks = self.wordsep_re.split(text)
        else:
            chunks = self.wordsep_simple_re.split(text)
        chunks = [c for c in chunks if c]
        return chunks

    def _fix_sentence_endings(self, chunks):
        i = 0
        patsearch = self.sentence_end_re.search
        while i < (len(chunks) - 1):
            if (chunks[(i + 1)] == " ") and patsearch(chunks[i]):
                chunks[(i + 1)] = "  "
                i += 2
            else:
                i += 1

    def _handle_long_word(self, reversed_chunks, cur_line, cur_len, width):
        if width < 1:
            space_left = 1
        else:
            space_left = width - cur_len
        if self.break_long_words:
            cur_line.append(reversed_chunks[(-1)][:space_left])
            reversed_chunks[(-1)] = reversed_chunks[(-1)][space_left:]
        elif not cur_line:
            cur_line.append(reversed_chunks.pop())

    def _wrap_chunks(self, chunks):
        lines = []
        if self.width <= 0:
            raise ValueError(("invalid width %r (must be > 0)" % self.width))
        if self.max_lines:
            if self.max_lines > 1:
                indentation = self.subsequent_indent
            else:
                indentation = self.initial_indent
            if (len(indentation) + len(self.placeholder.lstrip())) > self.width:
                raise ValueError("placeholder too large for max width")
        chunks.reverse()
        while chunks:
            cur_line = []
            cur_len = 0
            if lines:
                indentation = self.subsequent_indent
            else:
                indentation = self.initial_indent
            width = self.width - len(indentation)
            if self.drop_whitespace and (chunks[(-1)].strip() == "") and lines:
                del chunks[(-1)]
            while chunks:
                l = len(chunks[(-1)])
                if (cur_len + l) <= width:
                    cur_line.append(chunks.pop())
                    cur_len += l
                else:
                    break
            if chunks and (len(chunks[(-1)]) > width):
                self._handle_long_word(chunks, cur_line, cur_len, width)
                cur_len = sum(map(len, cur_line))
            if self.drop_whitespace and cur_line and (cur_line[(-1)].strip() == ""):
                cur_len -= len(cur_line[(-1)])
                del cur_line[(-1)]
            if self.max_lines:
                that_the_end_1 = (len(lines) + 1) < self.max_lines
            else:
                that_the_end_1 = False
            that_the_end_2 = (not chunks) or (
                self.drop_whitespace and (len(chunks) == 1) and (not chunks[0].strip())
            )
            if cur_line:
                if (
                    (self.max_lines is None)
                    or that_the_end_1
                    or (that_the_end_2 and (cur_len <= width))
                ):
                    lines.append((indentation + "".join(cur_line)))
                else:
                    while cur_line:
                        if cur_line[(-1)].strip() and (
                            (cur_len + len(self.placeholder)) <= width
                        ):
                            cur_line.append(self.placeholder)
                            lines.append((indentation + "".join(cur_line)))
                            break
                        cur_len -= len(cur_line[(-1)])
                        del cur_line[(-1)]
                    else:
                        if lines:
                            prev_line = lines[(-1)].rstrip()
                            if (len(prev_line) + len(self.placeholder)) <= self.width:
                                lines[(-1)] = prev_line + self.placeholder
                                break
                        lines.append((indentation + self.placeholder.lstrip()))
                    break
        return lines

    def _split_chunks(self, text):
        text = self._munge_whitespace(text)
        return self._split(text)

    def wrap(self, text):
        chunks = self._split_chunks(text)
        if self.fix_sentence_endings:
            self._fix_sentence_endings(chunks)
        return self._wrap_chunks(chunks)

    def fill(self, text):
        return "\n".join(self.wrap(text))

def wrap(text, width=None, **kwargs):
    if width is None:
        width = 79
    w = TextWrapper(width=width, **kwargs)
    return w.wrap(text)

def fill(text, width=70, **kwargs):
    w = TextWrapper(width=width, **kwargs)
    return w.fill(text)

def shorten(text, width, **kwargs):
    w = TextWrapper(width=width, max_lines=1, **kwargs)
    return w.fill(" ".join(text.strip().split()))

_whitespace_only_re = re.compile("^[ \t]+$", re.MULTILINE)
_leading_whitespace_re = re.compile("(^[ \t]*)(?:[^ \t\n])", re.MULTILINE)

def dedent(text):
    margin = None
    text = _whitespace_only_re.sub("", text)
    indents = _leading_whitespace_re.findall(text)
    for indentation in indents:
        if margin is None:
            margin = indentation
        elif indentation.startswith(margin):
            pass
        elif margin.startswith(indentation):
            margin = indentation
        else:
            margin = ""
            break
    if margin:
        for line in text.split("\n"):
            assert (not line) or line.startswith(margin), "line = %r, margin = %r" % (
                line,
                margin,
            )
        text = re.sub(("(?m)^" + margin), "", text)
    return text

def indent(text, prefix, predicate=None):
    if predicate is None:

        def predicate(line):
            return line.strip()

    def prefixed_lines():
        for line in text.splitlines(True):
            (yield ((prefix + line) if predicate(line) else line))
    return "".join(prefixed_lines())

class DescriptionString:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if value and (not isinstance(value, str)):
            raise TypeError(
                ("'%s' value must be a str type or None" % self.public_name)
            )
        if self.private_name != value:
            setattr(obj, self.private_name, value)

class SynopsisList:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if value and (not isinstance(value, list)):
            raise TypeError(
                ("'%s' value must be a list type or None" % self.public_name)
            )
        if self.private_name != value:
            setattr(obj, self.private_name, value)

class DescriptionDict:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if value and (not isinstance(value, dict)):
            raise TypeError(
                ("'%s' value must be a dict type or None" % self.public_name)
            )
        if self.private_name != value:
            setattr(obj, self.private_name, value)

class DescriptionBoolean:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if value and (not isinstance(value, bool)):
            raise TypeError(
                ("'%s' value must be a dict type or None" % self.public_name)
            )
        if self.private_name != value:
            setattr(obj, self.private_name, value)

class UtilityDescription:
    name = DescriptionString()
    synopsis = SynopsisList()
    description = DescriptionString()
    options = DescriptionString()
    operator = DescriptionString()
    stdin = DescriptionString()
    input_files = DescriptionString()
    environment_variables = DescriptionString()
    asynchronous_events = DescriptionString()
    stdout = DescriptionString()
    stderr = DescriptionString()
    output_files = DescriptionString()
    extended_description = DescriptionString()
    exit_status = DescriptionDict()
    consequences_of_errors = DescriptionString()
    application_usage = DescriptionString()
    examples = DescriptionString()
    rationale = DescriptionString()
    future_directions = DescriptionString()
    see_also = DescriptionString()
    change_history = DescriptionString()
    add_help = DescriptionBoolean()
    prog = DescriptionString()
    short_description = DescriptionString()

    def __init__(
        self,
        name=None,
        prog=None,
        synopsis=None,
        description=None,
        short_description=None,
        options=None,
        operator=None,
        stdin=None,
        input_files=None,
        environment_variables=None,
        asynchronous_events=None,
        stdout=None,
        stderr=None,
        output_files=None,
        extended_description=None,
        exit_status=None,
        consequences_of_errors=None,
        application_usage=None,
        examples=None,
        rationale=None,
        future_directions=None,
        see_also=None,
        change_history=None,
        add_help=None,
    ):
        self.name = name
        self.prog = prog
        self.synopsis = synopsis
        self.description = description
        self.short_description = short_description
        self.options = options
        self.operands = operator
        self.stdin = stdin
        self.input_files = input_files
        self.environment_variables = environment_variables
        self.asynchronous_events = asynchronous_events
        self.stdout = stdout
        self.stderr = stderr
        self.output_files = output_files
        self.extended_description = extended_description
        self.exit_status = exit_status
        self.consequences_of_errors = consequences_of_errors
        self.application_usage = application_usage
        self.examples = examples
        self.rationale = rationale
        self.future_directions = future_directions
        self.see_also = see_also
        self.change_history = change_history
        self.add_help = add_help


users_re = re.compile("[ugoa]+")
operation_re = re.compile("[+=-]")
permissions_re = re.compile("[rwxXsugo]+")

def _apply_symbolic_mode(mode, users, operation, permissions, umask, isdir):
    if users == "":
        users = "a"
    else:
        umask = 0
    mult = 0
    user_bits = S_ISGID | S_ISUID
    if ("u" in users) or ("a" in users):
        mult = mult + S_IXUSR
        user_bits = user_bits | S_IRWXU
    if ("g" in users) or ("a" in users):
        mult = mult + S_IXGRP
        user_bits = user_bits | S_IRWXG
    if ("o" in users) or ("a" in users):
        mult = mult + S_IXOTH
        user_bits = user_bits | S_IRWXO
    assert mult != 0
    mask = 0
    if "r" in permissions:
        mask = mask | (S_IROTH * mult)
    if "w" in permissions:
        mask = mask | (S_IWOTH * mult)
    if ("x" in permissions) or (("X" in permissions) and isdir):
        mask = mask | (S_IXOTH * mult)
    elif "X" in permissions:
        if mode & ((S_IXOTH | S_IXGRP) | S_IXUSR):
            mask = mask | (S_IXOTH * mult)
    if "u" in permissions:
        mask = mask | (((mode & S_IRWXU) >> 6) * mult)
    if "g" in permissions:
        mask = mask | (((mode & S_IRWXG) >> 3) * mult)
    if "o" in permissions:
        mask = mask | (((mode & S_IRWXO) >> 0) * mult)
    if "s" in permissions:
        if "u" in users:
            mask = mask | S_ISUID
        if "g" in users:
            mask = mask | S_ISGID
        if "o" in users:
            raise ValueError("Cannot use 'o' user flag with 's' permissions")
        if "a" in users:
            raise ValueError("Cannot use 'a' user flag with 's' permissions")
    if operation == "+":
        mode = (mode & umask) | ((mode | mask) & (~umask))
    elif operation == "-":
        mode = (mode & umask) | ((mode & (~mask)) & (~umask))
    elif operation == "=":
        umask = umask | (~user_bits)
        mode = (mode & umask) | (mask & (~umask))
    else:
        raise AssertionError(("unknown operation " + operation))
    return mode

def symbolic_mode(symbolic, mode=None, isdir=0, umask=0):
    pos = 0
    if mode is None:
        mode = 493
    while pos < len(symbolic):
        m = users_re.match(symbolic, pos)
        if m is None:
            users = ""
        else:
            users = m.group(0)
            pos = pos + len(users)
        while 1:
            m = operation_re.match(symbolic, pos)
            if m is None:
                raise TypeError("Missing operation in mode")
            operation = m.group(0)
            pos = pos + len(operation)
            m = permissions_re.match(symbolic, pos)
            if m is None:
                permissions = ""
            else:
                permissions = m.group(0)
                pos = pos + len(permissions)
            mode = _apply_symbolic_mode(
                mode, users, operation, permissions, umask, isdir
            )
            if not (pos < len(symbolic)):
                break
            if symbolic[pos] == ",":
                pos = pos + 1
                break
    return mode


OPTIONAL = "?"
ZERO_OR_MORE = "*"
ONE_OR_MORE = "+"
PARSER = "A..."
REMAINDER = "..."

class WrapperCmdLineArgParser:
    def __init__(self, parser):
        self.parser = parser

    def __call__(self, func):
        if not self.parser:
            self.parser = func(None, None, None, True)

        def wrapped_function(*args):
            line = args[1].split()
            try:
                parsed = self.parser.parse_args(line)
            except SystemExit:
                return None
            return func(*args, parsed)
        return wrapped_function

class Namespace:
    pass

class _ArgError(BaseException):
    pass

class _Arg:
    def __init__(self, names, dest, action, nargs, const, default, arg_type, arg_help):
        self.names = names
        self.dest = dest
        self.action = action
        self.nargs = nargs
        self.const = const
        self.default = default
        self.type = arg_type
        self.help = arg_help

    def parse(self, optname, eq_arg, args):
        if self.action in {"store", "append"}:
            if self.nargs is None:
                if eq_arg:
                    return self.type(eq_arg)
                if args:
                    return self.type(args.pop(0))
                raise _ArgError(("expecting value for %s" % optname))
            if self.nargs == OPTIONAL:
                if eq_arg:
                    return self.type(eq_arg)
                if args:
                    return self.type(args.pop(0))
                return self.default
            ret = []
            if self.nargs == ZERO_OR_MORE:
                n = -1
            elif self.nargs == ONE_OR_MORE:
                if not args:
                    raise _ArgError(("expecting value for %s" % optname))
                n = -1
            elif self.nargs == REMAINDER:
                n = 0
                while args:
                    ret.append(args.pop(0))
            else:
                n = int(self.nargs)
            stop_at_opt = True
            while args and (n != 0):
                if stop_at_opt and args[0].startswith("-") and (args[0] != "-"):
                    if args[0] == "--":
                        stop_at_opt = False
                        args.pop(0)
                    else:
                        break
                else:
                    ret.append(args.pop(0))
                    n -= 1
            if n > 0:
                raise _ArgError(("expecting value for %s" % optname))
            return ret
        if self.action == "store_const":
            return self.const
        assert False

def _dest_from_optnames(opt_names):
    dest = opt_names[0]
    for name in opt_names:
        if name.startswith("--"):
            dest = name
            break
    return dest.lstrip("-").replace("-", "_")

class ArgumentParser(UtilityDescription):
    def __init__(self, **kwargs):
        UtilityDescription.__init__(self)
        self.columns = 79
        add_help = kwargs.get("add_help", False)
        self.name = kwargs.get("name", None)
        self.synopsis = kwargs.get("synopsis", None)
        self.description = kwargs.get("description", None)
        self.options = kwargs.get("options", None)
        self.operands = kwargs.get("operands", None)
        self.stdin = kwargs.get("stdin", None)
        self.input_files = kwargs.get("input_files", None)
        self.environment_variables = kwargs.get("environment_variables", None)
        self.asynchronous_events = kwargs.get("asynchronous_events", None)
        self.stdout = kwargs.get("stdout", None)
        self.stderr = kwargs.get("stderr", None)
        self.output_files = kwargs.get("output_files", None)
        self.extended_description = kwargs.get("extended_description", None)
        self.exit_status = kwargs.get("exit_status", None)
        self.consequences_of_errors = kwargs.get("consequences_of_errors", None)
        self.application_usage = kwargs.get("application_usage", None)
        self.examples = kwargs.get("examples", None)
        self.rationale = kwargs.get("rationale", None)
        self.future_directions = kwargs.get("future_directions", None)
        self.see_also = kwargs.get("see_also", None)
        self.change_history = kwargs.get("change_history", None)
        self.opt = []
        self.pos = []
        if add_help:
            self.add_argument(
                "-h",
                "--help",
                dest="help",
                action="store_true",
                help="Show this help message and exit",
            )

    def add_argument(self, *args, **kwargs):
        action = kwargs.get("action", "store")
        if action == "store_true":
            action = "store_const"
            const = True
            default = kwargs.get("default", False)
        elif action == "store_false":
            action = "store_const"
            const = False
            default = kwargs.get("default", True)
        elif action == "append":
            const = None
            default = kwargs.get("default", [])
        else:
            const = kwargs.get("const", None)
            default = kwargs.get("default", None)
        if args and args[0].startswith("-"):
            args_list = self.opt
            dest = kwargs.get("dest")
            if dest is None:
                dest = _dest_from_optnames(args)
        else:
            args_list = self.pos
            dest = kwargs.get("dest")
            if dest is None:
                dest = args[0]
            if not args:
                args = [dest]
        args_list.append(
            _Arg(
                args,
                dest,
                action,
                kwargs.get("nargs", None),
                const,
                default,
                kwargs.get("type", str),
                kwargs.get("help", ""),
            )
        )

    @staticmethod
    def error(msg):
        sys.stderr.write(("Error: %s\n" % msg))
        sys.exit(2)

    def parse_args(self, args=None, namespace=None):
        return self._parse_args_impl(args, namespace, False)

    def parse_known_args(self, args=None, namespace=None):
        return self._parse_args_impl(args, namespace, True)

    def _parse_args_impl(self, args, namespace, return_unknown):
        if args is None:
            args = sys.argv[1:]
        else:
            args = args[:]
        if namespace is None:
            namespace = Namespace()
        try:
            return self._parse_args(args, namespace, return_unknown)
        except _ArgError as e:
            self.print_usage()
            self.error(str(e))
            return None

    def _parse_args(self, args, arg_holder, return_unknown):
        for opt in self.opt:
            setattr(arg_holder, opt.dest, opt.default)
        unknown = []

        def consume_unknown():
            while args and (not args[0].startswith("-")):
                unknown.append(args.pop(0))
        parsed_pos = False
        while args or (not parsed_pos):
            if (
                args
                and args[0].startswith("-")
                and (args[0] != "-")
                and (args[0] != "--")
            ):
                a = args.pop(0)
                if ("--" not in a) and (len(a) > 2):
                    index_focus = 0
                    for letter in a.replace("-", ""):
                        args.insert(index_focus, ("-%s" % letter))
                        index_focus += 1
                    a = args.pop(0)
                eq_arg = None
                if a.startswith("--") and ("=" in a):
                    (a, eq_arg) = a.split("=", 1)
                found = False
                for _, opt in enumerate(self.opt):
                    if a in opt.names:
                        val = opt.parse(a, eq_arg, args)
                        if opt.action == "append":
                            getattr(arg_holder, opt.dest).append(val)
                        else:
                            setattr(arg_holder, opt.dest, val)
                        found = True
                        break
                if not found:
                    if return_unknown:
                        unknown.append(a)
                        consume_unknown()
                    else:
                        raise _ArgError(("unknown option %s" % a))
            else:
                if parsed_pos:
                    if return_unknown:
                        unknown = unknown + args
                        break
                    raise _ArgError(("extra args: %s" % " ".join(args)))
                for pos in self.pos:
                    setattr(arg_holder, pos.dest, pos.parse(pos.names[0], None, args))
                parsed_pos = True
                if return_unknown:
                    consume_unknown()
        return (arg_holder, unknown) if return_unknown else arg_holder

    @staticmethod
    def render_arg(arg):
        if arg.action == "store":
            if arg.nargs == ONE_OR_MORE:
                return " %s..." % arg.dest
            if arg.nargs == ZERO_OR_MORE:
                return " [%s...]" % arg.dest
            if arg.nargs == OPTIONAL:
                return " [%s]" % arg.dest
            return " %s" % arg.dest
        return ""

    def format_usage(self):
        if self.synopsis:
            for usage in self.synopsis:
                if usage == self.synopsis[0]:
                    sys.stdout.write(("Usage: %s\n" % usage))
                else:
                    sys.stdout.write(("       %s\n" % usage))
        else:
            if self.name:
                sys.stdout.write(("Usage: %s" % self.name.split()[0]))
            else:
                sys.stdout.write(("Usage: %s" % sys.argv[0]))
            for opt in self.opt:
                sys.stdout.write((" [%s]" % ", ".join(opt.names)))
            for pos in self.pos:
                sys.stdout.write(self.render_arg(pos))
            sys.stdout.write("\n")
            if self.pos is None:
                pass

    def format_help(self, columns):
        if columns is None:
            self.columns = 79
        else:
            self.columns = columns
        if self.name:
            application_name = self.name.split()[0]
        else:
            application_name = sys.argv[0]
        self._format_help_name()
        self._format_help_synopsis(application_name)
        self._format_help_description()
        self._format_help_operands()
        self._format_help_options()
        self._format_exit_status()

    def _format_help_name(self):
        if self.name:
            sys.stdout.write(("%s\n" % get_bold_text("NAME")))
            for line in wrap(self.name, self.columns, replace_whitespace=False):
                sys.stdout.write(("%s\n" % indent(line, "  ")))

    def _format_help_synopsis(self, application_name):
        sys.stdout.write(("\n%s\n" % get_bold_text("SYNOPSIS")))
        if self.synopsis:
            for synopsis_variation in self.synopsis:
                for line in wrap(
                    synopsis_variation, self.columns, replace_whitespace=False
                ):
                    sys.stdout.write(
                        (
                            "%s\n"
                            % indent(
                                line.replace(
                                    application_name, get_bold_text(application_name)
                                ),
                                "  ",
                            )
                        )
                    )
        else:
            if self.name:
                sys.stdout.write(("  %s" % get_bold_text(self.name.split()[0])))
            else:
                sys.stdout.write(("  %s" % get_bold_text(sys.argv[0])))
            for opt in self.opt:
                sys.stdout.write((" [%s]" % ", ".join(opt.names)))
            for pos in self.pos:
                sys.stdout.write(self.render_arg(pos))
            sys.stdout.write("\n")

    def _format_help_description(self):
        if self.description:
            sys.stdout.write(("\n%s\n" % get_bold_text("DESCRIPTION")))
            for line in wrap(self.description, self.columns, replace_whitespace=False):
                sys.stdout.write(("%s\n" % indent(line, "  ")))

    def _format_help_operands(self):
        if self.pos:
            sys.stdout.write(("\n%s\n" % get_bold_text("OPERANDS")))
            max_size = max((len(x.names[0]) for x in self.pos))
            for pos in self.pos:
                the_name = pos.names[0]
                pos.help = pos.help[0].upper() + pos.help[1:]
                the_help = wrap(pos.help, ((self.columns - max_size) - 4))
                sys.stdout.write(indent(get_bold_text(the_name), "  "))
                for help_line in the_help:
                    if help_line == the_help[0]:
                        sys.stdout.write(
                            indent(
                                help_line, (" " * int(((max_size - len(the_name)) + 2)))
                            )
                        )
                        sys.stdout.write("\n")
                    else:
                        sys.stdout.write(indent(help_line, (" " * int((max_size + 4)))))
                        sys.stdout.write("\n")

    def _format_help_options(self):
        if self.opt:
            sys.stdout.write(("\n%s\n" % get_bold_text("OPTIONS")))
            max_size = max((len(", ".join(x.names)) for x in self.opt))
            for opt in self.opt:
                the_name = ", ".join(opt.names)
                opt.help = opt.help[0].upper() + opt.help[1:]
                the_help = wrap(opt.help, ((self.columns - max_size) - 4))
                sys.stdout.write(indent(get_bold_text(the_name), "  "))
                for help_line in the_help:
                    if help_line == the_help[0]:
                        sys.stdout.write(
                            indent(
                                help_line, (" " * int(((max_size - len(the_name)) + 2)))
                            )
                        )
                        sys.stdout.write("\n")
                    else:
                        sys.stdout.write(indent(help_line, (" " * int((max_size + 4)))))
                        sys.stdout.write("\n")

    def _format_exit_status(self):
        if self.exit_status:
            sys.stdout.write(("\n%s\n" % get_bold_text("EXIT STATUS")))
            max_size = max(
                (
                    len(exit_code)
                    for (exit_code, description) in self.exit_status.items()
                )
            )
            for exit_code, description in self.exit_status.items():
                sys.stdout.write(indent(get_bold_text(exit_code), "  "))
                if description:
                    the_help = wrap(description, (self.columns - 4))
                    for help_line in the_help:
                        if help_line == the_help[0]:
                            sys.stdout.write(
                                indent(
                                    help_line,
                                    (" " * int(((max_size - len(exit_code)) + 2))),
                                )
                            )
                            sys.stdout.write("\n")
                        else:
                            sys.stdout.write(
                                indent(help_line, (" " * int((max_size + 4))))
                            )
                            sys.stdout.write("\n")
                else:
                    sys.stdout.write("\n")

    def print_usage(self):
        self.format_usage()

    def print_help(self, columns=None):
        self.format_help(columns=columns)

class FileType:
    def __init__(self, mode="r", bufsize=(-1), encoding=None, errors=None):
        self._mode = mode
        self._bufsize = bufsize
        self._encoding = encoding
        self._errors = errors

    def __call__(self, string):
        if string == "-":
            if "r" in self._mode:
                return sys.stdin
            if "w" in self._mode:
                return sys.stdout
            raise ValueError(('argument "-" with mode %r' % self._mode))
        try:
            return open(string, self._mode, self._bufsize, self._encoding, self._errors)
        except OSError as e:
            args = {"filename": string, "error": e}
            message = "can't open '%(filename)s': %(error)s"
            raise TypeError((message % args)) from e

    def __repr__(self):
        args = (self._mode, self._bufsize)
        kwargs = [("encoding", self._encoding), ("errors", self._errors)]
        args_str = ", ".join(
            (
                [repr(arg) for arg in args if (arg != (-1))]
                + [("%s=%r" % (kw, arg)) for (kw, arg) in kwargs if (arg is not None)]
            )
        )
        return "%s(%s)" % (type(self).__name__, args_str)


def columnize(columnize_data, display_width=80):
    if not columnize_data:
        sys.stdout.write("<empty>\n")
        return
    non_strings = [
        i
        for i in range(len(columnize_data))
        if (not isinstance(columnize_data[i], str))
    ]
    if non_strings:
        sys.stderr.write(
            ("list[i] not a string for i in %s" % ", ".join(map(str, non_strings)))
        )
        return
    size = len(columnize_data)
    if size == 1:
        sys.stdout.write(("%s\n" % str(columnize_data[0])))
        return
    for num_rows in range(1, len(columnize_data)):
        num_cols = ((size + num_rows) - 1) // num_rows
        col_widths = []
        tot_width = -2
        for col in range(num_cols):
            colwidth = 0
            for row in range(num_rows):
                i = row + (num_rows * col)
                if i >= size:
                    break
                x = columnize_data[i]
                colwidth = max(colwidth, len(x))
            col_widths.append(colwidth)
            tot_width += colwidth + 2
            if tot_width > display_width:
                break
        if tot_width <= display_width:
            break
    else:
        num_rows = len(columnize_data)
        num_cols = 1
        col_widths = [0]
    for row in range(num_rows):
        texts = []
        for col in range(num_cols):
            i = row + (num_rows * col)
            if i >= size:
                x = ""
            else:
                x = columnize_data[i]
            texts.append(x)
        while texts and (not texts[(-1)]):
            del texts[(-1)]
        for col, _ in enumerate(texts):
            texts[col] = "%-*s" % (col_widths[col], texts[col])
        sys.stdout.write(("%s\n" % str("  ".join(texts))))


try:
    import subprocess
except ImportError:
    subprocess = None
parser_man = ArgumentParser(
    prog="man",
    description="The man utility shall write information about each of the name operands.",
    add_help=True,
)
parser_man.add_argument(
    "name", nargs="?", help="A keyword or the name of a standard utility."
)
PROMPT = "(Cmd) "
IDENTCHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

class Cmd:
    prompt = PROMPT
    identchars = IDENTCHARS
    ruler = "="
    lastcmd = ""
    intro = None
    doc_leader = ""
    doc_header = "Documented commands (type man <topic>):"
    misc_header = "Miscellaneous help topics:"
    undoc_header = "Undocumented commands:"
    nohelp = "No manual entry for %s"
    use_rawinput = 1

    def __init__(self, completekey="tab"):
        self.cmdqueue = []
        self.completekey = completekey
        self.completion_matches = []
        self.exit_code = 0
        self.rc_file = ".glxshrc"
        self.logout_file = ".glxsh_logout"
        self.history_path = expanduser("~/.glxsh_history")
        self.history_length = 100

    def cmdloop(self, intro=None):
        self.preloop()
        if self.use_rawinput and self.completekey:
            try:
                import readline

                self.old_completer = readline.get_completer()
                readline.set_completer(self.complete)
                readline.parse_and_bind((self.completekey + ": complete"))
                self.old_delims = readline.get_completer_delims()
                readline.set_completer_delims(self.old_delims.replace("-", ""))
                readline.parse_and_bind("set colored-completion-prefix off")
                readline.parse_and_bind("set show-all-if-unmodified on")
                readline.parse_and_bind("set horizontal-scroll-mode on")
                if not exists(self.history_path):
                    open(self.history_path, "a+").close()
                readline.read_history_file(self.history_path)
                readline.set_history_length(self.history_length)
            except ImportError:
                pass
        try:
            if intro is not None:
                self.intro = intro
            if self.intro:
                sys.stdout.write((str(self.intro) + "\n"))
            stop = None
            while not stop:
                if self.cmdqueue:
                    line = self.cmdqueue.pop(0)
                elif self.use_rawinput:
                    try:
                        sys.stdout.write(self.prompt)
                        sys.stdout.flush()
                        line = input()
                    except EOFError:
                        line = "EOF"
                    except KeyboardInterrupt:
                        sys.stdout.write("^C")
                        sys.stdout.flush()
                        line = ""
                else:
                    try:
                        sys.stdout.write(self.prompt)
                        sys.stdout.flush()
                        line = sys.stdin.readline()
                        if not len(line):
                            line = "EOF"
                        else:
                            line = line.rstrip("\r\n")
                    except KeyboardInterrupt:
                        sys.stdout.write("^C")
                        sys.stdout.flush()
                        line = ""
                line = self.precmd(line)
                stop = self.onecmd(line)
                stop = self.postcmd(stop, line)
            self.postloop()
        finally:
            if self.use_rawinput and self.completekey:
                try:
                    import readline

                    readline.set_completer(self.old_completer)
                    readline.set_completer_delims(self.old_delims)
                    readline.write_history_file(self.history_path)
                except ImportError:
                    pass
            return self.exit_code

    def precmd(self, line):
        return line

    def postcmd(self, stop, line):
        return stop

    def preloop(self):
        pass

    def postloop(self):
        pass

    def parseline(self, line):
        line = line.strip()
        if not line:
            return (None, None, line)
        elif line[0] == "?":
            line = "man " + line[1:]
        elif line[0] == "!":
            if hasattr(self, "do_shell"):
                line = "shell " + line[1:]
            else:
                return (None, None, line)
        (i, n) = (0, len(line))
        while (i < n) and (line[i] in self.identchars):
            i = i + 1
        (cmd, arg) = (line[:i], line[i:].strip())
        return (cmd, arg, line)

    def onecmd(self, line):
        (cmd, arg, line) = self.parseline(line)
        if not line:
            return self.emptyline()
        if cmd is None:
            return self.default(line)
        self.lastcmd = line
        if line == "EOF":
            self.lastcmd = ""
        if cmd == "":
            return self.default(line)
        else:
            try:
                func = getattr(self, ("do_" + cmd))
            except AttributeError:
                return self.default(line)
            return func(arg)

    def onecmdhooks(self, line):
        self.onecmd(line)
        return self.exit_code

    def emptyline(self):
        if self.lastcmd:
            return self.onecmd(self.lastcmd)

    def default(self, line):
        sys.stdout.write(("*** Unknown syntax: %s\n" % line))

    def default_completer(self, *ignored):
        return []

    def completenames(self, text, *ignored):
        return [
            ("%s " % a[3:]) for a in self.get_names() if a.startswith(("do_%s" % text))
        ]

    def complete(self, text, state):
        if state == 0:
            import readline

            original_line = readline.get_line_buffer()
            line = original_line.lstrip()
            stripped = len(original_line) - len(line)
            start_index = readline.get_begidx() - stripped
            end_index = readline.get_endidx() - stripped
            if start_index > 0:
                (cmd, args, foo) = self.parseline(line)
                if cmd == "":
                    complete_function = self.default_completer
                else:
                    try:
                        complete_function = getattr(self, ("complete_" + cmd))
                    except AttributeError:
                        complete_function = self.default_completer
            else:
                complete_function = self.completenames
            self.completion_matches = complete_function(
                text, line, start_index, end_index
            )
        try:
            return self.completion_matches[state]
        except IndexError:
            return None

    def get_names(self):
        return dir(self.__class__)

    def complete_man(self, *args):
        commands = set(
            [a[3:] for a in self.get_names() if a.startswith(("do_" + args[0]))]
        )
        topics = set(
            (a[5:] for a in self.get_names() if a.startswith(("help_" + args[0])))
        )
        return list((commands | topics))

    @staticmethod
    def help_man():
        parser_man.print_help()

    @WrapperCmdLineArgParser(parser_man)
    def do_man(self, arg, parsed):
        if parsed.help:
            self.help_man()
            return 0
        if arg:
            try:
                func = getattr(self, ("help_" + arg))
            except AttributeError:
                sys.stdout.write(("%s\n" % str((self.nohelp % (arg,)))))
                return 1
            return func()
        else:
            names = self.get_names()
            cmds_doc = []
            cmds_undoc = []
            help = {}
            for name in names:
                if name[:5] == "help_":
                    help[name[5:]] = 1
            names.sort()
            prevname = ""
            for name in names:
                if name[:3] == "do_":
                    if name == prevname:
                        continue
                    prevname = name
                    cmd = name[3:]
                    if cmd in help:
                        cmds_doc.append(cmd)
                        del help[cmd]
                    else:
                        cmds_undoc.append(cmd)
            sys.stdout.write(("%s\n" % self.doc_leader))
            self.print_topics(self.doc_header, cmds_doc, 15, 80)
            self.print_topics(self.misc_header, list(help.keys()), 15, 80)
            if cmds_undoc != ["EOF"]:
                self.print_topics(self.undoc_header, cmds_undoc, 15, 80)
            return 0

    def print_topics(self, header, cmds, cmdlen, maxcol):
        if cmds:
            sys.stdout.write(("%s\n" % header))
            if self.ruler:
                sys.stdout.write(("%s\n" % str((self.ruler * len(header)))))
            columnize(cmds, (maxcol - 1))
            sys.stdout.write("\n")

class GLXAlias:
    def __init__(self):
        self.__alias = None
        self.alias = None

    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self, value):
        if value is None:
            value = {}
        if value and (not isinstance(value, dict)):
            raise TypeError("'alias' property value must be a dict type or None")
        if self.alias != value:
            self.__alias = value

def tabulate(tabular_data, headers, tablefmt, colalign):
    value_to_return = []
    if tablefmt is None:
        tablefmt = None
    columns_info = {}
    if headers:
        tabular_data.insert(0, headers)
    for line in tabular_data:
        for index_col, cell_value in enumerate(line):
            columns_info[index_col] = {}
            columns_info[index_col]["data"] = []
            columns_info[index_col]["text"] = []
            columns_info[index_col]["size"] = 0
            columns_info[index_col]["colalign"] = None
    for line in tabular_data:
        for index_col, cell_value in enumerate(line):
            columns_info[index_col]["data"].append(cell_value)
            columns_info[index_col]["text"].append(cell_value)
            if colalign:
                columns_info[index_col]["colalign"] = colalign[index_col]
            if len(str(cell_value)) > columns_info[index_col]["size"]:
                columns_info[index_col]["size"] = len(str(cell_value))
    for _, value in columns_info.items():
        for index, item in enumerate(value["data"]):
            value["text"][index] = str(value["text"][index])
            if len(str(item)) < value["size"]:
                if value["colalign"].lower() == "right":
                    spacing = " " * int((value["size"] - len(str(item))))
                    value["text"][index] = "%s%s" % (spacing, value["text"][index])
                elif value["colalign"].lower() == "center":
                    spacing = " " * int((int((value["size"] - len(str(item)))) / 2))
                    value["text"][index] = "%s%s" % (spacing, value["text"][index])
                    while len(value["text"][index]) < value["size"]:
                        value["text"][index] = "%s " % value["text"][index]
                else:
                    spacing = " " * int((value["size"] - len(str(item))))
                    value["text"][index] = "%s%s" % (value["text"][index], spacing)
    line_to_append = ""
    spacing = " "
    for line, line_value in enumerate(tabular_data):
        for col, _ in enumerate(line_value):
            line_to_append += "%s%s" % (columns_info[col]["text"][line], spacing)
        value_to_return.append(line_to_append.strip(" "))
        line_to_append = ""
    return "\n".join(value_to_return)

class EINVAL(Exception):
    pass

class ENOMEM(Exception):
    pass

class GLXEnviron:
    def __init__(self):
        self.__environ = None
        self.environ = {}

    @property
    def environ(self) -> dict:
        return self.__environ

    @environ.setter
    def environ(self, value):
        if value is None:
            value = {}
        if not isinstance(value, dict):
            raise TypeError("'environ' property value must be a dict type or None")
        if self.environ != value:
            self.__environ = value

    def getenv(self, name=None):
        if name and (not isinstance(name, str)):
            raise TypeError("'name' parameter must be a str or None")
        return self.environ.get(name, None)

    def setenv(self, envname=None, envval=None, overwrite=None):
        if not isinstance(envname, str):
            raise TypeError("'name' parameter must be a str")
        if not isinstance(envval, str):
            raise TypeError("'value' parameter must be a str")
        if (envname == "") or ("=" in envname):
            raise EINVAL()
        if (envname in self.environ) and (overwrite == 0):
            return 0
        if ((envname in self.environ) and (overwrite != 0)) or (
            envname not in self.environ
        ):
            try:
                self.environ[envname] = envval
                return 0
            except MemoryError as exc:
                raise ENOMEM() from exc
        return -1

    def unsetenv(self, name):
        if not isinstance(name, str):
            raise TypeError("'name' parameter value must be a str type")
        if (name == "") or ("=" in name):
            raise EINVAL()
        if name not in self.environ:
            return 0
        try:
            del self.environ[name]
            return 0
        except KeyError:
            return -1


def _append_slash_if_dir(p):
    if p and isdir(p) and (p[(-1)] != sep):
        return p + sep
    else:
        return p

def glxsh_completer_directory(_, line, __, ___):
    arg = line.split()[1:]
    if not arg:
        return [(normpath(f) + sep) for f in os.listdir(getcwd()) if isdir(f)]
    else:
        (directory, part, base) = arg[(-1)].rpartition(sep)
        if part == "":
            directory = getcwd()
        elif directory == "":
            directory = sep
        completions = []
        for f in os.listdir(directory):
            if f.startswith(base):
                if isdir(joinpath(directory, f)):
                    completions.append(joinpath(f, ""))
        return completions

def glxsh_completer_file(_, line, __, ___):
    arg = line.split()[1:]
    if not arg:
        return os.listdir(getcwd())
    else:
        (directory, part, base) = arg[(-1)].rpartition(sep)
        if part == "":
            directory = getcwd()
        elif directory == "":
            directory = sep
        return [
            ((normpath(f) + sep) if isdir(f) else normpath(f))
            for f in os.listdir(directory)
            if f.startswith(base)
        ]

def glxsh_complete_chmod(text, line, begidx, endidx):
    return glxsh_completer_file(text, line, begidx, endidx)

def glxsh_complete_rmdir2(_, line, begidx, endidx):
    before_arg = line.rfind(" ", 0, begidx)
    if before_arg == (-1):
        return
    fixed = line[(before_arg + 1) : begidx]
    arg = line[(before_arg + 1) : endidx]
    pattern = arg + "*"
    completions = []
    for path in glob(pattern):
        path = _append_slash_if_dir(path)
        completions.append(path.replace(fixed, "", 1))
    return completions

def glxsh_complete_rmdir(_, line, __, ___):
    if line == "rmdir":
        return ["rmdir "]
    arg = line.split()[1:]
    if not arg:
        return [(normpath(f) + sep) for f in os.listdir(getcwd()) if isdir(f)]
    else:
        (directory, part, base) = arg[(-1)].rpartition(sep)
        if part == "":
            directory = "." + sep
        elif directory == "":
            directory = sep
        completions = []
        for f in os.listdir(directory):
            if f.startswith(base):
                if isdir(os.path.join(directory, f)):
                    completions.append((f + sep))
    return completions

var_env_pattern = re.compile(".*\\$$", re.IGNORECASE)
var_env_name_pattern = re.compile(".*\\$(\\w+)$", re.IGNORECASE)

def glxsh_complete_echo(_, line, __, ___, shell=None):
    if line == "echo":
        return ["echo "]
    arg = line.split()[1:]
    if not arg:
        pass
    else:
        completions = []
        if var_env_name_pattern.match(arg[(-1)]):
            search_result = re.search(var_env_name_pattern, arg[(-1)])
            if not search_result:
                return None
            for key, value in shell.environ.items():
                if str(key).startswith(search_result.group(1)) and (
                    key != search_result.group(1)
                ):
                    completions.append(("%s " % key))
            return completions
        elif var_env_pattern.match(arg[(-1)]):
            search_result = re.search(var_env_pattern, arg[(-1)])
            if not search_result:
                return None
            for key, value in shell.environ.items():
                completions.append(("%s " % key))
            return completions
        else:
            return None

def glxsh_complete_du(text, line, begidx, endidx, shell=None):
    if line == "du":
        return ["du "]
    arg = line.split()[1:]
    completions = []
    if not arg:
        for f in os.listdir(getcwd()):
            if isdir(f):
                completions.append((normpath(f) + sep))
            if isfile(f) or islink(f):
                completions.append(normpath(f))
    else:
        (directory, part, base) = arg[(-1)].rpartition(sep)
        if part == "":
            directory = "." + sep
        elif directory == "":
            directory = sep
        completions = []
        for f in os.listdir(directory):
            if f.startswith(base) or f.startswith((base + sep)):
                if isdir(f):
                    completions.append((normpath(f) + sep))
                if isfile(f) or islink(f):
                    completions.append(normpath(f))
    return completions


parser_alias = ArgumentParser(
    name="alias - define or display aliases",
    description="The alias utility shall create or redefine alias definitions or write the values of existing alias definitions to standard output. An alias definition provides a string value that shall replace a command name when it is encountered",
    synopsis=["alias [alias-name[=string]...]"],
    exit_status={
        "0": "Successful completion.",
        ">0": "One of the name operands specified did not have an alias definition, or an error occurred.",
    },
)
parser_alias.add_argument(
    "alias-name",
    nargs="*",
    type=str,
    help="Write the alias definition to standard output.",
)
parser_alias.add_argument(
    "alias-name=string",
    nargs="*",
    help="Assign the value of string to the alias alias-name.",
)

def glxsh_alias(**kwargs):
    shell = kwargs.get("shell", None)
    string = kwargs.get("string", None)
    exit_code = 0
    if string is None:
        if shell:
            for key, value in shell.alias.items():
                sys.stdout.write(("%s='%s'\n" % (key, value)))
            return 0
        else:
            return 1
    try:
        split_line = quoted_split(string)
        if split_line:
            for alias_name in split_line:
                if "=" in alias_name:
                    spited_value = alias_name.split("=")
                    shell.alias[spited_value[0]] = str(
                        spited_value[1].strip('"').strip("'")
                    )
                elif alias_name in shell.alias:
                    sys.stdout.write(
                        ("%s='%s'\n" % (alias_name, shell.alias[alias_name]))
                    )
            return exit_code
        else:
            for key, value in shell.alias.items():
                sys.stdout.write(("%s='%s'\n" % (key, value)))
            return 0
    except OSError as error:
        sys.stderr.write(("alias: %s\n" % error_code_to_text(error.errno)))
        return 1


parser_basename = ArgumentParser(
    name="basename - return non-directory portion of a pathname",
    prog="basename",
    description="Print string with any leading directory components removed. If specified, also remove a trailing suffix.",
)
parser_basename.add_argument(
    "string", type=str, nargs="?", default=None, help="a string"
)
parser_basename.add_argument("suffix", nargs="?", default=None, help="a string")

def glxsh_basename(string=None, suffix=None):
    try:
        sys.stdout.write(("%s\n" % basename(string, suffix)))
        return 0
    except (Exception, ArithmeticError) as error:
        sys.stderr.write(("basename: %s\n" % error))
        return 1


parser_cat = ArgumentParser(
    name="cat - concatenate and print files",
    description="The cat utility shall read files in sequence and shall write their contents to the standard output in the same sequence.",
)
parser_cat.add_argument(
    "file",
    nargs="*",
    type=FileType("r"),
    help="A pathname of an input file. If no file operands are specified, the standard input shall be used. If a file is '-', the cat utility shall read from the standard input at that point in the sequence. The cat utility shall not close and reopen standard input when it is referenced in this way, but shall accept multiple occurrences of '-' as a file operand.",
)
parser_cat.add_argument(
    "-u", dest="update", action="store_true", default=False, help="ignored"
)

def glxsh_cat(files):
    def read_file_in_chunks(file_object, chunk_size=3072):
        while True:
            data = file_object.read(chunk_size)
            if not data:
                break
            (yield data)

    def read_stdin(file_object):
        while True:
            data = file_object.readline()
            if not data:
                break
            (yield data)
    try:
        if (files is None) or (files == []):
            files = ["-"]
        for file in files:
            if file == "-":
                for piece in read_stdin(sys.stdin):
                    sys.stdout.write(piece)
            else:
                with open(file, "r") as f:
                    for piece in read_file_in_chunks(f):
                        sys.stdout.write(piece)
        return 0
    except (Exception, ArithmeticError) as error:
        sys.stderr.write(("cat: %s\n" % error))
        return 1


parser_cd = ArgumentParser(
    name="cd - change the working directory",
    description="The cd utility shall change the working directory of the current shell execution environment",
)
parser_cd.add_argument(
    "directory",
    nargs="?",
    const=0,
    help="An absolute or relative pathname of the directory that shall become the new working directory. The interpretation of a relative pathname by cd depends on the -L option and the CDPATH and PWD environment variables. If directory is an empty string, the directory be come HOME environment variable.",
)
parser_cd.add_argument(
    "-P",
    dest="physical",
    action="store_true",
    default=False,
    help="Handle the operand dot-dot physically; symbolic link components shall be resolved before dot-dot components are processed",
)
parser_cd.add_argument(
    "-L",
    dest="logical",
    action="store_true",
    default=False,
    help="Handle the operand dot-dot logically; symbolic link components shall not be resolved before dot-dot components are processed ",
)

def glxsh_cd(directory=None, logical=None, physical=None, shell=None):
    if directory is None:
        directory = shell.getenv("HOME")
    if logical and physical:
        physical = False
    if (not logical) and (not physical):
        logical = True
    if directory == "-":
        if shell.getenv("OLDPWD"):
            directory = shell.getenv("OLDPWD")
        else:
            directory = shell.getenv("PWD")
    elif directory:
        directory = expanduser(directory)
    try:
        if logical:
            os.chdir(normpath(directory))
        else:
            os.chdir(realpath(directory))
        shell.setenv("OLDPWD", shell.getenv("PWD"), 1)
        shell.setenv("PWD", os.getcwd(), 1)
        return 0
    except (Exception, ArithmeticError) as error:
        sys.stderr.write(
            ("cd: %s: '%s'\n" % (error_code_to_text(error.errno), directory))
        )
        return 1


parser_chmod = ArgumentParser(
    name="chmod - change the file modes",
    description="The chmod utility shall change any or all of the file mode bits of the file named by each file operand in the way specified by the mode operandself.\n\nOnly a process whose effective user ID matches the user ID of the file, or a process with appropriate privileges, shall be permitted to change the file mode bits of a file.\n",
)
parser_chmod.add_argument(
    "-R",
    dest="recursive",
    action="store_true",
    default=False,
    help="Recursively change file mode bits.",
)
parser_chmod.add_argument(
    "mode",
    dest="mode",
    help="Represents the change to be made to the file mode bits of each file named by one of the file operands",
)
parser_chmod.add_argument(
    "file",
    dest="file",
    nargs="+",
    help="A pathname of a file whose file mode bits shall be modified.",
)

def glxsh_chmod(recursive=None, mode=None, file=None):
    exit_code = 0

    def _chmod(path, mode):
        try:
            os.chmod(path, mode)
            return 0
        except OSError as error:
            sys.stderr.write(
                ("chmod: %s: '%s'\n" % (error_code_to_text(error.errno), path))
            )
            return 1
        except (Exception, BaseException) as error:
            sys.stderr.write(("chmod: %s: '%s'\n" % (error, path)))
            return 1
    for path in file:
        if recursive:
            dir_scan = glob(("%s/**/*" % path))
        else:
            dir_scan = glob(path)
        for f in dir_scan:
            if stat.S_ISDIR(os.stat(f)[0]):
                try:
                    mode = symbolic_mode(
                        mode, mode=os.stat(f).st_mode, umask=os.umask(0), isdir=1
                    )
                except TypeError:
                    pass
            else:
                try:
                    mode = symbolic_mode(
                        mode, mode=os.stat(f).st_mode, umask=os.umask(0), isdir=0
                    )
                except TypeError:
                    pass
            if not isinstance(mode, int):
                mode = int(mode, 8)
            exit_code += _chmod(f, mode)
    return 1 if exit_code else 0


parser_clear = ArgumentParser(name="clear", description="Clear screen")

def glxsh_clear():
    try:
        sys.stdout.write("\x1b[2J\x1b[H")
        return 0
    except (Exception, ArithmeticError) as error:
        sys.stderr.write(("clear: %s\n" % error))
        return 1


parser_cp = ArgumentParser(
    name="cp - copy files",
    description="The first synopsis form is denoted by two operands, neither of which are existing files of type directory. The cp utility shall copy the contents of source_file (or, if source_file is a file of type symbolic link, the contents of the file referenced by source_file) to the destination path named by target_file.",
    exit_status={
        "0": "The utility executed successfully and all requested changes were made.",
        ">0": "An error occurred.",
    },
)
parser_cp.add_argument(
    "-f",
    dest="force",
    action="store_true",
    help="If a file descriptor for a destination file cannot be obtained, as described in step 3.a.ii., attempt to unlink the destination file and proceed.",
)
parser_cp.add_argument(
    "-i",
    dest="interactive",
    action="store_true",
    help="Write a prompt to standard error before copying to any existing non-directory destination file.",
)
parser_cp.add_argument(
    "source_file",
    nargs="+",
    help="A pathname of a file to be copied. If a source_file operand is '-', it shall refer to a file named -; implementations shall not treat it as meaning standard input. target_file",
)
parser_cp.add_argument(
    "target_file",
    help="A pathname of an existing or nonexistent file, used for the output when a single file is copied. If a target_file operand is '-', it shall refer to a file named -; implementations shall not treat it as meaning standard output.",
)

def glxsh_cp(source_file, target_file, interactive=False):
    try:
        with open(source_file, "r") as source_file_descriptor:
            pass
    except (Exception, ArithmeticError) as error:
        sys.stderr.write(
            ("cp: %s: '%s'\n" % (error_code_to_text(error.errno), source_file))
        )
        return 1
    if interactive and exists(target_file):
        if (
            input(("do you want to overwrite %s file ? (Y/n)" % target_file))
            .upper()
            .startswith("N")
        ):
            return 0
    try:
        with open(target_file, "w") as target_file_descriptor:
            pass
    except (Exception, ArithmeticError) as error:
        sys.stderr.write(
            ("cp: %s: '%s'\n" % (error_code_to_text(error.errno), target_file))
        )
        return 1
    try:
        with open(source_file, "r") as source_file_descriptor:
            with open(target_file, "w") as target_file_descriptor:
                target_file_descriptor.write(source_file_descriptor.read())
        return 0
    except (Exception, ArithmeticError) as error:
        sys.stderr.write(("cp: %s:\n" % error_code_to_text(error.errno)))
        return 1


parser_date = ArgumentParser(
    name="date - write the date and time",
    description="The date utility shall write the date and time to standard output or attempt to set the system date and time. By default, the current date and time shall be written. If an operand beginning with '+' is specified, the output format of date shall be controlled by the conversion specifications and other text in the operand.",
)
parser_date.add_argument(
    "-u",
    dest="u",
    action="store_true",
    help="Perform operations as if the TZ environment variable was set to the string 'UTC0', or its equivalent historical value of 'GMT0'. Otherwise, date shall use the timezone indicated by the TZ environment variable or the system default if that variable is unset or null.",
)
parser_date.add_argument(
    "format",
    nargs="*",
    help="When the format is specified, each conversion specifier shall be replaced in the standard output by its corresponding value. All other characters shall be copied to the output without change. The output shall always be terminated with a <newline>.",
)

def glxsh_date(u=None, custom_format=None, shell=None):
    exit_code = 0
    from time import localtime, tzname

    tm = localtime()
    dow = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
    dow_full = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    )
    mon = (
        "???",
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    )
    mon_full = (
        "???",
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    )
    if custom_format == "":
        custom_format = "+%a %b %e %H:%M:%S %Z %Y"
    if custom_format.startswith('"') and custom_format.endswith('"'):
        custom_format = custom_format[1:][:(-1)]
    if custom_format.startswith("'") and custom_format.endswith("'"):
        custom_format = custom_format[1:][:(-1)]
    if custom_format and str(custom_format).startswith("+"):
        custom_format = custom_format.replace("%a", dow[tm[6]])
        custom_format = custom_format.replace("%A", dow_full[tm[6]])
        custom_format = custom_format.replace("%b", mon[tm[1]])
        custom_format = custom_format.replace("%B", mon_full[tm[1]])
        custom_format = custom_format.replace("%C", ("%02d" % int((tm[0] / 100))))
        custom_format = custom_format.replace("%d", ("%02d" % tm[2]))
        custom_format = custom_format.replace(
            "%D", ("%02d/%02d/%s" % (tm[1], tm[2], str(tm[0])[(-2):]))
        )
        custom_format = custom_format.replace("%e", ("%d" % tm[2]))
        custom_format = custom_format.replace("%h", mon[tm[1]])
        custom_format = custom_format.replace("%H", ("%02d" % tm[3]))
        if tm[3] in range(13, 23, 1):
            hour = tm[3] - 12
        elif tm[3] == 0:
            hour = 12
        else:
            hour = tm[3]
        custom_format = custom_format.replace("%i", ("%02d" % hour))
        custom_format = custom_format.replace("%j", ("%003d" % tm[7]))
        custom_format = custom_format.replace("%m", ("%02d" % tm[1]))
        custom_format = custom_format.replace("%M", ("%02d" % tm[4]))
        custom_format = custom_format.replace("%n", "\n")
        if tm[3] in range(1, 11, 1):
            am_pm_text = "AM"
        elif tm[3] in range(13, 23, 1):
            am_pm_text = "PM"
        elif tm[3] == 0:
            am_pm_text = "AM"
        else:
            am_pm_text = ""
        custom_format = custom_format.replace("%p", am_pm_text)
        custom_format = custom_format.replace(
            "%r", ("%02d:%02d:%02d %s" % (hour, tm[4], tm[5], am_pm_text))
        )
        custom_format = custom_format.replace("%S", ("%02d" % tm[5]))
        custom_format = custom_format.replace("%t", "\t")
        custom_format = custom_format.replace(
            "%T", ("%02d:%02d:%02d" % (tm[3], tm[4], tm[5]))
        )
        custom_format = custom_format.replace("%u", ("%1d" % int((tm[6] + 1))))
        custom_format = custom_format.replace("%U", ("%02d" % int(((tm[7] + 6) / 7))))
        custom_format = custom_format.replace("%V", ("%02d" % int(((tm[7] + 6) / 7))))
        custom_format = custom_format.replace("%w", ("%1d" % int((tm[6] + 1))))
        custom_format = custom_format.replace("%W", ("%02d" % int(((tm[6] / 7) or 7))))
        custom_format = custom_format.replace("%y", ("%s" % str(tm[0])[(-2):]))
        custom_format = custom_format.replace("%Y", ("%d" % tm[0]))
        if u:
            custom_format = custom_format.replace("%Z", "UTC")
        elif shell.environ.get("TZ"):
            custom_format = custom_format.replace(
                "%Z", ("%s" % shell.environ.get("TZ"))
            )
        elif tzname:
            custom_format = custom_format.replace("%Z", tzname[0])
        else:
            custom_format = custom_format.replace("%Z ", "")
        custom_format = custom_format.replace("%%", "%")
        custom_format = custom_format[1:]
        sys.stdout.write(("%s\n" % custom_format))
    else:
        exit_code += 1
    return 1 if exit_code else 0


parser_df = ArgumentParser(
    name="df - report free disk space",
    description="The df utility shall write the amount of available space and file slots for file systems on which the invoking user has appropriate read access. File systems shall be specified by the file operands; when none are specified, information shall be written for all file systems.The format of the default output from df is unspecified, but all space figures are reported in 512-byte units, unless the -k option is specified. This output shall contain at least the file system names, amount of available space on each of these file systems, and, if no options other than -t are specified, the number of free file slots, or inodes, available; when -t is specified, the output shall contain the total allocated space as well.",
)
parser_df.add_argument(
    "-h",
    dest="human_readable",
    action="store_true",
    default=False,
    help="print sizes in powers of 1024 (e.g., 1023M)",
)
parser_df.add_argument(
    "-k",
    dest="kilo",
    action="store_const",
    const=1024,
    help="use 1024-byte units, instead of the default 512-byte units, when writing space figures.",
)
parser_df.add_argument(
    "-P",
    dest="portability",
    action="store_true",
    default=True,
    help="produce a POSIX output",
)
parser_df.add_argument(
    "-t",
    dest="total",
    action="store_true",
    help="include total allocated-space figures in the output. ",
)
parser_df.add_argument(
    "file",
    nargs="?",
    const=0,
    help="A pathname of a file within the hierarchy of the desired file system. If a file other than a FIFO, a regular file, a directory, or a special file representing the device containing the file system (for example, /dev/dsk/0s1) is specified, the results are unspecified. If the file operand names a file other than a special file containing a file system, df shall write the amount of free space in the file system containing the specified file operand. Otherwise, df shall write the amount of free space in that file system. ",
)

def glxsh_df(file=None, block_size=None, total=None, human_readable=None):
    if block_size is None:
        block_size = 512
    devices_list = []
    if file:
        if not exists(file):
            return "df: %s: No such file or directory" % file
        if (not os.access(file, os.R_OK)) or (
            not os.access(df_find_mount_point(file), os.R_OK)
        ):
            return "df: %s : Permission denied\n" % file
        for line in df_get_devices():
            if df_find_mount_point(file) == line[1]:
                devices_list.append(
                    df_get_device_information(
                        file_system_name=line[0],
                        file_system_root=line[1],
                        block_size=block_size,
                    )
                )
    else:
        for line in df_get_devices():
            devices_list.append(
                df_get_device_information(
                    file_system_name=line[0],
                    file_system_root=line[1],
                    block_size=block_size,
                )
            )
    if devices_list:
        if total:
            (total_space_free, total_space_used, total_total_space) = df_get_totals(
                devices_list
            )
            devices_list.append(
                [
                    "total",
                    total_total_space,
                    total_space_used,
                    total_space_free,
                    (
                        "%d%%"
                        % int(
                            math.ceil(
                                (
                                    100
                                    * (
                                        float((total_total_space - total_space_free))
                                        / total_total_space
                                    )
                                )
                            )
                        )
                    ),
                    "-",
                ]
            )
        (block_size_text, tabular_data) = df_get_info_to_print(
            block_size, devices_list, human_readable
        )
        df_print_final(block_size_text, tabular_data)
        return 0
    else:
        return 1

def df_get_info_to_print(block_size, devices_list, human_readable):
    block_size_text = f"{block_size}-blocks"
    if human_readable:
        tabular_data = []
        block_size_text = "Size"
        for line in devices_list:
            if (
                (str(line[1]) != "-")
                and (str(line[2]) != "-")
                and (str(line[3]) != "-")
            ):
                tabular_data.append(
                    [
                        line[0],
                        size_of(size=(int(line[1]) * block_size), suffix=""),
                        size_of(size=(int(line[2]) * block_size), suffix=""),
                        size_of(size=(int(line[3]) * block_size), suffix=""),
                        line[4],
                        line[5],
                    ]
                )
            else:
                tabular_data.append(line)
    else:
        tabular_data = devices_list
    return (block_size_text, tabular_data)

def df_get_totals(devices_list):
    total_total_space = 0
    total_space_used = 0
    total_space_free = 0
    for device in devices_list:
        try:
            total_total_space += int(device[1])
        except ValueError:
            pass
        try:
            total_space_used += int(device[2])
        except ValueError:
            pass
        try:
            total_space_free += int(device[3])
        except ValueError:
            pass
    return (total_space_free, total_space_used, total_total_space)

def df_print_final(block_size_text, tabular_data):
    sys.stdout.write(
        (
            "%s\n"
            % tabulate(
                tabular_data=tabular_data,
                headers=[
                    "Filesystem",
                    block_size_text,
                    "Used",
                    "Available",
                    "Capacity",
                    "Mounted on",
                ],
                tablefmt="plain",
                colalign=("left", "right", "right", "right", "right", "left"),
            )
        )
    )

def df_find_mount_point(path):
    if not islink(path):
        path = abspath(path)
    elif islink(path) and lexists(os.readlink(path)):
        path = realpath(path)
    if hasattr(os, "path") and hasattr(os.path, "ismount"):
        while not os.path.ismount(path):
            path = dirname(path)
            if islink(path) and lexists(os.readlink(path)):
                path = realpath(path)
    return path

def df_get_device_information(
    file_system_name=None, file_system_root=None, block_size=None
):
    try:
        statvfs = os.statvfs(file_system_root)
        if type(statvfs) == tuple:
            space_free = (statvfs[4] * statvfs[1]) / block_size
            total_space = (statvfs[2] * statvfs[1]) / block_size
        else:
            space_free = (statvfs.f_bavail * statvfs.f_frsize) / block_size
            total_space = (statvfs.f_blocks * statvfs.f_frsize) / block_size
        space_used = total_space - space_free
        if total_space == 0:
            percentage_used = "-"
        else:
            percentage_used = "%d%%" % int(
                math.ceil((100 * (float((total_space - space_free)) / total_space)))
            )
        return [
            ("%s" % file_system_name),
            ("%d" % total_space),
            ("%d" % space_used),
            ("%d" % space_free),
            ("%s" % percentage_used),
            ("%s" % file_system_root),
        ]
    except PermissionError:
        return [
            ("%s" % file_system_name),
            ("%s" % "-"),
            ("%s" % "-"),
            ("%s" % "-"),
            ("%s" % "-"),
            ("%s" % file_system_root),
        ]

def df_get_devices(file=None):
    if (file is None) and exists("/etc/mtab"):
        file = "/etc/mtab"
    if (file is None) and exists("/proc/mounts"):
        file = "/proc/mounts"
    if file is None:
        raise SystemError("Impossible to locate /etc/mtab or /proc/mounts file")
    file_entries = []
    for line in df_get_file_content(file=file).splitlines():
        if len(line.split()) < 4:
            continue
        file_entries.append(line.split())
    return file_entries

def df_get_file_content(file=None):
    if not exists(file):
        raise FileExistsError(f"{file} do not exist")
    if not os.access(file, os.R_OK):
        raise PermissionError(f"{file} can't be read")
    with open(file) as datafile:
        return datafile.read().strip()


parser_dirname = ArgumentParser(
    name="dirname - return the directory portion of a pathname",
    description="The string operand shall be treated as a pathname, as defined in XBD Pathname. The string string shall be converted to the name of the directory containing the filename corresponding to the last pathname component in string.",
)
parser_dirname.add_argument("string", nargs="?", const=0, help="A string")

def glxsh_dirname(string=None):
    try:
        sys.stdout.write(("%s\n" % dirname(string)))
        return 0
    except (Exception, ArithmeticError) as error:
        sys.stderr.write(("dirname: %s\n" % error))
        return 1


parser_du = ArgumentParser(
    name="du - estimate file space usage",
    description="The du utility shall write to standard output the size of the file space allocated to, and the size of the file space allocated to each subdirectory of, the file hierarchy rooted in each of the specified files.",
    synopsis=["du [-a|-s] [-kx] [-H|-L] [file...]"],
    exit_status={"0": "Successful completion.", ">0": "An error occurred."},
)
parser_du.add_argument(
    "-a",
    action="store_true",
    dest="a",
    help="In addition to the default output, report the size of each file not of type directory in the file hierarchy rooted in the specified file. The -a option shall not affect whether non-directories given as file operands are listed.",
)
parser_du.add_argument(
    "-H",
    action="store_true",
    dest="H",
    help="If a symbolic link is specified on the command line, du shall count the size of the file or file hierarchy referenced by the link.",
)
parser_du.add_argument(
    "-k",
    action="store_true",
    dest="k",
    default=False,
    help="Write the files sizes in units of 1024 bytes, rather than the default 512-byte units.",
)
parser_du.add_argument(
    "-L",
    action="store_true",
    dest="L",
    help="If a symbolic link is specified on the command line or encountered during the traversal of a file hierarchy, du shall count the size of the file or file hierarchy referenced by the link.",
)
parser_du.add_argument(
    "-s",
    action="store_true",
    dest="s",
    help="Instead of the default output, report only the total sum for each of the specified files.",
)
parser_du.add_argument(
    "-x",
    action="store_true",
    dest="x",
    help="When evaluating file sizes, evaluate only those files that have the same device as the file specified by the file operand.",
)
parser_du.add_argument(
    "file",
    dest="files",
    nargs="*",
    help="The pathname of a file whose size is to be written. If no file is specified, the current directory shall be used.",
)

def glxsh_du(a, H, k, L, s, x, files):
    exit_code = 0
    if k:
        byte_unit = 1024
    else:
        byte_unit = 512
    if not files:
        files = [getcwd()]
    try:
        for path in files:
            if os.access(path, os.R_OK):
                if islink(path):
                    sys.stdout.write(("%d %s\n" % (os.lstat(path).st_size, path)))
                if isfile(path):
                    sys.stdout.write(
                        (
                            "%d %s\n"
                            % (((os.lstat(path).st_blocks * 512) / byte_unit), path)
                        )
                    )
                have = []
                for directory_path, directory_names, filenames in os.walk(path):
                    for f in filenames:
                        fp = joinpath(directory_path, f)
                        if islink(fp):
                            sys.stdout.write(("%d %s\n" % (os.lstat(fp).st_size, fp)))
                            continue
                        st = os.lstat(fp)
                        if st.st_ino in have:
                            continue
                        have.append(st.st_ino)
                        sys.stdout.write(
                            ("%d %s\n" % (((st.st_blocks * 512) / byte_unit), fp))
                        )
                    for d in directory_names:
                        dp = joinpath(directory_path, d)
                        if islink(dp):
                            sys.stdout.write(("%d %s\n" % (os.lstat(dp).st_size, dp)))
            else:
                sys.stderr.write(("du: %s: '%s'\n" % (error_code_to_text(13), path)))
    except OSError as error:
        sys.stderr.write(("du: %s\n" % error_code_to_text(error.errno)))
        exit_code += 1
    except KeyboardInterrupt:
        sys.stdout.write("\n")
    return exit_code


parser_echo = ArgumentParser(
    name="echo - write arguments to standard output",
    description="The echo utility writes its arguments to standard output, followed by a <newline>. If there are no arguments, only the <newline> is written.",
)
parser_echo.add_argument(
    "-n",
    dest="newline",
    action="store_true",
    help="Suppress the <newline> that would otherwise follow the final argument in the output.",
)
parser_echo.add_argument(
    "string",
    nargs="*",
    type=str,
    help="A string to be written to standard outputself.\n",
)

def glxsh_echo(**kwargs):
    shell = kwargs.get("shell", None)
    newline = kwargs.get("newline", False)
    string = kwargs.get("string", "")
    try:
        value_to_return = str(string)
        if string.startswith('"') and string.endswith('"'):
            value_to_return = string[1:][:(-1)]
            for value in value_to_return.split(" "):
                if value.startswith("$"):
                    value_to_return = value_to_return.replace(
                        value, shell.environ.get(value.replace("$", ""), "")
                    )
        if string.startswith("$") and (" " not in string):
            value_to_return = string.replace(
                string, shell.environ.get(string.replace("$", ""), "")
            )
        sys.stdout.write(value_to_return)
        if not newline:
            sys.stdout.write("\n")
        return 0
    except (Exception, BaseException) as error:
        sys.stderr.write(error)
        return 1


parser_env = ArgumentParser(
    name="env - set the environment for command invocation",
    description="The env utility shall obtain the current environment, modify it according to its arguments, then invoke the utility named by the utility operand with the modified environment.",
)
parser_env.add_argument(
    "-i",
    dest="invoke",
    action="store_true",
    help="Invoke utility with exactly the environment specified by the arguments; the inherited environment shall be ignored completely.",
)
parser_env.add_argument(
    "name",
    nargs="?",
    dest="name",
    help="Arguments of the form name= value shall modify the execution environment, and shall be placed into the inherited environment before the utility is invoked.",
)
parser_env.add_argument(
    "utility",
    nargs="?",
    dest="utility",
    help="The name of the utility to be invoked. If the utility operand names any of the special built-in utilities in Special Built-In Utilities, the results are undefined.",
)
parser_env.add_argument(
    "argument",
    nargs="?",
    dest="argument",
    help="A string to pass as an argument for the invoked utility.",
)

def glxsh_env(name, utility, argument, shell):
    if shell and hasattr(shell, "environ"):
        if name:
            try:
                func = getattr(shell, ("do_" + utility))
                return func(argument)
            except AttributeError:
                try:
                    pr = subprocess.run(utility, argument, env=shell.environ)
                    return pr.returncode
                except (Exception, BaseException):
                    return shell.default(utility)
        else:
            for name, value in shell.environ.items():
                sys.stdout.write(("%s=%s\n" % (name, value)))
            return 0


parser_exit = ArgumentParser(
    name="exit", description="exit shell with a given exit code"
)
parser_exit.add_argument("code", nargs="*", type="int", help="exit code")

def glxsh_exit(*args, **kwargs):
    shell = kwargs.get("shell", None)
    code = kwargs.get("code", None)
    if (code is None) or (not code):
        code = 0
    else:
        code = code[0]
    if shell:
        shell.exit_code = code
        sys.exit(code)
    else:
        return code

parser_false = ArgumentParser(
    name="false - return false value",
    synopsis=["false"],
    description="The false utility shall return with a non-zero exit code.",
    exit_status={"1": ""},
)

def glxsh_false():
    return 1


parser_head = ArgumentParser(
    name="head - copy the first part of",
    description="The head utility shall copy its input files to the standard output, ending the output for each file at a designated point. ",
)
parser_head.add_argument(
    "file",
    nargs="*",
    help="A pathname of an input file. If no file operands are specified, the standard input shall be used.",
)
parser_head.add_argument(
    "-n",
    dest="number",
    type=int,
    default=10,
    help="The first number lines of each input file shall be copied to standard output. ",
)

def glxsh_head(files, number=10):
    if isinstance(number, int) and (number < 1):
        return 0
    if (files is None) or (not isinstance(files, list)) or (files == []):
        files = ["-"]

    def read_stdin():
        stdin_count = 1
        while stdin_count <= number:
            data = sys.stdin.readline()
            if not data:
                break
            (yield data)
            stdin_count += 1
    try:
        count = 0
        for file in files:
            filename = file
            if file == "-":
                filename = "standard input"
            if (count == 0) and (len(files) > 1):
                sys.stdout.write(("==> %s <==\n" % filename))
            elif count > 0:
                sys.stdout.write(("\n==> %s <==\n" % filename))
            if file == "-":
                try:
                    for piece in read_stdin():
                        sys.stdout.write(piece)
                except KeyboardInterrupt:
                    sys.stdout.write("\n")
                    return 130
            else:
                with open(file) as f:
                    for _ in range(number):
                        line = f.readline()
                        if not line:
                            break
                        sys.stdout.write(line)
            count += 1
        return 0
    except (Exception, ArithmeticError) as error:
        sys.stderr.write(("head: %s\n" % error))
        return 1


parser_ls = ArgumentParser(
    name="ls - list directory contents",
    description="List information about the files (the current directory by default).\nSort entries alphabetically if none of -cftuvSUX is specified.",
    synopsis=[
        "ls [-ikqrs] [-glno] [-A|-a] [-C|-m|-x|-1] [-F|-p] [-H|-L] [-R|-d] [-S|-f|-t] [-c|-u] [file...]"
    ],
)
parser_ls.add_argument(
    "-A", action="store_true", dest="A", help="Do not list implied . and .."
)
parser_ls.add_argument(
    "-C", action="store_true", dest="C", help="List entries by columns"
)
parser_ls.add_argument(
    "-F",
    dest="F",
    action="store_true",
    help="Append indicator (one of */=>@|) to entries",
)
parser_ls.add_argument(
    "-H",
    dest="H",
    action="store_true",
    help="Follow symbolic links listed on the command line",
)
parser_ls.add_argument(
    "-L",
    dest="L",
    action="store_true",
    help="when showing file information for a symbolic link, show information for the file the link references rather than for the link itself",
)
parser_ls.add_argument(
    "-R", dest="recurse", action="store_true", help="List subdirectories recursively"
)
parser_ls.add_argument(
    "-S", dest="S", action="store_true", help="sort by file size, largest first"
)
parser_ls.add_argument(
    "-a", dest="a", action="store_true", help="do not ignore entries starting with ."
)
parser_ls.add_argument(
    "-c",
    dest="c",
    action="store_true",
    help="with -lt: sort by, and show, ctime (time of last modification of file status information); otherwise: sort by ctime, newest first list entries by columns",
)
parser_ls.add_argument(
    "-d",
    dest="d",
    action="store_true",
    help="list directories themselves, not their contents",
)
parser_ls.add_argument(
    "-f",
    dest="f",
    action="store_true",
    help="do not sort, enable -aU, disable -ls --color",
)
parser_ls.add_argument(
    "-g", dest="g", action="store_true", help="group directories before files;"
)
parser_ls.add_argument(
    "-i", dest="i", action="store_true", help="print the index number of each file"
)
parser_ls.add_argument(
    "-k",
    dest="k",
    action="store_true",
    help="default to 1024-byte blocks for disk usage; used only with -s and per directory totals",
)
parser_ls.add_argument(
    "-l", dest="l", action="store_true", help="use a long listing format"
)
parser_ls.add_argument(
    "-m",
    dest="m",
    action="store_true",
    help="fill width with a comma separated list of entries",
)
parser_ls.add_argument(
    "-n",
    dest="n",
    action="store_true",
    help="like -l, but list numeric user and group IDs",
)
parser_ls.add_argument(
    "-o",
    dest="o",
    action="store_true",
    help="like -l, but do not list group information",
)
parser_ls.add_argument(
    "-p", dest="p", action="store_true", help="append / indicator to directories"
)
parser_ls.add_argument(
    "-q", dest="q", action="store_true", help="enclose entry names in double quotes"
)
parser_ls.add_argument(
    "-r", dest="r", action="store_true", help="reverse order while sorting"
)
parser_ls.add_argument(
    "-s",
    dest="s",
    action="store_true",
    help="print the allocated size of each file, in blocks",
)
parser_ls.add_argument(
    "-t", dest="t", action="store_true", help="sort by time, newest first"
)
parser_ls.add_argument(
    "-u",
    dest="u",
    action="store_true",
    help="with -lt: sort by, and show, access time; with -l: show access time and sort by name; otherwise: sort by access time, newest first",
)
parser_ls.add_argument(
    "-x",
    dest="x",
    action="store_true",
    help="list entries by lines instead of by columns",
)
parser_ls.add_argument(
    "-1",
    dest="one",
    action="store_true",
    help="list one file per line.  Avoid '\n' with -q or -b",
)
parser_ls.add_argument(
    "file",
    nargs="*",
    help="A pathname of a file to be written. If the file specified is not found, a diagnostic message shall be output on standard error.",
)

def glxsh_ls(
    A=None,
    C=None,
    F=None,
    H=None,
    L=None,
    recurse=None,
    S=None,
    a=None,
    c=None,
    d=None,
    f=None,
    g=None,
    i=None,
    k=None,
    l=None,
    m=None,
    n=None,
    o=None,
    p=None,
    q=None,
    r=None,
    s=None,
    t=None,
    u=None,
    x=None,
    one=None,
    file=None,
    **kwargs
):
    def _print_long_format(list_to_display):
        tabular_data = []
        for pathname in list_to_display:
            lstat = os.stat(pathname)
            tabular_data.append(
                [
                    ("%s" % filemode(lstat.st_mode)),
                    ("%u" % lstat.st_nlink),
                    ("%s" % getpwuid(lstat.st_uid)[0]),
                    ("%s" % getgrgid(lstat.st_gid)[0]),
                    ("%u" % lstat.st_mode),
                    (
                        "%s"
                        % time.strftime("%b %d %H:%M", time.localtime(lstat.st_mtime))
                    ),
                    ("%s" % _add_slash_if_is_dir(pathname)),
                ]
            )
        sys.stdout.write(
            (
                "%s\n"
                % tabulate(
                    tabular_data=tabular_data,
                    headers=[],
                    tablefmt="plain",
                    colalign=(
                        "left",
                        "right",
                        "right",
                        "right",
                        "left",
                        "right",
                        "left",
                    ),
                )
            )
        )

    def _add_slash_if_is_dir(item):
        if p and isdir(item) and (not item.endswith("/")):
            return "%s/" % item
        return item
    exit_code = 0
    stdout = kwargs.get("stdout", sys.stdout)
    stdin = kwargs.get("stdin", sys.stdin)
    stderr = kwargs.get("stderr", sys.stderr)
    shell = kwargs.get("shell") or None
    _files_to_look = []
    if not file:
        if recurse:
            _files_to_look = ["**/*"]
        else:
            _files_to_look = ["*"]
    if file:
        for _file in file:
            if isdir(_file):
                if recurse:
                    _files_to_look.append(("%s/**/*" % _file))
                else:
                    _files_to_look.append(("%s/*" % _file))
            else:
                _files_to_look.append(_file)
    for pathname in _files_to_look:
        try:
            list_to_display = []
            dir_scan = glob(pathname)
            if a:
                dir_scan.insert(0, "..")
                dir_scan.insert(0, ".")
            for f in dir_scan:
                if F:
                    if isdir(("%s/%s" % (pathname, f))):
                        f = "%s/" % f
                    elif os.access(("%s/%s" % (pathname, f)), os.X_OK):
                        f = "%s*" % f
                    elif islink(("%s/%s" % (pathname, f))):
                        f = "%s@" % f
                if A or a:
                    if A:
                        if (f != ".") and (f != ".."):
                            list_to_display.append(f)
                    else:
                        list_to_display.append(f)
                elif not f.startswith("."):
                    list_to_display.append(f)
            if C and (not l):
                columnize(list_to_display)
            elif l:
                _print_long_format(list_to_display)
            else:
                for f in list_to_display:
                    f = _add_slash_if_is_dir(f)
                    sys.stdout.write(("%s\n" % f))
        except (Exception, ArithmeticError) as error:
            sys.stderr.write(("ls: %s: '%s'\n" % (error, pathname)))
            exit_code += 1
    return exit_code


parser_mkdir = ArgumentParser(
    name="mkdir - make directories",
    description="The mkdir utility shall create the directories specified by the operands",
)
parser_mkdir.add_argument(
    "-p",
    dest="parents",
    action="store_true",
    help="Create any missing intermediate pathname components.",
)
parser_mkdir.add_argument(
    "-m",
    dest="mode",
    nargs="?",
    type=str,
    default="755",
    help="Set the file permission bits of the newly-created directory to the specified mode value.",
)
parser_mkdir.add_argument(
    "dir", nargs="+", help="A pathname of a directory to be created."
)

def glxsh_mkdir(directories=None, parents=False, mode="755"):
    exit_code = 0

    def make_directory(path, path_mode):
        try:
            from os import mkdir

            try:
                mkdir(path=path, mode=path_mode)
            except TypeError:
                mkdir(path)
        except ImportError as error:
            sys.stderr.write(("mkdir: '%s'\n" % error))
        except OSError as error:
            sys.stderr.write(
                ("mkdir: '%s': %s\n" % (path, error_code_to_text(error.errno)))
            )
            return 1
        return 0
    for directory in directories:
        if parents:
            if directory.startswith(sep):
                directory_to_create = sep
            else:
                directory_to_create = ""
            for sub_directory in directory.split(sep):
                if directory_to_create == sep:
                    directory_to_create = "%s%s" % (directory_to_create, sub_directory)
                elif (directory_to_create != "") and (sub_directory != ""):
                    directory_to_create = joinpath(directory_to_create, sub_directory)
                elif sub_directory == "":
                    continue
                elif sub_directory == ".":
                    directory_to_create = "."
                    continue
                elif sub_directory == "..":
                    directory_to_create = ".."
                    continue
                else:
                    directory_to_create = sub_directory
                exit_code += make_directory(directory_to_create, mode)
        else:
            exit_code += make_directory(directory, mode)
    return 1 if exit_code else 0


parser_mv = ArgumentParser(
    name="mv - move files",
    description="The mv utility shall move the file named by the source_file operand to the destination specified by the target_file. This first synopsis form is assumed when the final operand does not name an existing directory and is not a symbolic link referring to an existing directory. In this case, if source_file names a non-directory file and target_file ends with a trailing <slash> character, mv shall treat this as an error and no source_file operands will be processed.",
)
parser_mv.add_argument(
    "source_file", nargs="?", help="A pathname of a file or directory to be moved."
)
parser_mv.add_argument(
    "target_file",
    nargs="?",
    help="A new pathname for the file or directory being moved.",
)
parser_mv.add_argument(
    "target_dir",
    nargs="?",
    help="A pathname of an existing directory into which to move the input files.",
)
parser_mv.add_argument(
    "-f",
    dest="force",
    action="store_true",
    default=False,
    help="Do not prompt for confirmation if the destination path exists. Any previous occurrence of the -i option is ignored.",
)
parser_mv.add_argument(
    "-i",
    dest="interactive",
    action="store_true",
    default=False,
    help="Prompt for confirmation if the destination path exists. Any previous occurrence of the -f option is ignored.",
)

def glxsh_mv(
    source_file=None, target_file=None, target_dir=None, force=None, interactive=None
):
    if interactive and exists(target_file):
        sys.stdout.write(("do you want to overwrite %s file ? (Y/n) " % target_file))
        sys.stdout.flush()
        if sys.stdin.readline().upper().startswith("N"):
            return 0
    try:
        if os.access(source_file, os.F_OK):
            os.rename(source_file, target_file)
            return 0
        else:
            return 1
    except Exception as error:
        sys.stderr.write(("mv: %s\n" % error))
        return 1


parser_pwd = ArgumentParser(
    name="pwd - return working directory name",
    description="The pwd utility shall write to standard output an absolute pathname of the current working directory, which does not contain the filenames dot or dot-dot.",
)
parser_pwd.add_argument(
    "-L",
    dest="logical",
    action="store_true",
    default=False,
    help="Print the value of $PWD if it names the current working directory",
)
parser_pwd.add_argument(
    "-P",
    dest="physical",
    action="store_true",
    default=False,
    help="Print the physical directory, without any symbolic links",
)

def glxsh_pwd(logical=None, physical=None):
    if (not logical) and (not physical):
        logical = True
    try:
        if logical:
            sys.stdout.write(("%s\n" % normpath(os.getcwd())))
        else:
            sys.stdout.write(("%s\n" % realpath(os.getcwd())))
        return 0
    except (Exception, ArithmeticError) as error:
        sys.stderr.write(("pwd: %s\n" % error))
        return 1


parser_rm = ArgumentParser(
    name="rm - remove directory entries",
    description="The rm utility shall remove the directory entry specified by each file argument.\n\nIf either of the files dot or dot-dot are specified as the basename portion of an operand (that is, the final pathname component) or if an operand resolves to the root directory, rm shall write a diagnostic message to standard error and do nothing more with such operands.",
)
parser_rm.add_argument(
    "-i",
    dest="interactive",
    action="store_true",
    help="Prompt for confirmation as described previously. Any previous occurrences of the -f option shall be ignored.",
)
parser_rm.add_argument(
    "-R",
    "-r",
    dest="recursive",
    action="store_true",
    help="Remove file hierarchies. See the DESCRIPTION.",
)
parser_rm.add_argument(
    "-f",
    dest="force",
    action="store_true",
    help="Do not prompt for confirmation. Do not write diagnostic messages or modify the exit status in the case of no file operands, or in the case of operands that do not exist. Any previous occurrences of the -i option shall be ignored.",
)
parser_rm.add_argument(
    "file", nargs="+", help="A pathname of a directory entry to be removed."
)

def glxsh_rm(file=None, recursive=None, interactive=None, force=None):
    exit_code = 0
    if force:
        interactive = False

    def _rm(path):
        try:
            os.remove(path)
            return 0
        except OSError as error:
            sys.stderr.write(
                ("rm: %s: '%s'\n" % (error_code_to_text(error.errno), path))
            )
            return 1
        except (Exception, BaseException) as error:
            sys.stderr.write(("chmod: %s: '%s'\n" % (error, path)))
            return 1
    for path in file:
        if recursive:
            for dirpath, dirnames, filenames in os.walk(path):
                for dname in dirnames:
                    if interactive:
                        if (
                            input(
                                (
                                    "do you want to remove %s directory ? (Y/n)"
                                    % joinpath(dirpath, dname)
                                )
                            )
                            .upper()
                            .startswith("Y")
                        ):
                            exit_code += _rm(joinpath(dirpath, dname))
                    else:
                        exit_code += _rm(joinpath(dirpath, dname))
                for fname in filenames:
                    if interactive:
                        if (
                            input(
                                (
                                    "do you want to remove %s file ? (Y/n)"
                                    % joinpath(dirpath, fname)
                                )
                            )
                            .upper()
                            .startswith("Y")
                        ):
                            exit_code += _rm(joinpath(dirpath, fname))
                    else:
                        exit_code += _rm(joinpath(dirpath, fname))
        elif interactive:
            if (
                input(("do you want to remove %s file ? (Y/n)" % path))
                .upper()
                .startswith("Y")
            ):
                exit_code += _rm(path)
        else:
            exit_code += _rm(path)
    return 1 if exit_code else 0


parser_rmdir = ArgumentParser(
    name="rmdir - remove directories",
    description="The rmdir utility shall remove the directory entry specified by each dir operand.\n\nDirectories shall be processed in the order specified. If a directory and a subdirectory of that directory are specified in a single invocation of the rmdir utility, the application shall specify the subdirectory before the parent directory so that the parent directory will be empty when the rmdir utility tries to remove it.",
)
parser_rmdir.add_argument(
    "dir", dest="dir", nargs="*", help="A pathname of an empty directory to be removed."
)
parser_rmdir.add_argument(
    "-p",
    dest="parents",
    action="store_true",
    default=False,
    help="Remove all directories in a pathname.",
)

def glxsh_rmdir(directories=None, parents=False):
    exit_code = 0

    def rmdir(d):
        try:
            os.rmdir(path=d)
            return 0
        except (Exception, ArithmeticError) as error:
            sys.stderr.write(
                ("rmdir: %s: '%s'\n" % (error_code_to_text(error.errno), d))
            )
            return 1
    for directory in directories:
        if exists(directory) and parents:
            for path, _, files in os.walk(directory, False):
                for f in files:
                    os.unlink(((path + "/") + f))
                exit_code += rmdir(path)
        else:
            exit_code += rmdir(directory)
    return 1 if exit_code else 0


parser_sleep = ArgumentParser(
    name="sleep - suspend execution for an interval",
    description="The sleep utility shall suspend execution for at least the integral number of seconds specified by the time operand. ",
)
parser_sleep.add_argument(
    "time",
    default=0,
    help="A non-negative decimal integer or float specifying the number of seconds for which to suspend execution.",
)

def glxsh_sleep(sec):
    exit_code = 0

    def string_to_numeric_if_possible(x):
        try:
            val = float(x)
            return int(val) if (val == int(val)) else val
        except (TypeError, ValueError):
            return x
    try:
        time.sleep(string_to_numeric_if_possible(sec))
    except (Exception, ArithmeticError) as error:
        sys.stderr.write(("sleep: %s\n" % error))
        exit_code += 1
    except KeyboardInterrupt:
        sys.stdout.write("\n")
        exit_code += 1
    return exit_code


parser_tail = ArgumentParser(
    name="tail - copy the last part of a file",
    synopsis=["tail [-f] [-c number|-n number] [file]"],
    description="The tail utility shall copy its input file to the standard output beginning at a designated place.\n\nCopying shall begin at the point in the file indicated by the -c number or -n number options. The option-argument number shall be counted in units of lines or bytes, according to the options -n and -c. Both line and byte counts start from 1.",
)
parser_tail.add_argument(
    "-f",
    dest="f",
    action="store_true",
    default=False,
    help="If the input file is a regular file or if the file operand specifies a FIFO, do not terminate after the last line of the input file has been copied, but read and copy further bytes from the input file when they become available. If no file operand is specified and standard input is a pipe or FIFO, the -f option shall be ignored. If the input file is not a FIFO, pipe, or regular file, it is unspecified whether or not the -f option shall be ignored.",
)
parser_tail.add_argument(
    "-c",
    dest="c",
    type=str,
    help="The origin for counting shall be 1; that is, -c +1 represents the first byte of the file, -c -1 the last.",
)
parser_tail.add_argument(
    "-n",
    dest="n",
    type=str,
    help="This option shall be equivalent to -c number, except the starting location in the file shall be measured in lines instead of bytes. The origin for counting shall be 1; that is, -n +1 represents the first line of the file, -n -1 the last.",
)
parser_tail.add_argument(
    "file",
    nargs="*",
    type=FileType("r"),
    help="A pathname of an input file. If no file operand is specified, the standard input shall be used.",
)

def glxsh_tail(c, f, n, files):
    def follow(file, sleep_sec=0.1) -> Iterator[str]:
        line = ""
        while True:
            tmp = file.readline()
            if tmp is not None:
                line += tmp
                if line.endswith("\n"):
                    (yield line)
                    line = ""
            elif sleep_sec:
                sleep(sleep_sec)
    try:
        if (files is None) or (files == []):
            files = ["-"]
        if f:
            for file in files:
                if file == "-":
                    file = sys.stdin
                with open(file, "r") as fd:
                    loglines = follow(fd)
                    for line in loglines:
                        sys.stdout.write(("%s" % line))
            return 0
    except OSError as error:
        sys.stderr.write(("tail: %s\n" % error_code_to_text(error.errno)))
        return 1
    except KeyboardInterrupt:
        sys.stdout.write("\n")
        return 0


parser_tee = ArgumentParser(
    name="tee - duplicate standard input",
    synopsis=["tee [-ai] [file...]"],
    description="The tee utility shall copy standard input to standard output, making a copy in zero or more files. The tee utility shall not buffer output.\n\nIf the -a option is not specified, output files shall be written.",
    exit_status={
        "0": "The standard input was successfully copied to all output files.",
        ">0": "An error occurred.",
    },
)
parser_tee.add_argument(
    "-a",
    dest="a",
    action="store_true",
    default=False,
    help="Append the output to the files.",
)
parser_tee.add_argument(
    "-i", dest="i", action="store_true", default=False, help="Ignore the SIGINT signal."
)
parser_tee.add_argument(
    "file",
    nargs="*",
    type=FileType("r"),
    help="A pathname of an output file. If a file operand is '-', it refer to a file named '-'",
)

def glxsh_tee(a=None, i=None, files=None):
    a: bool
    i: bool
    files: list
    if a is True:
        mode = "a"
    else:
        mode = "w"
    exit_code = 0
    opened_files = []
    if files:
        for file in files:
            try:
                opened_files.append(open(file, mode))
            except (Exception, BaseException) as error:
                sys.stderr.write(
                    ("tee: %s: '%s'\n" % (error_code_to_text(error.errno), file))
                )
                exit_code += 1

    def read_stdin(file_object):
        while True:
            data = file_object.readline()
            if not data:
                break
            (yield data)

    def process_data(data):
        sys.stdout.write(piece)
        for opened_file in opened_files:
            opened_file.write(piece)
            opened_file.flush()

    def close_data():
        try:
            for opened_file in opened_files:
                opened_file.flush()
                opened_file.close()
            return 0
        except (Exception, BaseException) as err:
            sys.stderr.write(
                ("tee: %s: '%s'\n" % (error_code_to_text(err.errno), file))
            )
            return 1
    try:
        for piece in read_stdin(sys.stdin):
            process_data(piece)
    except KeyboardInterrupt:
        exit_code += close_data()
        return 1 if exit_code else 0
    finally:
        exit_code += close_data()
        return 1 if exit_code else 0


parser_time = ArgumentParser(
    name="time - time a simple command",
    description="The time utility shall invoke the utility named by the utility operand with arguments supplied as the argument operands and write a message to standard error that lists timing statistics for the utility. ",
    synopsis=["time [-p] utility [argument...]"],
    exit_status={
        "1-125": "An error occurred in the time utility.",
        "126": "The utility specified by utility was found but could not be invoked.",
        "127": "The utility specified by utility could not be found.",
    },
)
parser_time.add_argument(
    "-p",
    dest="p",
    action="store_true",
    help="Write the timing output to standard error",
)
parser_time.add_argument(
    "utility", nargs="?", help="The name of a utility that is to be invoked."
)
parser_time.add_argument(
    "argument",
    nargs="?",
    help="Any string to be supplied as an argument when invoking the utility named by the utility operand.",
)

def glxsh_time(p=None, utility=None, argument=None, line=None, shell=None):
    from os import times
    from time import time

    exit_code = 0
    en_time = times()
    start = time()
    exit_code = shell.onecmd(line)
    en_time = times()
    sys.stderr.write(
        (
            "real %f\nuser %f\nsys %f\n"
            % ((time() - start), en_time.user, en_time.system)
        )
    )
    sys.stderr.flush()
    return exit_code


parser_touch = ArgumentParser(
    name="touch - change file access and modification times",
    description="The touch utility shall change the last data modification timestamps, the last data access timestamps, or both.\n\nThe time used can be specified by the -t time option-argument, the corresponding time fields of the file referenced by the -r ref_file option-argument, or the -d date_time option-argument, as specified in the following sections. If none of these are specified, touch shall use the current time.",
    synopsis=["touch [-acm] [-r ref_file|-t time|-d date_time] file..."],
    exit_status={
        "0": "The utility executed successfully and all requested changes were made.",
        ">0": "An error occurred.",
    },
)
parser_touch.add_argument(
    "-a",
    action="store_true",
    default=False,
    help="Change the access time of file. Do not change the modification time unless -m is also specified.",
)
parser_touch.add_argument(
    "-c",
    action="store_true",
    default=False,
    help="Do not create a specified file if it does not exist. Do not write any diagnostic messages concerning this condition.",
)
parser_touch.add_argument(
    "-m",
    action="store_true",
    default=False,
    help="Change the modification time of file. Do not change the access time unless -a is also specified.",
)
parser_touch.add_argument(
    "-d", nargs="?", help="Use the specified date_time instead of the current time"
)
parser_touch.add_argument(
    "-r",
    nargs="?",
    help="Use the corresponding time of the file named by the pathname ref_file instead of the current time.",
)
parser_touch.add_argument(
    "-t",
    nargs="?",
    help="Use the specified time instead of the current time. The option-argument shall be a decimal number of the form",
)
parser_touch.add_argument(
    "file",
    nargs="+",
    help="A pathname of a file whose times shall be modified.",
    type=FileType("w"),
)

def glxsh_touch(a=None, c=None, d=None, m=None, r=None, t=None, files=None):
    exit_code = 0
    if d:
        if is_iso8601(d) is False:
            sys.stderr.write("-d argument is not a valid iso8601 format\n")
        return 1
    if files is None:
        files = []
    for file in files:
        if exists(file):
            try:
                if r:
                    os.utime(file, ns=(os.stat(r).st_atime_ns, os.stat(r).st_mtime_ns))
                elif d:
                    os.utime(file, ns=(time.time_ns(), parse_date(d).timetuple()))
                elif (a is True) and (m is False):
                    os.utime(file, ns=(time.time_ns(), os.stat(file).st_mtime_ns))
                elif (a is False) and (m is True):
                    os.utime(file, ns=(os.stat(file).st_atime_ns, time.time_ns()))
                else:
                    os.utime(file, None)
            except OSError as error:
                sys.stderr.write(
                    ("touch: %s: '%s'\n" % (error_code_to_text(error.errno), file))
                )
                exit_code += 1
        elif c is False:
            try:
                with open(file, "w"):
                    pass
                if r:
                    os.utime(file, ns=(os.stat(r).st_atime_ns, os.stat(r).st_mtime_ns))
                elif d:
                    os.utime(file, ns=(time.time_ns(), parse_date(d).timetuple()))
                elif (a is True) and (m is False):
                    os.utime(file, ns=(time.time_ns(), os.stat(file).st_mtime_ns))
                elif (a is False) and (m is True):
                    os.utime(file, ns=(os.stat(file).st_atime_ns, time.time_ns()))
                else:
                    os.utime(file, None)
            except OSError as error:
                sys.stderr.write(
                    ("touch: %s: '%s'\n" % (error_code_to_text(error.errno), file))
                )
                exit_code += 1
    return 1 if exit_code else 0

parser_true = ArgumentParser(
    name="true - return true value",
    synopsis=["true"],
    description="The true utility shall return with exit code zero.",
    exit_status={"0": ""},
)

def glxsh_true():
    return 0


parser_tty = ArgumentParser(
    name="tty - return user's terminal name",
    description="The tty utility shall write to the standard output the name of the terminal that is open as standard input.",
)

def glxsh_tty():
    try:
        sys.stdout.write(("%s\n" % os.ttyname(sys.stdin.fileno())))
        return 0
    except OSError:
        sys.stdout.write("not a tty\n")
        return 1
    except (Exception, ArithmeticError) as error:
        sys.stderr.write(("tty: %s\n" % error_code_to_text(error.errno)))
        return 1


def symbolic_matcher():
    return re.compile("([ugo]*|a)([+-=])([^\\s,]*)")

order = "rwx"
name_to_value = {"x": 1, "w": 2, "r": 4}
value_to_name = {v: k for (k, v) in name_to_value.items()}
class_to_loc = {"u": 6, "g": 3, "o": 0}
loc_to_class = {v: k for (k, v) in class_to_loc.items()}
function_map = {
    "+": (lambda orig, new: (orig | new)),
    "-": (lambda orig, new: (orig & (~new))),
    "=": (lambda orig, new: new),
}

def invert(perms):
    return 511 - perms

def get_oct_digits(mode):
    if not (0 <= mode <= 511):
        raise ValueError("expected a value between 000 and 777")
    return {"u": ((mode & 448) >> 6), "g": ((mode & 56) >> 3), "o": (mode & 7)}

def from_oct_digits(digits):
    o = 0
    for c, m in digits.items():
        o |= m << class_to_loc[c]
    return o

def get_symbolic_rep_single(digit):
    o = ""
    for sym in "rwx":
        num = name_to_value[sym]
        if digit & num:
            o += sym
            digit -= num
    return o

def get_symbolic_rep(number):
    digits = get_oct_digits(number)
    return "u=%s,g=%s,o=%s" % (
        get_symbolic_rep_single(digits["u"]),
        get_symbolic_rep_single(digits["g"]),
        get_symbolic_rep_single(digits["o"]),
    )

def get_numeric_rep_single(rep):
    o = 0
    for sym in set(rep):
        o += name_to_value[sym]
    return o

parser_umask = ArgumentParser(
    name="umask - get or set the file mode creation mask",
    description="The umask utility shall set the file mode creation mask of the current shell execution environment (see Shell Execution Environment) to the value specified by the mask operand. This mask shall affect the initial value of the file permission bits of subsequently created files. If umask is called in a subshell or separate utility execution environment, such as one of the following:\n\n(umask 002)\nnohup umask ...\nfind . -exec umask ... \\;\n\nit shall not affect the file mode creation mask of the caller's environment.\n\nIf the mask operand is not specified, the umask utility shall write to standard output the value of the file mode creation mask of the invoking process.\n",
)
parser_umask.add_argument(
    "mask",
    nargs="?",
    const=0,
    help="A string specifying the new file mode creation mask. The string is treated in the same way as the mode operand described in the EXTENDED DESCRIPTION section for chmod.\nFor a symbolic_mode value, the new value of the file mode creation mask shall be the logical complement of the file permission bits portion of the file mode specified by the symbolic_mode string.\n\nIn a symbolic_mode value, the permissions op characters '+' and '-' shall be interpreted relative to the current file mode creation mask; '+' shall cause the bits for the indicated permissions to be cleared in the mask; '-' shall cause the bits for the indicated permissions to be set in the mask.\n\nThe interpretation of mode values that specify file mode bits other than the file permission bits is unspecified.\n\nIn the octal integer form of mode, the specified bits are set in the file mode creation mask.\n\nThe file mode creation mask shall be set to the resulting numeric value.\n\nThe default output of a prior invocation of umask on the same system with no operand also shall be recognized as a mask operand.\n",
)
parser_umask.add_argument(
    "-S",
    dest="symbolic",
    action="store_true",
    default=False,
    help="Produce symbolic output.",
)

def single_symbolic_arg(arg, old=None):
    if old is None:
        old = os.umask(0)
        os.umask(old)
    match = symbolic_matcher.match(arg)
    if not match:
        raise ValueError(("could not parse argument %r" % arg))
    (class_, op, mask) = match.groups()
    if class_ == "a":
        class_ = "ugo"
    invalid_chars = [i for i in mask if (i not in name_to_value)]
    if invalid_chars:
        raise ValueError(("invalid mask %r" % mask))
    digits = get_oct_digits(old)
    new_num = get_numeric_rep_single(mask)
    for c in set(class_):
        digits[c] = function_map[op](digits[c], new_num)
    return from_oct_digits(digits)

def valid_numeric_argument(x):
    try:
        return (len(x) == 3) and all(((0 <= int(i) <= 7) for i in x))
    except:
        return False

def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]
    for permissions in [int(n) for n in str(octal)]:
        for value, letter in value_letters:
            if permissions >= value:
                result += letter
                permissions -= value
            else:
                result += "-"
    return result

def glxsh_umask(mask=None, symbolic=True):
    cur = os.umask(0)
    os.umask(cur)
    if mask:
        print(cur)
        print(mask)
        sys.stdout.write(
            ("%s\n" % oct((511 - symbolic_mode(mask, umask=cur, isdir=0))))
        )
        return 0
    else:
        if symbolic:
            sys.stdout.write(("%s\n" % get_symbolic_rep(invert(cur))))
            sys.stdout.write(("%s\n" % octal_to_string(invert(cur))))
            return 0
        else:
            to_print = oct(cur)[2:]
            while len(to_print) < 3:
                to_print = "0%s" % to_print
        sys.stdout.write(("%s\n" % to_print))
        return 0


parser_unalias = ArgumentParser(
    name="unalias - remove alias definitions",
    description="The unalias utility shall remove the definition for each alias name specified.",
    synopsis=["unalias alias-name..."],
    exit_status={
        "0": "Successful completion.",
        ">0": "One of the alias-name operands specified did not represent a valid alias definition, or an error occurred.",
    },
)
parser_unalias.add_argument(
    "-a",
    dest="a",
    action="store_true",
    help="Remove all alias definitions from the current shell execution environment.",
)
parser_unalias.add_argument(
    "alias-name",
    dest="alias_name",
    nargs="*",
    type=str,
    help="The name of an alias to be removed.",
)

def glxsh_unalias(a=None, alias_name=None, shell=None):
    exit_code = 0
    try:
        if a:
            shell.alias = {}
        else:
            for alias in alias_name:
                if alias in shell.alias:
                    del shell.alias[alias]
                else:
                    exit_code += 1
        return exit_code
    except (Exception, BaseException) as error:
        sys.stderr.write(("alias: %s\n" % error))
        return 1


parser_uname = ArgumentParser(
    name="uname - return system name",
    description="By default, the uname utility shall write the operating system name to standard output. When options are specified, symbols representing one or more system characteristics shall be written to the standard output.",
)
parser_uname.add_argument(
    "-a",
    dest="all",
    action="store_true",
    help="Behave as though all of the options -mnrsv were specified.",
)
parser_uname.add_argument(
    "-s",
    dest="sysname",
    action="store_true",
    help="Write the name of the implementation of the operating system.",
)
parser_uname.add_argument(
    "-n",
    dest="nodename",
    action="store_true",
    help="Write the name of this node within an implementation-defined communications network.",
)
parser_uname.add_argument(
    "-r",
    dest="release",
    action="store_true",
    help="Write the current release level of the operating system implementation.",
)
parser_uname.add_argument(
    "-v",
    action="store_true",
    dest="version",
    help="Write the current version level of this release of the operating system implementation.",
)
parser_uname.add_argument(
    "-m",
    dest="machine",
    action="store_true",
    help="Write the name of the hardware type on which the system is running.",
)

def glxsh_uname(
    all=False,
    sysname=False,
    nodename=False,
    release=False,
    version=False,
    machine=False,
):
    try:
        info = os.uname()

        def gen_lines():
            if all or nodename:
                (yield info.nodename)
            if all or release:
                (yield info.release)
            if all or version:
                (yield info.version)
            if all or machine:
                (yield info.machine)
        lines = list(gen_lines())
        if all or sysname or (not lines):
            lines.insert(0, info.sysname)
        sys.stdout.write(("%s\n" % " ".join(lines)))
        return 0
    except (Exception, ArithmeticError) as error:
        sys.stderr.write(("uname: %s\n" % error_code_to_text(error.errno)))
        return 1


try:
    import subprocess
except ImportError:
    subprocess = None

class GLXUsh(Cmd, GLXEnviron, GLXAlias):
    if hasattr(sys.implementation, "mpy"):
        loader_mpy = "MPY %s" % sys.implementation.mpy
    else:
        loader_mpy = ""
    if hasattr(gc, "mem_free") and hasattr(gc, "mem_alloc"):
        gc.collect()
        memory_total = (
            "%s MEMORY SYSTEM\n"
            % str(size_of((gc.mem_free() + gc.mem_alloc()))).upper()
        )
        memory_free = "%s FREE\n" % str(size_of(gc.mem_free())).upper()
    elif hasattr(os, "sysconf"):
        memory_total = (
            "%s RAM SYSTEM\n"
            % str(
                size_of((os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES")))
            ).upper()
        )
        memory_free = (
            "%s FREE\n"
            % str(
                size_of((os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_AVPHYS_PAGES")))
            ).upper()
        )
    else:
        memory_total = ""
        memory_free = ""
    intro = (
        "******************************* %s V%s **********************************\n\n%s\nLOADER %s %s %s\nEXEC PYTHON V%s\n%s%s"
        % (
            APPLICATION_NAME.upper(),
            APPLICATION_VERSION.upper(),
            APPLICATION_LICENSE.upper(),
            sys.implementation.name.upper(),
            ".".join((str(item).upper() for item in list(sys.implementation.version))),
            loader_mpy,
            sys.version.upper(),
            memory_total,
            memory_free,
        )
    )
    dow = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
    mon = (
        "???",
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    )
    ps1_clean_up_1 = re.compile("\\$\\{.*\\}")
    ps1_clean_up_2 = re.compile("\\$\\(.*\\)")
    ps1_exit_code = re.compile("\\$\\?")
    ps1_hostname_sort = re.compile("\\\\h")
    ps1_hostname = re.compile("\\\\H")
    ps1_date = re.compile("\\\\d")
    ps1_shell = re.compile("\\\\s")
    ps1_username = re.compile("\\\\u")
    ps1_shell_version = re.compile("\\\\v")
    ps1_shell_release = re.compile("\\\\V")
    ps1_working_directory = re.compile("\\\\w")
    ps1_working_directory_basename = re.compile("\\\\W")
    ps1_prompt_sign = re.compile("\\\\\\$")
    ps1_newline = re.compile("\\\\n")
    ps1_carriage_return = re.compile("\\\\r")
    ps1_bell = re.compile("\\\\a")
    ps1_time_24_hour = re.compile("\\\\t")
    ps1_time_12_hour = re.compile("\\\\T")
    ps1_time_am_pm = re.compile("\\\\@")
    ps1_begin_a_sequence_of_non_printing_characters = re.compile("\\\\\\[\\\\033")
    ps1_end_a_sequence_of_non_printing_characters = re.compile("\\\\\\]")
    ps1_virtual_env = re.compile("\\$VIRTUAL_ENV")

    def __init__(self):
        super().__init__()
        GLXEnviron.__init__(self)
        GLXAlias.__init__(self)
        if os.isatty(sys.stdin.fileno()):
            self.init_inside_a_tty = True
        else:
            self.init_inside_a_tty = False
        if hasattr(os, "environ"):
            self.environ = os.environ.copy()
        else:
            self.setenv("PATH", getcwd(), 1)
            self.setenv("HOME", sep, 1)
            self.setenv("PWD", getcwd(), 1)
        self.setenv(
            "PS1",
            "$VIRTUAL_ENV\\[\\033[01;32m\\]\\u@\\h\\[\\033[00m\\]:\\[\\033[00;34m\\]\\w\\[\\033[00m\\]\\$ ",
        )
        self.update_columns_and_lines_vars()
        self.load_alias()

    def load_alias(self):
        file = expanduser(("~%s.glxsh_alias" % sep))
        if exists(file):
            with open(file=file, mode="r", encoding="utf8") as alias_file:
                for line in alias_file.readlines():
                    self.do_alias(line)

    @property
    def prompt(self):
        tm = localtime()
        if self.environ.get("PS1"):
            tmp_value = self.environ.get("PS1")
            if self.environ.get("VIRTUAL_ENV"):
                tmp_value = self.ps1_virtual_env.sub(
                    ("(%s)" % basename(self.environ.get("VIRTUAL_ENV"))), tmp_value
                )
            tmp_value = self.ps1_clean_up_1.sub("", tmp_value)
            tmp_value = self.ps1_clean_up_2.sub("", tmp_value)
            if self.exit_code:
                exit_code = "\x1b[01;31m%s\x1b[00m" % self.exit_code
            else:
                exit_code = "\x1b[01;32m%s\x1b[00m" % self.exit_code
            tmp_value = self.ps1_exit_code.sub(exit_code, tmp_value)
            tmp_value = self.ps1_date.sub(
                ("%s %s %02d" % (self.dow[tm[6]], self.mon[tm[1]], tm[2])), tmp_value
            )
            tmp_value = self.ps1_hostname_sort.sub(gethostname(), tmp_value)
            tmp_value = self.ps1_hostname.sub(getfqdn(), tmp_value)
            tmp_value = self.ps1_shell.sub(APPLICATION_NAME, tmp_value)
            tmp_value = self.ps1_time_24_hour.sub(
                ("%02d:%02d:%02d" % (tm[3], tm[4], tm[5])), tmp_value
            )
            if tm[3] in range(13, 23, 1):
                hour = tm[3] - 12
            elif tm[3] == 0:
                hour = 12
            else:
                hour = tm[3]
            tmp_value = self.ps1_time_12_hour.sub(
                ("%02d:%02d:%02d" % (hour, tm[4], tm[5])), tmp_value
            )
            if tm[3] in range(1, 11, 1):
                am_pm_text = "AM"
            elif tm[3] in range(13, 23, 1):
                am_pm_text = "PM"
            elif tm[3] == 0:
                am_pm_text = "AM"
            else:
                am_pm_text = ""
            tmp_value = self.ps1_time_am_pm.sub(am_pm_text, tmp_value)
            tmp_value = self.ps1_username.sub(getuser(), tmp_value)
            tmp_value = self.ps1_shell_version.sub(APPLICATION_VERSION, tmp_value)
            tmp_value = self.ps1_shell_release.sub(
                ("%s.%s" % (APPLICATION_VERSION, APPLICATION_PATCH_LEVEL)), tmp_value
            )
            tmp_value = self.ps1_working_directory.sub(
                getcwd().replace(
                    ("%s%s" % (self.environ.get("HOME"), sep)), ("~%s" % sep)
                ),
                tmp_value,
            )
            tmp_value = self.ps1_working_directory_basename.sub(
                basename(self.environ.get("PWD")), tmp_value
            )
            tmp_value = self.ps1_prompt_sign.sub(
                ("$" if os.getuid() else "#"), tmp_value
            )
            tmp_value = self.ps1_newline.sub("\n", tmp_value)
            tmp_value = self.ps1_carriage_return.sub("\r", tmp_value)
            tmp_value = self.ps1_bell.sub("\x07", tmp_value)
            tmp_value = self.ps1_begin_a_sequence_of_non_printing_characters.sub(
                "\x1b", tmp_value
            )
            tmp_value = self.ps1_end_a_sequence_of_non_printing_characters.sub(
                "", tmp_value
            )
            return tmp_value
        return "%s%s " % (self.exit_code, ">")

    @staticmethod
    def do_EOF(_):
        sys.stdout.write("\n")
        sys.stdout.flush()
        return True

    def default(self, line):
        sys.stdout.write(("glxsh: %s\n" % line))
        self.exit_code = 127

    def precmd(self, line):
        if (not str(line).startswith("alias")) and (
            not str(line).startswith("unalias")
        ):
            for key, value in self.alias.items():
                if line.rstrip() == key:
                    line = line.replace(key, value)
        return line

    def postcmd(self, stop, line):
        self.update_columns_and_lines_vars()
        return stop

    def onecmd(self, line):
        (cmd, arg, line) = self.parseline(line)
        if not line:
            return self.emptyline()
        if cmd is None:
            return self.default(("cmd is None for: %s" % line))
        self.lastcmd = line
        if line == "EOF":
            self.lastcmd = ""
        if cmd == "":
            return self.default(("cmd is '' for: %s" % line))
        if "|" in line:
            return self.run_multiple_commands(line)
        return self.run_simple_command(cmd, arg, line)

    def update_columns_and_lines_vars(self):
        if self.init_inside_a_tty:
            self.environ["COLUMNS"] = str(os.get_terminal_size().columns)
            self.environ["LINES"] = str(os.get_terminal_size().lines)

    @staticmethod
    def cmdline_split(s, platform=1):
        if platform == "this":
            platform = sys.platform != "win32"
        if platform == 1:
            RE_CMD_LEX = '"((?:\\\\["\\\\]|[^"])*)"|\'([^\']*)\'|(\\\\.)|(&&?|\\|\\|?|\\d?\\>|[<])|([^\\s\'"\\\\&|<>]+)|(\\s+)|(.)'
        elif platform == 0:
            RE_CMD_LEX = '"((?:""|\\\\["\\\\]|[^"])*)"?()|(\\\\\\\\(?=\\\\*")|\\\\")|(&&?|\\|\\|?|\\d?>|[<])|([^\\s"&|<>]+)|(\\s+)|(.)'
        else:
            raise AssertionError(("unkown platform %r" % platform))
        args = []
        accu = None
        for qs, qss, esc, pipe, word, white, fail in re.findall(RE_CMD_LEX, s):
            if word:
                pass
            elif esc:
                word = esc[1]
            elif white or pipe:
                if accu is not None:
                    args.append(accu)
                if pipe:
                    args.append(pipe)
                accu = None
                continue
            elif fail:
                raise ValueError("invalid or incomplete shell string")
            elif qs:
                word = qs.replace('\\"', '"').replace("\\\\", "\\")
                if platform == 0:
                    word = word.replace('""', '"')
            else:
                word = qss
            accu = (accu or "") + word
        if accu is not None:
            args.append(accu)
        return args

    def run_multiple_commands(self, line):
        (s_in, s_out) = (0, 0)
        s_in = os.dup(0)
        s_out = os.dup(1)
        fdin = os.dup(s_in)
        for command in line.split("|"):
            os.dup2(fdin, 0)
            os.close(fdin)
            if command == line.split("|")[(-1)]:
                fdout = os.dup(s_out)
            else:
                (fdin, fdout) = os.pipe()
            os.dup2(fdout, 1)
            os.close(fdout)
            (tmp_cmd, tmp_arg, tmp_line) = self.parseline(command)
            self.run_simple_command(tmp_cmd, tmp_arg, tmp_line)
        os.dup2(s_in, 0)
        os.dup2(s_out, 1)
        os.close(s_in)
        os.close(s_out)

    def run_simple_command(self, cmd, arg, line):
        if hasattr(self, ("do_%s" % cmd)):
            try:
                func = getattr(self, ("do_%s" % cmd))
                self.exit_code = func(arg)
                self.setenv("?", str(self.exit_code))
            except KeyboardInterrupt:
                pass
            except SystemExit as code:
                self.exit_code = code
                self.setenv("?", str(self.exit_code))
                return True
            return None
        try:
            stdin_fd = sys.stdin.fileno()
            save_settings = termios.tcgetattr(stdin_fd)
        except (ModuleNotFoundError, IOError):
            save_settings = None
            stdin_fd = -1
        try:
            pr = subprocess.run(
                line.split(" "), start_new_session=True, env=self.environ, check=False
            )
            self.exit_code = pr.returncode
            self.setenv("?", str(self.exit_code))
        except KeyboardInterrupt:
            pass
        except FileNotFoundError:
            sys.stdout.write(("%s: %s : command not found\n" % (APPLICATION_NAME, cmd)))
            self.exit_code = 127
            self.setenv("?", str(self.exit_code))
        finally:
            if save_settings:
                termios.tcsetattr(stdin_fd, termios.TCSANOW, save_settings)
        return None

    def _print_help(self, parser):
        if self.environ.get("COLUMNS"):
            parser.print_help(columns=int(self.environ.get("COLUMNS")))
        else:
            parser.print_help()

    def help_alias(self):
        self._print_help(parser_alias)

    def do_alias(self, line):
        return glxsh_alias(string=line, shell=self)

    def help_basename(self):
        self._print_help(parser_basename)

    @WrapperCmdLineArgParser(parser_basename)
    def do_basename(self, _, parsed):
        return glxsh_basename(string=parsed.string, suffix=parsed.suffix)

    @WrapperCmdLineArgParser(parser_cat)
    def do_cat(self, _, parsed):
        return glxsh_cat(files=parsed.file)

    def help_cat(self):
        self._print_help(parser_cat)

    @staticmethod
    def complete_cat(text, line, begidx, endidx):
        return glxsh_completer_file(text, line, begidx, endidx)

    @WrapperCmdLineArgParser(parser_cd)
    def do_cd(self, _, parsed):
        return glxsh_cd(
            directory=parsed.directory,
            logical=parsed.logical,
            physical=parsed.physical,
            shell=self,
        )

    def help_cd(self):
        self._print_help(parser_cd)

    @staticmethod
    def complete_cd(text, line, begidx, endidx):
        return glxsh_completer_directory(text, line, begidx, endidx)

    @WrapperCmdLineArgParser(parser_clear)
    def do_clear(self, _, __):
        return glxsh_clear()

    def help_clear(self):
        self._print_help(parser_clear)

    @WrapperCmdLineArgParser(parser_chmod)
    def do_chmod(self, _, parsed):
        if (not parsed.mode) or (not parsed.file):
            parser_chmod.print_usage()
            return 1
        return glxsh_chmod(
            recursive=parsed.recursive, mode=parsed.mode, file=parsed.file
        )

    def help_chmod(self):
        self._print_help(parser_chmod)

    @staticmethod
    def complete_chmod(text, line, begidx, endidx):
        return glxsh_complete_chmod(text, line, begidx, endidx)

    @WrapperCmdLineArgParser(parser_cp)
    def do_cp(self, _, parsed):
        return glxsh_cp(
            source_file=parsed.source_file,
            target_file=parsed.target_file,
            interactive=parsed.interactive,
        )

    def help_cp(self):
        self._print_help(parser_cp)

    @WrapperCmdLineArgParser(parser_date)
    def do_date(self, line, parsed):
        if parsed.u:
            line = line.replace("-u ", "")
            line = line.replace("-u", "")
        return glxsh_date(u=parsed.u, custom_format=line, shell=self)

    def help_date(self):
        self._print_help(parser_date)

    @WrapperCmdLineArgParser(parser_df)
    def do_df(self, _, parsed):
        return glxsh_df(
            file=parsed.file,
            block_size=parsed.kilo,
            total=parsed.total,
            human_readable=parsed.human_readable,
        )

    def help_df(self):
        self._print_help(parser_df)

    @WrapperCmdLineArgParser(parser_dirname)
    def do_dirname(self, _, parsed):
        return glxsh_dirname(parsed.string)

    def help_dirname(self):
        self._print_help(parser_dirname)

    @WrapperCmdLineArgParser(parser_du)
    def do_du(self, _, parsed):
        return glxsh_du(
            a=parsed.a,
            H=parsed.H,
            k=parsed.k,
            L=parsed.L,
            s=parsed.s,
            x=parsed.x,
            files=parsed.files,
        )

    @staticmethod
    def complete_du(text, line, begidx, endidx):
        return glxsh_complete_du(text, line, begidx, endidx)

    def help_du(self):
        self._print_help(parser_du)

    def help_echo(self):
        self._print_help(parser_echo)

    @WrapperCmdLineArgParser(parser_echo)
    def do_echo(self, line, parsed):
        if parsed.newline:
            line = line.replace("-n ", "")
        return glxsh_echo(string=line, newline=parsed.newline, shell=self)

    def complete_echo(self, text, line, begidx, endidx):
        return glxsh_complete_echo(text, line, begidx, endidx, shell=self)

    def help_env(self):
        self._print_help(parser_env)

    @WrapperCmdLineArgParser(parser_env)
    def do_env(self, _, parsed):
        return glxsh_env(
            name=parsed.name,
            utility=parsed.utility,
            argument=parsed.argument,
            shell=self,
        )

    @WrapperCmdLineArgParser(parser_exit)
    def do_exit(self, _, parsed):
        if parsed.code:
            self.exit_code = parsed.code[0]
        return glxsh_exit(code=parsed.code, shell=self)

    def help_exit(self):
        self._print_help(parser_exit)

    @WrapperCmdLineArgParser(parser_false)
    def do_false(self, _, __):
        return glxsh_false()

    def help_false(self):
        self._print_help(parser_false)

    @WrapperCmdLineArgParser(parser_head)
    def do_head(self, _, parsed):
        return glxsh_head(files=parsed.file, number=parsed.number)

    @staticmethod
    def complete_head(text, line, begidx, endidx):
        return glxsh_completer_file(text, line, begidx, endidx)

    def help_head(self):
        self._print_help(parser_head)

    def emptyline(self):
        sys.stdout.write("\n")

    @WrapperCmdLineArgParser(parser_ls)
    def do_ls(self, _, parsed):
        return glxsh_ls(
            A=parsed.A,
            C=parsed.C,
            F=parsed.F,
            H=parsed.H,
            L=parsed.L,
            recurse=parsed.recurse,
            S=parsed.S,
            a=parsed.a,
            c=parsed.c,
            d=parsed.d,
            f=parsed.f,
            g=parsed.g,
            i=parsed.i,
            k=parsed.k,
            l=parsed.l,
            m=parsed.m,
            n=parsed.n,
            o=parsed.o,
            p=parsed.p,
            q=parsed.q,
            r=parsed.r,
            s=parsed.s,
            t=parsed.t,
            u=parsed.u,
            x=parsed.x,
            one=parsed.one,
            file=parsed.file,
            shell=self,
        )

    def help_ls(self):
        self._print_help(parser_ls)

    @WrapperCmdLineArgParser(parser_mkdir)
    def do_mkdir(self, _, parsed):
        if not parsed.dir:
            parser_mkdir.print_usage()
            return 1
        return glxsh_mkdir(
            directories=parsed.dir, parents=parsed.parents, mode=parsed.mode
        )

    def help_mkdir(self):
        self._print_help(parser_mkdir)

    @WrapperCmdLineArgParser(parser_mv)
    def do_mv(self, _, parsed):
        if (not parsed.target_file) or parsed.source_file:
            parser_mv.print_usage()
            return 1
        return glxsh_mv(
            source_file=parsed.source_file,
            target_file=parsed.target_file,
            target_dir=parsed.target_dir,
            force=parsed.force,
            interactive=parsed.interactive,
        )

    def help_mv(self):
        self._print_help(parser_mv)

    @WrapperCmdLineArgParser(parser_pwd)
    def do_pwd(self, _, parsed):
        return glxsh_pwd(logical=parsed.logical, physical=parsed.physical)

    def help_pwd(self):
        self._print_help(parser_pwd)

    @WrapperCmdLineArgParser(parser_rm)
    def do_rm(self, _, parsed):
        if not parsed.file:
            parser_rm.print_usage()
            return 1
        return glxsh_rm(
            file=parsed.file,
            recursive=parsed.recursive,
            interactive=parsed.interactive,
            force=parsed.force,
        )

    def help_rm(self):
        self._print_help(parser_rm)

    @staticmethod
    def complete_rmdir(text, line, begidx, endidx):
        return glxsh_complete_rmdir(text, line, begidx, endidx)

    @WrapperCmdLineArgParser(parser_rmdir)
    def do_rmdir(self, _, parsed):
        if not parsed.dir:
            parser_rmdir.print_usage()
            return 1
        return glxsh_rmdir(directories=parsed.dir, parents=parsed.parents)

    def help_rmdir(self):
        self._print_help(parser_rmdir)

    @WrapperCmdLineArgParser(parser_sleep)
    def do_sleep(self, _, parsed):
        if not parsed.time:
            parser_sleep.print_usage()
            return 1
        return glxsh_sleep(sec=parsed.time)

    @WrapperCmdLineArgParser(parser_tee)
    def do_tee(self, _, parsed):
        return glxsh_tee(a=parsed.a, i=parsed.i, files=parsed.file)

    def help_tee(self):
        self._print_help(parser_tee)

    @WrapperCmdLineArgParser(parser_time)
    def do_time(self, line, parsed):
        return glxsh_time(
            p=parsed.p,
            utility=parsed.utility,
            argument=parsed.argument,
            line=line,
            shell=self,
        )

    def help_time(self):
        self._print_help(parser_time)

    @WrapperCmdLineArgParser(parser_touch)
    def do_touch(self, _, parsed):
        return glxsh_touch(
            a=parsed.a,
            c=parsed.c,
            d=parsed.d,
            m=parsed.m,
            r=parsed.r,
            t=parsed.t,
            files=parsed.file,
        )

    def help_touch(self):
        self._print_help(parser_touch)

    @WrapperCmdLineArgParser(parser_true)
    def do_true(self, _, __):
        return glxsh_true()

    def help_true(self):
        self._print_help(parser_true)

    @WrapperCmdLineArgParser(parser_tty)
    def do_tty(self, _, __):
        return glxsh_tty()

    def help_tty(self):
        self._print_help(parser_tty)

    def help_sleep(self):
        if self.environ.get("COLUMNS"):
            parser_sleep.print_help(columns=int(self.environ.get("COLUMNS")))
        else:
            parser_sleep.print_help()

    @WrapperCmdLineArgParser(parser_uname)
    def do_uname(self, _, parsed):
        return glxsh_uname(
            all=parsed.all,
            sysname=parsed.sysname,
            nodename=parsed.nodename,
            release=parsed.release,
            version=parsed.version,
            machine=parsed.machine,
        )

    def help_uname(self):
        self._print_help(parser_uname)

    def help_umask(self):
        self._print_help(parser_umask)

    @WrapperCmdLineArgParser(parser_umask)
    def do_umask(self, _, parsed):
        return glxsh_umask(mask=parsed.mask, symbolic=parsed.symbolic)

    def help_unalias(self):
        self._print_help(parser_unalias)

    @WrapperCmdLineArgParser(parser_unalias)
    def do_unalias(self, _, parsed):
        return glxsh_unalias(a=parsed.a, alias_name=parsed.alias_name, shell=self)

    @WrapperCmdLineArgParser(parser_tail)
    def do_tail(self, _, parsed):
        return glxsh_tail(c=parsed.c, f=parsed.f, n=parsed.n, files=parsed.file)

    def help_tail(self):
        self._print_help(parser_tail)


parser_glxsh = ArgumentParser(prog="glxsh", add_help=True)
parser_glxsh.add_argument(
    "command",
    nargs="?",
    help="optional commands or file to run, if no commands given, enter an interactive shell",
)
parser_glxsh.add_argument(
    "command_args",
    nargs="...",
    help="if commands is not a file use optional arguments for commands",
)

def main():
    if len(sys.argv) > 1:
        args = parser_glxsh.parse_args(sys.argv[1:])
        if args.help:
            parser_glxsh.print_help()
            return 0
        if isfile(args.command):
            try:
                with open(args.command) as rcFile:
                    for line in rcFile.readlines():
                        line = line.rstrip()
                        if (len(line) > 0) and (line[0] != "#"):
                            exit_code = GLXUsh().onecmdhooks(("%s" % line))
            except IOError:
                exit_code = 1
            else:
                return exit_code
        else:
            return GLXUsh().onecmdhooks(
                ("%s %s" % (args.command, " ".join(args.command_args)))
            )
    else:
        return GLXUsh().cmdloop()

if __name__ == "__main__":
    sys.exit(main())
