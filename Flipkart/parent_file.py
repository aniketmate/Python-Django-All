class Base:
    """Parent File"""
    def __str__(self):
        return f"\n{self.__dict__}"

    def __repr__(self):
        return str(self)
        