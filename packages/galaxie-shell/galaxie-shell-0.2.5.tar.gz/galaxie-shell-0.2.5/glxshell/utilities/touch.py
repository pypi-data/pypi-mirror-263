# https://pubs.opengroup.org/onlinepubs/9699919799/utilities/touch.html
import os
import sys
import time
from glxshell.lib.argparse import ArgumentParser
from glxshell.lib.argparse import FileType
from glxshell.lib.path import exists
from glxshell.lib.utils import error_code_to_text
from glxshell.lib.iso8601 import is_iso8601
from glxshell.lib.iso8601 import parse_date

parser_touch = ArgumentParser(
    name="touch - change file access and modification times",
    description="The touch utility shall change the last data modification timestamps, the last data access timestamps,"
    " or both.\n\n"
    "The time used can be specified by the -t time option-argument, the corresponding time fields of the "
    "file referenced by the -r ref_file option-argument, or the -d date_time option-argument, "
    "as specified in the following sections. If none of these are specified, touch shall use the current "
    "time.",
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
    help="Do not create a specified file if it does not exist. Do not write any diagnostic messages "
    "concerning this condition.",
)
parser_touch.add_argument(
    "-m",
    action="store_true",
    default=False,
    help="Change the modification time of file. Do not change the access time unless -a is also specified.",
)

parser_touch.add_argument(
    "-d",
    nargs="?",
    help="Use the specified date_time instead of the current time",
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
    """
    The glxsh_touch function shall change the last data modification timestamps, the last data access timestamps,
    or both.

    The time used can be specified by the ``time`` option-argument, the corresponding time fields of the file
    referenced by the -r ref_file option-argument, or the -d date_time option-argument, as specified in the following
    sections.

    If none of these are specified, touch shall use the current time

    date_time format:
        YYYY-MM-DDThh:mm:SS[.frac][tz]
        or
        YYYY-MM-DDThh:mm:SS[,frac][tz]
        
        where:
         - YYYY are at least four decimal digits giving the year.
         - MM, DD, hh, mm, and SS are as with -t time.
         - T is the time designator, and can be replaced by a single <space>.
         - [.frac] and [,frac] are either empty, or a <period> ( '.' ) or a <comma> ( ',' ) respectively, followed by one or more decimal digits, specifying a fractional second.
         - [tz] is either empty, signifying local time, or the letter 'Z', signifying UTC. If [tz] is empty, the resulting time shall be affected by the value of the TZ environment variable.

    :param a: Change the access time of file. Do not change the modification time unless ``m`` is also specified.
    :type a: bool
    :param c: Do not create a specified file if it does not exist. Do not write any diagnostic messages concerning this conditionself.
    :type c: bool
    :param d: Use the specified date_time instead of the current time.
    :type d: string
    :param m: Change the modification time of file. Do not change the access time unless -a is also specifiedself.
    :type m: bool
    :param r: Use the corresponding time of the file path named by the value instead of the current time.
    :type r: string
    :param t: Use the specified time instead of the current time.
    :param files: A pathname of a file whose times shall be modified.
    :type files: list
    :param date_time: Use the specified ``date_time`` instead of the current time.
    :type date_time: string
    :param time: Use the specified ``time`` instead of the current time.
    :type time: int or float
    """
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
                else:
                    if a is True and m is False:
                        os.utime(file, ns=(time.time_ns(), os.stat(file).st_mtime_ns))
                    elif a is False and m is True:
                        os.utime(file, ns=(os.stat(file).st_atime_ns, time.time_ns()))
                    else:
                        os.utime(file, None)

            except OSError as error:
                sys.stderr.write("touch: %s: '%s'\n" % (error_code_to_text(error.errno), file))
                exit_code += 1
                
        else:
            if c is False:
                try:
                    with open(file, "w"):
                        pass
                    if r:
                        os.utime(file, ns=(os.stat(r).st_atime_ns, os.stat(r).st_mtime_ns))
                    elif d:
                        os.utime(file, ns=(time.time_ns(), parse_date(d).timetuple()))
                    else:
                        if a is True and m is False:
                            os.utime(file, ns=(time.time_ns(), os.stat(file).st_mtime_ns))
                        elif a is False and m is True:
                            os.utime(file, ns=(os.stat(file).st_atime_ns, time.time_ns()))
                        else:
                            os.utime(file, None)
                except OSError as error:
                    sys.stderr.write("touch: %s: '%s'\n" % (error_code_to_text(error.errno), file))
                    exit_code += 1
        
    return 1 if exit_code else 0 
