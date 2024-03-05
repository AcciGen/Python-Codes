import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys

from PyQt6.QtWidgets import QWidget

class Button(QPushButton):
     def __init__(self, text):
        super().__init__(text)

        self.setFixedSize(120, 120)
        self.setStyleSheet("""
						font-size: 25pt;
                        border-radius: 15px;
                        color: lime;
                        border-color: lime;
            			border-width: 3px;
            			border-style: solid;
                           """)

class TicTacToe(QWidget):
	def __init__(self):
		super().__init__()
		self.show()
		self.setFixedSize(520, 500)
		self.setWindowTitle("Tic Tac Toe")
		self.setWindowIcon(QIcon("C:\\Codes\\PyCodes\\PyQt6\\Tic Tac Toe.ico"))
		self.setStyleSheet("background: black; color: lime; font-size: 20px")

		self.side = 0
		self.btn1 = Button("")
		self.btn2 = Button("")
		self.btn3 = Button("")
		self.btn4 = Button("")
		self.btn5 = Button("")
		self.btn6 = Button("")
		self.btn7 = Button("")
		self.btn8 = Button("")
		self.btn9 = Button("")

		self.msg = QMessageBox()
		self.msg.setWindowTitle("Tic Tac Toe")
        
		self.btns = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9]
		for i in self.btns:
			i.clicked.connect(self.checkBox)

		self.grid = QGridLayout()
            
		self.grid.addWidget(self.btn1,0,0)
		self.grid.addWidget(self.btn2,0,1)
		self.grid.addWidget(self.btn3,0,2)
        
		self.grid.addWidget(self.btn4,1,0)
		self.grid.addWidget(self.btn5,1,1)
		self.grid.addWidget(self.btn6,1,2)
        
		self.grid.addWidget(self.btn7,2,0)
		self.grid.addWidget(self.btn8,2,1)
		self.grid.addWidget(self.btn9,2,2)

		self.setLayout(self.grid)
            
	def checkBox(self):
		btn = self.sender()
		for i in self.btns:
			if btn == i:
				if self.side % 2 == 0 and i.text() == "":
					i.setText("X")
					self.check()
					self.draw()

				elif self.side % 2 != 0 and i.text() == "":
					i.setText("O")
					self.check()
					self.draw()

				self.side += 1
		
	def check(self):
		if self.btn1.text() == self.btn2.text() == self.btn3.text() == "X":
			self.msg.setText("X Winner")
			self.msg.show()
			sys.exit(self.msg.exec())
		elif self.btn4.text() == self.btn5.text() == self.btn6.text() == "X":
			self.msg.setText("X Winner")
			self.msg.show()
			sys.exit(self.msg.exec())
		elif self.btn7.text() == self.btn8.text() == self.btn9.text() == "X":
			self.msg.setText("X Winner")
			self.msg.show()
			sys.exit(self.msg.exec())
		elif self.btn1.text() == self.btn4.text() == self.btn7.text() == "X":
			self.msg.setText("X Winner")
			self.msg.show()
			sys.exit(self.msg.exec())
		elif self.btn2.text() == self.btn5.text() == self.btn8.text() == "X":
			self.msg.setText("X Winner")
			self.msg.show()
			sys.exit(self.msg.exec())
		elif self.btn3.text() == self.btn6.text() == self.btn9.text() == "X":
			self.msg.setText("X Winner")
			self.msg.show()
			sys.exit(self.msg.exec())
		elif self.btn1.text() == self.btn5.text() == self.btn9.text() == "X":
			self.msg.setText("X Winner")
			self.msg.show()
			sys.exit(self.msg.exec())
		elif self.btn3.text() == self.btn5.text() == self.btn7.text() == "X":
			self.msg.setText("X Winner")
			self.msg.show()
			sys.exit(self.msg.exec())


		if self.btn1.text() == self.btn2.text() == self.btn3.text() == "O":
			self.msg.setText("O Winner")
			self.msg.show()
			sys.exit(self.msg.exec())
		elif self.btn4.text() == self.btn5.text() == self.btn6.text() == "O":
			self.msg.setText("O Winner")
			self.msg.show()
			sys.exit(self.msg.exec())
		elif self.btn7.text() == self.btn8.text() == self.btn9.text() == "O":
			self.msg.setText("O Winner")
			self.msg.show()
			sys.exit(self.msg.exec())
		elif self.btn1.text() == self.btn4.text() == self.btn7.text() == "O":
			self.msg.setText("O Winner")
			self.msg.show()
			sys.exit(self.msg.exec())
		elif self.btn2.text() == self.btn5.text() == self.btn8.text() == "O":
			self.msg.setText("O Winner")
			self.msg.show()
			sys.exit(self.msg.exec())
		elif self.btn3.text() == self.btn6.text() == self.btn9.text() == "O":
			self.msg.setText("O Winner")
			self.msg.show()
			sys.exit(self.msg.exec())
		elif self.btn1.text() == self.btn5.text() == self.btn9.text() == "O":
			self.msg.setText("O Winner")
			self.msg.show()
			sys.exit(self.msg.exec())
		elif self.btn3.text() == self.btn5.text() == self.btn7.text() == "O":
			self.msg.setText("O Winner")
			self.msg.show()
			sys.exit(self.msg.exec())

	def draw(self):
		bx = True
		for i in self.btns:
			if i.text() == "":
				bx = False
				break
		if bx:
			self.msg.setText("Draw")
			self.msg.show()


app = QApplication(sys.argv)
project = TicTacToe()
sys.exit(app.exec())