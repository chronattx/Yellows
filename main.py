import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPoint
import random


class YelCir(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.clc)
        self.f = 0

    def clc(self):
        self.f = 1
        self.update()

    def paintEvent(self, a0):
        if self.f == 1:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(220, 220, 0))
            r = random.randint(10, 50)
            qp.drawEllipse(QPoint(65, 120), r, r)
            qp.drawEllipse(QPoint(265, 165), r, r)
            qp.drawEllipse(QPoint(155, 210), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YelCir()
    ex.show()
    sys.exit(app.exec())