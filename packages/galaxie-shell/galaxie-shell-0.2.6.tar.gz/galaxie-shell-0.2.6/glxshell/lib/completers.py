import os
import re

from glxshell.lib.glob import glob
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


def glxsh_completer_directory(_, line, __, ___):

    arg = line.split()[1:]

    if not arg:
        return [normpath(f) + sep for f in os.listdir(getcwd()) if isdir(f)]
    else:
        directory, part, base = arg[-1].rpartition(sep)
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
        directory, part, base = arg[-1].rpartition(sep)
        if part == "":
            directory = getcwd()
        elif directory == "":
            directory = sep
        return [normpath(f) + sep if isdir(f) else normpath(f) for f in os.listdir(directory) if f.startswith(base)]


def glxsh_complete_chmod(text, line, begidx, endidx):
    return glxsh_completer_file(text, line, begidx, endidx)


def glxsh_complete_rmdir2(_, line, begidx, endidx):
    before_arg = line.rfind(" ", 0, begidx)
    if before_arg == -1:
        return  # arg not found

    fixed = line[before_arg + 1:begidx]  # fixed portion of the arg
    arg = line[before_arg + 1:endidx]
    pattern = arg + '*'

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
        return [normpath(f) + sep for f in os.listdir(getcwd()) if isdir(f)]
    else:
        directory, part, base = arg[-1].rpartition(sep)
        if part == '':
            directory = '.' + sep
        elif directory == '':
            directory = sep

        completions = []
        for f in os.listdir(directory):
            if f.startswith(base):
                if isdir(os.path.join(directory, f)):
                    completions.append(f + sep)

    return completions


var_env_pattern = re.compile(r".*\$$", re.IGNORECASE)
var_env_name_pattern = re.compile(r".*\$(\w+)$", re.IGNORECASE)


def glxsh_complete_echo(_, line, __, ___, shell=None):
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
        directory, part, base = arg[-1].rpartition(sep)
        if part == '':
            directory = '.' + sep
        elif directory == '':
            directory = sep

        completions = []
        for f in os.listdir(directory):
            if f.startswith(base) or f.startswith(base + sep):
                if isdir(f):
                    completions.append(normpath(f) + sep)
                if isfile(f) or islink(f):
                    completions.append(normpath(f))

    return completions

