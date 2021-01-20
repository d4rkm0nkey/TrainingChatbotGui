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
            self.name = data.name
        else:
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
            Database.insert(Database.COLLECTIONS.CATEGORY, self)
            self.isSaved = True
        else:
            raise Exception("Category can't be saved without name.")

    def revert(self):
        self.isSaved = True
        __load__data__(self.data)
