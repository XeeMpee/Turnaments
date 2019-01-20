from Participant import *
from Confrontation import *
from Exceptions import NoSuchParticipant
from Exceptions import InadequateNumberOfParticipants
class Graph:
    """
    Class of "Graph" - turnament structure. 
    
    Atributes:
    # _participants [ ] : Participant  
    # _confrontations [ ] : Confrontation
    # _levels : int | number of graph levels

    Methods:
    + addParticipant(str name) : void 
    + deleteParticipant(str name) : void | raise NoSuchParticipant
    + getParticipant(str name) : Participant

    + createConfrontations() : void
    - static __isPowerOfTwo(int) : bool

    + clearGraph() : void

    + printParticipants() : void        
    + levels() : int    | return number of graph levels
    """

    def __init__(self) :
        self._participants = list()
        self._confrontations = list()
        self._levels = 0
        pass


    def addParticipant(self, participant):
        if not isinstance(participant, Participant):
            raise ValueError("Participant is {0} |  must be Participant!" .format(type(participant)))
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

    
    def createConfrontations(self):
            # Creating only when number of participants is power of two:
            if(not Graph.__isPowerOfTwo(len(self._participants))):
                raise InadequateNumberOfParticipants
            
            # Counting number of graphs levels:
            tmpLevels = len(self._participants)
            count = 0
            while(tmpLevels != 0):
                count += 1
                tmpLevels = (tmpLevels // 2) 
                pass
            self._levels = count
            del tmpLevels
            del count

            # Creating empty confrontations:
            tmpNum = len(self._participants)
            tmpNum = tmpNum // 2
            for i in range(0, self._levels):
                self._confrontations.append(list())
                for j in range(0, tmpNum):
                    self._confrontations[i].append(Confrontation())
                tmpNum = tmpNum // 2

            # Setting confrontations:
            for i in range(0, self._levels-2):
                for j in self._confrontations[i]:
                    index = self._confrontations[i].index(j)
                    indexOfNextLevel = index // 2
                    print("index: {}, nlindex: {}" .format(index, indexOfNextLevel))
                    j.assignNextConfrontation(self._confrontations[i+1][indexOfNextLevel])

            # Setting first level participants:
            index=0; 
            for i in self._confrontations[0]:
                i.setParticipant1(self._participants[index])
                index += 1
                i.setParticipant2(self._participants[index])
                index += 1


    @staticmethod
    def __isPowerOfTwo(number) -> bool:
        sqrt = number ** (1/2)
        if(sqrt == int(sqrt)):
            return True
        else:
            return False


    
    def clearGraph(self):
       del self._confrontations[:] 
       del self._participants[:] 

    
    def printParticipants(self):
        for i in self._participants:
            print(i.getName())

    def printConfrontations(self):
        for i in self._confrontations:
            print("\n---")
            for j in i:
                print("confr", end=" ")
    
    def printGraph(self):
        for i in self._confrontations:
            for j in i:
                con = False
                if(j.getParticipant1() is None):
                    print("None|", end="")
                    con = True
                if(j.getParticipant2() is None):
                    print("None", end="   ")
                    con = True
                if con is True:
                    continue

                print(j.getParticipant1().getName(), end="|")
                print(j.getParticipant2().getName(), end="   ")
            print("\n")
            print(20*'-')
            
        pass
                

    def levels(self) -> int:
        return self._levels

