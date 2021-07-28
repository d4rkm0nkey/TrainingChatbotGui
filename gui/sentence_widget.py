from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QCheckBox, QTreeWidgetItem

class SentenceWidget(QTreeWidgetItem):
    def __init__(self,  *args, **kwargs):
        super(SentenceWidget, self).__init__(*args, **kwargs)
        self.edit = QLineEdit()

        self.neutral = QCheckBox()
        self.happy = QCheckBox()
        self.sad = QCheckBox()
        self.angry = QCheckBox()

    def addTo(self, tree):
        tree.addTopLevelItem(self)
        tree.setItemWidget(self, 0, self.edit)
        tree.setItemWidget(self, 1, self.neutral)
        tree.setItemWidget(self, 2, self.happy)
        tree.setItemWidget(self, 3, self.sad)
        tree.setItemWidget(self, 4, self.angry)

    def setEmotions(self, emos):
        self.neutral.setChecked(emos[0])
        self.happy.setChecked(emos[1])
        self.sad.setChecked(emos[2])
        self.angry.setChecked(emos[3])

    def getEmotions(self):
        return [
            self.neutral.isChecked(),
            self.happy.isChecked(),
            self.sad.isChecked(),
            self.angry.isChecked()
        ]

    def setText(self, text):
        self.edit.setText(text)

    def getText(self):
        return self.edit.text()

    def onDataChanged(self, listener):
        self.edit.editingFinished.connect(listener)
        self.neutral.stateChanged.connect(listener)
        self.happy.stateChanged.connect(listener)
        self.sad.stateChanged.connect(listener)
        self.angry.stateChanged.connect(listener)

