import os
from glxshell.lib.glob import glob
import re
from glxshell.lib.path import isdir
from glxshell.lib.path import isfile
from glxshell.lib.path import islink
from glxshell.lib.path import joinpath
from glxshell.lib.path import normpath
from glxshell.lib.path import sep
from glxshell.lib.path import getcwd


def _append_slash_if_dir(p):
    if p and isdir(p) and p[-1] != sep:
        return p + sep
    else:
        return p


def glxsh_completer_directory(text, line, begidx, endidx):
    arg = line.split()[1:]

    if not arg:
        return [normpath(f) + "/" for f in os.listdir(os.getcwd()) if isdir(f)]
    else:
        directory, part, base = arg[-1].rpartition("/")
        if part == "":
            directory = os.getcwd()
        elif directory == "":
            directory = "/"
        completions = []
        for f in os.listdir(directory):
            if f.startswith(base):
                if isdir(joinpath(directory, f)):
                    completions.append(joinpath(f, ""))
        return completions


def glxsh_completer_file(text, line, begidx, endidx):
    arg = line.split()[1:]

    if not arg:
        return os.listdir(os.getcwd())
    else:
        directory, part, base = arg[-1].rpartition("/")
        if part == "":
            directory = os.getcwd()
        elif directory == "":
            directory = "/"
        return [normpath(f) + "/" if isdir(f) else normpath(f) for f in os.listdir(directory) if f.startswith(base)]


def glxsh_complete_chmod(text, line, begidx, endidx):
    return glxsh_completer_file(text, line, begidx, endidx)


def glxsh_complete_rmdir2(text, line, begidx, endidx):
    before_arg = line.rfind(" ", 0, begidx)
    if before_arg == -1:
        return  # arg not found

    fixed = line[before_arg + 1:begidx]  # fixed portion of the arg
    arg = line[before_arg + 1:endidx]
    pattern = arg + '*'

    completions = []
    for path in glob.glob(pattern):
        path = _append_slash_if_dir(path)
        completions.append(path.replace(fixed, "", 1))
    return completions


def glxsh_complete_rmdir(text, line, begidx, endidx):
    if line == "rmdir":
        return ["rmdir "]

    arg = line.split()[1:]

    if not arg:
        return [normpath(f) + sep for f in os.listdir(os.getcwd()) if isdir(f)]
    else:
        dir, part, base = arg[-1].rpartition(sep)
        if part == '':
            dir = './'
        elif dir == '':
            dir = '/'

        completions = []
        for f in os.listdir(dir):
            if f.startswith(base):
                if isdir(os.path.join(dir, f)):
                    completions.append(f + "/")

    return completions


var_env_pattern = re.compile(r".*\$$", re.IGNORECASE)
var_env_name_pattern = re.compile(r".*\$(\w+)$", re.IGNORECASE)


def glxsh_complete_echo(text, line, begidx, endidx, shell=None):
    if line == "echo":
        return ["echo "]

    arg = line.split()[1:]

    if not arg:
        pass
    else:
        completions = []
        if var_env_name_pattern.match(arg[-1]):
            search_result = re.search(var_env_name_pattern, arg[-1])
            if not search_result:
                return None

            for key, value in shell.environ.items():
                if str(key).startswith(search_result.group(1)) and key != search_result.group(1):
                    completions.append("%s " % key)
            return completions

        elif var_env_pattern.match(arg[-1]):
            search_result = re.search(var_env_pattern, arg[-1])
            if not search_result:
                return None

            for key, value in shell.environ.items():
                completions.append("%s " % key)
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
                completions.append(normpath(f) + sep)
            if isfile(f) or islink(f):
                completions.append(normpath(f))

    else:
        dir, part, base = arg[-1].rpartition(sep)
        if part == '':
            dir = './'
        elif dir == '':
            dir = '/'

        completions = []
        for f in os.listdir(dir):
            if f.startswith(base) or f.startswith(base + sep):
                if isdir(f):
                    completions.append(normpath(f) + sep)
                if isfile(f) or islink(f):
                    completions.append(normpath(f))

    return completions

