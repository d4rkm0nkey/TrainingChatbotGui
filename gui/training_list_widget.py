from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QFrame, QComboBox, QVBoxLayout, QListWidget, QCompleter, QPushButton, QLabel
from PyQt5.QtGui import QBrush, QColor
from .elements.list_item import ListItem


class TrainingListWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(TrainingListWidget, self).__init__(*args, **kwargs)
        self.entries = []
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setStyleSheet("background-color: rgb(54,197,254); color: rgb(2,4,40)")

        # Select Bot
        selectBot = QWidget()
        selectBotLayout = QHBoxLayout()
        selectBot.setLayout(selectBotLayout)

        self.selectBotBar = QComboBox()
        self.selectBotBar.addItem("General")
        self.selectBotBar.addItem("Gustav")
        self.addBotButton = QPushButton('+')
        self.addBotButton.setFixedWidth(30)
        self.deleteBotButton = QPushButton('x')
        self.deleteBotButton.setFixedWidth(30)

        self.selectBotBar.currentIndexChanged.connect(self.dropDownListener)


        selectBotLayout.addWidget(self.selectBotBar)
        selectBotLayout.addWidget(self.addBotButton)
        selectBotLayout.addWidget(self.deleteBotButton)

        # Category List
        self.resultList = QListWidget() # write own class with entries

        # Add remove Categories
        self.addButton = QPushButton("+", self)
        self.addButton.setToolTip('Add a new training entry')
        self.addButton.setStyleSheet("background-color: rgb(54,197,254); color: rgb(2,4,40)")
        self.removeButton = QPushButton("-", self)
        self.removeButton.setToolTip('Remove current entry')
        self.removeButton.setStyleSheet("background-color: rgb(54,197,254); color: rgb(2,4,40)")
        buttonWidget = QWidget()
        buttonLayout = QHBoxLayout()
    
        buttonLayout.addWidget(self.addButton)
        buttonLayout.addWidget(self.removeButton)
        buttonLayout.setContentsMargins(0, 0, 0, 0)
        buttonWidget.setLayout(buttonLayout)
        buttonWidget.setStyleSheet("background-color: rgb(2,4,40)")

        layout.addWidget(selectBot)
        layout.addWidget(self.resultList)
        layout.addWidget(buttonWidget)

    def display(self, entries, currentEntry):
        self.entries = entries
        self.listItems = []
        self.resultList.clear()
        i=0
        for entry in entries:
            listItem = ListItem(entry.name)
            if(not entry.isSaved):
                brush = QBrush(QColor(255,255,0))
                listItem.setForeground(brush)
            self.listItems.append(listItem)
            self.resultList.addItem(listItem)
        self.selectEntry(currentEntry)

    def selectEntry(self, selectedEntry):
        selectedId = id(selectedEntry)
        i = 0
        for entry in self.entries:
            if(id(entry) == selectedId):
                self.resultList.setCurrentRow(i)
            i += 1

    def convertListitem(self, listItem):
        i = 0
        for item in self.listItems:
            if(item is listItem):
                return self.entries[i]
            i += 1

    def dropDownListener(self, index):
        if index == 0:
            self.deleteBotButton.setEnabled(False)
        else:
            self.deleteBotButton.setEnabled(True)

    def updateBots(self, bots):
        self.selectBotBar.clear()
        for bot in bots:
            self.selectBotBar.addItem(bot.name)