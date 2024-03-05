import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys
import os
from PyQt6.QtWidgets import QWidget
import mysql.connector as my

# class Project(QTabWidget):
#     def __init__(self, parent = None):
#         super(Project, self).__init__(parent)
#         self.setFixedSize(1520, 782)
#         self.setFont(QFont("Poor Richard", 24))

#         self.insert = QWidget()
#         self.update = QWidget()
#         self.delete = QWidget()
#         self.showD = QWidget()

#         self.addTab(self.insert, "Insert data")
#         self.addTab(self.update, "Update data")
#         self.addTab(self.delete, "Delete data")
#         self.addTab(self.showD, "View data")

#         self.update_tab()
#         self.insert_tab()
#         self.delete_tab()
#         self.show_tab()

#     def update_tab(self):
#         self.update.setStyleSheet("background: lime;")

#     def addDatabases(self, database = 'Music'):
#         con = my.connect(user = 'root', password = '1551734', host = 'localhost')
#         curs = con.cursor()
#         curs.execute(f"Create database if not exists {database}")

#     def addTable(self, database = 'Music', table = 'song'):
#         con = my.connect(user = 'root', password = '1551734', host = 'localhost')
#         curs = con.cursor()
#         curs.execute(f"Create table if not exists {table}(id int primary key auto_increment, name varchar(30), author varchar(30), ex_date date, poet varchar(30), downloads int, duration time);")

#     def insert_tab(self):
#         self.insert.setStyleSheet("background: yellow;")

#         self.lb = QLabel("Qo'shiq nomi: ", self)
#         self.lb.setGeometry(50, 100, 250, 50)
#         self.lb.setStyleSheet("color: blue")

#         self.name = QLineEdit(self)
#         self.name.setGeometry(310, 100, 250, 50)
#         self.name.setStyleSheet("""color: blue;
#                                 background: antique white;
#                                 border-radius: 15px;
#                                 border-width: 3px;
#                                 border-wtyle: solid;
#                                 border-color: red;""")
#         self.name.setAlignment(Qt.AlignmentFlag(20))

#         self.lb = QLabel("Qo'shiq muallifi: ", self)
#         self.lb.setGeometry(50, 100, 250, 50)
#         self.lb.setStyleSheet("color: blue")

#         self.name = QLineEdit(self)
#         self.name.setGeometry(310, 100, 250, 50)
#         self.name.setStyleSheet("""color: blue;
#                                 background: antique white;
#                                 border-radius: 15px;
#                                 border-width: 3px;
#                                 border-style: solid;
#                                 border-color: red;""")
#         self.name.setAlignment(Qt.AlignmentFlag(20))

#     def delete_tab(self):
#         self.delete.setStyleSheet("background: red;")

#     def show_tab(self):
#         self.showD.setStyleSheet("background: cyan;")

#     def insert_data(self):
#         self.addDatabases()
        
        
# app = QApplication(sys.argv)
# pr = Project()
# pr.show()
# sys.exit(app.exec())



# class Translater(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setFixedSize(500, 300)
#         self.setStyleSheet("background: black; color: lime; font-size: 20px;")
#         self.hBox = QHBoxLayout()
#         self.hBox1 = QHBoxLayout()
#         self.vBox = QVBoxLayout()

#         self.ln = QLineEdit()
#         self.ln.setStyleSheet("border-radius: 15px; border-width: 3px; border-style: solid; border-color: lime;")    

#         self.btn = QPushButton("> Interpret <")
#         self.btn.setShortcut("Ctrl+S")
#         self.btn.clicked.connect(self.inputData)

#         self.lb = QLabel()

#         self.hBox.addWidget(self.ln)
#         self.hBox.addWidget(self.btn)
#         self.hBox1.addWidget(self.lb)

#         self.vBox.addLayout(self.hBox)
#         self.vBox.addLayout(self.hBox1)

#         self.setLayout(self.vBox)

#     def inputData(self):
#         self.con = my.connect(user = "root", password = "1551734", host = "localhost", database = "translater")
#         self.curs = self.con.cursor()
#         self.curs.execute(f"Select * From enguz")
#         res = self.curs.fetchall()
#         text = self.ln.text()
#         for i in res:
#             if i[1] == text:
#                 self.lb.setText(f"{i[2]}")

#         if self.lb.text() == "":
#             self.inp,ok = QInputDialog().getText(self, 'Dang!!',"Input Here")
#             if ok:
#                 sql = "INSERT INTO enguz(eng,uz)values(%s,%s)"
#                 values = (text,self.inp)
#                 self.curs.execute(sql,values)
#                 self.con.commit()
# app = QApplication(sys.argv)
# project = Translater()
# project.show()
# sys.exit(app.exec())



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
        if self.lnPassword.text() == self.lnRepeat.text():
            value = (self.lnLogin.text(), self.lnPassword.text())
            self.cur.execute(sql, value)
            self.con.commit()
            self.lnLogin.clear()
            self.lnPassword.clear()
            self.lnRepeat.clear()
            self.loading.setText("Signed Up Successfully!")
        else:
            self.lnPassword.clear()
            self.lnRepeat.clear()
            self.lnPassword.setPlaceholderText("Passwords Not Same!")
            self.lnRepeat.setPlaceholderText("Passwords Not Same!")

app = QApplication(sys.argv)
project = SignUp()
project.show()
sys.exit(app.exec())