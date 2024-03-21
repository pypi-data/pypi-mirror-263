# Inspired by: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/ls.html
import os
import sys
import time
from grp import getgrgid
from pwd import getpwuid
from glxshell.lib.argparse import ArgumentParser
from glxshell.lib.path import isdir
from glxshell.lib.path import islink
from glxshell.lib.columnize import columnize
from glxshell.lib.tabulate import tabulate

from glxshell.lib.glob import glob
from glxshell.lib.stat import filemode

parser_ls = ArgumentParser(
    name="ls - list directory contents",
    description="List information about the files (the current directory by default).\n"
                "Sort entries alphabetically if none of -cftuvSUX is specified.",
    synopsis=["ls [-ikqrs] [-glno] [-A|-a] [-C|-m|-x|-1] [-F|-p] [-H|-L] [-R|-d] [-S|-f|-t] [-c|-u] [file...]"]
)
parser_ls.add_argument(
    "-A",
    action="store_true",
    dest="A",
    help="Do not list implied . and ..",
)
parser_ls.add_argument(
    "-C",
    action="store_true",
    dest="C",
    help="List entries by columns",
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
    "-R",
    dest="recurse",
    action="store_true",
    help="List subdirectories recursively",
)

parser_ls.add_argument(
    "-S",
    dest="S",
    action="store_true",
    help="sort by file size, largest first",
)

parser_ls.add_argument(
    "-a",
    dest="a",
    action="store_true",
    help="do not ignore entries starting with .",
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
    "-g",
    dest="g",
    action="store_true",
    help="group directories before files;",
)

parser_ls.add_argument(
    "-i",
    dest="i",
    action="store_true",
    help="print the index number of each file",
)

parser_ls.add_argument(
    "-k",
    dest="k",
    action="store_true",
    help="default to 1024-byte blocks for disk usage; used only with -s and per directory totals",
)

parser_ls.add_argument(
    "-l",
    dest="l",
    action="store_true",
    help="use a long listing format",
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
    "-p",
    dest="p",
    action="store_true",
    help="append / indicator to directories",
)

parser_ls.add_argument(
    "-q",
    dest="q",
    action="store_true",
    help="enclose entry names in double quotes",
)

parser_ls.add_argument(
    "-r",
    dest="r",
    action="store_true",
    help="reverse order while sorting",
)

parser_ls.add_argument(
    "-s",
    dest="s",
    action="store_true",
    help="print the allocated size of each file, in blocks",
)

