from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys
import os
os.chdir("C:\\Codes\\Py_Codes\\PyQt6")

# class FromDigitToText(QWidget):
# 	def __init__(self):
# 		super().__init__()
# 		self.setStyleSheet("background: lime; color: black")
# 		self.show()
# 		self.setWindowTitle("From Digit to Text")
# 		self.setGeometry(200, 200, 400, 400)
# 		self.hBox = QHBoxLayout()
# 		self.vBox = QVBoxLayout()

# 		self.text = QLineEdit()
# 		self.text.setFixedSize(160, 60)
# 		self.text.setStyleSheet("font-size: 20pt")
# 		self.result = QLabel('')
# 		self.result.setStyleSheet("font-size: 20pt")

# 		self.btn = QPushButton("Convert to Text")
# 		self.btn.setStyleSheet("background: orange")
# 		self.btn.setFixedSize(160, 30)
# 		self.btn.clicked.connect(self.toText)

# 		self.vBox.addStretch()
# 		self.vBox.addWidget(self.result)
# 		self.vBox.addStretch()
# 		self.vBox.addWidget(self.text)
# 		self.vBox.addSpacing(20)
# 		self.vBox.addWidget(self.btn)
# 		self.vBox.addSpacing(20)
# 		self.vBox.addStretch()

# 		self.hBox.addLayout(self.vBox)
# 		self.setLayout(self.hBox)

# 	def toText(self):
# 		first = {
# 			"1":"On",
# 			"2":"Yigirma",
# 			"3":"O'ttiz",
# 			"4":"Qirq",
# 			"5":"Ellik",
# 			"6":"Oltmish",
# 			"7":"Yetmish",
# 			"8":"Sakson",
# 			"9":"To'qson"
# 		}
# 		second = {
# 			"1":"Bir",
# 			"2":"Ikki",
# 			"3":"Uch",
# 			"4":"To'rt",
# 			"5":"Besh",
# 			"6":"Olti",
# 			"7":"Yetti",
# 			"8":"Sakkiz",
# 			"9":"To'qqiz"
# 		}
# 		text = ''
# 		num = list(self.text.text())
# 		if len(num) == 2:
# 			text += first[num[0]]+" "+second[num[-1]]
# 		elif len(num) == 1:
# 			text += second[num[0]]
# 		self.result.setText(text)

# app = QApplication(sys.argv)
# project = FromDigitToText()
# sys.exit(app.exec())