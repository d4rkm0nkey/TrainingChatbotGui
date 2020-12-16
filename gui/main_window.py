from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QSplitter, QFrame
from PyQt5.QtGui import QPalette, QColor

from gui import TrainingListWidget, EditEntryWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Training Chatbot AI")
        self.setGeometry(100, 100, 600, 400)
        self.UiComponents()
        self.showMaximized()
        self.show()
    
    def UiComponents(self):
        layout = QHBoxLayout()
        splitter = QSplitter(QtCore.Qt.Horizontal)
        splitter.addWidget(TrainingListWidget())
        splitter.addWidget(EditEntryWidget())
        splitter.setStretchFactor(1, 1)
        layout.addWidget(splitter)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

class Color(QFrame):

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)