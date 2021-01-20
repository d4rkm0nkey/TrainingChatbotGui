# logic for changing entries
from data import Category
from data import Entries

class MainController():
    def __init__(self):
        super().__init__()
        Entries.loadEntries()

    def setEntry(self, entry):
        Entries.setCurrentEntry(entry)

    def saveCurrentEntry(self, entry):
        Entries.currentEntry.__load__data__(entry)
        Entries.saveEntry(Entries.currentEntry)

    def newEntry(self):
        Entries.newEntry()
