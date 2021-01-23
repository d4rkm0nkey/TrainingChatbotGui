# logic for changing entries
from data import Category, Entries, Emotions

class MainController():
    def __init__(self):
        super().__init__()
        Emotions.loadEmotions()
        Entries.loadEntries()

    def setEntry(self, entry):
        Entries.setCurrentEntry(entry)

    def saveCurrentEntry(self, entry):
        Entries.currentEntry.__load__data__(entry)
        Entries.saveEntry(Entries.currentEntry)

    def removeCurrentEntry(self):
        Entries.removeEntry(Entries.currentEntry)

    def newEntry(self):
        Entries.newEntry()

    def changeCurrentTitle(self, title):
        Entries.changeCurrentTitle(title)

    def revertCurrent(self):
        Entries.revertEntry(Entries.currentEntry)