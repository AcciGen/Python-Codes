import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys
import os
from PyQt6.QtWidgets import QWidget
import mysql.connector as my

class SignUp(QWidget):
    def __init__(self):
        super().__init__()
        self.con = my.connect(user = "root", password = "1551734", host = "localhost")
        self.cur = self.con.cursor()
        self.cur.execute("Create database if not exists login")
        self.cur.execute("Use login")
        self.cur.execute("Create table if not exists users(id int primary key auto_increment, login varchar(40), password varchar(40))")
        self.con.commit()

        self.setFixedSize(300, 250)
        self.setStyleSheet("background: black; color: lime; font-size: 20px;")
        self.vBox = QVBoxLayout()

        self.lbTitle = QLabel("SIGN UP")
        self.vBox.addWidget(self.lbTitle)

        self.lnLogin = QLineEdit()
        self.lnLogin.setPlaceholderText("Login")
        self.lnLogin.setStyleSheet("border-radius: 10px; border-width: 2px; border-style: solid; border-color: lime;")
        self.vBox.addWidget(self.lnLogin)

        self.lnPassword = QLineEdit()
        self.lnPassword.setPlaceholderText("Password")
        self.lnPassword.setStyleSheet("border-radius: 10px; border-width: 2px; border-style: solid; border-color: lime;")
        self.lnPassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.vBox.addWidget(self.lnPassword)

        self.lnRepeat = QLineEdit()
        self.lnRepeat.setPlaceholderText("Repeat password")
        self.lnRepeat.setStyleSheet("border-radius: 10px; border-width: 2px; border-style: solid; border-color: lime;")
        self.lnRepeat.setEchoMode(QLineEdit.EchoMode.Password)
        self.vBox.addWidget(self.lnRepeat)

        self.btnRegistrate = QPushButton(">> Registrate <<")
        self.btnRegistrate.setStyleSheet("border-radius: 15px; border-width: 3px; border-style: solid; border-color: lime;")
        self.btnRegistrate.setShortcut("Ctrl+S")
        self.btnRegistrate.clicked.connect(self.inputData)
        self.vBox.addWidget(self.btnRegistrate)

        self.loading = QLabel()
        self.vBox.addWidget(self.loading)

        self.setLayout(self.vBox)

    def inputData(self):
        sql = f"INSERT into users(login, password) Values (%s, %s)"
        if self.lnPassword.text() == self.lnRepeat.text() and self.lnLogin.text() != "" and self.lnPassword.text() != "" and self.lnRepeat.text() != "":
            value = (self.lnLogin.text(), self.lnPassword.text())
            self.cur.execute(sql, value)
            self.con.commit()
            self.lnLogin.clear()
            self.lnPassword.clear()
            self.lnRepeat.clear()
            self.lnPassword.setPlaceholderText("Password")
            self.lnPassword.setStyleSheet("border-radius: 10px; border-width: 2px; border-style: solid; border-color: lime;")
            self.lnRepeat.setStyleSheet("border-radius: 10px; border-width: 2px; border-style: solid; border-color: lime;")
            self.lnRepeat.setPlaceholderText("Repeat password")
            self.loading.setText("Signed Up Successfully!")
        elif self.lnRepeat.text() != "" and self.lnPassword.text() != self.lnRepeat.text():
            self.lnPassword.clear()
            self.lnRepeat.clear()
            self.lnPassword.setStyleSheet("border-radius: 10px; border-width: 2px; border-style: solid; border-color: red;")
            self.lnRepeat.setStyleSheet("border-radius: 10px; border-width: 2px; border-style: solid; border-color: red;")
            self.lnPassword.setPlaceholderText("Passwords Not Same!")
            self.lnRepeat.setPlaceholderText("Passwords Not Same!")
        else:
            self.lnLogin.setStyleSheet("border-radius: 10px; border-width: 2px; border-style: solid; border-color: red;")
            self.lnPassword.setStyleSheet("border-radius: 10px; border-width: 2px; border-style: solid; border-color: red;")
            self.lnRepeat.setStyleSheet("border-radius: 10px; border-width: 2px; border-style: solid; border-color: red;")
            self.loading.setText("Fill The Gaps!")

