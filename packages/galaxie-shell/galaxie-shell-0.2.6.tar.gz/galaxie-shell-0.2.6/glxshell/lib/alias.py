class GLXAlias:
    def __init__(self):
        self.__alias = None
        self.alias = None

    @property
    def alias(self):
        """
        Return the alias property value
        """
        return self.__alias

    @alias.setter
    def alias(self, value):
        """
        Set the alias property value

        :param value: the property value
        :type value: dict or None
        :raise TypeError: when the property value is not a dict type or None
        """
        if value is None:
            value = {}
        if value and not isinstance(value, dict):
            raise TypeError("'alias' property value must be a dict type or None")
        if self.alias != value:
            self.__alias = value
