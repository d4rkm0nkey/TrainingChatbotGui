from data import Database, sentence
from data import Sentence
from data import Bots

class Category():
    def __init__(self, bot, data=None):
        if bot is not None:
            self.bot = bot._id
        self.sentences = []
        self.sentence_ids = []
        self.patterns = []
        self.data = data
        self.isSaved = False
        self.name = ""
        self.domain = "none"
        if(data is not None):
            self.isSaved = True
            self.__load__data__(data)

    def __load__data__(self, data):
        if(isinstance(data, Category)):
            if hasattr(data, "_id"):
                self._id = data._id
            self.name = data.name
            if hasattr(data, "domain"):
                self.domain = data.domain
            self.patterns = data.patterns
            self.sentences = data.sentences
            self.sentence_ids = data.sentence_ids
        else:
            self._id = data["_id"]
            self.name = data["name"]

            self.domain = data.get("domain")
            if self.domain is None: self.domain = "none"
            patterns = data.get("patterns")
            if patterns is None: patterns = []
            for pat in patterns:
                self.patterns.append(pat)
            self.sentence_ids = data.get("sentences")
            self.sentences = []
            if self.sentence_ids is None:
                self.sentence_ids = []
            for id in self.sentence_ids:
                data = Database.find_one(Database.COLLECTIONS.SENTENCE, {"_id": id})
                s = Sentence()
                s.load_from_dict(data)
                self.sentences.append(s)
             
    def addPattern(self, pattern):
        if len(pattern) > 0:
            self.patterns.append(pattern)

    def removePattern(self, id):
        if id > 0 and id < self.patterns.length:
            del self.patterns[id]

    def setName(self, name):
        self.isSaved = False
        self.name = name

    def setDomain(self, domain):
        self.domain = domain

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
            self.sentence_ids = []
            for s in self.sentences:
                s.save()
                self.sentence_ids.append(s._id)
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
            "name": self.name,
            "bot": self.bot,
            "domain": self.domain,
            "patterns": self.patterns,
            "sentences": self.sentence_ids
        }
        if hasattr(self, "_id"):
            dict["_id"] = self._id
        return dict
