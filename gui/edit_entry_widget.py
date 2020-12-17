from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFrame, QLineEdit, QVBoxLayout, QPushButton, QLabel, QListWidget, QListWidgetItem


class EditEntryWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(EditEntryWidget, self).__init__(*args, **kwargs)
        layout = QVBoxLayout()

        nameWidget = QWidget()
        nameLayout = QVBoxLayout()
        nameLabel = QLabel("Entry Name")
        nameTextEdit = QLineEdit()
        nameLayout.addWidget(nameLabel)
        nameLayout.addWidget(nameTextEdit)
        nameWidget.setLayout(nameLayout)

        layout.addWidget(nameWidget)

        # Keyword list
        keywordWidget = QWidget()
        keywordLayout = QVBoxLayout()
        keywordLabel = QLabel("Keywords")
        keywordList = QListWidget()
        testButton = QListWidgetItem("Test")
        keywordList.addItem(testButton)

        keywordLayout.addWidget(keywordLabel)
        keywordLayout.addWidget(keywordList)
        keywordWidget.setLayout(keywordLayout)

        layout.addWidget(keywordWidget)

        # answer list
        answerWidget = QWidget()
        answerLayout = QVBoxLayout()
        answerLabel = QLabel("Answers")
        answerList = QListWidget()

        answerLayout.addWidget(answerLabel)
        answerLayout.addWidget(answerList)
        answerWidget.setLayout(answerLayout)

        layout.addWidget(answerWidget)

        # Buttons
        buttonBar = QWidget()
        buttonLayout = QHBoxLayout()
        saveButton = QPushButton("save")
        cancelButton = QPushButton("cancel")

        buttonLayout.addWidget(saveButton)
        buttonLayout.addWidget(cancelButton)
        buttonBar.setLayout(buttonLayout)
        layout.addWidget(buttonBar)

        self.setLayout(layout)