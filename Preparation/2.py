from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QGridLayout
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys

class Reverser(QWidget):
    def __init__(self):
        super().__init__()
        self.show()
        self.setFixedSize(400, 380)
        self.setWindowTitle("Reverser")
        self.setStyleSheet("background: black; color: lime; font-size: 20px")

        self.line = QLineEdit()
        self.line.setPlaceholderText("Write a text")

        self.lb = QLabel()

        self.btn = QPushButton("Push Me!")
        self.btn.setShortcut("N")
        self.btn.clicked.connect(self.check)

        self.grid = QGridLayout()
        self.grid.addWidget(self.line, 0, 1)
        self.grid.addWidget(self.lb, 1, 1)
        self.grid.addWidget(self.btn, 2, 1)

        self.setLayout(self.grid)
        self.check()
    
    def check(self):
        self.lb.setText(self.line.text()[::-1].upper())


app = QApplication(sys.argv)
project = Reverser()
sys.exit(app.exec())