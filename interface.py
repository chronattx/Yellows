from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPoint
import random
import io


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPushButton" name="pushButton">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>10</y>
     <width>381</width>
     <height>20</height>
    </rect>
   </property>
   <property name="text">
    <string>Даёшь жёлтые окружности!</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class YelCir(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        a = io.StringIO(template)
        uic.loadUi(a, self)
        self.pushButton.clicked.connect(self.clc)
        self.f = 0

    def clc(self):
        self.f = 1
        self.update()

    def paintEvent(self, a0):
        if self.f == 1:
            qp = QPainter()
            qp.begin(self)
            qc = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            qp.setPen(QColor(qc))
            r = random.randint(10, 50)
            qp.drawEllipse(QPoint(65, 120), r, r)
            qp.drawEllipse(QPoint(265, 165), r, r)
            qp.drawEllipse(QPoint(155, 210), r, r)