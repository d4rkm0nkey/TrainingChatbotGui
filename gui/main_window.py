from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QSplitter, QFrame
from PyQt5.QtGui import QPalette, QColor

from util import Observer
from gui import TrainingListWidget, EditEntryWidget
from data import Entries, Category

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
        self.setStyleSheet("background-color: rgb(2,4,40)")
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.showMaximized()
        self.show()

    def displayEntries(self, entries, current):
        self.listWidget.display(entries, current, self.editEntry)

    def editEntry(self, entry):
        self.editWidget.show(entry)

    def update(self, type):
        if(type == Entries.UPDATE.ALL):
            self.displayEntries(Entries.entries, Entries.currentEntry)
        elif(type == Entries.UPDATE.CURRENT):
            self.editEntry(Entries.currentEntry)
        elif(type == Entries.UPDATE.SAVED):
            self.editWidget.setStatusSaved(Entries.currentEntry.isSaved)
            self.displayEntries(Entries.entries, Entries.currentEntry)
        else:
            print("Unknown update type")

    def update_attribute(self, attribute_name, attribute_value):
        if(attribute_name == "currentEntry"):
            self.editWidget.show(attribute_value)
        elif(attribute_name == "entryIsSaved"):
            self.editWidget.setStatusSaved(attribute_value)

    def getEntryData(self):
        data = Category()
        data.name = self.editWidget.getName()
        return data