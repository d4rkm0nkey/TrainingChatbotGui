from data import Database

class Bot():
    def __init__(self, name=""):
        self.name = name

    def setName(self, name):
        self.name = name

    def load(self, doc):
        self._id = doc["_id"]

    def save(self):
        if(self.name is not None):
            if hasattr(self, "_id"):
                Database.replace(Database.COLLECTIONS.BOT, self.toDict())
            else:
                self._id = Database.insert(Database.COLLECTIONS.BOT, self.toDict())
        else:
            raise Exception("Bot can't be saved without name.")

    def toDict(self):
        dict = {
            "name": self.name
        }
        if hasattr(self, "_id"):
            dict["_id"] = self._id
        return dict

    def delete(self):
        Database.delete_one(Database.COLLECTIONS.BOT, {"_id": self._id})


class Bots():
    _observers = set()
    GENERAL_NAME_TAG = "All"
    BOT_UPDATE = "bot_update"
    __bots__ = []


    @staticmethod
    def attach(observer):
        """
        attach an observer
        the observer will then be notifed by changes
        """
        Bots._observers.add(observer)

    @staticmethod
    def detach(observer):
        """
        detaches an observer
        the observer will no longer receive updates
        """
        Bots._observers.discard(observer)

    @staticmethod
    def _notify():
        """
        method called by child classes to completly update its observers
        """
        for observer in Bots._observers:
            observer.update(Bots.BOT_UPDATE)

    @staticmethod
    def getGeneral():
        if len(Bots.__bots__) < 1:
            Bots.loadBots()
        return Bots.__bots__[0]

    @staticmethod
    def loadBots():
        bots = Database.find(Database.COLLECTIONS.BOT, {})
        Bots.__bots__ = []
        for document in bots:
            bot = Bot(document["name"])
            bot.load(document)
            Bots.__bots__.append(bot)
        
        if not any(bot.name == Bots.GENERAL_NAME_TAG for bot in Bots.__bots__):
            bot = Bot(Bots.GENERAL_NAME_TAG)
            bot.save()
            Bots.__bots__.insert(0, bot)

        Bots._notify()
    
    @staticmethod
    def get(index):
        return Bots.__bots__[index]

    @staticmethod
    def deleteBot(index):
        Bots.__bots__[index].delete()
        del(Bots.__bots__[index])
        Bots._notify()

    @staticmethod
    def createBot(bot):
        newBot = Bot(bot)
        Bots.__bots__.append(newBot)
        newBot.save()
        Bots._notify()
        return newBot

    @staticmethod
    def containsBot(name):
        for bot in Bots.__bots__:
            if bot.name == name:
                return True
        return False

    @staticmethod
    def getIndex(bot):
        return Bots.__bots__.index(bot)