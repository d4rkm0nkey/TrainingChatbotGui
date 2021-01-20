import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtGui
from dotenv import load_dotenv
load_dotenv()

from data import Database
from gui import MainWindow
from logic import MainController, Adapter

Database.initialize()

app = QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon('logo.png'))

w = MainWindow()
c = MainController()
adapter = Adapter(c, w)


w.show()

sys.exit(app.exec_())