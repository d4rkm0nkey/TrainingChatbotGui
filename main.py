import sys
from PyQt5.QtWidgets import QApplication, QWidget

from gui import MainWindow

app = QApplication(sys.argv)

w = MainWindow()

w.show()

sys.exit(app.exec_())