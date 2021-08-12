from data.sentence import Sentence
from data import Entries, Bots, Domains
from PyQt5.QtWidgets import QErrorMessage, QInputDialog, QMessageBox
class Adapter():
    def __init__(self, controller, view):
        # setup click listener
        self.view = view
        self.controller = controller
        Entries.attach(view)
        Bots.attach(view)
        Domains.attach(view)
        Domains.load()
        Bots._notify()
        view.update(Entries.UPDATE.ALL)
        Domains._notify()
        view.listWidget.addButton.clicked.connect(controller.newEntry)
        view.listWidget.removeButton.clicked.connect(controller.removeCurrentEntry)
        view.editWidget.saveButton.clicked.connect(self.saveEntry(controller, view))
        view.editWidget.cancelButton.clicked.connect(controller.revertCurrent)
        view.listWidget.resultList.itemClicked.connect(self.setCurrentEntry)
        view.editWidget.nameTextEdit.textEdited.connect(controller.changeCurrentTitle)
        view.listWidget.selectBotBar.currentIndexChanged.connect(controller.changeBot)
        view.listWidget.addBotButton.clicked.connect(self.getBotName)
        view.listWidget.deleteBotButton.clicked.connect(self.deleteBot)
        view.editWidget.domains.clicked.connect(view.editWidget.openDomainEdit)
        view.editWidget.domainDialog.addButton.clicked.connect(self.addDomain)
        view.editWidget.domainDialog.removeButton.clicked.connect(self.removeDomain)
        view.editWidget.addAnswerButton.clicked.connect(self.addAnswer)
        view.editWidget.removeAnswerButton.clicked.connect(self.removeAnswer)
        view.editWidget.domainSelector.currentIndexChanged.connect(self.domainChanged)


    def addDomain(self):
        domain = self.view.editWidget.domainDialog.getName()
        if len(domain) > 0:
            self.controller.saveDomain(domain)

    def removeDomain(self):
        domain = self.view.editWidget.domainDialog.getDomain()
        self.controller.removeDomain(domain)


    def saveEntry(self, controller, view):
        return lambda: controller.saveCurrentEntry(view.getEntryData())

    def setCurrentEntry(self, listItem):
        entry = self.view.listWidget.convertListitem(listItem)
        self.view.selectEntry(entry)
        self.controller.setEntry(entry)

    def deleteBot(self):
        m = QMessageBox(self.view)
        m.setStyleSheet("QWidget {color:rgb(255,255,255)}")
        cont = m.question(self.view, "Delete Bot", "Do you really want to delete the bot? If you delete it all it's data gets deleted as well.", QMessageBox.Yes | QMessageBox.Abort)
        if cont == QMessageBox.Yes:
            self.controller.deleteCurrentBot()

    def getBotName(self):
        name, ok = QInputDialog.getText(self.view, "Botname", "How do you want to call the new bot?")
        if ok and not Bots.containsBot(name) and len(name) > 0:
            index = self.controller.addBot(name)
            self.view.listWidget.selectBotBar.setCurrentIndex(index)
        else:
            error_dialog = QErrorMessage()
            error_dialog.showMessage('Invalid name.')

    def addAnswer(self):
        self.view.editWidget.addAnswer(Sentence(""))
        Entries.setCurrentUnsaved()

    def removeAnswer(self):
        self.view.editWidget.removeCurrentAnswer()
        Entries.setCurrentUnsaved()

    def domainChanged(self):
        Entries.setCurrentUnsaved()