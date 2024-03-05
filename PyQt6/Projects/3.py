from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import os
import sys
os.chdir("C:\\Codes\\PyCodes\\PyQt6\\Projects")


class project(QMainWindow):
    __ball_test = 0
    def __init__(self):
        super().__init__()
        self.setMaximumSize(800,600)
        self.setMinimumSize(800,600)
        self.setFont(QFont("Poor Richard",20))
        
        self.txt = QTextEdit(self)
        self.txt.setGeometry(50,70,700,490)
       
        open_file = QAction(QIcon("C:\\Codes\\PyCodes\\PyQt6\\Projects\\folder.ico"),"Open File",self)
        open_file.setShortcut("Ctrl+O")
        open_file.triggered.connect(self.open_f)
        
        save_file = QAction(QIcon("C:\\Codes\\PyCodes\\PyQt6\\Projects\\save_1.ico"),"Save File",self)
        save_file.setShortcut("Ctrl+S")
        save_file.triggered.connect(self.save)
        
        menu = QMenuBar(self)
        menu.resize(600,50)
        #menu.setStyleSheet("background-color: rgb(250,240,230);color: rgb(0,0,255);")
        
        File  = QMenu("File",self)
        File.setFont(QFont("Consolas",18))
        
        File.addAction(open_file)
        File.addAction(save_file)
        menu.addMenu(File)
        
        edit_color = QAction(QIcon("C:\\Codes\\PyCodes\\PyQt6\\Projects\\color.ico"),"Edit Color",self)
        edit_color.setShortcut("Ctrl+R")
        edit_color.triggered.connect(self.change_color)
        
        edit_font = QAction(QIcon("C:\\Codes\\PyCodes\\PyQt6\\Projects\\font.ico"),"Edit Font",self)
        edit_font.setShortcut("Ctrl+F")
        edit_font.triggered.connect(self.change_font)
        
        Edit = QMenu("Edit",self)
        Edit.setFont(QFont("Poor Richard",18))
        
        edit = QMenu("edit",self)
        edit.setFont(QFont("Poor Richard",18))
        edit.addActions([edit_color,edit_font])
        
        Edit.addMenu(edit)
        menu.addMenu(Edit)
        
        # self.btn = QPushButton(self)
        # self.btn.setGeometry(540,540,250,50)
        # self.btn.setStyleSheet("color: rgb(0,255,0);background-color: black")
        # self.btn.addAction(edit_color)
        # self.btn.setFont(QFont("Poor Richard",20))  
    
    def open_f(self):
        os.system("cls")
        filename = QFileDialog().getOpenFileName(self,"Faylni tanlang: ","C:\\Codes\\PyCodes",filter="*.txt")[0]
        file = open(filename,"rt")
        data = file.read()
        self.txt.setText(data)
       
    def save(self):
        os.system("cls")
        filename = QFileDialog().getSaveFileName(self,"Faylni kiriting: ", "C:\\Codes\\PyCodes",filter="*.txt")[0]
        file = open(filename, "w")
        data = self.txt.toPlainText()
        file.write(data)
        file.close()

    def change_color(self):
        color = QColorDialog().getColor()
        if color:
            self.txt.setStyleSheet(f"color: {color.name()}")
    
    def change_font(self):
        font = QFontDialog().getFont()
        if font[1]:
            self.txt.setFont(QFont(font[0]))

app =QApplication(sys.argv)
dastur = project()
dastur.show()
sys.exit(app.exec())
