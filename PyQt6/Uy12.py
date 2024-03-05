import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys

from PyQt6.QtWidgets import QWidget


#1
class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.setFixedSize(380, 360)
		self.setWindowTitle("Survey")
		self.setStyleSheet("background: grey; font-size: 15px")
		self.setWindowIcon(QIcon("C:\\Codes\\Py_Codes\\PyQt6\\survey.ico"))

		w = QWidget()
		self.vBox = QVBoxLayout()

		self.q1 = QLabel("1. 11 x 21 = ...", w)
		self.q1.move(10, 8)
		self.g1 = QButtonGroup(w)
		self.a1 = QRadioButton("211", w)
		self.a1.move(10, 30)
		self.b1 = QRadioButton("221", w)
		self.b1.move(100, 30)
		self.c1 = QRadioButton("231", w)#
		self.c1.move(190, 30)
		self.g1.addButton(self.a1)
		self.g1.addButton(self.b1)
		self.g1.addButton(self.c1)

		self.q2 = QLabel("2. 60 x 30 = ....", w)
		self.q2.move(10, 58)
		self.g2 = QButtonGroup(w)
		self.a2 = QRadioButton("1800", w)#
		self.a2.move(10, 80)
		self.b2 = QRadioButton("1900", w)
		self.b2.move(100, 80)
		self.c2 = QRadioButton("2000", w)
		self.c2.move(190, 80)
		self.g2.addButton(self.a2)
		self.g2.addButton(self.b2)
		self.g2.addButton(self.c2)

		self.q3 = QLabel("3. AG**2 = ....", w)
		self.q3.move(10, 108)
		self.g3 = QButtonGroup(w)
		self.a3 = QRadioButton("AG", w)
		self.a3.move(10, 130)
		self.b3 = QRadioButton("AGAG", w)#
		self.b3.move(100, 130)
		self.c3 = QRadioButton("AG AG", w)
		self.c3.move(190, 130)
		self.g3.addButton(self.a3)
		self.g3.addButton(self.b3)
		self.g3.addButton(self.c3)

		self.q4 = QLabel("4. 11**2 = ...", w)
		self.q4.move(10, 158)
		self.g4 = QButtonGroup(w)
		self.a4 = QRadioButton("111", w)
		self.a4.move(10, 180)
		self.b4 = QRadioButton("121", w)#
		self.b4.move(100, 180)
		self.c4 = QRadioButton("131", w)
		self.c4.move(190, 180)
		self.g4.addButton(self.a4)
		self.g4.addButton(self.b4)
		self.g4.addButton(self.c4)

		self.q5 = QLabel("5. Kali .....", w)
		self.q5.move(10, 208)
		self.g5 = QButtonGroup(w)
		self.a5 = QRadioButton("Ubuntu", w)
		self.a5.move(10, 230)
		self.b5 = QRadioButton("Windows", w)
		self.b5.move(100, 230)
		self.c5 = QRadioButton("Linux", w)#
		self.c5.move(190, 230)
		self.g5.addButton(self.a5)
		self.g5.addButton(self.b5)
		self.g5.addButton(self.c5)

		self.btn = QPushButton("Submit", w)
		self.btn.move(140, 280)
		self.btn.clicked.connect(self.points)

		self.vBox.addWidget(w)
		self.setLayout(self.vBox)

	def points(self):
		pts = 0
		if self.c1.isChecked():
			pts += 1
		if self.a2.isChecked():
			pts += 1
		if self.b3.isChecked():
			pts += 1
		if self.b4.isChecked():
			pts += 1
		if self.c5.isChecked():
			pts += 1
		print(f"Overall: {pts} points")
		app.quit()

app = QApplication(sys.argv)
project = Window()
project.show()
sys.exit(app.exec())



#2
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setFixedSize(620, 600)
#         self.setWindowTitle("Menu")
#         self.setStyleSheet("background: #3FC15B; font-size: 20pt")

#         self.vBox = QVBoxLayout()
#         self.vBox2 = QVBoxLayout()
#         self.hBox = QHBoxLayout()

