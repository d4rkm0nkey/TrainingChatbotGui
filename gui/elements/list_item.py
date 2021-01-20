from PyQt5.QtWidgets import QListWidgetItem

class ListItem(QListWidgetItem):
    def __init__(self, name):
        super().__init__(name)