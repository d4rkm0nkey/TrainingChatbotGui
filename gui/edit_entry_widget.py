from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFrame, QLineEdit, QVBoxLayout, QPushButton, QLabel


class EditEntryWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(EditEntryWidget, self).__init__(*args, **kwargs)
        layout = QVBoxLayout()

        nameWidget = QWidget()
        nameLayout = QHBoxLayout()
        nameLabel = QLabel("Entry Name")
        nameTextEdit = QLineEdit()
        nameLayout.addWidget(nameLabel)
        nameLayout.addWidget(nameTextEdit)
        nameWidget.setLayout(nameLayout)

        layout.addWidget(nameWidget)

        # Keyword list

        # answer list

        self.setLayout(layout)