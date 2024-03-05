import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import os
import sys
from random import shuffle

from PyQt6.QtWidgets import QWidget

class ExtraButton(QPushButton):
    def __init__(self,text):
        super().__init__(text)

        self.setFixedSize(150,60)
        self.setStyleSheet("""
                        border-radius: 15px;
                        color: lime;
                        border-color: lime;
            			border-width: 4px;
            			border-style: solid;
""")
        
class Button(QPushButton):
     def __init__(self,text):
        super().__init__(text)

        self.setFixedSize(120,120)
        self.setStyleSheet("""
                        border-radius: 15px;
                        color: lime;
                        border-color: lime;
            			border-width: 4px;
            			border-style: solid;
""")
    
class Game(QWidget):
    def __init__(self, size = 4):
        super().__init__()
        self.size = size
        self.numbers = 0
        self.count = 0
        self.start = True
        self.count_move = 0
        self.matrix = list()
        
        self.menu = QMenuBar(self)
        self.menu.setStyleSheet("background: black")
        self.menu.setGeometry(180, 9, 30, 30)

        self.opt = QMenu("OPTIONS", self)
        self.nGame = QAction("New Game", self)
        self.nGame.setShortcut("Ctrl+N")
        self.nGame.triggered.connect(self.__new_game)
		
        self.tCnt = QAction("Tries", self)
        self.tCnt.setShortcut("Tab")
        self.tCnt.triggered.connect(self.tries)
		
        self.ex = QAction("Exit", self)
        self.ex.setShortcut("Esc")
        self.ex.triggered.connect(self.exit)

        self.menu.addMenu(self.opt)
        self.opt.addActions([self.nGame, self.tCnt, self.ex])

        self.setWindowTitle("Game Puzzle")
        self.setStyleSheet("""
            font-size: 30px;
            background: black;
            color: lime""")
        self.initUi()
        self.show()

        # self.btn_pause.clicked.connect(self.start_stop)
        # self.btn_restart.clicked.connect(self.__res_game)
        # self.btn_new.clicked.connect(self.__new_game)


    def initUi(self):

        self.v_box = QVBoxLayout()
        self.top_box = QHBoxLayout()
        self.bottom_box = QHBoxLayout()
        self.grid = QGridLayout()

        self.timer =QLabel("Time : 0 s ")
        self.moves =QLabel("Moves : 0")

        # self.btn_restart = ExtraButton("Restart")
        # self.btn_pause = ExtraButton("Pause")
        # self.btn_new = ExtraButton("New game")

        timer = QTimer(self)
        timer.timeout.connect(self.__show_Time)
        timer.start(1000)

        self.__create_grid()
        self.__connect_btn()
        self.__create_window()
        if self.check_winner():
            self.start_stop()
            self.btn_pause.setEnabled(False)

    def __create_grid(self):
        self.fill_matrix()
        for i in range(self.size):
            for j in range(self.size):
                self.grid.addWidget(self.matrix[i][j],i,j)

    def __create_window(self):
        self.top_box.addWidget(self.timer)
        self.top_box.addStretch()
        self.top_box.addStretch()
        self.top_box.addWidget(self.moves)

        # self.bottom_box.addWidget(self.btn_new)
        # self.bottom_box.addWidget(self.btn_restart)
        # self.bottom_box.addWidget(self.btn_pause)
        

        self.v_box.addLayout(self.top_box)
        self.v_box.addLayout(self.grid)
        self.v_box.addLayout(self.bottom_box)

        self.setLayout(self.v_box)

    def fill_matrix(self):
        i = 0
        self.numbers = self.__create_numbers(1)
        for _ in range(self.size):
            row = list()
            for _ in range(self.size):
                row.append(Button((self.numbers[i])))
                i+=1
            self.matrix.append(row)

    def __create_numbers(self,num = 0):
        nums= list(range(1,self.size * self.size))
        nums = list(map(str,nums)) + [''] 
        if num:
            shuffle(nums)
        return nums
    
    def __connect_btn(self):
        for x in range(self.size):
            for y in range(self.size):
                self.matrix[x][y].clicked.connect(self.__changePossition)
                if not self.matrix[x][y].text():
                    self.matrix[x][y].hide()

    def __changePossition(self):
        btn = self.sender()
        for i in range(self.size):
            for j in range(self.size):
                if btn == self.matrix[i][j]:
                    if i-1 >= 0 and self.matrix[i-1][j].text() == '': 
                        self.matrix[i-1][j].setText(btn.text())
                        self.matrix[i-1][j].show()
                        btn.setText('')
                        btn.hide()  
                        self.count_move +=1

                    elif i+1 < self.size and self.matrix[i+1][j].text() == '':                        
                        self.matrix[i+1][j].setText(btn.text())
                        self.matrix[i+1][j].show()
                        btn.setText('')
                        btn.hide()
                        self.count_move +=1

                    elif j-1 >= 0 and self.matrix[i][j-1].text() == '':
                        self.matrix[i][j-1].setText(btn.text())
                        self.matrix[i][j-1].show()
                        btn.setText('')
                        btn.hide()
                        self.count_move +=1
                    
                    elif j+1 < self.size and self.matrix[i][j+1].text() == '':                        
                        self.matrix[i][j+1].setText(btn.text())
                        self.matrix[i][j+1].show()
                        btn.setText('')
                        btn.hide()
                        self.count_move +=1  
                    self.moves.setText(f'Moves: {self.count_move}')
                    if self.check_winner():
                        self.start_stop()
                        self.btn_pause.setEnabled(False)
                        msg = QMessageBox()
                        msg.setText("Congratulation")
                        msg.setFixedSize(300,100)
                        msg.setStyleSheet("background : gold;color:black;font-size :15pt")
                        msg.exec_()
    def __show_Time(self):
        if self.start:
            self.count +=1
            text = f"Time : {self.count} s"
            self.timer.setText(text)

    def start_stop(self):
        if self.start:
            self.btn_pause.setText('Start')
            self.__disable_buttons()
        else:
            self.btn_pause.setText('Pause')
            self.__activate_buttons()
        self.start = not self.start 
        
    def __disable_buttons(self):
        for x in range(self.size):
            for y in range(self.size):
                self.matrix[x][y].setEnabled(False)  

    def __activate_buttons(self):
        for x in range(self.size):
            for y in range(self.size):
                self.matrix[x][y].setEnabled(True) 

    def check_winner(self):
        numbers = self.__create_numbers()
        i = 0
        for x in range(self.size):
            for y in range(self.size):
                if self.matrix[x][y].text() != numbers[i]:
                    return False
                i+=1 
        return True
    
    def __res_game(self):
        self.res_raund = Game(self.size)
        self.close()
        self.res_raund.show()

    def __new_game(self):
        self.new_raund = Game()
        self.close()
        self.new_raund.show()
        
    def tries(self):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Info")
        self.msg.setText("Tries: "+str(self.count_move))
        self.msg.setFont(QFont("Calibri", 18))
        self.msg.show()

    def exit(self):
        app.exit()

app = QApplication(sys.argv)
project = Game()
project.show()
sys.exit(app.exec())