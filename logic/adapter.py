from data import Entries
class Adapter():
    def __init__(self, controller, view):
        # setup click listener
        Entries.attach(view)
        view. update(Entries.UPDATE.ALL)
        view.listWidget.addButton.clicked.connect(controller.newEntry)
        view.editWidget.saveButton.clicked.connect(self.saveEntry(controller, view))

    def saveEntry(self, controller, view):
        return lambda: controller.saveCurrentEntry(view.getEntryData())
