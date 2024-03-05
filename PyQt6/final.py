import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys
import os

from PyQt6.QtWidgets import QWidget

class Project(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Flag")
		self.setFixedSize(400, 280)
		self.setStyleSheet("background: grey")

		self.btn1 = QPushButton(self)
		self.btn2 = QPushButton(self)
		self.btn3 = QPushButton(self)
		
		self.btn1.setGeometry(100, 30, 200, 60)
		self.btn2.setGeometry(100, 90, 200, 60)
		self.btn3.setGeometry(100, 150, 200, 60)

		self.btn1.clicked.connect(self.click1)
		self.btn2.clicked.connect(self.click2)
		self.btn3.clicked.connect(self.click3)

	def click1(self):
		color = QColorDialog().getColor()
		if color:
			self.btn1.setStyleSheet(f"background: {color.name()}")

	def click2(self):
		color = QColorDialog().getColor()
		if color:
			self.btn2.setStyleSheet(f"background: {color.name()}")

	def click3(self):
		color = QColorDialog().getColor()
		if color:
			self.btn3.setStyleSheet(f"background: {color.name()}")

app = QApplication(sys.argv)
pr = Project()
pr.show()
sys.exit(app.exec())