app = QApplication(sys.argv)
project = SignUp()
project.show()
sys.exit(app.exec())



# class Counter(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setFixedSize(300, 250)
#         self.setStyleSheet("background-color: black; color: lime; font-size: 20px;")

#         self.vBox = QVBoxLayout()

#         self.lnWord = QLineEdit()
#         self.lnWord.setPlaceholderText("Enter the words")
#         self.lnWord.setStyleSheet(f"""border-radius: 10px;
#                                 border-width: 2px;
#                                 border-style: solid;
#                                 border-color: lime;
#                                 padding: 3px;""")
        
#         self.lnLetter = QLineEdit()
#         self.lnLetter.setPlaceholderText("Enter the letter")
#         self.lnLetter.setStyleSheet("""border-radius: 10px;
#                                     border-width: 2px;
#                                     border-style: solid;
#                                     border-color: lime;
#                                     padding: 3px;""")
        
        
#         self.btnCount = QPushButton()
#         self.btnCount.setText("Count")
#         self.btnCount.setStyleSheet("""border-radius: 15px;
#                                     border-width: 2px;
#                                     border-style: solid;
#                                     border-color: lime;""")
#         self.btnCount.setShortcut("Ctrl+S")
#         self.btnCount.clicked.connect(self.countLetter)

#         self.lb = QLabel()
#         self.lb.setText("Press Ctrl + S to Count")

#         self.vBox.addStretch()
#         self.vBox.addWidget(self.lnWord)
#         self.vBox.addStretch()
#         self.vBox.addWidget(self.lnLetter)
#         self.vBox.addStretch()
#         self.vBox.addWidget(self.btnCount)
#         self.vBox.addStretch()
#         self.vBox.addWidget(self.lb)
#         self.vBox.addStretch()


#         self.setLayout(self.vBox)

#     def countLetter(self):
#         if self.lnWord.text() == "" or self.lnLetter.text() == "":
#             self.lnWord.setStyleSheet("""border-radius: 10px;
#                                     border-width: 2px;
#                                     border-style: solid;
#                                     border-color: red;
#                                     padding: 3px;""")
            
#             self.lnLetter.setStyleSheet("""border-radius: 10px;
#                                     border-width: 2px;
#                                     border-style: solid;
#                                     border-color: red;
#                                     padding: 3px;""")
            
#             self.lb.setText("Fill The Lines!")
#             self.lb.setStyleSheet("color: red;")

#         elif self.lnWord.text() != "" and self.lnLetter.text() != "":
#             self.lnWord.setStyleSheet("""border-radius: 10px;
#                                     border-width: 2px;
#                                     border-style: solid;
#                                     border-color: lime;
#                                     padding: 3px;""")
            
#             self.lnLetter.setStyleSheet("""border-radius: 10px;
#                                     border-width: 2px;
#                                     border-style: solid;
#                                     border-color: lime;
#                                     padding: 3px;""")
            
#             self.lb.clear()
#             self.lb.setStyleSheet("color: lime;")

#             if len(self.lnLetter.text()) > 1:
#                 self.lb.setText("Please Enter Only 1 Letter!")
#                 self.lb.setStyleSheet("color: red;")
#             else:
#                 self.lb.clear()
#                 self.lb.setStyleSheet("color: lime;")

#                 cnt = 0
#                 for i in self.lnWord.text():
#                     if i == self.lnLetter.text():
#                         cnt += 1
#                 if cnt > 0:
#                     self.lb.setText(f"{self.lnLetter.text()}-{cnt}")
#                 else:
#                     self.lb.setText("404 Not Found")
#                     self.lb.setStyleSheet("color: red;")

# app = QApplication(sys.argv)
# project = Counter()
# project.show()
# app.exec()