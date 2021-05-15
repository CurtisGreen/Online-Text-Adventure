from Stats import Stats

class Enemy:
    def __init__(self, sessionKey = None):
        self.stats = Stats(sessionKey)