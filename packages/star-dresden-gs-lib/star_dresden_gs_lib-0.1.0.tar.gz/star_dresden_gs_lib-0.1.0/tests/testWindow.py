import sys
from random import random

from PyQt6.uic.properties import QtWidgets

from star_dresden_gs_lib.components.getter import GetterWidget


class MainWindow(QtWidgets.QMainWindow):
    count = 0

    def __init__(self, parent=None):
        super().__init__(parent)
        self.echotext_widget2 = None
        self.echotext_widget = None
        self.layout = None
        self.window = None
        self.init_gui()
        self.count = 0

    def init_gui(self):
        self.window = QtWidgets.QWidget()
        self.layout = QtWidgets.QGridLayout()
        self.setCentralWidget(self.window)
        self.window.setLayout(self.layout)

        self.echotext_widget = GetterWidget("alpha", self.add1, button_pos=(5, 7), text_pos=(9,9))
        self.echotext_widget2 = GetterWidget("beta", self.rand_num)

        self.layout.addWidget(self.echotext_widget, 0, 0)
        self.layout.addWidget(self.echotext_widget2, 1, 1)

    def add1(self):
        self.count += 1
        return self.count

    def rand_num(self):
        return random.randint(0, 200)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    win = MainWindow()
    win.show()

    sys.exit(app.exec())