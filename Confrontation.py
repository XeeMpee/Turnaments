from Participant import *
from enum import Enum
from Exceptions import OverridingParticipantError
from Exceptions import UnsetNextConfrontation
from Exceptions import UnsetParticipant

class ParticipantsEnum(Enum):
    PARTICIPANT1 = 1
    PARTICIPANT2 = 2


class Confrontation:
    """
    Class represents confrontation of two participants
    
    Atributes:
    # _participant1 : Participant
    # _participant2 : Participant
    # _winner : Participant
    # _looser : Participant 
    # _nextConfrontation: Confrontation

    Methods:
    + doConfronatation() : void 
    + assignNextConfrontation() | "Assigns winner confrontation"
    + setParticipant1(Participant p) : void
    + setParticipant2(Participant p) : void
    + doConfrontation(ParticipantEnum pe)
    + getParticipant1() : Participant
    + getParticipant2() : Participant
    + printConfrontation() : void
    """

    def __init__(self):
        self._participant1 = None
        self._participant2 = None
        self._winner = None
        self._looser = None
        self._nextConfrontation = None
        pass

    
    def doConfrontation(self, participante):
        if(not isinstance(participante,ParticipantsEnum)):
            raise ValueError("Parametr participante is {} | must be instance of ParticipanteEnum" .format(participante))
        if(self._nextConfrontation is None):
            raise UnsetNextConfrontation

        if(participante == ParticipantsEnum.PARTICIPANT1):
            if(isinstance(self._participant1, type(None))):
                raise UnsetParticipant("None partcipant cant win!")
            self._winner = self._participant1
            self._looser = self._participant2
        elif(participante == ParticipantsEnum.PARTICIPANT2):
            if(isinstance(self._participant2, type(None))):
                raise UnsetParticipant("None partcipant cant win!")
            self._winner = self._participant2
            self._looser = self._participant1

        try:
            self._nextConfrontation.setParticipant1(self._winner)
        except OverridingParticipantError:
            try:
                self._nextConfrontation.setParticipant2(self._winner)
            except OverridingParticipantError:
                raise OverridingParticipantError
            
        pass

   
    def assignNextConfrontation(self, confrontation):
        """ Assigns winner confrontation """
        
        if(not isinstance(confrontation,(Confrontation,type(None)))):
            raise ValueError("confrontation is {} | must be instance of Confrontation" .format(confrontation))
        
        self._nextConfrontation = confrontation

    
    def setParticipant1(self, participant, force=False):
        if(force == False and self._participant1 != None):
            raise OverridingParticipantError

        if(not isinstance(participant,Participant)):
           raise ValueError("participant is {} | must be Participant!" .format(type(participant)))
        self._participant1 = participant

    
    def setParticipant2(self, participant, force=False):
        if(force == False and self._participant2 != None):
            raise OverridingParticipantError

        if(not isinstance(participant,Participant)):
            raise ValueError("participant is {} | must be Participant!" .format(type(participant)))
        self._participant2 = participant

   
    def getParticipant1(self) -> Participant:
        return self._participant1


    def getParticipant2(self) -> Participant:
        return self._participant2


    def printConfrontation(self):
        print("Confrontation:")
        try:
            print("Participant1: {}".format(self._participant1.getName()))
        except AttributeError:
            print("Participant1: None")
        try:
            print("Participant2: {}" .format(self._participant2.getName()))
        except AttributeError:
            print("Participant2: None")