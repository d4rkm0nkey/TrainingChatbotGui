from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QFrame, QLineEdit, QVBoxLayout, QListWidget, QCompleter, QPushButton


class TrainingListWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(TrainingListWidget, self).__init__(*args, **kwargs)
        layout = QVBoxLayout()
        self.setLayout(layout)

        names = ["Hallo", "Tschau", "Ich liebe dich", "Hi"]
        completer = QCompleter(names)
        searchBar = QLineEdit()
        searchBar.setCompleter(completer)
        resultList = QListWidget()
        addButton = QPushButton("+", self)
        addButton.setToolTip('Add a new training entry')
        layout.addWidget(searchBar)
        layout.addWidget(resultList)
        layout.addWidget(addButton)
