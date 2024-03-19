# from https://github.com/octopusengine/micropython-shell/blob/master/vt100.py
import sys


def get_cursor_position():
    height = 0
    width = 0
    num = ''

    sys.stdout.write('\x1b[6n')
    while True:
        char = sys.stdin.read(1)
        if char == 'R':
            width = int(num)
            break
        if char == '\x1b':
            width = 0
            height = 0
            num = ''
            continue
        if char == '[':
            continue
        if char == ';':
            height = int(num)
            num = ''
            continue
        num += char
    return (width, height)


def get_terminal_size():
    """Print out a sequence of ANSI escape code which will report back the
    size of the window.
    """
    # ESC 7         - Save cursor position
    # ESC 8         - Restore cursor position
    # ESC [r        - Enable scrolling for entire display
    # ESC [row;colH - Move to cursor position
    # ESC [6n       - Device Status Report - send ESC [row;colR
    repl= None
    if 'repl_source' in dir(pyb):
        repl = pyb.repl_source()
    if repl is None:
        repl = pyb.USB_VCP()
    repl.send(b'\x1b7\x1b[r\x1b[999;999H\x1b[6n')
    pos = b''
    while True:
        char = repl.recv(1)
        if char == b'R':
            break
        if char != b'\x1b' and char != b'[':
            pos += char
    repl.send(b'\x1b8')
    (height, width) = [int(i, 10) for i in pos.split(b';')]
    return height, width