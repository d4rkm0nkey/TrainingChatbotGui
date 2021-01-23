import abc
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFrame, QLineEdit, QVBoxLayout, QPushButton, QLabel, QListWidget, QListWidgetItem

class EditEntryWidget(QWidget):
    def __init__(self, *args, **kwargs):
        __metaclass__ = abc.ABCMeta
        super(EditEntryWidget, self).__init__(*args, **kwargs)
        layout = QVBoxLayout()
        self.setStyleSheet("color: rgb(54,197,254)")
        nameWidget = QWidget()
        nameLayout = QVBoxLayout()
        nameLabel = QLabel("Entry Name")
        self.nameTextEdit = QLineEdit()
        self.nameTextEdit.setStyleSheet("background-color: rgb(54,197,254); color: rgb(2,4,40)")
        nameLayout.addWidget(nameLabel)
        nameLayout.addWidget(self.nameTextEdit)
        nameWidget.setLayout(nameLayout)

        layout.addWidget(nameWidget)
        # TODO split into seperate methods
        # Keyword list
        keywordWidget = QWidget()
        keywordLayout = QVBoxLayout()
        keywordHeaderWidget = QWidget()
        keywordHeaderLayout = QHBoxLayout()

        keywordLabel = QLabel("Keywords")
        keywordList = QListWidget()
        keywordList.setStyleSheet("background-color: rgb(54,197,254); color: rgb(2,4,40)")
        #testButton = QListWidgetItem("Test")
        #keywordList.addItem(testButton)
        self.addKeywordButton = QPushButton("+")
        self.removeKeywordButton = QPushButton("-")

        keywordHeaderLayout.addWidget(keywordLabel)
        keywordHeaderLayout.addStretch(1)
        keywordHeaderLayout.addWidget(self.addKeywordButton)
        keywordHeaderLayout.addWidget(self.removeKeywordButton)

        keywordHeaderWidget.setLayout(keywordHeaderLayout)
        keywordLayout.addWidget(keywordHeaderWidget)
        keywordLayout.addWidget(keywordList)
        keywordWidget.setLayout(keywordLayout)

        layout.addWidget(keywordWidget)

        # answer list
        answerWidget = QWidget()
        answerLayout = QVBoxLayout()
        answerLabel = QLabel("Answers")
        answerList = QListWidget()

        answerHeaderWidget = QWidget()
        answerHeaderLayout = QHBoxLayout()
        answerHeaderLayout.addWidget(answerLabel)
        answerHeaderLayout.addStretch(1)

        self.addKeywordButton = QPushButton("+")
        self.removeKeywordButton = QPushButton("-")

        answerHeaderLayout.addWidget(self.addKeywordButton)
        answerHeaderLayout.addWidget(self.removeKeywordButton)

        answerHeaderWidget.setLayout(answerHeaderLayout)

        answerLayout.addWidget(answerHeaderWidget)
        answerLayout.addWidget(answerList)
        answerWidget.setLayout(answerLayout)
        answerList.setStyleSheet("background-color: rgb(54,197,254)")

        layout.addWidget(answerWidget)

        # Buttons
        buttonBar = QWidget()
        buttonLayout = QHBoxLayout()
        self.saveButton = QPushButton("save")
        self.saveButton.setStyleSheet("color: rgb(54,197,254)")
        self.cancelButton = QPushButton("cancel")

        buttonLayout.addWidget(self.saveButton)
        buttonLayout.addWidget(self.cancelButton)
        buttonBar.setLayout(buttonLayout)
        layout.addWidget(buttonBar)

        self.setLayout(layout)
    
    def show(self, entry):
        self.item = entry
        self.nameTextEdit.setText(entry.name)

    def setStatusSaved(self, status):
        if(status == True):
            self.saveButton.setStyleSheet("color: rgb(54,197,254)")
        else:
            self.saveButton.setStyleSheet("color: rgb(150,254,150)")

    def getName(self):
        return self.nameTextEdit.text()