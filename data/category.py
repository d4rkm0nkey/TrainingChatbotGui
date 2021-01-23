from data import Database
from data import Sentence

class Category():
    def __init__(self, data=None):
        self.sentences = []
        self.data = data
        self.isSaved = False
        self.name = ""
        if(data is not None):
            self.isSaved = True
            self.__load__data__(data)

    def __load__data__(self, data):
        if(isinstance(data, Category)):
            if hasattr(data, "_id"):
                self._id = data._id
            self.name = data.name
        else:
            self._id = data["_id"]
            self.name = data["name"]
             

    def setName(self, name):
        self.isSaved = False
        self.name = name

    def addSentence(self, sentence):
        self.isSaved = False
        if(isinstance(sentence, Sentence)):
            self.sentences.append(sentence)
        else:
            raise TypeError("Object can't be saved, because it is not of type Sentence.")
    
    def getSentence(self, index):
        return self.sentences[index]

    def getSentences(self):
        return self.sentences

    def save(self):
        if(self.name is not None):
            if hasattr(self, "_id"):
                Database.replace(Database.COLLECTIONS.CATEGORY, self.toDict())
            else:
                self._id = Database.insert(Database.COLLECTIONS.CATEGORY, self.toDict())
            self.isSaved = True
            self.data = self.toDict()
        else:
            raise Exception("Category can't be saved without name.")

    def revert(self):
        self.isSaved = True
        self.__load__data__(self.data)

    def toDict(self):
        dict = {
            "name": self.name
        }
        if hasattr(self, "_id"):
            dict["_id"] = self._id
        return dict
