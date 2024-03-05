from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys

#1
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.show()
#         self.setFixedSize(600, 200)
#         self.setWindowTitle("Temperature Converter")
#         self.setStyleSheet("background:black;color:white")

#         self.h_box = QHBoxLayout()
#         self.h_box1 = QHBoxLayout()
#         self.h_box2 = QHBoxLayout()
#         self.h_box3 = QHBoxLayout()
#         self.v_box = QVBoxLayout()

#         self.label1 = QLabel("Fahrenheit:")
#         self.label1.setStyleSheet("font-size:20px")
#         self.line1 = QLineEdit()
#         self.line1.setPlaceholderText("0")
#         self.line1.setStyleSheet("font-size:20px")
#         self.label2 = QLabel("Celsius:")
#         self.label2.setStyleSheet("font-size:20px")
#         self.line2 = QLineEdit()
#         self.line2.setPlaceholderText("0")
#         self.line2.setStyleSheet("font-size:20px")
#         self.btn = QPushButton("Convert to Celsius")
#         self.btn.setStyleSheet("background: grey;border-radius:15px;font-size:20px")
#         self.btn1 = QPushButton("Convert to Fahrenheit")
#         self.btn1.setStyleSheet("background: grey;border-radius:15px;font-size:20px")
#         self.label3 = QLabel("Result:")
#         self.label3.setStyleSheet("font-size:20px")
#         self.label4 = QLabel("")
#         self.label4.setStyleSheet("font-size:20pt")

#         self.h_box.addWidget(self.label1)
#         self.h_box.addWidget(self.line1)
#         self.h_box.addWidget(self.label2)
#         self.h_box.addWidget(self.line2)

#         self.h_box1.addWidget(self.btn)
#         self.h_box1.addWidget(self.btn1)

#         self.h_box2.addWidget(self.label3)
#         self.h_box3.addWidget(self.label4)

#         self.v_box.addLayout(self.h_box)
#         self.v_box.addLayout(self.h_box1)
#         self.v_box.addLayout(self.h_box2)
#         self.v_box.addLayout(self.h_box3)

#         self.setLayout(self.v_box)

#         self.btn.clicked.connect(lambda: self.fill(1))
#         self.btn1.clicked.connect(lambda: self.fill(0))

#     def fill(self, btn):
#         if btn:
#             text = self.line1.text()
#             try:
#                 self.label4.setText("{:.2f} °C".format((5/9*(float(text)-32))))
#             except ValueError:
#                 self.label4.setText("Error!")
#         else:
#             text = self.line2.text()
#             try:
#                 self.label4.setText("{:.2f} °F".format(((float(text)*9/5)+32)))
#             except ValueError:
#                 self.label4.setText("Error!")

# app = QApplication(sys.argv)
# window = Window()
# app.exec()


#2
class Buttons(QPushButton):
    def __init__(self,text):
        super().__init__(text)
        self.setFixedSize(90,50)
        self.setStyleSheet("background: #17E612;border-radius:15px;font-size:25px")

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.show()
        self.setFixedSize(500, 500)
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("C:\\Codes\\Py_Codes\\PyQt6\\Calculator.ico"))
        self.setStyleSheet("background: gold;color:white")

        self.h_box = QHBoxLayout()
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()
        self.v_box = QVBoxLayout()

        self.btn = Buttons('0')
        self.btn1 = Buttons('1')
        self.btn2 = Buttons('2')
        self.btn3 = Buttons('3')
        self.btn4 = Buttons('4')
        self.btn5 = Buttons('5')
        self.btn6 = Buttons('6')
        self.btn7 = Buttons('7')
        self.btn8 = Buttons('8')
        self.btn9 = Buttons('9')
        self.btn10 = Buttons('+')
        self.btn11 = Buttons('-')
        self.btn12 = Buttons('*')
        self.btn13 = Buttons('/')
        self.btn14 = Buttons('.')

        self.btn15 = Buttons('=')
        self.btn15.setFixedSize(90,90)
        self.btn15.setStyleSheet("background:red;border-radius:15px;font-size:30px")

        self.clear = QPushButton()
        self.clear.setFixedSize(100,60)
        self.clear.setText("Clear")
        self.clear.setStyleSheet("background:#17E612;border-radius:15px;font-size:20pt")

        self.edit = QLineEdit()
        self.edit.setFixedSize(320,60)
        self.edit.setPlaceholderText("0")
        self.edit.setStyleSheet("background:#17E612;border-radius:15px;font-size:30px")

        self.h_box.addWidget(self.edit)
        self.h_box.addWidget(self.clear)

        self.h_box1.addWidget(self.btn7)
        self.h_box1.addWidget(self.btn8)
        self.h_box1.addWidget(self.btn9)
        self.h_box1.addWidget(self.btn13)

        self.h_box2.addWidget(self.btn4)
        self.h_box2.addWidget(self.btn5)
        self.h_box2.addWidget(self.btn6)
        self.h_box2.addWidget(self.btn12)

        self.h_box3.addWidget(self.btn1)
        self.h_box3.addWidget(self.btn2)
        self.h_box3.addWidget(self.btn3)
        self.h_box3.addWidget(self.btn11)

        self.h_box4.addWidget(self.btn)
        self.h_box4.addWidget(self.btn14)
        self.h_box4.addWidget(self.btn10)
        self.h_box4.addWidget(self.btn15)
        
        self.v_box.addLayout(self.h_box)
        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)

        self.setLayout(self.v_box)

        self.btn.clicked.connect(lambda : self.fill(self.btn))
        self.btn1.clicked.connect(lambda : self.fill(self.btn1))
        self.btn2.clicked.connect(lambda : self.fill(self.btn2))
        self.btn3.clicked.connect(lambda : self.fill(self.btn3))
        self.btn4.clicked.connect(lambda : self.fill(self.btn4))
        self.btn5.clicked.connect(lambda : self.fill(self.btn5))
        self.btn6.clicked.connect(lambda : self.fill(self.btn6))
        self.btn7.clicked.connect(lambda : self.fill(self.btn7))
        self.btn8.clicked.connect(lambda : self.fill(self.btn8))
        self.btn9.clicked.connect(lambda : self.fill(self.btn9))
        self.btn10.clicked.connect(lambda : self.fill(self.btn10))
        self.btn11.clicked.connect(lambda : self.fill(self.btn11))
        self.btn12.clicked.connect(lambda : self.fill(self.btn12))
        self.btn13.clicked.connect(lambda : self.fill(self.btn13))
        self.btn14.clicked.connect(lambda : self.fill(self.btn14))

        self.clear.clicked.connect(self.res)
        self.btn15.clicked.connect(self.result)

    def fill(self,btn):
        text = self.edit.text()
        text2 = btn.text()
        text+=text2
        self.edit.setText(text)
    
    def res(self):
        self.edit.setText('')

    def result(self):
        try:
            result = self.edit.text()
            result = eval(result)
            self.edit.setText(f'{result}')
        except SyntaxError:
            self.edit.setText("Error!")
        except ZeroDivisionError:
            self.edit.setText("Zero Division!")

        except NameError:
            self.edit.setText("Only Numbers!")

app = QApplication(sys.argv)
window = Window()
app.exec()