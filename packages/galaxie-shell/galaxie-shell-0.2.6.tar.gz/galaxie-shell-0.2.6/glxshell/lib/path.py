import os

from glxshell.lib.stat import S_ISREG
from glxshell.lib.stat import S_ISDIR
from glxshell.lib.stat import S_ISLNK

sep = "/"


def normcase(path):
    """Normalize case of pathname.  Has no effect under Posix"""
    return path


def normpath(path):
    """Normalize path, eliminating double slashes, etc."""
    if path == "":
        return "."
    initial_slashes = path.startswith(sep)
    # POSIX allows one or two initial slashes, but treats three or more
    # as single slash.
    # (see http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap04.html#tag_04_13)
    if initial_slashes and path.startswith(sep * 2) and not path.startswith(sep * 3):
        initial_slashes = 2
    new_comps = []
    for comp in path.split(sep):
        if comp in {"", "."}:
            continue
        if comp != ".." or (not initial_slashes and not new_comps) or (new_comps and new_comps[-1] == ".."):
            new_comps.append(comp)
        elif new_comps:
            new_comps.pop()
    path = sep.join(new_comps)
    if initial_slashes:
        path = sep * initial_slashes + path
    return path or "."


def getcwd():
    return os.getcwd()


def abspath(path):
    """Return an absolute path."""
    if not isabs(path):
        return normpath(joinpath(getcwd(), path))
    return normpath(path)


def joinpath(*args):
    """
    Join two or more pathname components, inserting '/' as needed.
    If any component is an absolute path, all previous path components
    will be discarded.  An empty last part will result in a path that
    ends with a separator.

    :param args: components it will compose teh pathname
    :type args: any
    :return: A pathname composed by components joins by '/'
    :rtype: str
    """
    res = ""
    for a in args:
        if not res or a.startswith(sep):
            res = a
        else:
            res += sep + a
    return res.replace(sep * 2, sep)


def split(path):
    if path == "":
        return "", ""
    r = path.rsplit(sep, 1)
    if len(r) == 1:
        return "", path
    head = r[0]  # .rstrip(sep)
    if not head:
        head = sep
    return head, r[1]


def splitext(path):
    # Split a path in root and extension.
    # The extension is everything starting at the last dot in the last
    # pathname component; the root is everything before that.
    # It is always true that root + ext == p.
    r = path.rsplit(".", 1)
    if len(r) == 1:
        return path, ""
    if not r[0]:
        return path, ""
    return r[0], "." + r[1]


def splitdrive(path):
    return "", path


# https://pubs.opengroup.org/onlinepubs/9699919799/utilities/dirname.html
def dirname(path):
    if not path or sep not in path:
        return "."

    if path in (sep, sep * 2, sep * 3):
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

    if string in (sep, sep * 2, sep * 3):
        return sep

    if sep not in string:
        return string

    if suffix:
        return normpath(string).split(sep)[-1].replace(suffix, "")

    return normpath(string).split(sep)[-1]


def exists(path):
    try:
        os.stat(path)
    except OSError:
        return False
    return True
    # return os.access(path, os.F_OK)


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
    """Test whether a path is absolute"""
    return path.startswith(sep)


# Return a canonical path (i.e. the absolute location of a file on the
# filesystem).


def realpath(filename, *, strict=False):
    """Return the canonical path of the specified filename, eliminating any
    symbolic links encountered in the path."""
    filename = os.fspath(filename)
    path, _ = _joinrealpath(filename[:0], filename, strict, {})
    return abspath(path)


# Join two paths, normalizing and eliminating any symbolic links
# encountered in the second path.
def _joinrealpath(path, rest, strict, seen):

    curdir = "."
    pardir = ".."

    if isabs(rest):
        rest = rest[1:]
        path = sep

    while rest:
        name, _, rest = rest.partition(sep)
        if not name or name == curdir:
            # current dir
            continue
        if name == pardir:
            # parent dir
            if path:
                path, name = split(path)
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
        # Resolve the symbolic link
        if newpath in seen:
            # Already seen this path
            path = seen[newpath]
            if path is not None:
                # use cached value
                continue
            # The symlink is not resolved, so we must have a symlink loop.
            if strict:
                # Raise OSError(errno.ELOOP)
                os.stat(newpath)
            else:
                # Return already resolved part + rest of the path unchanged.
                return joinpath(newpath, rest), False
        seen[newpath] = None  # not resolved symlink
        path, ok = _joinrealpath(path, os.readlink(newpath), strict, seen)
        if not ok:
            return joinpath(path, rest), False
        seen[newpath] = path  # resolved symlink

    return path, True


def expanduser(s):
    if s == "~" or s.startswith("~" + sep):
        h = os.getenv("HOME")
        return h + s[1:]
    if s[0] == "~":
        # Sorry folks, follow conventions
        return sep + "home" + sep + s[1:]
    return s


# Return the longest prefix of all list elements.
def commonprefix(m):
    """Given a list of pathnames, returns the longest common leading component"""
    if not m:
        return ""
    s1 = min(m)
    s2 = max(m)
    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i]
    return s1


# From CPython git tag v3.4.10.
def relpath(path, start=None):
    """Return a relative version of a path"""

    if not path:
        raise ValueError("no path specified")

    curdir = "."
    pardir = ".."

    if start is None:
        start = curdir

    start_list = [x for x in abspath(start).split(sep) if x]
    path_list = [x for x in abspath(path).split(sep) if x]

    # Work out how much of the filepath is shared by start and path.
    i = len(commonprefix([start_list, path_list]))

    rel_list = [pardir] * (len(start_list) - i) + path_list[i:]
    if not rel_list:
        return curdir
    return joinpath(*rel_list)
