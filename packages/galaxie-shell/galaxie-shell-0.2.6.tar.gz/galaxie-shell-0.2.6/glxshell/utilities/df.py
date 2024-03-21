# https://pubs.opengroup.org/onlinepubs/9699919799/utilities/df.html

import math
import os
import sys
from glxshell.lib.tabulate import tabulate
from glxshell.lib.argparse import ArgumentParser
from glxshell.lib.utils import size_of
from glxshell.lib.path import exists
from glxshell.lib.path import lexists
from glxshell.lib.path import islink
from glxshell.lib.path import abspath
from glxshell.lib.path import realpath
from glxshell.lib.path import dirname

parser_df = ArgumentParser(
    name="df - report free disk space",
    description="The df utility shall write the amount of available space and file slots for file systems on which "
    "the invoking user has appropriate read access. File systems shall be specified by the file "
    "operands; when none are specified, information shall be written for all file systems."
    "The format of the default output from df is unspecified, but all space figures are reported in "
    "512-byte units, unless the -k option is specified. This output shall contain at least the "
    "file system names, amount of available space on each of these file systems, and, if no options "
    "other than -t are specified, the number of free file slots, or inodes, available; when -t"
    " is specified, the output shall contain the total allocated space as well.",
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
    help="A pathname of a file within the hierarchy of the desired file system. If a file other than a FIFO, "
    "a regular file, a directory, or a special file representing the device containing the file system (for "
    "example, /dev/dsk/0s1) is specified, the results are unspecified. If the file operand names a "
    "file other than a special file containing a file system, df shall write the amount of free space in the "
    "file system containing the specified file operand. Otherwise, df shall write the amount of free space in "
    "that file system. ",
)


def glxsh_df(file=None, block_size=None, total=None, human_readable=None):

    # Return True to stop the command loop
    if block_size is None:
        block_size = 512

    devices_list = []
    if file:
        if not exists(file):
            return "df: %s: No such file or directory" % file

        if not os.access(file, os.R_OK) or not os.access(df_find_mount_point(file), os.R_OK):  # pragma: no cover
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
            total_space_free, total_space_used, total_total_space = df_get_totals(devices_list)

            devices_list.append(
                [
                    "total",
                    total_total_space,
                    total_space_used,
                    total_space_free,
                    "%d%%" % int(math.ceil(100 * (float(total_total_space - total_space_free) / total_total_space))),
                    "-",
                ]
            )

        block_size_text, tabular_data = df_get_info_to_print(block_size, devices_list, human_readable)
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
            if str(line[1]) != "-" and str(line[2]) != "-" and str(line[3]) != "-":
                tabular_data.append(
                    [
                        line[0],
                        size_of(size=int(line[1]) * block_size, suffix=""),
                        size_of(size=int(line[2]) * block_size, suffix=""),
                        size_of(size=int(line[3]) * block_size, suffix=""),
                        line[4],
                        line[5],
                    ]
                )
            else:
                tabular_data.append(line)
    else:
        tabular_data = devices_list

    return block_size_text, tabular_data


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
    return total_space_free, total_space_used, total_total_space


def df_print_final(block_size_text, tabular_data):
    sys.stdout.write(
        "%s\n"
        % tabulate(
            tabular_data=tabular_data,
            headers=["Filesystem", block_size_text, "Used", "Available", "Capacity", "Mounted on"],
            tablefmt="plain",
            colalign=("left", "right", "right", "right", "right", "left"),
        )
    )


def df_find_mount_point(path):
    if not islink(path):
        path = abspath(path)
    elif islink(path) and lexists(os.readlink(path)):  # pragma: no cover
        path = realpath(path)
    if hasattr(os, "path") and hasattr(os.path, "ismount"):
        while not os.path.ismount(path):
            path = dirname(path)
            if islink(path) and lexists(os.readlink(path)):  # pragma: no cover
                path = realpath(path)
    return path


def df_get_device_information(file_system_name=None, file_system_root=None, block_size=None):
    try:
        statvfs = os.statvfs(file_system_root)
        if type(statvfs) == tuple:
            #     statvfs[0] = f_bsize
            #     statvfs[1] = f_frsize
            #     statvfs[2] = f_blocks
            #     statvfss[3] = f_bfree
            #     statvfs[4] = f_bavail
            #     statvfss[5] = f_files
            #     statvfs[6] = f_ffree
            #     statvfs[7] = f_favail
            #     statvfs[8] = f_flags
            #     statvfss[9] = f_namemax
            space_free = statvfs[4] * statvfs[1] / block_size
            total_space = statvfs[2] * statvfs[1] / block_size
        else:
            space_free = statvfs.f_bavail * statvfs.f_frsize / block_size
            total_space = statvfs.f_blocks * statvfs.f_frsize / block_size
        space_used = total_space - space_free
        if total_space == 0:
            percentage_used = "-"
        else:
            percentage_used = "%d%%" % int(math.ceil(100 * (float(total_space - space_free) / total_space)))

        return [
            "%s" % file_system_name,
            "%d" % total_space,
            "%d" % space_used,
            "%d" % space_free,
            "%s" % percentage_used,
            "%s" % file_system_root,
        ]
    except PermissionError:  # pragma: no cover
        return [
            "%s" % file_system_name,
            "%s" % "-",
            "%s" % "-",
            "%s" % "-",
            "%s" % "-",
            "%s" % file_system_root,
        ]


def df_get_devices(file=None):
    if file is None and exists("/etc/mtab"):
        file = "/etc/mtab"
    if file is None and exists("/proc/mounts"):  # pragma: no cover
        file = "/proc/mounts"
    if file is None:  # pragma: no cover
        raise SystemError("Impossible to locate /etc/mtab or /proc/mounts file")

    file_entries = []
    for line in df_get_file_content(file=file).splitlines():
        if len(line.split()) < 4:  # pragma: no cover
            continue
        file_entries.append(line.split())
    return file_entries


def df_get_file_content(file=None):
    if not exists(file):
        raise FileExistsError(f"{file} do not exist")
    if not os.access(file, os.R_OK):  # pragma: no cover
        raise PermissionError(f"{file} can't be read")

    with open(file) as datafile:
        return datafile.read().strip()
