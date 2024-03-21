import re
import sys


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
    """
    Scale bytes to its proper format

    **Example:**
        1253656 => '1.20MB'
        1253656678 => '1.17GB'

    :param size: bytes size to convert
    :type size: int
    :param suffix: what suffix is add at the end of the returned value
    :type suffix: str
    """
    for unit in ("", "K", "M", "G", "T", "P", "E", "Z", "Y"):
        if size < 1024:
            return "{size:.2f}{unit}{suffix}".format(size=size, unit=unit, suffix=suffix)
        size /= 1024
    return "{size:.2f}".format(size=size)


def get_bold_text(text):
    if sys.stdout.isatty():
        return "\033[1m%s\033[0m" % text
    return "%s" % text


class Xlator(dict):
    """ All-in-one multiple-string-substitution class """

    def _make_regex(self):
        """ Build re object based on the keys of the current dictionary """
        return re.compile("|".join(map(re.escape, self.keys())))

    def __call__(self, match):
        """ Handler invoked for each regex match """
        return self[match.group(0)]

    def xlat(self, text):
        """ Translate text, returns the modified text. """
        return self._make_regex().sub(self, text)


def quoted_split(s):
    def strip_quotes(s):
        if s and (s[0] == '"' or s[0] == "'") and s[0] == s[-1]:
            return s[1:-1]
        return s

    return [strip_quotes(p).replace('\\"', '"').replace("\\'", "'") \
            for p in
            re.findall(r'(?:[^"\s]*"(?:\\.|[^"])*"[^"\s]*)+|(?:[^\'\s]*\'(?:\\.|[^\'])*\'[^\'\s]*)+|[^\s]+', s)]


def humanized_size(num, suffix='B', si=False):
    if si:
        units = ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']
        last_unit = 'Y'
        div = 1000.0
    else:
        units = ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']
        last_unit = 'Yi'
        div = 1024.0
    for unit in units:
        if abs(num) < div:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= div
    return "%.1f%s%s" % (num, last_unit, suffix)
