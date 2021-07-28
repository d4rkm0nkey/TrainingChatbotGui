import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtGui
from dotenv import load_dotenv
load_dotenv()

from data import Database
from gui import MainWindow
from logic import MainController, Adapter

def main():
    try:
        Database.initialize()
    except Exception as e:
        print(e)
        return

    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('logo.png'))

    c = MainController()
    w = MainWindow()
    adapter = Adapter(c, w)


    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()