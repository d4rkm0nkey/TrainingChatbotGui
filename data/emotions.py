from data import Database

class Emotions():
    __emotions__ = []

    @staticmethod
    def loadEmotions():
        emotions = Database.find(Database.COLLECTIONS.EMOTION, {})
        __emotions__ = []
        for document in emotions:
          __emotions__.append(document["name"])

    @staticmethod
    def getLength():
        return len(__emotions__)