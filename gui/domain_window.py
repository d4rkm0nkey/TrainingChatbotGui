from PyQt5.QtWidgets import QTextEdit, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QApplication
from PyQt5 import QtCore
from data import Domains

class DomainEditor(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QVBoxLayout()
        self.setStyleSheet("background-color: rgb(2,4,40); color: rgb(54,197,254); QTextEditor {background-color: rgb(54,197,254)}")
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setWindowTitle("Domain Editor")
        self.nameEdit = QTextEdit()
        self.list = QListWidget()
        self.addButton = QPushButton("+")
        self.removeButton = QPushButton("-")

        buttons = QWidget()
        buttLayout = QHBoxLayout()
        buttons.setLayout(buttLayout)
        buttLayout.addWidget(self.addButton)
        buttLayout.addWidget(self.removeButton)
        layout.addWidget(self.list)
        layout.addWidget(self.nameEdit)
        self.list.itemClicked.connect(self.itemActivated_event)

        self.nameEdit.setMaximumHeight(30)
        self.currentDomain = "none"

        layout.addWidget(buttons)
        self.setLayout(layout)
        self.center()

    def showDomains(self):
        self.list.clear()
        for domain in Domains.getDomains():
            self.list.addItem(domain)

    def getName(self):
        return self.nameEdit.toPlainText()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def itemActivated_event(self, item):
        self.currentDomain = item.text()

    def getDomain(self):
        return self.currentDomain