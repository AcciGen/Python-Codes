import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import os
import sys

from PyQt6.QtWidgets import QWidget

os.system("cls")

class Project(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,640,480)
        self.setFont(QFont("Times New Roman", 20))
        self.cmb = QComboBox(self)
        self.cmb.setGeometry(50, 50, 250, 50)
        self.cmb.setStyleSheet("color: rgb(0,0,255);")

        self.cmb.addItem("Go Backend")
        self.cmb.addItem(".Net Backend")
        self.cmb.addItem("Full-Stack Backend")
        self.cmb.addItem("Flutter")

        self.cmb.currentTextChanged.connect(self.info)

    def info(self):
        self.msg = QMessageBox()
        self.msg.setText(self.cmb.currentText())
        self.msg.setFont(QFont("Calibri", 18))
        self.msg.show()



app = QApplication(sys.argv)
pr = Project()
pr.show()
sys.exit(app.exec())

#1
#combobox qoyib davlatlar ro'yhati bor 5ta bor ichida
#Usa bayrog'i chiqishi kerak combobox pasida agar tanlansa

#2
#kalkulyator