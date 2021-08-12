from data.entries import Entries
from data.answer_types import AnswerTypes
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QCheckBox, QTreeWidgetItem

class SentenceWidget(QTreeWidgetItem):
    def __init__(self,  sentence, *args, **kwargs):
        super(SentenceWidget, self).__init__(*args, **kwargs)
        self.sentence = sentence
        self.edit = QLineEdit()
        self.edit.setStyleSheet("color: rgb(0,0,0)")
        self.edit.setText(self.sentence.text)
        for type in AnswerTypes.getTypes():
            c = QCheckBox()
            if(self.sentence.type == type):
                c.setChecked = True
            self.__setattr__(type, c)
            c.stateChanged.connect(lambda : self.sentence.setType(type))
            
        self.neutral = QCheckBox()
        self.happy = QCheckBox()
        self.sad = QCheckBox()
        self.angry = QCheckBox()
        self.setEmotions(self.sentence.emotions)
        self.init_listeners()

    def addTo(self, tree):
        tree.addTopLevelItem(self)
        tree.setItemWidget(self, 0, self.edit)
        tree.setItemWidget(self, 1, self.neutral)
        tree.setItemWidget(self, 2, self.happy)
        tree.setItemWidget(self, 3, self.sad)
        tree.setItemWidget(self, 4, self.angry)
        for i, type in enumerate(AnswerTypes.getTypes()):
            tree.setItemWidget(self, 5+i, getattr(self, type))
            if i == 0:
                getattr(self, type).setChecked(True)


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


    def init_listeners(self):
        def changeText(text):
            self.sentence.setText(text)
            Entries.setCurrentUnsaved()

        def changeEmotions():
            self.sentence.setEmotions(self.getEmotions())
            Entries.setCurrentUnsaved()

        self.edit.textEdited.connect(changeText)
        self.neutral.stateChanged.connect(changeEmotions)
        self.happy.stateChanged.connect(changeEmotions)
        self.sad.stateChanged.connect(changeEmotions)
        self.angry.stateChanged.connect(changeEmotions)
