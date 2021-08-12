from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QSplitter, QFrame
from PyQt5.QtGui import QPalette, QColor

from util import Observer
from gui import TrainingListWidget, EditEntryWidget
from data import Entries, Category, Bots

class MetaMainWindow(type(QMainWindow), type(Observer)):
    pass

class MainWindow(QMainWindow, Observer, metaclass=MetaMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Training Chatbot AI")
        self.setGeometry(100, 100, 600, 400)

        layout = QHBoxLayout()
        splitter = QSplitter(QtCore.Qt.Horizontal)
        self.listWidget = TrainingListWidget()
        self.editWidget = EditEntryWidget()
        splitter.addWidget(self.listWidget)
        splitter.addWidget(self.editWidget)
        splitter.setStretchFactor(1, 1)
        layout.addWidget(splitter)
        self.setStyleSheet("background-color: rgb(2,4,40); color:rgb(54,197,254)")
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.showMaximized()
        self.show()

    def displayEntries(self, entries, current):
        self.listWidget.display(entries, current)

    def selectEntry(self, entry):
        # self.listWidget.selectEntry(entry)
        self.editEntry(entry)

    def editEntry(self, entry):
        self.editWidget.show(entry)

    def update(self, type):
        if(type == Entries.UPDATE.ALL):
            self.displayEntries(Entries.entries, Entries.currentEntry)
            self.editEntry(Entries.currentEntry)
            self.editWidget.setStatusSaved(Entries.currentEntry.isSaved)
        elif(type == Entries.UPDATE.CURRENT):
            self.editEntry(Entries.currentEntry)
        elif(type == Entries.UPDATE.SAVED):
            self.editWidget.setStatusSaved(Entries.currentEntry.isSaved)
            self.displayEntries(Entries.entries, Entries.currentEntry)
        elif(type == Bots.BOT_UPDATE):
            self.listWidget.updateBots(Bots.__bots__)
        else:
            print("Unknown update type")

    def update_attribute(self, attribute_name, attribute_value):
        if(attribute_name == "currentEntry"):
            self.editWidget.show(attribute_value)
        elif(attribute_name == "entryIsSaved"):
            self.editWidget.setStatusSaved(attribute_value)

    def getEntryData(self):
        data = Category(None)
        data.name = self.editWidget.getName()
        data.domain = self.editWidget.getDomain()
        data.patterns = []
        for i in range(self.editWidget.keywordList.count()):
            item = self.editWidget.keywordList.item(i)
            w = self.editWidget.keywordList.itemWidget(item)
            data.patterns.append(w.layout().itemAt(1).widget().text())
        data.sentences = []
        for i in range(self.editWidget.answerList.topLevelItemCount()):
            data.sentences.append(self.editWidget.answerList.topLevelItem(i).sentence)
        return data

    def updateDomains(self):
        self.editWidget.domainDialog.showDomains()
        self.editWidget.updateDomainSelection()