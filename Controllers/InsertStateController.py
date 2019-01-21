from Controllers.StateController import *
from Participant import *
from Exceptions import NoSuchParticipant
from Graph import *

class InsertStateController(StateController):

    """
    InsertStateController controlls "Inserting Participants States"

    Attributes:
    # inherited
    # participants : Participants [ ] 
    
    Methods:
    + addParticipant(Participant participant) : void
    + deleteParticipant(string name) : void
    + getParticipant(string name) : Participant
    + isParticipant(string name) : bool 
    + modifyParticipant(str name1, str name2) : void
    + createGraph() : void
    """

    def __init__(self, graph=None, nextState=None):
        super(InsertStateController, self).__init__(graph, nextState)
        self._participants = list()

    
    def addParticipant(self, participant):
        
        if(isinstance(participant,Participant)):
           self._participants.append(participant)
        elif(isinstance(participant,str)):
            newParticipant = Participant(participant)
            self._participants.append(newParticipant)
        else:
            raise ValueError
    

   
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
    
    
    def isParticipant(self, name) -> bool:
        if(not isinstance(name,str)):
            raise ValueError
        
        try:
            self.getParticipant(name)
        except NoSuchParticipant:
            return False
        
        return True
    
    
    def modifyParticipant(self, name1, name2):
        for i in self._participants:
            if i.getName() == name1:
                i.setName(name2)
        
    
    def createGraph(self):
        if(self._graph == None):
            self._graph = Graph()

        self._graph.setParticipants(self._participants)
        self._graph.createConfrontations()  
        pass