import gc
import os
import sys
import termios
import re
from getpass import getuser
from time import localtime

from socket import gethostname, getfqdn

try:
    import subprocess
except ImportError:
    subprocess = None

from glxshell import APPLICATION_NAME
from glxshell import APPLICATION_VERSION
from glxshell import APPLICATION_PATCH_LEVEL
from glxshell import APPLICATION_LICENSE

from glxshell.lib.argparse import WrapperCmdLineArgParser
from glxshell.lib.cmd import Cmd
from glxshell.lib.environ import GLXEnviron
from glxshell.lib.alias import GLXAlias
from glxshell.lib.path import getcwd
from glxshell.lib.path import basename
from glxshell.lib.path import expanduser
from glxshell.lib.path import exists
from glxshell.lib.path import sep

from glxshell.utilities.alias import glxsh_alias
from glxshell.utilities.alias import parser_alias

from glxshell.utilities.basename import glxsh_basename
from glxshell.utilities.basename import parser_basename

from glxshell.utilities.cat import glxsh_cat
from glxshell.utilities.cat import parser_cat

from glxshell.utilities.cd import glxsh_cd
from glxshell.utilities.cd import parser_cd

from glxshell.utilities.clear import glxsh_clear
from glxshell.utilities.clear import parser_clear

from glxshell.utilities.chmod import glxsh_chmod
from glxshell.utilities.chmod import parser_chmod

from glxshell.utilities.cp import glxsh_cp
from glxshell.utilities.cp import parser_cp

from glxshell.utilities.date import glxsh_date
from glxshell.utilities.date import parser_date

from glxshell.utilities.df import glxsh_df
from glxshell.utilities.df import parser_df

from glxshell.utilities.dirname import glxsh_dirname
from glxshell.utilities.dirname import parser_dirname

from glxshell.utilities.du import glxsh_du
from glxshell.utilities.du import parser_du
from glxshell.lib.completers import glxsh_complete_du

from glxshell.utilities.echo import glxsh_echo
from glxshell.utilities.echo import parser_echo

from glxshell.utilities.env import glxsh_env
from glxshell.utilities.env import parser_env

from glxshell.utilities.exit import glxsh_exit

from glxshell.utilities.false import glxsh_false
from glxshell.utilities.false import parser_false

from glxshell.utilities.head import glxsh_head
from glxshell.utilities.head import parser_head

from glxshell.utilities.umask import glxsh_umask
from glxshell.utilities.umask import parser_umask

from glxshell.utilities.ls import glxsh_ls
from glxshell.utilities.ls import parser_ls

from glxshell.utilities.mkdir import glxsh_mkdir
from glxshell.utilities.mkdir import parser_mkdir

from glxshell.utilities.mv import glxsh_mv
from glxshell.utilities.mv import parser_mv

from glxshell.utilities.pwd import glxsh_pwd
from glxshell.utilities.pwd import parser_pwd

from glxshell.utilities.rm import glxsh_rm
from glxshell.utilities.rm import parser_rm

from glxshell.utilities.rmdir import glxsh_rmdir
from glxshell.utilities.rmdir import parser_rmdir

from glxshell.utilities.sleep import glxsh_sleep
from glxshell.utilities.sleep import parser_sleep

from glxshell.utilities.uname import glxsh_uname
from glxshell.utilities.uname import parser_uname

from glxshell.utilities.unalias import glxsh_unalias
from glxshell.utilities.unalias import parser_unalias

from glxshell.utilities.tail import glxsh_tail
from glxshell.utilities.tail import parser_tail

from glxshell.utilities.tee import glxsh_tee
from glxshell.utilities.tee import parser_tee

from glxshell.utilities.time import glxsh_time
from glxshell.utilities.time import parser_time

from glxshell.utilities.touch import glxsh_touch
from glxshell.utilities.touch import parser_touch

from glxshell.utilities.true import glxsh_true
from glxshell.utilities.true import parser_true

from glxshell.utilities.tty import glxsh_tty
from glxshell.utilities.tty import parser_tty

from glxshell.lib.utils import size_of
from glxshell.utilities.exit import parser_exit

from glxshell.lib.completers import glxsh_completer_file
from glxshell.lib.completers import glxsh_completer_directory
from glxshell.lib.completers import glxsh_complete_chmod
from glxshell.lib.completers import glxsh_complete_rmdir
from glxshell.lib.completers import glxsh_complete_echo


