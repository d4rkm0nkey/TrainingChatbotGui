from PyQt5.QtWidgets import QListWidgetItem

class OutputItem(QListWidgetItem):
    def __init__(self, *args, **kwargs):
        super(OutputItem, self).__init__(*args, **kwargs)