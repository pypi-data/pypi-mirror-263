
from glxshell.lib.argparse import ArgumentParser


class Command(object):
    def __init__(self):
        self.__parser = None
        self.__exit_status = None
        self.__stdin = None
        self.__stdout = None
        self.__stderr = None

        self.parser = None
        self.exit_status = None
        self.stdin = None
        self.stdout = None
        self.stderr = None

    @property
    def parser(self):
        return self.__parser

    @parser.setter
    def parser(self, value):
        if value is None:
            self.__parser = None
        if not isinstance(value, ArgumentParser):
            raise TypeError("'parser' property value must be a ArgumentParser instance or None")
        if value != self.parser:
            self.__parser = value

    @property
    def exit_status(self):
        return self.__exit_status

    @exit_status.setter
    def exit_status(self, value):
        if value is None:
            self.__exit_status = 0
        if type(value) != int:
            raise TypeError("'exit_status' property value must be a int type or None")
        if value != self.exit_status:
            self.__exit_status = value
