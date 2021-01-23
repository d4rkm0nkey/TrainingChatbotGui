from data import Entries
class Adapter():
    def __init__(self, controller, view):
        # setup click listener
        self.view = view
        self.controller = controller
        Entries.attach(view)
        view.update(Entries.UPDATE.ALL)
        view.listWidget.addButton.clicked.connect(controller.newEntry)
        view.listWidget.removeButton.clicked.connect(controller.removeCurrentEntry)
        view.editWidget.saveButton.clicked.connect(self.saveEntry(controller, view))
        view.editWidget.cancelButton.clicked.connect(controller.revertCurrent)
        view.listWidget.resultList.itemClicked.connect(self.setCurrentEntry)
        view.editWidget.nameTextEdit.textEdited.connect(controller.changeCurrentTitle)

    def saveEntry(self, controller, view):
        return lambda: controller.saveCurrentEntry(view.getEntryData())

    def setCurrentEntry(self, listItem):
        entry = self.view.listWidget.convertListitem(listItem)
        self.view.selectEntry(entry)
        self.controller.setEntry(entry)
