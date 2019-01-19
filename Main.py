from Participant import *
print("HelloWorld!")


# Tests participant:
participant = Participant("Andrzej")
print(participant.getName())
participant2 = Participant()
print(participant2.getName())
participant.setName("Adam")
print(participant.getName())
try:
    participant2.setName(12)
except ValueError:
    print("Wrong type - test ok")
# ------------------------------------------------