class GLXUsh(Cmd, GLXEnviron, GLXAlias):
    if hasattr(sys.implementation, "mpy"):
        loader_mpy = "MPY %s" % sys.implementation.mpy
    else:
        loader_mpy = ""

    if hasattr(gc, "mem_free") and hasattr(gc, "mem_alloc"):
        gc.collect()
        memory_total = "%s MEMORY SYSTEM\n" % str(size_of(gc.mem_free() + gc.mem_alloc())).upper()
        memory_free = "%s FREE\n" % str(size_of(gc.mem_free())).upper()
    elif hasattr(os, "sysconf"):
        memory_total = "%s RAM SYSTEM\n" % str(
            size_of(os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES"))).upper()
        memory_free = "%s FREE\n" % str(size_of(os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_AVPHYS_PAGES"))).upper()
    else:
        memory_total = ""
        memory_free = ""

    intro = """******************************* %s V%s **********************************

%s
LOADER %s %s %s
EXEC PYTHON V%s
%s%s""" % (
        APPLICATION_NAME.upper(),
        APPLICATION_VERSION.upper(),
        APPLICATION_LICENSE.upper(),
        sys.implementation.name.upper(),
        ".".join(str(item).upper() for item in list(sys.implementation.version)),
        loader_mpy,
        sys.version.upper(),
        memory_total,
        memory_free,
    )
    dow = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
    mon = ("???", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

    ps1_clean_up_1 = re.compile(r'\$\{.*\}')
    ps1_clean_up_2 = re.compile(r'\$\(.*\)')
    ps1_exit_code = re.compile(r"\$\?")
    ps1_hostname_sort = re.compile(r"\\h")
    ps1_hostname = re.compile(r"\\H")
    ps1_date = re.compile(r"\\d")
    ps1_shell = re.compile(r"\\s")
    ps1_username = re.compile(r"\\u")
    ps1_shell_version = re.compile(r"\\v")
    ps1_shell_release = re.compile(r"\\V")
    ps1_working_directory = re.compile(r"\\w")
    ps1_working_directory_basename = re.compile(r"\\W")
    ps1_prompt_sign = re.compile(r"\\\$")
    ps1_newline = re.compile(r"\\n")
    ps1_carriage_return = re.compile(r"\\r")
    ps1_bell = re.compile(r"\\a")
    ps1_time_24_hour = re.compile(r"\\t")
    ps1_time_12_hour = re.compile(r"\\T")
    ps1_time_am_pm = re.compile(r"\\@")
    ps1_begin_a_sequence_of_non_printing_characters = re.compile(r"\\\[\\033")
    ps1_end_a_sequence_of_non_printing_characters = re.compile(r"\\\]")
    ps1_virtual_env = re.compile(r"\$VIRTUAL_ENV")

    def __init__(self):
        super().__init__()

        GLXEnviron.__init__(self)
        GLXAlias.__init__(self)
        if os.isatty(sys.stdin.fileno()):
            self.init_inside_a_tty = True
        else:
            self.init_inside_a_tty = False

        # Create Environment
        if hasattr(os, "environ"):
            self.environ = os.environ.copy()
        else:
            self.setenv("PATH", getcwd(), 1)
            self.setenv("HOME", sep, 1)
            self.setenv("PWD", getcwd(), 1)

        # PS1
        self.setenv("PS1", r"$VIRTUAL_ENV\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[00;34m\]\w\[\033[00m\]\$ ")
        self.update_columns_and_lines_vars()
        self.load_alias()

    def load_alias(self):
        file = expanduser("~%s.glxsh_alias" % sep)
        if exists(file):
            with open(file=file, mode="r", encoding="utf8") as alias_file:
                for line in alias_file.readlines():
                    self.do_alias(line)

    @property
    def prompt(self):
        tm = localtime()

        if self.environ.get("PS1"):
            tmp_value = self.environ.get("PS1")
            if self.environ.get("VIRTUAL_ENV"):
                tmp_value = self.ps1_virtual_env.sub(
                    "(%s)" % basename(self.environ.get("VIRTUAL_ENV")),
                    tmp_value)

            tmp_value = self.ps1_clean_up_1.sub("", tmp_value)
            tmp_value = self.ps1_clean_up_2.sub("", tmp_value)

            # Exit code
            if self.exit_code:
                exit_code = "\x1b[01;31m%s\x1b[00m" % self.exit_code
            else:
                exit_code = "\x1b[01;32m%s\x1b[00m" % self.exit_code
            tmp_value = self.ps1_exit_code.sub(exit_code, tmp_value)

            # Special prompt variable characters:
            #  \d   The date, in "Weekday Month Date" format (e.g., "Tue May 26").
            tmp_value = self.ps1_date.sub("%s %s %02d" % (self.dow[tm[6]], self.mon[tm[1]], tm[2]), tmp_value)

            #  \h   The hostname, up to the first . (e.g. deckard)
            tmp_value = self.ps1_hostname_sort.sub(gethostname(), tmp_value)

            #  \H   The hostname. (e.g. deckard.SS64.com)
            tmp_value = self.ps1_hostname.sub(getfqdn(), tmp_value)

            #  \j   The number of jobs currently managed by the shell.

            #  \l   The basename of the shell's terminal device name.

            #  \s   The name of the shell, the basename of $0 (the portion following the final slash).
            tmp_value = self.ps1_shell.sub(APPLICATION_NAME, tmp_value)

            #  \t   The time, in 24-hour HH:MM:SS format.
            tmp_value = self.ps1_time_24_hour.sub("%02d:%02d:%02d" % (tm[3], tm[4], tm[5]), tmp_value)

            #  \T   The time, in 12-hour HH:MM:SS format.
            if tm[3] in range(13, 23, 1):
                hour = tm[3] - 12
            elif tm[3] == 0:
                hour = 12
            else:
                hour = tm[3]
            tmp_value = self.ps1_time_12_hour.sub("%02d:%02d:%02d" % (hour, tm[4], tm[5]), tmp_value)

            #  \@   The time, in 12-hour am/pm format.
            if tm[3] in range(1, 11, 1):
                am_pm_text = 'AM'
            elif tm[3] in range(13, 23, 1):
                am_pm_text = 'PM'
            elif tm[3] == 0:
                am_pm_text = 'AM'
            else:
                am_pm_text = ''
            tmp_value = self.ps1_time_am_pm.sub(am_pm_text, tmp_value)

            #  \u   The username of the current user.
            tmp_value = self.ps1_username.sub(getuser(), tmp_value)

            #  \v   The version of Bash (e.g., 2.00)
            tmp_value = self.ps1_shell_version.sub(APPLICATION_VERSION, tmp_value)

            #  \V   The release of Bash, version + patchlevel (e.g., 2.00.0)
            tmp_value = self.ps1_shell_release.sub("%s.%s" % (APPLICATION_VERSION, APPLICATION_PATCH_LEVEL), tmp_value)

            #  \w   The current working directory.
            tmp_value = self.ps1_working_directory.sub(getcwd().replace("%s%s" % (self.environ.get("HOME"), sep),
                                                                        "~%s" % sep),
                                                       tmp_value)

            #  \W   The basename of $PWD.
            tmp_value = self.ps1_working_directory_basename.sub(basename(self.environ.get("PWD")), tmp_value)

            #  \!   The history number of this command.

            #  \#   The command number of this command.

            #  \$   If you are not root, inserts a "$"; if you are root, you get a "#"  (root uid = 0)
            tmp_value = self.ps1_prompt_sign.sub("$" if os.getuid() else "#", tmp_value)

            #  \nnn   The character whose ASCII code is the octal value nnn.

            #  \n   A newline.
            tmp_value = self.ps1_newline.sub("\n", tmp_value)

            #  \r   A carriage return.
            tmp_value = self.ps1_carriage_return.sub("\r", tmp_value)

            #  \e   An escape character (typically a color code).

            #  \a   A bell character.
            tmp_value = self.ps1_bell.sub("\a", tmp_value)

            #  \\   A backslash.
            # "\\": "\\",

            #  \[   Begin a sequence of non-printing characters. (like color escape sequences). This
            #       allows bash to calculate word wrapping correctly.
            tmp_value = self.ps1_begin_a_sequence_of_non_printing_characters.sub("\x1b", tmp_value)

            #  \]   End a sequence of non-printing characters.
            tmp_value = self.ps1_end_a_sequence_of_non_printing_characters.sub("", tmp_value)

            return tmp_value

        return "%s%s " % (self.exit_code, ">")

    @staticmethod
    def do_EOF(_):
        sys.stdout.write("\n")
        sys.stdout.flush()
        return True

    def default(self, line):
        sys.stdout.write("glxsh: %s\n" % line)
        self.exit_code = 127

    def precmd(self, line):
        if not str(line).startswith("alias") and not str(line).startswith("unalias"):
            for key, value in self.alias.items():
                # TODO: Create a true regexpr for found and replace alias
                # line = line.replace(" %s " % key, " %s " % value)
                # line = line.replace("%s " % key, "%s " % value)
                # line = line.replace(" %s" % key, " %s" % value)
                if line.rstrip() == key:
                    line = line.replace(key, value)

        return line

    def postcmd(self, stop, line):
        self.update_columns_and_lines_vars()
        return stop

    def onecmd(self, line):
        cmd, arg, line = self.parseline(line)

        if not line:
            return self.emptyline()
        if cmd is None:
            return self.default("cmd is None for: %s" % line)
        self.lastcmd = line
        if line == "EOF":
            self.lastcmd = ""
        if cmd == "":
            return self.default("cmd is '' for: %s" % line)

        if "|" in line:
            return self.run_multiple_commands(line)

        return self.run_simple_command(cmd, arg, line)

    def update_columns_and_lines_vars(self):
        if self.init_inside_a_tty:
            self.environ["COLUMNS"] = str(os.get_terminal_size().columns)
            self.environ["LINES"] = str(os.get_terminal_size().lines)

    @staticmethod
    def cmdline_split(s, platform=1):
        """Multi-platform variant of shlex.split() for command-line splitting.
        For use with subprocess, for argv injection etc. Using fast REGEX.

        platform: 'this' = auto from current platform;
                  1 = POSIX;
                  0 = Windows/CMD
                  (other values reserved)
        """
        if platform == 'this':
            platform = (sys.platform != 'win32')
        if platform == 1:
            RE_CMD_LEX = r'''"((?:\\["\\]|[^"])*)"|'([^']*)'|(\\.)|(&&?|\|\|?|\d?\>|[<])|([^\s'"\\&|<>]+)|(\s+)|(.)'''
        elif platform == 0:
            RE_CMD_LEX = r'''"((?:""|\\["\\]|[^"])*)"?()|(\\\\(?=\\*")|\\")|(&&?|\|\|?|\d?>|[<])|([^\s"&|<>]+)|(\s+)|(.)'''
        else:
            raise AssertionError('unkown platform %r' % platform)

        args = []
        accu = None  # collects pieces of one arg
        for qs, qss, esc, pipe, word, white, fail in re.findall(RE_CMD_LEX, s):
            if word:
                pass  # most frequent
            elif esc:
                word = esc[1]
            elif white or pipe:
                if accu is not None:
                    args.append(accu)
                if pipe:
                    args.append(pipe)
                accu = None
                continue
            elif fail:
                raise ValueError("invalid or incomplete shell string")
            elif qs:
                word = qs.replace('\\"', '"').replace('\\\\', '\\')
                if platform == 0:
                    word = word.replace('""', '"')
            else:
                word = qss  # may be even empty; must be last

            accu = (accu or '') + word

        if accu is not None:
            args.append(accu)

        return args

    def run_multiple_commands(self, line):
        # save stdin and stdout for restoring later on
        s_in, s_out = (0, 0)
        s_in = os.dup(0)
        s_out = os.dup(1)

        # first command takes command from stdin
        fdin = os.dup(s_in)

        # iterate over all the commands that are piped
        for command in line.split("|"):
            # fdin will be stdin if it's the first iteration
            # and the readable end of the pipe if not.
            os.dup2(fdin, 0)
            os.close(fdin)

            # restore stdout if this is the last command
            if command == line.split("|")[-1]:
                fdout = os.dup(s_out)
            else:
                fdin, fdout = os.pipe()

            # redirect stdout to pipe
            os.dup2(fdout, 1)
            os.close(fdout)

            # make tasks it use sys.stdin or/and sys.stdout
            tmp_cmd, tmp_arg, tmp_line = self.parseline(command)
            self.run_simple_command(tmp_cmd, tmp_arg, tmp_line)

        # restore stdout and stdin
        os.dup2(s_in, 0)
        os.dup2(s_out, 1)
        os.close(s_in)
        os.close(s_out)

    def run_simple_command(self, cmd, arg, line):
        if hasattr(self, "do_%s" % cmd):
            try:
                func = getattr(self, "do_%s" % cmd)
                self.exit_code = func(arg)
                self.setenv("?", str(self.exit_code))
            except KeyboardInterrupt:
                pass
            except SystemExit as code:
                self.exit_code = code
                self.setenv("?", str(self.exit_code))
                return True
            return None

        try:
            stdin_fd = sys.stdin.fileno()
            save_settings = termios.tcgetattr(stdin_fd)
        except (ModuleNotFoundError, IOError):
            save_settings = None
            stdin_fd = -1

        try:
            pr = subprocess.run(line.split(" "), start_new_session=True, env=self.environ, check=False)
            self.exit_code = pr.returncode
            self.setenv("?", str(self.exit_code))
        except KeyboardInterrupt:
            pass

        except FileNotFoundError:
            sys.stdout.write("%s: %s : command not found\n" % (APPLICATION_NAME, cmd))
            self.exit_code = 127
            self.setenv("?", str(self.exit_code))
        finally:
            if save_settings:
                termios.tcsetattr(stdin_fd, termios.TCSANOW, save_settings)
        return None

    def _print_help(self, parser):
        if self.environ.get("COLUMNS"):
            parser.print_help(columns=int(self.environ.get("COLUMNS")))
        else:
            parser.print_help()

    ##### Commands
    def help_alias(self):
        self._print_help(parser_alias)

    def do_alias(self, line):
        return (glxsh_alias(
            string=line,
            shell=self,
        ))

    def help_basename(self):
        self._print_help(parser_basename)

    @WrapperCmdLineArgParser(parser_basename)
    def do_basename(self, _, parsed):
        return glxsh_basename(
            string=parsed.string,
            suffix=parsed.suffix,
        )

    @WrapperCmdLineArgParser(parser_cat)
    def do_cat(self, _, parsed):
        return glxsh_cat(
            files=parsed.file,
        )

    def help_cat(self):
        self._print_help(parser_cat)

    @staticmethod
    def complete_cat(text, line, begidx, endidx):
        return glxsh_completer_file(text, line, begidx, endidx)

    @WrapperCmdLineArgParser(parser_cd)
    def do_cd(self, _, parsed):
        return glxsh_cd(
            directory=parsed.directory,
            logical=parsed.logical,
            physical=parsed.physical,
            shell=self,
        )

    def help_cd(self):
        self._print_help(parser_cd)

    @staticmethod
    def complete_cd(text, line, begidx, endidx):
        return glxsh_completer_directory(text, line, begidx, endidx)

    # clear
    @WrapperCmdLineArgParser(parser_clear)
    def do_clear(self, _, __):
        return glxsh_clear()

    def help_clear(self):
        self._print_help(parser_clear)

    @WrapperCmdLineArgParser(parser_chmod)
    def do_chmod(self, _, parsed):
        if not parsed.mode or not parsed.file:
            parser_chmod.print_usage()
            return 1
        return glxsh_chmod(
            recursive=parsed.recursive,
            mode=parsed.mode,
            file=parsed.file,
        )

    def help_chmod(self):
        self._print_help(parser_chmod)

    @staticmethod
    def complete_chmod(text, line, begidx, endidx):
        return glxsh_complete_chmod(text, line, begidx, endidx)

    # cp
    @WrapperCmdLineArgParser(parser_cp)
    def do_cp(self, _, parsed):
        return glxsh_cp(
            source_file=parsed.source_file,
            target_file=parsed.target_file,
            interactive=parsed.interactive,
        )

    def help_cp(self):
        self._print_help(parser_cp)

    @WrapperCmdLineArgParser(parser_date)
    def do_date(self, line, parsed):
        if parsed.u:
            line = line.replace("-u ", "")
            line = line.replace("-u", "")

        return glxsh_date(
            u=parsed.u,
            custom_format=line,
            shell=self,
        )

    def help_date(self):
        self._print_help(parser_date)

    # df
    @WrapperCmdLineArgParser(parser_df)
    def do_df(self, _, parsed):
        return glxsh_df(
            file=parsed.file,
            block_size=parsed.kilo,
            total=parsed.total,
            human_readable=parsed.human_readable,
        )

    def help_df(self):
        self._print_help(parser_df)

    # dirname
    @WrapperCmdLineArgParser(parser_dirname)
    def do_dirname(self, _, parsed):
        return glxsh_dirname(
            parsed.string,
        )

    def help_dirname(self):
        self._print_help(parser_dirname)

    @WrapperCmdLineArgParser(parser_du)
    def do_du(self, _, parsed):
        return glxsh_du(
            a=parsed.a,
            H=parsed.H,
            k=parsed.k,
            L=parsed.L,
            s=parsed.s,
            x=parsed.x,
            files=parsed.files
        )

    @staticmethod
    def complete_du(text, line, begidx, endidx):
        return glxsh_complete_du(text, line, begidx, endidx)

    def help_du(self):
        self._print_help(parser_du)

    def help_echo(self):
        self._print_help(parser_echo)

    @WrapperCmdLineArgParser(parser_echo)
    def do_echo(self, line, parsed):
        if parsed.newline:
            line = line.replace("-n ", "")
        return glxsh_echo(
            string=line,
            newline=parsed.newline,
            shell=self,
        )

    def complete_echo(self, text, line, begidx, endidx):
        return glxsh_complete_echo(text, line, begidx, endidx, shell=self)

    def help_env(self):
        self._print_help(parser_env)

    @WrapperCmdLineArgParser(parser_env)
    def do_env(self, _, parsed):
        return glxsh_env(
            name=parsed.name,
            utility=parsed.utility,
            argument=parsed.argument,
            shell=self,
        )

    @WrapperCmdLineArgParser(parser_exit)
    def do_exit(self, _, parsed):
        if parsed.code:
            self.exit_code = parsed.code[0]
        return glxsh_exit(code=parsed.code, shell=self)

    def help_exit(self):
        self._print_help(parser_exit)

    @WrapperCmdLineArgParser(parser_false)
    def do_false(self, _, __):
        return glxsh_false()

    def help_false(self):
        self._print_help(parser_false)

    @WrapperCmdLineArgParser(parser_head)
    def do_head(self, _, parsed):
        return glxsh_head(
            files=parsed.file,
            number=parsed.number,
        )

    @staticmethod
    def complete_head(text, line, begidx, endidx):
        return glxsh_completer_file(text, line, begidx, endidx)

    def help_head(self):
        self._print_help(parser_head)

    def emptyline(self):
        sys.stdout.write("\n")

    @WrapperCmdLineArgParser(parser_ls)
    def do_ls(self, _, parsed):
        return glxsh_ls(
            A=parsed.A,
            C=parsed.C,
            F=parsed.F,
            H=parsed.H,
            L=parsed.L,
            recurse=parsed.recurse,
            S=parsed.S,
            a=parsed.a,
            c=parsed.c,
            d=parsed.d,
            f=parsed.f,
            g=parsed.g,
            i=parsed.i,
            k=parsed.k,
            l=parsed.l,
            m=parsed.m,
            n=parsed.n,
            o=parsed.o,
            p=parsed.p,
            q=parsed.q,
            r=parsed.r,
            s=parsed.s,
            t=parsed.t,
            u=parsed.u,
            x=parsed.x,
            one=parsed.one,
            file=parsed.file,
            shell=self,
        )

    def help_ls(self):
        self._print_help(parser_ls)

    @WrapperCmdLineArgParser(parser_mkdir)
    def do_mkdir(self, _, parsed):
        if not parsed.dir:
            parser_mkdir.print_usage()
            return 1

        return glxsh_mkdir(
            directories=parsed.dir,
            parents=parsed.parents,
            mode=parsed.mode,
        )

    def help_mkdir(self):
        self._print_help(parser_mkdir)

    @WrapperCmdLineArgParser(parser_mv)
    def do_mv(self, _, parsed):
        if not parsed.target_file or parsed.source_file:
            parser_mv.print_usage()
            # return 1
            return 1

        return glxsh_mv(
            source_file=parsed.source_file,
            target_file=parsed.target_file,
            target_dir=parsed.target_dir,
            force=parsed.force,
            interactive=parsed.interactive,
        )

    def help_mv(self):
        self._print_help(parser_mv)

    @WrapperCmdLineArgParser(parser_pwd)
    def do_pwd(self, _, parsed):
        return glxsh_pwd(
            logical=parsed.logical,
            physical=parsed.physical,
        )

    def help_pwd(self):
        self._print_help(parser_pwd)

    @WrapperCmdLineArgParser(parser_rm)
    def do_rm(self, _, parsed):
        if not parsed.file:
            parser_rm.print_usage()
            return 1

        return glxsh_rm(
            file=parsed.file,
            recursive=parsed.recursive,
            interactive=parsed.interactive,
            force=parsed.force,
        )

    def help_rm(self):
        self._print_help(parser_rm)

    @staticmethod
    def complete_rmdir(text, line, begidx, endidx):
        return glxsh_complete_rmdir(text, line, begidx, endidx)

    @WrapperCmdLineArgParser(parser_rmdir)
    def do_rmdir(self, _, parsed):
        if not parsed.dir:
            parser_rmdir.print_usage()
            return 1

        return glxsh_rmdir(
            directories=parsed.dir,
            parents=parsed.parents,
        )

    def help_rmdir(self):
        self._print_help(parser_rmdir)

    @WrapperCmdLineArgParser(parser_sleep)
    def do_sleep(self, _, parsed):
        if not parsed.time:
            parser_sleep.print_usage()
            return 1

        return glxsh_sleep(
            sec=parsed.time,
        )

    @WrapperCmdLineArgParser(parser_tee)
    def do_tee(self, _, parsed):
        return glxsh_tee(
            a=parsed.a,
            i=parsed.i,
            files=parsed.file,
        )

    def help_tee(self):
        self._print_help(parser_tee)

    @WrapperCmdLineArgParser(parser_time)
    def do_time(self, line, parsed):
        return glxsh_time(
            p=parsed.p,
            utility=parsed.utility,
            argument=parsed.argument,
            line=line,
            shell=self,
        )

    def help_time(self):
        self._print_help(parser_time)

    @WrapperCmdLineArgParser(parser_touch)
    def do_touch(self, _, parsed):
        return glxsh_touch(
            a=parsed.a,
            c=parsed.c,
            d=parsed.d,
            m=parsed.m,
            r=parsed.r,
            t=parsed.t,
            files=parsed.file,
        )

    def help_touch(self):
        self._print_help(parser_touch)

    @WrapperCmdLineArgParser(parser_true)
    def do_true(self, _, __):
        return glxsh_true()

    def help_true(self):
        self._print_help(parser_true)

    @WrapperCmdLineArgParser(parser_tty)
    def do_tty(self, _, __):
        return glxsh_tty()

    def help_tty(self):
        self._print_help(parser_tty)

    def help_sleep(self):
        if self.environ.get("COLUMNS"):
            parser_sleep.print_help(columns=int(self.environ.get("COLUMNS")))
        else:
            parser_sleep.print_help()

    @WrapperCmdLineArgParser(parser_uname)
    def do_uname(self, _, parsed):
        return glxsh_uname(
            all=parsed.all,
            sysname=parsed.sysname,
            nodename=parsed.nodename,
            release=parsed.release,
            version=parsed.version,
            machine=parsed.machine,
        )

    def help_uname(self):
        self._print_help(parser_uname)

    def help_umask(self):
        self._print_help(parser_umask)

    @WrapperCmdLineArgParser(parser_umask)
    def do_umask(self, _, parsed):
        return glxsh_umask(
            mask=parsed.mask,
            symbolic=parsed.symbolic,
        )

    def help_unalias(self):
        self._print_help(parser_unalias)

    @WrapperCmdLineArgParser(parser_unalias)
    def do_unalias(self, _, parsed):
        return glxsh_unalias(
            a=parsed.a,
            alias_name=parsed.alias_name,
            shell=self,
        )

    @WrapperCmdLineArgParser(parser_tail)
    def do_tail(self, _, parsed):
        return glxsh_tail(
            c=parsed.c,
            f=parsed.f,
            n=parsed.n,
            files=parsed.file,
        )

    def help_tail(self):
        self._print_help(parser_tail)
