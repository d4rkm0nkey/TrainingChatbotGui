# logic for changing entries
from data import Category, Entries, Emotions, Bots, Domains

class MainController():
    def __init__(self):
        super().__init__()
        Emotions.loadEmotions()
        Bots.loadBots()
        self.__current__bot__ = Bots.getGeneral()
        self.__current__bot__index__ = 0
        Entries.loadEntries(self.__current__bot__)

    def setEntry(self, entry):
        Entries.setCurrentEntry(entry)

    def saveCurrentEntry(self, entry):
        entry.bot = self.__current__bot__
        Entries.currentEntry.__load__data__(entry)
        Entries.saveEntry(Entries.currentEntry)

    def removeCurrentEntry(self):
        Entries.removeEntry(Entries.currentEntry)

    def newEntry(self):
        Entries.newEntry(self.__current__bot__)

    def changeCurrentTitle(self, title):
        Entries.changeCurrentTitle(title)

    def revertCurrent(self):
        Entries.revertEntry(Entries.currentEntry)

    def changeBot(self, botindex):
        self.__current__bot__index__ = botindex
        self.__current__bot__ = Bots.get(botindex)
        Entries.loadEntries(self.__current__bot__)

    def deleteCurrentBot(self):
        Entries.deleteEntries(self.__current__bot__)
        Bots.deleteBot(self.__current__bot__index__)
        self.__current__bot__index__ = 0
        self.__current__bot__ = Bots.getGeneral()

    def addBot(self, name):
        bot = Bots.createBot(name)
        self.__current__bot__ = bot
        self.__current__bot__index__ = Bots.getIndex(bot)
        return self.__current__bot__index__

    def saveDomain(self, domain):
        Domains.addDomain(domain)

    def removeDomain(self, name):
        Domains.removeDomain(name)

    def removeAnswer(self, answer):
        pass