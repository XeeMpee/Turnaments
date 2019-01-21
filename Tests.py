class Tests:
    
    def __init__(self):
        pass

    def run(self):
        from Participant import *
        from Graph import *
        from Views.MainWindow import *
        from termcolor import colored
        print("HelloWorld!\n\n")


        # Tests participant:
        print("Participants tests:\n{}".format(20*'-'))
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
        print()
        # ------------------------------------------------

        # Test Graph:
        print("Graph tests:\n{}" .format(20*"-"))

        print(colored("Creating participants...", "green"), end=" ")
        #:
        participant0 = Participant("Andrzej")
        participant1 = Participant("Adam")
        participant2 = Participant("Jacek")
        participant3 = Participant("Mariusz")
        participant4 = Participant("Piotr")
        participant5 = Participant("Paweł")
        #.
        print(colored("ok", "green"))

        print(colored("Creating graph...", "green"),end=" ")
        #:
        graph = Graph()
        #.
        print(colored("ok", "green"))

        print(colored("Adding participants to graph...", "green"), end=" ")
        #:
        graph.addParticipant(participant0)
        graph.addParticipant(participant1)
        graph.addParticipant(participant2)
        graph.addParticipant(participant3)
        graph.addParticipant(participant4)
        graph.addParticipant(participant5)
        #.
        print(colored("ok", "green"))

        print(colored("Printing the graph out...", "green"))
        #:
        graph.printParticipants()
        #.
        print(colored("ok", "green"))

        print(colored("Deleting participants...", "green"))
        graph.printParticipants()
        graph.deleteParticipant("Andrzej")
        print(colored("ok", "green"))
        graph.deleteParticipant("Piotr")
        print(colored("ok", "green"))
        graph.printParticipants()
        print(colored("Deleting non-existing participants...", "green"))
        try:
            graph.deleteParticipant("Guncel")
        except NoSuchParticipant as e:
            print("No such participant in set.")    
            print(colored("ok", "green"))
        print()
    
        print(colored("Getting participant from graph...", "green"))
        part=graph.getParticipant("Jacek")
        print(part.getName())
        print(colored("ok", "green"))
        part.setName("Bolko")
        graph.printParticipants()
        print(colored("ok", "green"))
        print()

        print(colored("Clearing graph", "green"))
        graph.printParticipants()
        graph.clearGraph()
        print(colored("ok", "green"))
        graph.printParticipants()
        print(colored("ok", "green"))



        graph.addParticipant(Participant("Adam"))
        graph.addParticipant(Participant("Gwiedymin"))
        graph.addParticipant(Participant("Witold"))
        graph.addParticipant(Participant("Kazimierz"))
        graph.addParticipant(Participant("Delfin"))
        graph.addParticipant(Participant("Otto"))
        graph.addParticipant(Participant("Henryk"))
        graph.addParticipant(Participant("Bolko"))
        graph.addParticipant(Participant("Zygmunt"))
        graph.addParticipant(Participant("Boleslav"))
        graph.addParticipant(Participant("Guncel"))
        graph.addParticipant(Participant("Peszko"))
        graph.addParticipant(Participant("Pelka"))
        graph.addParticipant(Participant("Manir"))
        graph.addParticipant(Participant("Strucker"))
        graph.addParticipant(Participant("Miner"))
        graph.printParticipants()
        print(colored("Creating confrontations...", "green"))
        graph.createConfrontations()
        print(colored("ok", "green"))

        # graph.deleteParticipant("Otto")
        # try:
        #     graph.createConfrontations()
        # except InadequateNumberOfParticipants as e:
        #     print("InadequateNumberOfParticipants")
        #     print(colored("ok", "green"))
        #     pass

        print(colored("Getting number of levels", "green"))
        print(graph.levels())
        print(colored("ok", "green"))
        print()


        print(colored("Printing confrontations...", "green"))
        graph.printConfrontations()
        print(colored("ok", "green"))


        print(colored("Printing graph...", "green"))
        graph.printGraph()
        print(colored("ok", "green"))
        
        
        print(colored("Getting confrontation...", "green"))
        confrontation = graph.getConfrontation(0,3)
        confrontation.printConfrontation()
        print(colored("ok", "green"))
        
        
        print(colored("Do confrontation...", "green"))
        confrontation.doConfrontation(ParticipantsEnum.PARTICIPANT1)
        graph.printGraph() 
        print(colored("ok", "green"))

        print(colored("Do confrontation...", "green"))
        graph.getConfrontation(0,0).doConfrontation(ParticipantsEnum.PARTICIPANT2)
        graph.getConfrontation(0,1).doConfrontation(ParticipantsEnum.PARTICIPANT1)
        graph.getConfrontation(1,0).doConfrontation(ParticipantsEnum.PARTICIPANT1)

        try:
            graph.getConfrontation(1,1).doConfrontation(ParticipantsEnum.PARTICIPANT2)
        except UnsetParticipant:
            pass
        graph.printGraph()

        print(colored("ok", "green"))
        # ---------------------------------------------------