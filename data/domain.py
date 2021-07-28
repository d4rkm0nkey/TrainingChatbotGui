from data import Database

class Domains():
    __domains__ = []
    _observers = set()
    __currentDomain__ = "none"

    @staticmethod
    def load():
        domains = Database.find(Database.COLLECTIONS.DOMAIN, {})
        Domains.__domains__ = []
        for document in domains :
            Domains.__domains__ .append(document["name"])
        Domains._notify()

    @staticmethod
    def addDomain(name):
        if not name in Domains.__domains__:
            Domains.__domains__.append(name)
            Domains._notify()
            Domains.save()

    @staticmethod
    def removeDomain(name):
        if name in Domains.__domains__:
            Domains.__domains__.remove(name)
            Domains._notify()
            Domains.save()

    @staticmethod
    def save():
        Database.delete_all(Database.COLLECTIONS.DOMAIN)
        for domain in Domains.__domains__:
            Database.insert(Database.COLLECTIONS.DOMAIN, {"name": domain})

    @staticmethod
    def setCurrentDomain(domain):
        Domains.__currentDomain__ = domain
        Domains._notify()

    @staticmethod
    def getCurrentDomain():
        return Domains.__currentDomain__

    @staticmethod
    def getLength():
        return len(Domains.__domains__)

    @staticmethod
    def attach(observer):
        """
        attach an observer
        the observer will then be notifed by changes
        """
        Domains._observers.add(observer)

    @staticmethod
    def detach(observer):
        """
        detaches an observer
        the observer will no longer receive updates
        """
        Domains._observers.discard(observer)

    @staticmethod
    def _notify():
        """
        method called by child classes to completly update its observers
        """
        for observer in Domains._observers:
            observer.updateDomains()

    @staticmethod
    def getDomains():
        return Domains.__domains__