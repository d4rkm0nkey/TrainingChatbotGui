class Observable:
    """
    abstract class for classes which instances can be observed by observers
    """
    def __init__(self):
        self._observers = set()

    def attach(self, observer):
        """
        attach an observer
        the observer will then be notifed by changes
        """
        self._observers.add(observer)

    def detach(self, observer):
        """
        detaches an observer
        the observer will no longer receive updates
        """
        self._observers.discard(observer)

    def _notify(self):
        """
        method called by child classes to completly update its observers
        """
        for observer in self._observers:
            observer.update(self)

    def _notify_attribute_changed(self, attribute_name):
        """
        method called by child classes to update single attribute in observers
        """
        value = getattr(self, attribute_name)
        for observer in self._observers:
            observer.update_attribute(attribute_name, value)
