from Participant import *
from Exceptions import NoSuchParticipant
class Graph:
    """
    Class of "Graph" - turnament structure. 
    
    Atributes:
    # _participants [ ] : Participant
    # _confrontations [ ] : Confrontation

    Methods:
    + addParticipant(str name) : void 
    + deleteParticipant(str name) : void | raise NoSuchParticipant
    + getParticipant(str name) : Participant

    + createConfrontations() : void

    + clearGraph() : void

    + printParticipants() : void        
    """

    def __init__(self) :
        self._participants = list()
        self._confrontations = list()
        pass


    def addParticipant(self, participant):
        if not isinstance(participant, Participant):
            raise ValueError("Participant is {0} |  must be Participant!" .format(type(name)))
        else:
            self._participants.append(participant)

    def deleteParticipant(self, name):
        if not isinstance(name, str):
            raise ValueError
        else:
            for i in self._participants:
                if(i.getName() == name):
                    self._participants.remove(i)
                    break
            else:
                raise NoSuchParticipant

    def getParticipant(self, name):
        if not isinstance(name, str):
            raise ValueError
        else:
            for i in self._participants:
                if(i.getName() == name):
                    return i
            else:
                raise NoSuchParticipant

    def clearGraph(self):
       del self._participants[:] 
       del self._confrontations[:] 

    def printParticipants(self):
        for i in self._participants:
            print(i.getName())

