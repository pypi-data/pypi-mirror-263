import re
import os
import sys

from glxshell.lib.argparse import ArgumentParser
from glxshell.lib.symbolic_mode import symbolic_mode
from glxshell.lib.path import isdir
def symbolic_matcher():
    return re.compile(r"([ugo]*|a)([+-=])([^\s,]*)")


order = "rwx"
name_to_value = {"x": 1, "w": 2, "r": 4}
value_to_name = {v: k for k, v in name_to_value.items()}

class_to_loc = {"u": 6, "g": 3, "o": 0}  # how many bits to shift this class by
loc_to_class = {v: k for k, v in class_to_loc.items()}

function_map = {
    "+": lambda orig, new: orig | new,  # add the given permission
    "-": lambda orig, new: orig & ~new,  # remove the given permission
    "=": lambda orig, new: new,  # set the permissions exactly
}

def invert(perms):
    return 0o777 - perms


def get_oct_digits(mode):
    """
    Separate a given integer into its three components
    """
    if not 0 <= mode <= 0o777:
        raise ValueError("expected a value between 000 and 777")
    return {"u": (mode & 0o700) >> 6, "g": (mode & 0o070) >> 3, "o": mode & 0o007}


def from_oct_digits(digits):
    o = 0
    for c, m in digits.items():
        o |= m << class_to_loc[c]
    return o


def get_symbolic_rep_single(digit):
    """
    Given a single octal digit, return the appropriate string representation.
    For example, 6 becomes "rw".
    """
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
    """
    Given a string representation, return the appropriate octal digit.
    For example, "rw" becomes 6.
    """
    o = 0
    for sym in set(rep):
        o += name_to_value[sym]
    return o


parser_umask = ArgumentParser(
    name="umask - get or set the file mode creation mask",
    description="""The umask utility shall set the file mode creation mask of the current shell execution environment (see Shell Execution Environment) to the value specified by the mask operand. This mask shall affect the initial value of the file permission bits of subsequently created files. If umask is called in a subshell or separate utility execution environment, such as one of the following:

(umask 002)
nohup umask ...
find . -exec umask ... \;

it shall not affect the file mode creation mask of the caller's environment.

If the mask operand is not specified, the umask utility shall write to standard output the value of the file mode creation mask of the invoking process.
""",
)

parser_umask.add_argument(
    "mask",
    nargs="?",
    const=0,
    help="""A string specifying the new file mode creation mask. The string is treated in the same way as the mode operand described in the EXTENDED DESCRIPTION section for chmod.
For a symbolic_mode value, the new value of the file mode creation mask shall be the logical complement of the file permission bits portion of the file mode specified by the symbolic_mode string.

In a symbolic_mode value, the permissions op characters '+' and '-' shall be interpreted relative to the current file mode creation mask; '+' shall cause the bits for the indicated permissions to be cleared in the mask; '-' shall cause the bits for the indicated permissions to be set in the mask.

The interpretation of mode values that specify file mode bits other than the file permission bits is unspecified.

In the octal integer form of mode, the specified bits are set in the file mode creation mask.

The file mode creation mask shall be set to the resulting numeric value.

The default output of a prior invocation of umask on the same system with no operand also shall be recognized as a mask operand.
""",
)
parser_umask.add_argument(
    "-S",
    dest="symbolic",
    action="store_true",
    default=False,
    help="Produce symbolic output.",
)
def single_symbolic_arg(arg, old=None):
    # we'll assume this always operates in the "forward" direction (on the
    # current permissions) rather than on the mask directly.
    if old is None:
        old = os.umask(0)
        os.umask(old)

    match = symbolic_matcher.match(arg)
    if not match:
        raise ValueError("could not parse argument %r" % arg)

    class_, op, mask = match.groups()

    if class_ == "a":
        class_ = "ugo"

    invalid_chars = [i for i in mask if i not in name_to_value]
    if invalid_chars:
        raise ValueError("invalid mask %r" % mask)

    digits = get_oct_digits(old)
    new_num = get_numeric_rep_single(mask)

    for c in set(class_):
        digits[c] = function_map[op](digits[c], new_num)

    return from_oct_digits(digits)


def valid_numeric_argument(x):
    try:
        return len(x) == 3 and all(0 <= int(i) <= 7 for i in x)
    except:
        return False



def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]
    for permissions in [int(n) for n in str(octal)]:
        for value, letter in value_letters:
            if permissions >= value: # 
                result += letter
                permissions -= value # 
            else:
                result += "-"
    return result

def glxsh_umask(mask=None, symbolic=True):
    # Get the current umask which involves having to set it temporarily.
    cur = os.umask(0)
    os.umask(cur)
    if mask:
        print(cur)
        print(mask)
        sys.stdout.write("%s\n" % oct(0o777 - symbolic_mode(mask, umask=cur, isdir=0)))


        # os.umask(cur)
        return 0
    else:
        # When the mask operand is not specified, the umask utility shall write a message to standard output
        # that can later be used as a umask mask operand.
        if symbolic:
            # to_print = get_symbolic_rep(invert(cur))
            sys.stdout.write( "%s\n" % get_symbolic_rep(invert(cur)))
            sys.stdout.write( "%s\n" % octal_to_string(invert(cur)))
            return 0
        else:
            to_print = oct(cur)[2:]
            while len(to_print) < 3:
                to_print = "0%s" % to_print
        sys.stdout.write("%s\n" % to_print)
        return 0

