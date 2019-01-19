class Participant:

    """
    Represenation of participant in grpah.

    Atributes:
    _name

    Methods:
    __init__(name=None)
    getName()
    setName()

    """

    def __init__(self, name=None):
        self.setName(name)

    def getName(self) -> str:
        return self._name

    def setName(self, name) -> None:
         
        if isinstance(name, (str, type(None))):
            self._name = name
        else:
            raise ValueError("Wrong type of participants name: {0} | str expected!" .format(type(name)))




