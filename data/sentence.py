from data import answer_types
from data.answer_types import AnswerTypes
from data import Emotions
from data import AnswerTypes
from data import Database

class Sentence():
    def __init__(self, text="", type=AnswerTypes.NONE, emotions=None):
        self.type = type
        self.text = text
        if(emotions is not None):
            self.emotions = emotions
        else:
            self.emotions = [1 for x in range(Emotions.getLength())]
        self.data = self.to_dict()

    def setEmotions(self, emotions):
        self.emotions = emotions

    def save(self):
        if(self.text is not None):
            if hasattr(self, "_id"):
                Database.replace(Database.COLLECTIONS.SENTENCE, self.to_dict())
            else:
                self._id = Database.insert(Database.COLLECTIONS.SENTENCE, self.to_dict())
            self.data = self.to_dict()
        else:
            raise Exception("Category can't be saved without name.")
            
    def to_dict(self):
        dict = {
            "text": self.text,
            "type": self.type,
            "emotions": self.emotions
        }

        if hasattr(self, "_id"):
            dict["_id"] = self._id
        return dict

    def load_from_dict(self, dict):
        self.text = dict["text"]
        self.type = dict["type"]
        self.emotions = dict["emotions"]


    def revert(self):
        self.load_from_dict(self.data)

    def setText(self, text):
        self.text = text

    def setType(self, type):
        self.type = type