from data import Emotions
class Sentence():
    def __init__(self, text, emotions=None):
        self.text = text
        if(emotions is not None):
            self.emotions = emotions
        else:
            self.emotions = [1 for x in range(Emotions.getLength())]

    def setEmotions(self, emotions):
        self.emotions = emotions
