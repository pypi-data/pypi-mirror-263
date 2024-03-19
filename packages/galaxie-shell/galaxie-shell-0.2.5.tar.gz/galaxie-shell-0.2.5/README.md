[![License: WTFPL](https://img.shields.io/badge/License-WTFPL-brightgreen.svg)](http://www.wtfpl.net/about/) [![Documentation Status](https://readthedocs.org/projects/galaxie-shell/badge/?version=latest)](https://galaxie-shell.readthedocs.io/en/latest/?badge=latest)
```text
                  ________        __                 __        
                 /  _____/_____  |  | _____  ___  __|__| ____  
                /   \  ___\__  \ |  | \__  \ \  \/  /  |/ __ \ 
                \    \_\  \/ __ \|  |__/ __ \_>    <|  \  ___/_
                 \________(______/____(______/__/\__\__|\_____/
```
# GLXSH - Galaxie Shell
## The Project
The goal of Galaxie-Shell is to provide a POSIX Shell for micro system like pyBoard or MicroPi.

at end it should be possible to execute POSIX Script Shell on MicroPython (Long time target).

The application Galaxie Shell is a Read Eval Print Loop (`RELP <https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop>`_) write with `python <https://www.python.org/>`_ based on top of pycopy-lib `cmd <https://github.com/pfalcon/pycopy-lib/tree/master/cmd>`_ it self build on top of MicroPython.

The project implement POSIX Standard from the OpenGroup
https://pubs.opengroup.org/onlinepubs/9699919799/utilities/

The OpenGroup permit a implementation where all utilities are builtins command, and that is what Galaxie-Shell do.
I code it, because i like understand how a system work. Copy the code , use it , that is here for the public community.


## Links

  Codeberg: https://codeberg.org/Tuuux/galaxie-shell/

  Read the Doc: https://galaxie-shell.readthedocs.io/

  PyPI: https://pypi.org/project/galaxie-shell/

  PyPI Test: https://test.pypi.org/project/galaxie-shell/

  Wokwi: https://wokwi.com/projects/312818372713644610

## All ready implemented features

* Totally autonomous All in One shell
* Capability to build a **one-file** static binary file
* Can load a script file as argument
* Can execute command from passing arguments
* Interactive shell when call without arguments
* Builtins POSIX command (basename, cat, cd, mkdir, pwd, rmdir, uname, etc ...)
* Exit status for build in or external command
* POSIX Pipe
* Alias and UnAlias
* PS1 env var can be export

## Application

* Use on front of a [Unikernel](https://fr.wikipedia.org/wiki/Unikernel)
* Use on front of a minimal `Alpine Linux <https://alpinelinux.org/>`_ or `OpenWrt <https://openwrt.org/>`_
* Simplify CI CD
* Use a MicroPython device as a Unix host

## Installation
### Installation via pip
```bash
pip install galaxie-shell
```

### Installation via pip (test)
```bash
pip install -i https://test.pypi.org/simple/ galaxie-shell
```

## Next Step:

Now you can the start the **glxsh** entry point
On Unix host with MicroPython

```text
  $> micropython ./glxsh
  ******************************* GLXUSH V0.2.5 **********************************

  LICENSE WTFPL V2
  LOADER MICROPYTHON V1.18.0 MPY 2566
  EXEC PYTHON V3.4.0
  1.98MB MEMORY SYSTEM
  1.91MB FREE

  >
```
On Debian host with Python

```text
  ******************************* GLXSH V0.2.5 **********************************

  LICENSE WTFPL V2
  LOADER CPYTHON 3.9.2.FINAL.0
  EXEC PYTHON V3.9.2 (DEFAULT, FEB 28 2021, 17:03:44)
  [GCC 10.2.1 20210110]
  7.60GB RAM SYSTEM
  245.14MB FREE

  >
```

For each command you can get help with ``man`` command line, by exemple for ``ls`` help use ``man ls``, or call ``man`` without argument for know builtin commands list.

**Note**:
Internal builtins commands have precedence, if a command is not Internal builtins commands then glxshell , call it as subprocess.

```text
  > man

    Documented commands (type man <topic>):
    =======================================
    alias     cd     cp    dirname  env    head  mkdir  rm     tail  touch  umask
    basename  chmod  date  du       exit   ls    mv     rmdir  tee   true   unalias
    cat       clear  df    echo     false  man   pwd    sleep  time  tty    uname
```



## Builtins implemented utilities
* `alias <https://galaxie-shell.readthedocs.io/en/latest/man/alias.html>`_
* `basename <https://galaxie-shell.readthedocs.io/en/latest/man/basenme.html>`_
* `cat <https://galaxie-shell.readthedocs.io/en/latest/man/cat.html>`_
* `cd <https://galaxie-shell.readthedocs.io/en/latest/man/cd.html>`_
* `chmod <https://galaxie-shell.readthedocs.io/en/latest/man/chmod.html>`_
* `clear <https://galaxie-shell.readthedocs.io/en/latest/man/clear.html>`_
* `cp <https://galaxie-shell.readthedocs.io/en/latest/man/cp.html>`_
* `date <https://galaxie-shell.readthedocs.io/en/latest/man/date.html>`_
* `df <https://galaxie-shell.readthedocs.io/en/latest/man/df.html>`_
* `dirname <https://galaxie-shell.readthedocs.io/en/latest/man/dirname.html>`_
* `du <https://galaxie-shell.readthedocs.io/en/latest/man/du.html>`_
* `echo <https://galaxie-shell.readthedocs.io/en/latest/man/echo.html>`_
* `env <https://galaxie-shell.readthedocs.io/en/latest/man/env.html>`_
* `exit <https://galaxie-shell.readthedocs.io/en/latest/man/exit.html>`_
* `false <https://galaxie-shell.readthedocs.io/en/latest/man/false.html>`_
* `head <https://galaxie-shell.readthedocs.io/en/latest/man/head.html>`_
* `ls <https://galaxie-shell.readthedocs.io/en/latest/man/ls.html>`_
* `mkdir <https://galaxie-shell.readthedocs.io/en/latest/man/mkdir.html>`_
* `mv <https://galaxie-shell.readthedocs.io/en/latest/man/mv.html>`_
* `pwd <https://galaxie-shell.readthedocs.io/en/latest/man/pwd.html>`_
* `rm <https://galaxie-shell.readthedocs.io/en/latest/man/rm.html>`_
* `rmdir <https://galaxie-shell.readthedocs.io/en/latest/man/rmdir.html>`_
* `sleep <https://galaxie-shell.readthedocs.io/en/latest/man/sleep.html>`_
* `tail <https://galaxie-shell.readthedocs.io/en/latest/man/tail.html>`_
* `tee <https://galaxie-shell.readthedocs.io/en/latest/man/tee.html>`_
* `time <https://galaxie-shell.readthedocs.io/en/latest/man/time.html>`_
* `touch <https://galaxie-shell.readthedocs.io/en/latest/man/touch.html>`_
* `true <https://galaxie-shell.readthedocs.io/en/latest/man/true.html>`_
* `tty <https://galaxie-shell.readthedocs.io/en/latest/man/tty.html>`_
* `umask <https://galaxie-shell.readthedocs.io/en/latest/man/umask.html>`_
* `unalias <https://galaxie-shell.readthedocs.io/en/latest/man/unalias.html>`_
* `uname <https://galaxie-shell.readthedocs.io/en/latest/man/uname.html>`_

## Roadmap
* implement the POSIX utility as describe by the OpenGroup
* Background Task
* Implement reserved POSIX environment variable name (HOME, PS1, etc)
* deal with **env** and **export**
* better one-file binary distribution
* Load setting from a configuration file
* Have no dependency from outside
