import abc
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QLineEdit,QSpacerItem, QListWidgetItem, QHBoxLayout, QVBoxLayout, QFrame, QLineEdit, QComboBox, QVBoxLayout, QPushButton, QLabel, QListWidget, QListWidgetItem, QTreeWidget
from data import Domains
from gui import DomainEditor, SentenceWidget
from data import Entries

class EditEntryWidget(QWidget):
    def __init__(self, *args, **kwargs):
        __metaclass__ = abc.ABCMeta
        super(EditEntryWidget, self).__init__(*args, **kwargs)
        self.currentPattern = None
        layout = QVBoxLayout()
        self.setStyleSheet("color: rgb(54,197,254)")
        nameWidget = QWidget()
        nameLayout = QVBoxLayout()
        nameLabel = QLabel("Entry Name")
        self.nameTextEdit = QLineEdit()
        self.nameTextEdit.setStyleSheet("background-color: rgb(54,197,254); color: rgb(2,4,40)")
        self.domainDialog = DomainEditor()
        domainW = QWidget()
        domainLayout = QHBoxLayout()
    
        self.domainSelector = QComboBox(self)
        self.domainSelector.addItem('none')
        self.domains = QPushButton("Edit Domains")

        domainLayout.addWidget(self.domainSelector)
        domainLayout.addWidget(self.domains)
        domainW.setLayout(domainLayout)

        nameLayout.addWidget(nameLabel)
        nameLayout.addWidget(self.nameTextEdit)
        nameLayout.addWidget(QLabel("Domain"))
        nameLayout.addWidget(domainW)
        nameWidget.setLayout(nameLayout)

        layout.addWidget(nameWidget)
        # TODO split into seperate methods
        # Keyword list
        keywordWidget = QWidget()
        keywordLayout = QVBoxLayout()
        keywordHeaderWidget = QWidget()
        keywordHeaderLayout = QHBoxLayout()

        keywordLabel = QLabel("Keywords")
        self.keywordList = QListWidget()
        self.keywordList.setStyleSheet("background-color: rgb(54,197,254); color: rgb(2,4,40)")
        #testButton = QListWidgetItem("Test")
        #keywordList.addItem(testButton)
        self.addKeywordButton = QPushButton("+")
        self.removeKeywordButton = QPushButton("-")
        self.keywordList.itemClicked.connect(self.pattern_selected)
        self.addKeywordButton.clicked.connect(self.addPatternEvent)
        self.removeKeywordButton.clicked.connect(self.removePattern)

        keywordHeaderLayout.addWidget(keywordLabel)
        keywordHeaderLayout.addStretch(1)
        keywordHeaderLayout.addWidget(self.addKeywordButton)
        keywordHeaderLayout.addWidget(self.removeKeywordButton)

        keywordHeaderWidget.setLayout(keywordHeaderLayout)
        keywordLayout.addWidget(keywordHeaderWidget)
        keywordLayout.addWidget(self.keywordList)
        keywordWidget.setLayout(keywordLayout)

        layout.addWidget(keywordWidget)

        # answer list
        answerWidget = QWidget()
        answerLayout = QVBoxLayout()
        answerLabel = QLabel("Answers")
        self.answerList = QTreeWidget()
        self.answerList.setHeaderLabels(['Answer', "Neutral", "Happy", "Sad", "Angry"])

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
        answerLayout.addWidget(self.answerList)
        answerWidget.setLayout(answerLayout)
        self.answerList.setStyleSheet("background-color: rgb(54,197,254)")
        self.answerList.header().setStyleSheet("color:rgb(2,4,40)")

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
        idx = self.domainSelector.findText(entry.domain)
        if idx < 0: idx = 0
        self.domainSelector.setCurrentIndex(idx)

        self.keywordList.clear()
        for pattern in entry.patterns:
            self.addPattern(pattern)


    def setStatusSaved(self, status):
        if(status == True):
            self.saveButton.setStyleSheet("color: rgb(54,197,254)")
        else:
            self.saveButton.setStyleSheet("color: rgb(150,254,150)")

    def getName(self):
        return self.nameTextEdit.text()

    def getDomain(self):
        return self.domainSelector.currentText()

    def openDomainEdit(self):
        self.domainDialog.show()

    def updateDomainSelection(self):
        self.domainSelector.clear()
        self.domainSelector.addItem('none')
        domains = Domains.getDomains()
        for domain in domains:
            self.domainSelector.addItem(domain)

    def addPattern(self, str=""):
        w = QWidget()
        l = QHBoxLayout()
        l.addWidget(QLabel("▹"))
        edit = QLineEdit(str)
        edit.textEdited.connect(lambda : Entries.setCurrentUnsaved())
        l.addWidget(edit)
        l.addStretch()
        w.setLayout(l)
        item = QListWidgetItem()
        item.setSizeHint(l.sizeHint())
        self.keywordList.addItem(item)
        self.keywordList.setItemWidget(item, w)

    def addPatternEvent(self):
        self.addPattern()

    def removePattern(self):
        if self.currentPattern != None:
            self.keywordList.takeItem(self.keywordList.currentRow())

    def pattern_selected(self, item):
        self.currentPattern = item

    def addAnswer(self):
        a = SentenceWidget()
        a.addTo(self.answerList)