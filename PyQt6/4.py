from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import os
import sys
os.chdir("C:\\Codes\\Py_Codes\\PyQt6")


class project(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(600,550)
        self.setMinimumSize(600,550)
        self.setWindowTitle("Foundation N37")
        self.setWindowIcon(QIcon("C:\\Codes\\Py_Codes\\PyQt6\\Registr.ico"))
        
        #User ismini kiritish uchun
        
        self.name_lb = QLabel(self)
        self.name_lb.setGeometry(20,30,250,50)
        self.name_lb.setFont(QFont("Calibri",18))
        self.name_lb.setText("Enter Name: ")
        self.name_lb.setStyleSheet("color: rgb(0,0,255);")
        
        self.name = QLineEdit(self)
        self.name.move(275,30)
        self.name.resize(250,50)
        self.name.setFont(QFont("Consolas",18))
        self.name.setStyleSheet("""
            background-color: rgb(253,245,230);
            color: rgb(0,168,107);
            border-color: rgb(0,168,107);
            border-width: 3px;
            border-style: solid;
            border-radius: 15px;""")
        self.name.setAlignment(Qt.AlignmentFlag(20))        
        
        #user loginini kiritish uchun
        
        self.login_lb = QLabel(self)
        self.login_lb.setGeometry(20,90,250,50)
        self.login_lb.setFont(QFont("Calibri",18))
        self.login_lb.setText("Enter Login: ")
        self.login_lb.setStyleSheet("color: rgb(0,0,255);")
        
        self.login= QLineEdit(self)
        self.login.move(275,90)
        self.login.resize(250,50)
        self.login.setFont(QFont("Consolas",18))
        self.login.setStyleSheet("""
            background-color: rgb(253,245,230);
            color: rgb(0,168,107);
            border-color: rgb(0,168,107);
            border-width: 3px;
            border-style: solid;
            border-radius: 15px;""")
        self.login.setAlignment(Qt.AlignmentFlag(20))
        
        #User emailini kiritish uchun
        
        self.email_lb = QLabel(self)
        self.email_lb.setGeometry(20,150,250,50)
        self.email_lb.setFont(QFont("Calibri",18))
        self.email_lb.setText("Enter email: ")
        self.email_lb.setStyleSheet("color: rgb(0,0,255);")
        
        self.email= QLineEdit(self)
        self.email.move(275,150)
        self.email.resize(250,50)
        self.email.setFont(QFont("Consolas",18))
        self.email.setStyleSheet("""
            background-color: rgb(253,245,230);
            color: rgb(0,168,107);
            border-color: rgb(0,168,107);
            border-width: 3px;
            border-style: solid;
            border-radius: 15px;""")
        self.email.setAlignment(Qt.AlignmentFlag(20))
        
        #User Jinsini kiritish uchun
        
        self.sx_lb = QLabel(self)
        self.sx_lb.setGeometry(20,210,250,50)
        self.sx_lb.setFont(QFont("Calibri",18))
        self.sx_lb.setText("Choose gender: ")
        self.sx_lb.setStyleSheet("color: rgb(0,0,255);")
        
        self.rdb = QRadioButton("Ayol",self)
        self.rdb.setGeometry(280,210,90,50)
        self.rdb.setFont(QFont("Calibri",18))
        self.rdb.setStyleSheet("color: rgb(255,0,255);")
        
        self.rdb1 = QRadioButton("Erkak",self)
        self.rdb1.setGeometry(380,210,90,50)
        self.rdb1.setFont(QFont("Calibri",18))
        self.rdb1.setStyleSheet("color: rgb(0,0,205);")
        
        
        #User Tug'ulgan sanani kiritish uchun
        
        self.birth_lb = QLabel(self)
        self.birth_lb.setGeometry(20,270,250,50)
        self.birth_lb.setFont(QFont("Calibri",18))
        self.birth_lb.setText("Enter birthday: ")
        self.birth_lb.setStyleSheet("color: rgb(0,0,255);")
        
        self.birth= QLineEdit(self)
        self.birth.move(275,270)
        self.birth.resize(250,50)
        self.birth.setFont(QFont("Consolas",18))
        self.birth.setStyleSheet("""
            background-color: rgb(253,245,230);
            color: rgb(0,168,107);
            border-color: rgb(0,168,107);
            border-width: 3px;
            border-style: solid;
            border-radius: 15px;""")
        self.birth.setAlignment(Qt.AlignmentFlag(20))
        
        #User Passwordini kiritish uchun
        
        self.pass1_lb = QLabel(self)
        self.pass1_lb.setGeometry(20,330,250,50)
        self.pass1_lb.setFont(QFont("Calibri",18))
        self.pass1_lb.setText("Enter Password: ")
        self.pass1_lb.setStyleSheet("color: rgb(0,0,255);")
        
        self.pass1= QLineEdit(self)
        self.pass1.move(275,330)
        self.pass1.resize(250,50)
        self.pass1.setFont(QFont("Consolas",18))
        self.pass1.setStyleSheet("""
            background-color: rgb(253,245,230);
            color: rgb(0,168,107);
            border-color: rgb(0,168,107);
            border-width: 3px;
            border-style: solid;
            border-radius: 15px;""")
        self.pass1.setAlignment(Qt.AlignmentFlag(20))
        
        
        #User Passwordini kiritish uchun
        
        self.pass2_lb = QLabel(self)
        self.pass2_lb.setGeometry(20,390,250,50)
        self.pass2_lb.setFont(QFont("Calibri",18))
        self.pass2_lb.setText("Repeat Password: ")
        self.pass2_lb.setStyleSheet("color: rgb(0,0,255);")
        
        self.pass2= QLineEdit(self)
        self.pass2.move(275,390)
        self.pass2.resize(250,50)
        self.pass2.setFont(QFont("Consolas",18))
        self.pass2.setStyleSheet("""
            background-color: rgb(253,245,230);
            color: rgb(0,168,107);
            border-color: rgb(0,168,107);
            border-width: 3px;
            border-style: solid;
            border-radius: 15px;""")
        self.pass2.setAlignment(Qt.AlignmentFlag(20))
        
        
        btn = QPushButton("Register",self)
        btn.setGeometry(390,490,200,50)
        btn.setFont(QFont("Times New Roman",20))
        btn.setStyleSheet("""
            color: rgb(0,255,0);
            background-color: rgb(0,0,0);
            border-radius: 25px;
            border-width: 3px;
            border-style: inset;
            border-color: rgb(0,255,0);""")
        btn.clicked.connect(self.add_user)
    
    def add_user(self):
        file = open("Users.txt", "at+")
        if "@" in self.email.text():
            if self.rdb.isChecked() or self.rdb1.isChecked():
                if self.birth.text() > "17":
                    if self.pass1.text() == self.pass2.text():
                        if self.rdb.isChecked():
                            file.write(f"{self.name.text()}, {self.login.text()}, {self.email.text()}, {self.rdb.text()}, {self.birth.text()}, {self.pass1.text()}\n")
                            print("Joined")
                        elif self.rdb1.isChecked():
                            file.write(f"{self.name.text()}, {self.login.text()}, {self.email.text()}, {self.rdb1.text()}, {self.birth.text()}, {self.pass1.text()}\n")
                            print("Joined")
                    else:
                        print("Passwords aren't similar!")
                else:
                    print("You're under 18 years old!")
            else:
                print("Choose the gender!")
        else:
            print("Please enter the real email with @ !")

app = QApplication(sys.argv)
ilova = project()
ilova.show()
sys.exit(app.exec())
