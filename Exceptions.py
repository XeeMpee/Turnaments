
class NoSuchParticipant(Exception):
    pass

class InadequateNumberOfParticipants(Exception):
    pass

class OverridingParticipantError(Exception):
    pass

class UnsetNextConfrontation(Exception):
    pass

class UnsetParticipant(Exception):
    def __init__(self, message):
        super(UnsetParticipant, self).__init__(message)

    pass

