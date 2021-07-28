import enum
from data import Database
from data import Category

class Entries():
    _observers = set()
    entries = []
    unsaved_entries = []
    currentEntry = None

    class UPDATE(enum.Enum):
        ALL = "all"
        CURRENT = "current"
        SAVED = "saved"

    @staticmethod
    def attach(observer):
        """
        attach an observer
        the observer will then be notifed by changes
        """
        Entries._observers.add(observer)

    @staticmethod
    def detach(observer):
        """
        detaches an observer
        the observer will no longer receive updates
        """
        Entries._observers.discard(observer)

    @staticmethod
    def _notify(type):
        """
        method called by child classes to completly update its observers
        """
        for observer in Entries._observers:
            observer.update(type)
    
    @staticmethod
    def loadEntries(bot):
        Entries.entries = []
        if hasattr(bot, "_id"):
            categories = Database.find(Database.COLLECTIONS.CATEGORY, {"bot": bot._id})
            for data in categories:
                c = Category(bot, data)
                Entries.entries.append(c)
        
        if(len(Entries.entries) > 0):
            Entries.currentEntry = Entries.entries[0]
        else:
            Entries.currentEntry = Entries.newEntry(bot)
        Entries._notify(Entries.UPDATE.ALL)
        
    @staticmethod
    def newEntry(bot):
        entry = Category(bot)
        Entries.entries.append(entry)
        Entries.unsaved_entries.append(entry)
        Entries.currentEntry = entry
        Entries._notify(Entries.UPDATE.ALL)
        return entry

    # @staticmethod
    # def addEntry(entry):
    #     entries.append(entry)
    #     unsaved_entries.append(entry)
    #     Entries._notify(UPDATE.ALL)

    @staticmethod
    def saveEntries():
        for entry in Entries.unsaved_entries:
            entry.save()
            Entries.unsaved_entries.remove(entry)
        Entries._notify(Entries.UPDATE.SAVED)

    @staticmethod
    def saveEntry(entry):
        if(entry in Entries.unsaved_entries):
            entry.save()
            Entries.unsaved_entries.remove(entry)
            Entries._notify(Entries.UPDATE.SAVED)

    @staticmethod
    def editEntry(entry):
        Entries.unsaved_entries.insert(entry)
        Entries._notify(Entries.UPDATE.SAVED)

    @staticmethod
    def revertEntry(entry):
        if entry in Entries.unsaved_entries:
            entry.revert()
            Entries.unsaved_entries.remove(entry)
            Entries._notify(Entries.UPDATE.ALL)

    @staticmethod
    def setCurrentEntry(entry):
        Entries.currentEntry = entry

    @staticmethod
    def removeEntry(entry):
        pos = Entries.entries.index(entry)
        if(entry in Entries.unsaved_entries):
            Entries.unsaved_entries.remove(entry)
        Entries.entries.remove(entry)
        if hasattr(entry, "_id"):
            Database.delete_one(Database.COLLECTIONS.CATEGORY, {"_id": entry._id})

        if(entry is Entries.currentEntry):
            if((pos-1) < 0):
                if(len(Entries.entries) > 0):
                    Entries.setCurrentEntry(Entries.entries[0])
                else:
                    Entries.newEntry()
            else:
                Entries.setCurrentEntry(Entries.entries[pos-1])
        Entries._notify(Entries.UPDATE.ALL)

    @staticmethod
    def changeCurrentTitle(title):
        Entries.currentEntry.setName(title)
        Entries.unsaved_entries.append(Entries.currentEntry)
        Entries._notify(Entries.UPDATE.ALL)

    @staticmethod
    def deleteEntries(bot):
        Database.delete_many(Database.COLLECTIONS.CATEGORY, {"bot": bot._id})

    @staticmethod
    def setCurrentUnsaved():
        Entries.currentEntry.isSaved = False
        Entries.unsaved_entries.append(Entries.currentEntry)
        Entries._notify(Entries.UPDATE.SAVED)
