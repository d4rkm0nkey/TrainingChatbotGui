from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QFrame, QLineEdit, QVBoxLayout, QListWidget, QCompleter, QPushButton
from .elements.list_item import ListItem


class TrainingListWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(TrainingListWidget, self).__init__(*args, **kwargs)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setStyleSheet("background-color: rgb(54,197,254)")
        searchBar = QLineEdit()
        searchBar.setPlaceholderText("Filter...")
        self.resultList = QListWidget() # write own class with entries
        self.addButton = QPushButton("+", self)
        self.addButton.setToolTip('Add a new training entry')
        self.addButton.setStyleSheet("background-color: rgb(54,197,254); color: rgb(2,4,40)")
        layout.addWidget(searchBar)
        layout.addWidget(self.resultList)
        layout.addWidget(self.addButton)

    def display(self, entries, currentEntry, clickListener):
        self.resultList.clear()
        for entry in entries:
            self.resultList.addItem(ListItem(entry.name))
            self.resultList.itemClicked.connect(clickListener)
        self.resultList.setCurrentRow(0)