#         self.lb1 = QLabel("1-Taomlar")
#         self.mastava = QCheckBox("Mastava - 18 000")
#         self.chuchvara = QCheckBox("Chuchvara - 20 000")
#         self.kShorva = QCheckBox("Karam Sho'rva -  18 000")
#         self.lagmon = QCheckBox("Lag'mon - 22 000")
#         self.tShorva = QCheckBox("Tovuq Sho'rva - 24 000")

#         self.lb2 = QLabel("2-Taomlar")
#         self.osh = QCheckBox("Osh - 25 000")
#         self.kabob = QCheckBox("Kabob - 24 000")
#         self.manti = QCheckBox("Manti - 20 000")
#         self.bishteks = QCheckBox("Bishteks - 23 000")
#         self.somsa = QCheckBox("Somsa - 8 000")

#         self.lb3 = QLabel("Ichimliklar")
#         self.tea = QCheckBox("Choy - 7 000")
#         self.fanta = QCheckBox("Fanta - 9 000")
#         self.pepsi = QCheckBox("Pepsi - 9 000")
#         self.sprite = QCheckBox("Sprite - 9 000")
#         self.oSharbat = QCheckBox("O'rik sharbati - 7 000")

#         self.lb4 = QLabel("Desertlar")
#         self.napoleon = QCheckBox("Napoleon - 6 000")
#         self.olivye = QCheckBox("Olivye - 8 000")
#         self.tort = QCheckBox("To'rt - 15 000")
#         self.rulet = QCheckBox("Rulet - 12 000")
#         self.pirog = QCheckBox("Pirog - 10 000")

#         self.submit = QPushButton("Submit")
#         self.submit.setStyleSheet("background: grey")
        
#         self.vBox.addWidget(self.lb1)
#         self.vBox.addWidget(self.mastava)
#         self.vBox.addWidget(self.chuchvara)
#         self.vBox.addWidget(self.kShorva)
#         self.vBox.addWidget(self.lagmon)
#         self.vBox.addWidget(self.tShorva)
#         self.vBox.addWidget(self.lb3)
#         self.vBox.addWidget(self.tea)
#         self.vBox.addWidget(self.fanta)
#         self.vBox.addWidget(self.pepsi)
#         self.vBox.addWidget(self.sprite)
#         self.vBox.addWidget(self.oSharbat)
        
#         self.vBox2.addWidget(self.lb2)
#         self.vBox2.addWidget(self.osh)
#         self.vBox2.addWidget(self.kabob)
#         self.vBox2.addWidget(self.manti)
#         self.vBox2.addWidget(self.bishteks)
#         self.vBox2.addWidget(self.somsa)
#         self.vBox2.addWidget(self.lb4)
#         self.vBox2.addWidget(self.napoleon)
#         self.vBox2.addWidget(self.olivye)
#         self.vBox2.addWidget(self.tort)
#         self.vBox2.addWidget(self.rulet)
#         self.vBox2.addWidget(self.pirog)
#         self.vBox2.addWidget(self.submit)
#         self.submit.clicked.connect(self.Check)

#         self.hBox.addLayout(self.vBox)
#         self.hBox.addLayout(self.vBox2)
#         self.setLayout(self.hBox)

#         self.t1 = [self.mastava, self.chuchvara, self.kShorva, self.lagmon, self.tShorva]
#         self.t2 = [self.osh, self.kabob, self.manti, self.bishteks, self.somsa]
#         self.drink = [self.tea, self.fanta, self.pepsi, self.sprite, self.oSharbat]
#         self.desert = [self.napoleon, self.olivye, self.tort, self.rulet, self.pirog]

#     def Check(self):
#         print("Check >>")
#         for i in self.t1:
#             if i.isChecked():
#                 print(i.text())
#         for i in self.t2:
#             if i.isChecked():
#                 print(i.text())
#         for i in self.drink:
#             if i.isChecked():
#                 print(i.text())
#         for i in self.desert:
#             if i.isChecked():
#                 print(i.text())
#         app.exit()

# app = QApplication(sys.argv)
# project = Window()
# project.show()
# sys.exit(app.exec())