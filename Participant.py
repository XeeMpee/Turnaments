class Participant:

    """
    Represenation of participant in grpah.

    Atributes:
    #  _name

    Methods:
    + __init__(name=None)
    + getName() : str
    + setName(str name) : void

    Unfortunetly name is treated like a id number. 
    Must be unrepeatable in sets of participants!
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




