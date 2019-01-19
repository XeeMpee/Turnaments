from Participant import *
from enum import Enum
from Exceptions import OverridingParticipantError

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
        
        if(participante == ParticipantsEnum.PARTICIPANT1):
            self._winner = self._participant1
            self._looser = self._participant2
        if(participante == ParticipantsEnum.PARTICIPANT2):
            self._winner = self._participant2
            self._looser = self._participant1

        #TODO: przkazzac winnera do nastepnej konfornatacji
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