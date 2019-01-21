class StateController:
    
    """ 
    Abstract class of states controllers 
    
    Attributes:
    # graph : Graph
    # nextState : StateController
    """
    
    def __init__(self, graph=None, nextState=None):
        self._graph = graph
        self._nextState = nextState

    