import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys
import mysql.connector as myc

class project(QTabWidget):
    def __init__(self,parent = None):
        super(project,self).__init__(parent)
        self.con = myc.connect(user = 'root',password = '1551734',host = 'localhost')
        self.kursor = self.con.cursor()

        self.setMinimumSize(1520,800)
        self.setMaximumSize(1920,1050)
        
        self.setFont(QFont("Poor Richard",24))
        
        self.insert = QWidget()
        self.update = QWidget()
        self.delete = QWidget()
        self.show_d =   QWidget()
        
        self.addTab(self.insert,"Insert data")
        self.addTab(self.update,"Update data")
        self.addTab(self.delete,"Delete data")
        self.addTab(self.show_d,"View data")
        
        self.insert_tab()
        self.update_tab()
        self.delete_tab()
        self.show_tab()
        self.table = QTableWidget(self.insert)
        self.table.setVisible(False)

    def update_tab(self):
        self.update.setStyleSheet("background-color: rgb(255,204,153); color: blue")

        con = myc.connect(user = 'root',password = '1551734',host = 'localhost',database = "music")
        kursor = con.cursor()

        self.lb = QLabel("Qo'shiqni eski nomi:",self.update)
        self.lb.setGeometry(50,100,250,50)
        self.lb.setStyleSheet("color: rgb(0,0,255);")
        
        self.name = QLineEdit(self.update)
        self.name.setGeometry(310,100,300,50)
        self.name.setStyleSheet("""color: rgb(0,0,255);
            background-color: rgb(250,235,215);
            border-radius: 15px;
            border-width: 3px;
            border-style: solid;
            border-color: rgb(0,255,0);""")
        self.name.setPlaceholderText("Song tugmani bosing")
        self.name.setAlignment(Qt.AlignmentFlag(20)) 

        self.lb1 = QLabel("Qo'shiq muallifi: ",self.update)
        self.lb1.setGeometry(800,100,250,50)
        self.lb1.setStyleSheet("color: rgb(0,0,255);")
        
        self.author = QLineEdit(self.update)
        self.author.setGeometry(1060,100,300,50)
        self.author.setStyleSheet("""color: rgb(0,0,255);
            background-color: rgb(250,235,215);
            border-radius: 15px;
            border-width: 3px;
            border-style: solid;
            border-color: rgb(0,255,0);""")
        self.author.setAlignment(Qt.AlignmentFlag(20))
        
        self.lb2 = QLabel("Yaratilgan vaqt: ",self.update)
        self.lb2.setGeometry(50,160,250,50)
        self.lb2.setStyleSheet("color: rgb(0,0,255);")
        
        self.ex_date = QLineEdit(self.update)
        self.ex_date.setGeometry(310,160,300,50)
        self.ex_date.setStyleSheet("""color: rgb(0,0,255);
            background-color: rgb(250,235,215);
            border-radius: 15px;
            border-width: 3px;
            border-style: solid;
            border-color: rgb(0,255,0);""")
        self.ex_date.setAlignment(Qt.AlignmentFlag(20)) 

        self.lb3 = QLabel("She'r muallifi: ",self.update)
        self.lb3.setGeometry(800,160,250,50)
        self.lb3.setStyleSheet("color: rgb(0,0,255);")
        
        self.poem_author = QLineEdit(self.update)
        self.poem_author.setGeometry(1060,160,300,50)
        self.poem_author.setStyleSheet("""color: rgb(0,0,255);
            background-color: rgb(250,235,215);
            border-radius: 15px;
            border-width: 3px;
            border-style: solid;
            border-color: rgb(0,255,0);""")
        self.poem_author.setAlignment(Qt.AlignmentFlag(20))
    
        self.lb4 = QLabel("Yuklashlar soni: ",self.update)
        self.lb4.setGeometry(50,220,250,50)
        self.lb4.setStyleSheet("color: rgb(0,0,255);")
        
        self.count_d = QLineEdit(self.update)
        self.count_d.setGeometry(310,220,300,50)
        self.count_d.setStyleSheet("""color: rgb(0,0,255);
            background-color: rgb(250,235,215);
            border-radius: 15px;
            border-width: 3px;
            border-style: solid;
            border-color: rgb(0,255,0);""")
        self.count_d.setAlignment(Qt.AlignmentFlag(20)) 

        self.lb5 = QLabel("Qo'shiq uzunligi: ",self.update)
        self.lb5.setGeometry(800,220,250,50)
        self.lb5.setStyleSheet("color: rgb(0,0,255);")
        
        self.duration = QLineEdit(self.update)
        self.duration.setGeometry(1060,220,300,50)
        self.duration.setStyleSheet("""color: rgb(0,0,255);
            background-color: rgb(250,235,215);
            border-radius: 15px;
            border-width: 3px;
            border-style: solid;
            border-color: rgb(0,255,0);""")
        self.duration.setAlignment(Qt.AlignmentFlag(20))
        
        self.takeBtn = QPushButton("Eski nomini olish", self.update)
        self.takeBtn.setGeometry(310,30,300,60)
        self.takeBtn.setStyleSheet("""
            background-color: rgb(0,0,0);
            border-radius: 15px;
            border-width: 3px;
            border-style: solid;
            border-color: rgb(0,255,0);
                """)
        
        self.update_btn = QPushButton("Update data",self.update)
        self.update_btn.setGeometry(1400,130,450,100)
        self.update_btn.setStyleSheet("""
            color: rgb(0,255,0);
            background-color: rgb(0,0,0);
            border-radius: 15px;
            border-width: 3px;
            border-style: solid;
            border-color: rgb(0,255,0);
                """)
        
        self.lbs = QLabel(self.update)
        self.lbs.setGeometry(100,400,250,50)
        self.lbs.setStyleSheet("color: rgb(0,0,255);")
        
        self.takeBtn.clicked.connect(self.takeName)
        self.update_btn.clicked.connect(self.upData)


    def takeName(self):
        self.oldName = self.name.text()
        self.name.clear()
        self.lb.setText("Qo'shiqni nomi:")
        self.name.setPlaceholderText("Yangi ma'lumot kiriting")

    def upData(self):
        con = myc.connect(user = 'root',password = '1551734',host = 'localhost', database = 'music')
        kursor = con.cursor()
        if self.author.text() != "" and self.ex_date.text() != "" and self.poem_author.text() != "" and self.count_d.text() != "" and self.duration.text() != "":
            kursor.execute(f"UPDATE music set name = '{self.name.text()}', author = '{self.author.text()}', ex_date = '{self.ex_date.text()}', poet = '{self.poem_author.text()}', count_download = '{self.count_d.text()}', duration = '{self.duration.text()}' where name = '{self.oldName}'")
            con.commit()
            self.name.clear()
            self.author.clear()
            self.ex_date.clear()
            self.poem_author.clear()
            self.count_d.clear()
            self.duration.clear()
            self.lbs.setText("Updated!")

    def add_databases(self,database = 'Music'):
        con = myc.connect(user = 'root',password = '1551734',host = 'localhost')
        kursor = con.cursor()
        kursor.execute(f"Create database if not exists {database}")
        
    def add_table(self,database ='Music',table = 'music'):
        con = myc.connect(user = 'root',password = '1551734',host = 'localhost',database =f"{database}")
        kursor = con.cursor()
        kursor.execute(f"""Create table if not exists {table} 
                    (id int primary key auto_increment,
                    name varchar(30),author varchar(30),
                    EX_date  date, poet varchar(30),
                    count_download int, duration time);""")
        con.commit()
        
    def insert_tab(self):
        #self.insert.setStyleSheet("background-color: rgb(255,153,153);")
        
        self.lb = QLabel("Qo'shiq nomi: ",self.insert)
        self.lb.setFont(QFont("Poor Richard",24))
        self.lb.setGeometry(50,100,250,50)
        self.lb.setStyleSheet("color: rgb(0,0,255);")
        
        self.name = QLineEdit(self.insert)
        self.name.setFont(QFont("Poor Richard",24))
        self.name.setGeometry(310,100,250,50)
        self.name.setStyleSheet("""color: rgb(0,0,255);
            background-color: rgb(250,235,215);
            border-radius: 15px;
            border-width: 3px;
            border-style: solid;
            border-color: rgb(0,255,0);""")
        self.name.setAlignment(Qt.AlignmentFlag(20)) 

        self.lb1 = QLabel("Qo'shiq muallifi: ",self.insert)
        self.lb1.setFont(QFont("Poor Richard",24))
        self.lb1.setGeometry(800,100,250,50)
        self.lb1.setStyleSheet("color: rgb(0,0,255);")
        
        self.author = QLineEdit(self.insert)
        self.author.setFont(QFont("Poor Richard",24))
        self.author.setGeometry(1060,100,250,50)
        self.author.setStyleSheet("""color: rgb(0,0,255);
            background-color: rgb(250,235,215);
            border-radius: 15px;
            border-width: 3px;
            border-style: solid;
            border-color: rgb(0,255,0);""")
        self.author.setAlignment(Qt.AlignmentFlag(20))
        
        self.lb2 = QLabel("Yaratilgan vaqt: ",self.insert)
        self.lb2.setFont(QFont("Poor Richard",24))
        self.lb2.setGeometry(50,160,250,50)
        self.lb2.setStyleSheet("color: rgb(0,0,255);")
        
        self.ex_date = QLineEdit(self.insert)
        self.ex_date.setFont(QFont("Poor Richard",24))
        self.ex_date.setGeometry(310,160,250,50)
        self.ex_date.setStyleSheet("""color: rgb(0,0,255);
            background-color: rgb(250,235,215);
            border-radius: 15px;
            border-width: 3px;
            border-style: solid;
            border-color: rgb(0,255,0);""")
        self.ex_date.setAlignment(Qt.AlignmentFlag(20)) 

        self.lb3 = QLabel("She'r muallifi: ",self.insert)
        self.lb3.setFont(QFont("Poor Richard",24))
        self.lb3.setGeometry(800,160,250,50)
        self.lb3.setStyleSheet("color: rgb(0,0,255);")
        
        self.poem_author = QLineEdit(self.insert)
        self.poem_author.setFont(QFont("Poor Richard",24))
        self.poem_author.setGeometry(1060,160,250,50)
        self.poem_author.setStyleSheet("""color: rgb(0,0,255);
            background-color: rgb(250,235,215);
            border-radius: 15px;
            border-width: 3px;
            border-style: solid;
            border-color: rgb(0,255,0);""")
        self.poem_author.setAlignment(Qt.AlignmentFlag(20))
    
        self.lb4 = QLabel("Yuklashlar soni: ",self.insert)
        self.lb4.setFont(QFont("Poor Richard",24))
        self.lb4.setGeometry(50,220,250,50)
        self.lb4.setStyleSheet("color: rgb(0,0,255);")
        
        self.count_d = QLineEdit(self.insert)
        self.count_d.setFont(QFont("Poor Richard",24))
        self.count_d.setGeometry(310,220,250,50)
        self.count_d.setStyleSheet("""color: rgb(0,0,255);
            background-color: rgb(250,235,215);
            border-radius: 15px;
            border-width: 3px;
            border-style: solid;
            border-color: rgb(0,255,0);""")
        self.count_d.setAlignment(Qt.AlignmentFlag(20)) 

        self.lb5 = QLabel("Qo'shiq uzunligi: ",self.insert)
        self.lb5.setFont(QFont("Poor Richard",24))
        self.lb5.setGeometry(800,220,250,50)
        self.lb5.setStyleSheet("color: rgb(0,0,255);")
        
        self.duration = QLineEdit(self.insert)
        self.duration.setFont(QFont("Poor Richard",24))
        self.duration.setGeometry(1060,220,250,50)
        self.duration.setStyleSheet("""color: rgb(0,0,255);
            background-color: rgb(250,235,215);
            border-radius: 15px;
            border-width: 3px;
            border-style: solid;
            border-color: rgb(0,255,0);""")
        self.duration.setAlignment(Qt.AlignmentFlag(20))
        
        self.insert_btn = QPushButton("Insert data",self.insert)
        self.insert_btn.setGeometry(1350,130,450,100)
        self.insert_btn.setFont(QFont("Poor Richard",42))
        self.insert_btn.setStyleSheet("""
            color: rgb(0,255,0);
            background-color: rgb(0,0,0);
            border-radius: 15px;
            border-width: 3px;
            border-style: solid;
            border-color: rgb(0,255,0);
                """)
        self.insert_btn.clicked.connect(self.insert_data)
    
    def show_table(self):
        self.table.setVisible(True)
        self.table.setGeometry(100,350,1600,600)
        self.table.setFont(QFont("Poor Richard",20))
        con = myc.connect(user = 'root',password = '1551734',host = 'localhost',database ="music")
        kursor = con.cursor()
        kursor.execute("Select * from music")
        res = kursor.fetchall()
        rw_c = len(res)
        cl_c = 7
        
        self.table.setRowCount(rw_c)
        self.table.setColumnCount(cl_c)
        self.table.horizontalHeader().setFont(QFont("Poor Richard",20))
        ls = ["ID: ","Name ","Author","Expration date","Poet ","Count downloads","Duration"]
        self.table.setHorizontalHeaderLabels(ls)
        st = ","*rw_c
        self.table.setVerticalHeaderLabels(st.split(","))
        sch = 0
        # header = self.table.horizontalHeader()
        # for x in range(7):
            # header.setSectionResizeMode(x,QHeaderView.ResizeToContents)
        for x in res:
            self.table.setItem(sch,0,QTableWidgetItem(str(x[0])))
            self.table.setItem(sch,1,QTableWidgetItem(x[1]))
            self.table.setItem(sch,2,QTableWidgetItem(x[2]))
            self.table.setItem(sch,3,QTableWidgetItem(str(x[3])))
            self.table.setItem(sch,4,QTableWidgetItem(x[4]))
            self.table.setItem(sch,5,QTableWidgetItem(str(x[5])))
            self.table.setItem(sch,6,QTableWidgetItem(str(x[6])))
            sch += 1

    def delete_tab(self):
        con = myc.connect(user = 'root',password = '1551734',host = 'localhost',database = "music")
        kursor = con.cursor()
        self.delete.setStyleSheet("background: black; color: lime;")

        self.ln = QLineEdit(self.delete)
        self.ln.setPlaceholderText("Qo'shiq nomini yozing")
        self.ln.setStyleSheet("border-radius: 15px; border-width: 3px; border-style: solid; border-color: lime")
        self.ln.setGeometry(200, 100, 400, 60)

        self.btn = QPushButton("Click To Delete", self.delete)
        self.btn.setStyleSheet("border-radius: 15px; border-width: 3px; border-style: solid; border-color: lime")
        self.btn.setGeometry(200, 300, 300, 80)
        self.btn.clicked.connect(self.check)

        self.lbd = QLabel(self.delete)
        self.lbd.setGeometry(200, 500, 300, 60)

    def check(self):
        con = myc.connect(user = 'root',password = '1551734',host = 'localhost',database = "music")
        kursor = con.cursor()
        name = self.ln.text()
        kursor.execute(f"Delete from music where name = '{name}'")
        con.commit()
        self.lbd.setText("Deleted Successfully!")
        self.ln.clear()

    def show_tab(self):
        self.show_d.setStyleSheet("background-color: rgb(255,228,205);")
        

    def insert_data(self):
        
        self.add_databases()
        self.add_table()
        con = myc.connect(user = 'root',password = '1551734',host = 'localhost',database ="music")
        kursor = con.cursor()
        sql=("Insert into music (name,author,EX_date,poet,count_download,duration) Values (%s,%s,%s,%s,%s,%s);")
        name = self.name.text()
        author= self.author.text()
        ex_date = self.ex_date.text()
        poet = self.poem_author.text()
        count_d = int(self.count_d.text())
        duration = self.duration.text()
        value = (name,author,ex_date,poet,count_d,duration)
        kursor.execute(sql,value)
        con.commit()
        self.name.clear()
        self.author.clear()
        self.ex_date.clear()
        self.poem_author.clear()
        self.count_d.clear()
        self.duration.clear()
        self.show_table()
        os.system("cls")
        print("Ma'lumot qo'shildi")

        
app = QApplication(sys.argv)
ilova= project()
ilova.show()
sys.exit(app.exec())