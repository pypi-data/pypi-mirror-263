import re
from glxshell.lib.stat import S_IRWXU
from glxshell.lib.stat import S_IXUSR
from glxshell.lib.stat import S_IRWXG
from glxshell.lib.stat import S_IXGRP
from glxshell.lib.stat import S_IRWXO
from glxshell.lib.stat import S_IROTH
from glxshell.lib.stat import S_IWOTH
from glxshell.lib.stat import S_IXOTH
from glxshell.lib.stat import S_ISUID
from glxshell.lib.stat import S_ISGID

# The full regular expression is something like:
# [ugoa]*([+=-][rwxXsugo]+)+(,[ugoa]*([+=-][rwxXsugo]+)+)*
users_re = re.compile(r"[ugoa]+")
operation_re = re.compile(r"[+=-]")
permissions_re = re.compile(r"[rwxXsugo]+")


# These are known permissions but not (yet?) supported because
# they are platform specific.
#  t is GNU for specifying the swap device
#  l is IRIX for mandatory locking during access
# Standard POSIX names for the different fields
# Why isn't this available via an existing python module?

# General process:
#  1) construct a mask based on the symbolic information
#       this may need existing mode information (eg, for +ugo)
#  2) apply the mask as appropriate for the given operation
def _apply_symbolic_mode(mode, users, operation, permissions, umask, isdir):
    """(mode, users, operation, permission, umask, isdir) -> new mode
    Given the 'atom' of a symbolic mode (only one operation) and an
    existing umask and the flag to tell if this is a directory or file,
    apply the symbolic information (users, operation, permissions) to
    the existing mode and return the results.
    """
    # If no users are specified, treat it the same as 'a' except that
    # the umask should be used.  If users are specified, ignore the
    # umask (same as setting the umask value to 0).
    if users == "":
        users = "a"
    else:
        umask = 0
    # This multiplier is used to turn on the bits in the appropriate
    # field.  It is 01 for other, 010 for group, 0100 for user
    # 0101 for uo, 0111 for ugo, etc.
    mult = 0
    # This is used for the '=' operator, which should only affect
    # the user ranges specified.  It contains 1 for those bits which
    # are allowed to be changed.
    user_bits = S_ISGID | S_ISUID
    # construct the multiplier and set of bits to use
    if "u" in users or "a" in users:
        mult = mult + S_IXUSR
        user_bits = user_bits | S_IRWXU
    if "g" in users or "a" in users:
        mult = mult + S_IXGRP
        user_bits = user_bits | S_IRWXG
    if "o" in users or "a" in users:
        mult = mult + S_IXOTH
        user_bits = user_bits | S_IRWXO
    assert mult != 0
    # Construct the permissions mask
    mask = 0
    if "r" in permissions:
        mask = mask | (S_IROTH * mult)
    if "w" in permissions:
        mask = mask | (S_IWOTH * mult)
    if "x" in permissions or ("X" in permissions and isdir):
        mask = mask | (S_IXOTH * mult)
    elif "X" in permissions:
        # check if one of the excute bits is set
        if mode & (S_IXOTH | S_IXGRP | S_IXUSR):
            mask = mask | (S_IXOTH * mult)
    # copy from existing bits
    if "u" in permissions:
        mask = mask | ((mode & S_IRWXU) >> 6) * mult
    if "g" in permissions:
        mask = mask | ((mode & S_IRWXG) >> 3) * mult
    if "o" in permissions:
        mask = mask | ((mode & S_IRWXO) >> 0) * mult
    # set-uid/gui bit
    if "s" in permissions:
        if "u" in users:
            mask = mask | S_ISUID
        if "g" in users:
            mask = mask | S_ISGID
        if "o" in users:
            raise ValueError("Cannot use 'o' user flag with 's' permissions")
        if "a" in users:
            raise ValueError("Cannot use 'a' user flag with 's' permissions")
    # Apply the operation
    if operation == "+":
        mode = (mode & umask) | (mode | mask) & ~umask
    elif operation == "-":
        mode = (mode & umask) | (mode & ~mask) & ~umask
    elif operation == "=":
        # only affect the specified users
        umask = umask | ~user_bits
        mode = (mode & umask) | (mask) & ~umask
    else:
        raise AssertionError("unknown operation " + operation)
    return mode


# Break the full symbolic name into "atomic" terms; that is,
# break down into groups containing only:
#  a set of users
#  a single operation
#  a set of permissions
# This require saving the value of the users if there are successive
# operation/permission pairs
def symbolic_mode(symbolic, mode=None, isdir=0, umask=0):
    """
    Convert a symbolic mode string into a mode.

    Examples:
      symbolic_mode("u+w", mode=0444) == 0644
      symbolic_mode("=x", mode=0444, umask=0700) == 0411
      symbolic_mode("og-rxw", mode=0777) == 0700
      symbolic_mode("o-rxw,g-rxw", mode=0777) == 0700
      symbolic_mode("a=rx,u+w") == 0755
      symbolic_mode("og+X", mode=0644, isdir=0) == 0644
      symbolic_mode("og+X", mode=0644, isdir=1) == 0655
    
    For more detailed information, consult your local man page for chmod.
    
    :param symbolic: the symbilic mode representation
    :type symbolic: str
    :param mode: needed because some operation add, copy or remove bits from the old mode.  If no mode is given, the default is 0755.
    :type mode: oct
    :param isdir: the X permission acts differently on files than on directories. A true value indicates this should be treated like a directory.  The default is 0, which indicates a file.
    :type isdir: int
    :param umask: used when no users are given in the mode string. The default value is 0.
    :type umask: oct
    :return: mode
    :rtype: oct
    """
    # offset position in the input
    pos = 0
    # Default mode, according to the GNU documentation
    if mode is None:
        mode = 0o755
    # scan for atoms
    while pos < len(symbolic):
        # Find users
        m = users_re.match(symbolic, pos)
        if m is None:
            users = ""
        else:
            users = m.group(0)
            pos = pos + len(users)
        while 1:
            # Find the operation
            m = operation_re.match(symbolic, pos)
            if m is None:
                raise TypeError("Missing operation in mode")
            operation = m.group(0)
            pos = pos + len(operation)
            # Find the permissions
            m = permissions_re.match(symbolic, pos)
            if m is None:
                permissions = ""
            else:
                permissions = m.group(0)
                pos = pos + len(permissions)
            # Have an atom, so apply it to the existing mode, and
            # update the mode.
            mode = _apply_symbolic_mode(mode, users, operation, permissions, umask, isdir)
            # Am I done with everything (really need a double break here)
            if not pos < len(symbolic):
                break
            # Am I at the start of a new atom?
            if symbolic[pos] == ",":
                pos = pos + 1
                break
    return mode






