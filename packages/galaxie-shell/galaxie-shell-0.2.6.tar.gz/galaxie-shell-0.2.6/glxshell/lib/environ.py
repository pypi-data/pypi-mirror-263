# https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_12
class EINVAL(Exception):
    pass


class ENOMEM(Exception):
    pass


class GLXEnviron:
    def __init__(self):
        self.__environ = None
        self.environ = {}

    @property
    def environ(self) -> dict:
        """
        Return the environ property value
        """
        return self.__environ

    @environ.setter
    def environ(self, value):
        """
        Set the environ property value

        :param value: the property value
        :type value: dict or None
        :raise TypeError: when the property value is not a dict type or None
        """
        if value is None:
            value = {}
        if not isinstance(value, dict):
            raise TypeError("'environ' property value must be a dict type or None")
        if self.environ != value:
            self.__environ = value

    # https://pubs.opengroup.org/onlinepubs/9699919799/functions/getenv.html
    # The Open Group Base Specifications Issue 7, 2018 edition
    # IEEE Std 1003.1-2017 (Revision of IEEE Std 1003.1-2008)
    # Copyright © 2001-2018 IEEE and The Open Group
    def getenv(self, name=None):
        """
        getenv - get value of an environment variable

        The ``getenv()`` function shall search the environment of the calling process for
        the environment variable ``name`` if it exists and return the value of the environment variable. If
        the specified environment variable cannot be found, ``None`` shall be returned.

        :param name: the key name
        :type name: str
        """
        if name and not isinstance(name, str):
            raise TypeError("'name' parameter must be a str or None")
        return self.environ.get(name, None)

    # https://pubs.opengroup.org/onlinepubs/9699919799/functions/setenv.htm
    # The Open Group Base Specifications Issue 7, 2018 edition
    # IEEE Std 1003.1-2017 (Revision of IEEE Std 1003.1-2008)
    # Copyright © 2001-2018 IEEE and The Open Group
    def setenv(self, envname=None, envval=None, overwrite=None):
        """
        setenv - add or change environment variable

        The setenv() function shall update or add a variable in the environment of the calling process. The envname
        argument points to a string containing the name of an environment variable to be added or altered. The
        environment variable shall be set to the value to which envval points. The function shall fail if envname
        points to a string which contains an '=' character. If the environment variable named by envname already
        exists and the value of overwrite is non-zero, the function shall return success and the environment shall be
        updated. If the environment variable named by envname already exists and the value of overwrite is zero,
        the function shall return success and the environment shall remain unchanged.

        :param envname: the key name
        :type envname: str
        :param envval: the value of the key
        :type envval: str
        :param overwrite: non-zero
        :type overwrite: int
        :raise EINVAL: when envname argument points to an empty string or points to a string containing an '=' character
        :raise ENOMEM: when Insufficient memory was available to add a variable or its value to the environment.
        :raise TypeError: when he name argument value is not a str type or None
        :return: 0 if success, otherwise -1
        :rtype: int
        """
        if not isinstance(envname, str):
            raise TypeError("'name' parameter must be a str")
        if not isinstance(envval, str):
            raise TypeError("'value' parameter must be a str")
        if envname == "" or "=" in envname:
            raise EINVAL()
        if envname in self.environ and overwrite == 0:
            return 0
        if envname in self.environ and overwrite != 0 or envname not in self.environ:
            try:
                self.environ[envname] = envval
                return 0
            except MemoryError as exc:
                raise ENOMEM() from exc

        return -1

    # https://pubs.opengroup.org/onlinepubs/9699919799/functions/unsetenv.html
    # The Open Group Base Specifications Issue 7, 2018 edition
    # IEEE Std 1003.1-2017 (Revision of IEEE Std 1003.1-2008)
    # Copyright © 2001-2018 IEEE and The Open Group
    def unsetenv(self, name):
        """
        unsetenv - remove an environment variable

        The unsetenv() function shall remove an environment variable from the environment of the calling process. The
        name argument points to a string, which is the name of the variable to be removed. The named argument shall
        not contain an '=' character. If the named variable does not exist in the current environment,
        the environment shall be unchanged and the function is considered to have completed successfully.

        :param name: the name of the variable to be removed
        :type name: str
        :raise EINVAL: when he name argument value is an empty string, or a string containing an '=' character.
        :raise TypeError: when he name argument value is not a str type or None
        :return: 0 if success, otherwise -1
        :rtype: int
        """
        if not isinstance(name, str):
            raise TypeError("'name' parameter value must be a str type")
        if name == "" or "=" in name:
            raise EINVAL()
        if name not in self.environ:
            return 0

        try:
            del self.environ[name]
            return 0
        except KeyError:
            return -1
