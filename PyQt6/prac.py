import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
import sys

#1
# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         empty_widget = QWidget()
#         layout = QHBoxLayout()

#         self.setWindowTitle("Den Rov")
#         self.setGeometry(100, 100, 500, 400) # We can call functions there as well!
#         desktop = self.screen().availableGeometry()
#         # print(desktop.width())
#         # print(desktop.height())
#         self.move(desktop.width()//2 - 500//2, desktop.height()//2 - 400//2)
        
#         label = QLabel(self)
#         label.move(200, 180)
#         label.setText("Hellow World!")
#         # self.setCentralWidget(label)

#         input_text = QLineEdit()
#         layout = QVBoxLayout()
#         layout.addWidget(label)
#         layout.addWidget(input_text)

#         empty_widget.setLayout(layout)
#         self.setCentralWidget(empty_widget)

# app = QApplication(sys.argv) #Application qilish
# window = MyWindow() #Oyna ochish
# # window.setGeometry(0,0,1524,780)
# window.show()

# sys.exit(app.exec())


#2
# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         widget = QWidget()
#         layout = QVBoxLayout()

#         self.login_label = QLabel("Login")
#         self.username_input = QLineEdit()
#         self.password_input = QLineEdit()
#         self.submit_button = QPushButton("Enter")

#         self.submit_button.clicked.connect(self.enter)
#         layout.addWidget(self.login_label)
#         layout.addWidget(self.username_input)
#         layout.addWidget(self.password_input)
#         layout.addWidget(self.submit_button)

#         widget.setLayout(layout)

#         self.setCentralWidget(widget)

#     def enter(self):
#         print(f"Username: {self.username_input.text()}\nPassword: {self.password_input.text()}")
#         sys.exit(app.exec())

# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()

# sys.exit(app.exec())

class Buttons(QPushButton):
    def __init__(self,text):
        super().__init__(text)
        self.setFixedSize(100,60)
        self.setStyleSheet("background: #17E612;font-size:25px")

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.show()
        self.setFixedSize(500, 500)
        self.setWindowTitle("Calculator")

        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()
        self.h_box5 = QHBoxLayout()
        self.h_box6 = QHBoxLayout()
        self.v_box = QVBoxLayout()

        
        self.btn = Buttons('0')
        self.btn.setFixedSize(220, 60)
        self.btn1 = Buttons('1')
        self.btn2 = Buttons('2')
        self.btn3 = Buttons('3')
        self.btn4 = Buttons('4')
        self.btn5 = Buttons('5')
        self.btn6 = Buttons('6')
        self.btn7 = Buttons('7')
        self.btn8 = Buttons('8')
        self.btn9 = Buttons('9')
        self.btn10 = Buttons('.')
        self.btn11 = Buttons('+')
        self.btn11.setStyleSheet("background: yellow")
        self.btn12 = Buttons('-')
        self.btn12.setStyleSheet("background: yellow")
        self.btn13 = Buttons('*')
        self.btn13.setStyleSheet("background: yellow")
        self.btn14 = Buttons('/')
        self.btn14.setStyleSheet("background: yellow")
        self.btn15 = Buttons('=')
        self.btn15.setStyleSheet("background: yellow")
        self.btn16 = Buttons('AC')
        self.btn16.setFixedSize(220, 60)
        self.btn17 = Buttons("%")

        self.edit = QLineEdit()
        self.edit.setFixedSize(320,60)
        self.edit.setPlaceholderText("0")
        self.edit.setStyleSheet("background:#17E612;border-radius:15px;font-size:30px")

        self.h_box1.addWidget(self.edit)

        self.h_box2.addWidget(self.btn16)
        self.h_box2.addWidget(self.btn17)
        self.h_box2.addWidget(self.btn14)
        self.h_box3.addWidget(self.btn7)
        self.h_box3.addWidget(self.btn8)
        self.h_box3.addWidget(self.btn9)
        self.h_box3.addWidget(self.btn13)
        self.h_box4.addWidget(self.btn4)
        self.h_box4.addWidget(self.btn5)
        self.h_box4.addWidget(self.btn6)
        self.h_box4.addWidget(self.btn12)
        self.h_box5.addWidget(self.btn1)
        self.h_box5.addWidget(self.btn2)
        self.h_box5.addWidget(self.btn3)
        self.h_box5.addWidget(self.btn11)
        self.h_box6.addWidget(self.btn)
        self.h_box6.addWidget(self.btn10)
        self.h_box6.addWidget(self.btn15)

        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)
        self.v_box.addLayout(self.h_box5)
        self.v_box.addLayout(self.h_box6)

        self.setLayout(self.v_box)

app = QApplication(sys.argv)
window = Window()
app.exec()