parser_ls.add_argument(
    "-t",
    dest="t",
    action="store_true",
    help="sort by time, newest first",
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
    help="A pathname of a file to be written. If the file specified is not found, a diagnostic message shall be "
         "output on standard error.",
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
        **kwargs,
):
    # -A Write out all directory entries, including those whose names begin with a <period> ( '.' )
    #    but excluding the entries dot and dot-dot (if they exist).
    # -C Write multi-text-column output with entries sorted down the columns, according to the
    #    collating sequence. The number of text columns and the column separator characters are
    #    unspecified, but should be adapted to the nature of the output device.
    #    This option disables long format output.
    # -F Do not follow symbolic links named as operands unless the -H or -L options are specified. Write a <slash> ( '/' ) immediately after each pathname that is a directory, an <asterisk> ( '*' ) after each that is executable, a <vertical-line> ( '|' ) after each that is a FIFO, and an at-sign ( '@' ) after each that is a symbolic link. For other file types, other symbols may be written.
    # -H Evaluate the file information and file type for symbolic links specified on the command line to be those of the file referenced by the link, and not the link itself; however, ls shall write the name of the link itself and not the file referenced by the link.
    # -L Evaluate the file information and file type for all symbolic links (whether named on the command line or encountered in a file hierarchy) to be those of the file referenced by the link, and not the link itself; however, ls shall write the name of the link itself and not the file referenced by the link. When -L is used with -l, write the contents of symbolic links in the long format (see the STDOUT section).
    # -R Recursively list subdirectories encountered. When a symbolic link to a directory is encountered, the directory shall not be recursively listed unless the -L option is specified. The use of -R with -d or -f produces unspecified results.
    # -S Sort with the primary key being file size (in decreasing order) and the secondary key being filename in the collating sequence (in increasing order).
    # -a Write out all directory entries, including those whose names begin with a <period> ( '.' ).
    # -c Use time of last modification of the file status information (see XBD <sys/stat.h>) instead of last modification of the file itself for sorting ( -t) or writing (-l).
    # -d Do not follow symbolic links named as operands unless the -H or -L options are specified. Do not treat directories differently than other types of files. The use of -d with -R or -f produces unspecified results.
    # -f List the entries in directory operands in the order they appear in the directory. The behavior for non-directory operands is unspecified. This option shall turn on -a. When -f is specified, any occurrences of the -r, -S, and -t options shall be ignored and any occurrences of the -A, [XSI] [Option Start] -g, [Option End] -l, -n, [XSI] [Option Start] -o, [Option End] and -s options may be ignored. The use of -f with -R or -d produces unspecified results.
    # -g [XSI] [Option Start] Turn on the -l (ell) option, but disable writing the file's owner name or number. Disable the -C, -m, and -x options. [Option End]
    # -i For each file, write the file's file serial number (see stat() in the System Interfaces volume of POSIX.1-2017).
    # -k Set the block size for the -s option and the per-directory block count written for the -l, -n, -s, [XSI] [Option Start] -g, and -o [Option End] options (see the STDOUT section) to 1024 bytes.
    # -l (The letter ell.) Do not follow symbolic links named as operands unless the -H or -L options are specified. Write out in long format (see the STDOUT section). Disable the -C, -m, and -x options.
    # -m Stream output format; list pathnames across the page, separated by a <comma> character followed by a <space> character. Use a <newline> character as the list terminator and after the separator sequence when there is not room on a line for the next list entry. This option disables long format output.
    # -n Turn on the -l (ell) option, but when writing the file's owner or group, write the file's numeric UID or GID rather than the user or group name, respectively. Disable the -C, -m, and -x options.
    # -o [XSI] [Option Start] Turn on the -l (ell) option, but disable writing the file's group name or number. Disable the -C, -m, and -x options. [Option End]
    # -p Write a <slash> ( '/' ) after each filename if that file is a directory.
    # -q Force each instance of non-printable filename characters and <tab> characters to be written as the <question-mark> ( '?' ) character. Implementations may provide this option by default if the output is to a terminal device.
    # -r Reverse the order of the sort to get reverse collating sequence oldest first, or smallest file size first depending on the other options given.
    # -s Indicate the total number of file system blocks consumed by each file displayed. If the -k option is also specified, the block size shall be 1024 bytes; otherwise, the block size is implementation-defined.
    # -t Sort with the primary key being time modified (most recently modified first) and the secondary key being filename in the collating sequence. For a symbolic link, the time used as the sort key is that of the symbolic link itself, unless ls is evaluating its file information to be that of the file referenced by the link (see the -H and -L options).
    # -u Use time of last access (see XBD <sys/stat.h>) instead of last modification of the file for sorting (-t) or writing (-l).
    # -x The same as -C, except that the multi-text-column output is produced with entries sorted across, rather than down, the columns. This option disables long format output.
    # -1 (The numeric digit one.) Force output to be one entry per line. This option does not disable long format output. (Long format output is enabled by [XSI] [Option Start] -g, [Option End] -l (ell), -n, and [XSI] [Option Start] -o; [Option End] and disabled by -C, -m, and -x.)
    #
    # If an option that enables long format output ( [XSI] [Option Start] -g, [Option End] -l (ell), -n, and [XSI] [Option Start] -o, [Option End] is given with an option that disables long format output (-C, -m, and -x), this shall not be considered an error. The last of these options specified shall determine whether long format output is written.
    #
    # If -R, -d, or -f are specified, the results of specifying these mutually-exclusive options are specified by the descriptions of these options above. If more than one of any of the other options shown in the SYNOPSIS section in mutually-exclusive sets are given, this shall not be considered an error; the last option specified in each set shall determine the output.
    #
    # Note that if -t is specified, -c and -u are not only mutually-exclusive with each other, they are also mutually-exclusive with -S when determining sort order. But even if -S is specified after all occurrences of -c, -t, and -u, the last use of -c or -u determines the timestamp printed when producing long format output.

    def _print_long_format(list_to_display):
        tabular_data = []

        for pathname in list_to_display:
            lstat = os.stat(pathname)
            tabular_data.append([
                "%s" % filemode(lstat.st_mode),
                "%u" % lstat.st_nlink,
                "%s" % getpwuid(lstat.st_uid)[0],
                "%s" % getgrgid(lstat.st_gid)[0],
                "%u" % lstat.st_mode,
                "%s" % time.strftime("%b %d %H:%M", time.localtime(lstat.st_mtime)),
                "%s" % _add_slash_if_is_dir(pathname)

            ])

        sys.stdout.write(
            "%s\n"
            % tabulate(
                tabular_data=tabular_data,
                headers=[],
                tablefmt="plain",
                colalign=("left", "right", "right", "right", "left", "right", "left"),
            )
        )

    def _add_slash_if_is_dir(item):
        if p and isdir(item) and not item.endswith("/"):
            return "%s/" % item
        return item

    exit_code = 0
    stdout = kwargs.get("stdout", sys.stdout)
    stdin = kwargs.get("stdin" , sys.stdin)
    stderr = kwargs.get("stderr", sys.stderr)
    shell = kwargs.get("shell") or None
    # LS_COLORS = {}
    # if shell and shell.getenv("LS_COLORS"):
    #     for item in shell.getenv("LS_COLORS").split(':'):
    #         try:
    #             code, color = item.split('=', 1)
    #         except ValueError:
    #             continue # no key=value, just ignore
    #         if code.startswith('*.'):
    #             self._extensions[code[1:]] = color
    #         else:
    #             self._codes[code] = color
    #
    #     for color_info in shell.getenv("LS_COLORS").split(":"):
    #         if color_info:
    #             key, value = color_info.split("=")
    #             LS_COLORS[key] = value


    # for key, value in LS_COLORS.items():
    #     stdout.write("%s%s\033[0m" %(value, str(key)))
    #     stdout.write("\n")

    # Pre Processing for glob
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
                    _files_to_look.append("%s/**/*" % _file)
                else:
                    _files_to_look.append("%s/*" % _file)
            else:
                _files_to_look.append(_file)

    # Processing
    for pathname in _files_to_look:
        try:
            list_to_display = []
            dir_scan = glob(pathname)
            if a:
                dir_scan.insert(0, "..")
                dir_scan.insert(0, ".")
            for f in dir_scan:
                if F:
                    if isdir("%s/%s" % (pathname, f)):

                        f = "%s/" % f
                    elif os.access("%s/%s" % (pathname, f), os.X_OK):
                        f = "%s*" % f
                    elif islink("%s/%s" % (pathname, f)):
                        f = "%s@" % f


                if A or a:
                    if A:
                        if f != "." and f != "..":
                            list_to_display.append(f)
                    else:
                        # if "." not in list_to_display and ".." not in list_to_display:
                        list_to_display.append(f)


                else:
                    if not f.startswith("."):
                        list_to_display.append(f)


            if C and not l:
                columnize(list_to_display)
            elif l:
                _print_long_format(list_to_display)
            else:
                for f in list_to_display:
                    f = _add_slash_if_is_dir(f)
                    sys.stdout.write("%s\n" % f)

            # for f in l:
            #     st = os.stat("%s/%s" % (path, f))
            #     if st[0] & 0x4000:  # stat.S_IFDIR
            #         self.stdout.write("   <dir> %s\n" % f)
            #     else:
            #         self.stdout.write("% 8d %s\n" % (st[6], f))

        except (Exception, ArithmeticError) as error:
            sys.stderr.write("ls: %s: '%s'\n" % (error, pathname))
            exit_code += 1

    return exit_code
