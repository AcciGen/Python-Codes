import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys
import mysql.connector as myc

class project(QTabWidget):
    def __init__(self,parent = None):
        super(project,self).__init__(parent)
        
        self.setMinimumSize(1920,1050)
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
        self.setCurrentIndex(2)
        self.update_tab()
        self.insert_tab()
        self.delete_tab()
        self.show_tab()
        self.table = QTableWidget(self.insert)
        self.table.setVisible(False)
        self.table_update = QTableWidget(self.update)
        self.table_update.setVisible(False)
        self.show_table()
        self.show_table_update()
    def update_tab(self):
        self.lb1 = QLabel("Maydonni tanlang: ",self.update)
        self.lb1.setFont(QFont("Poor Richard",24))
        self.lb1.setGeometry(50,40,300,50)
        self.lb1.setStyleSheet("color: rgb(0,0,255);")
        
        self.change_value = QComboBox(self.update)
        self.change_value.setFont(QFont("Poor Richard",24))
        self.change_value.setGeometry(360,40,300,50)
        self.change_value.setStyleSheet("""color: rgb(0,0,255);
            background-color: rgb(250,235,215);
            border-radius: 5px;
            border-width: 3px;
            border-style: solid;
            border-color: rgb(0,255,0);""")
        ls = ["Name","Rejisor","EX_date", "cinema_genre","count_actor", "Oscar_laureate"]
        self.change_value.addItems(ls)
        self.change_value.currentIndexChanged.connect(self.ishla_qani)
        
        self.lb2 = QLabel("IDni tanlang: ",self.update)
        self.lb2.setFont(QFont("Poor Richard",24))
        self.lb2.setGeometry(50,100,300,50)
        self.lb2.setStyleSheet("color: rgb(0,0,255);")
        
        self.change_id = QComboBox(self.update)
        self.change_id.setFont(QFont("Poor Richard",24))
        self.change_id.setGeometry(360,100,100,50)
        self.change_id.setStyleSheet("""color: rgb(0,0,255);
            background-color: rgb(250,235,215);
            border-radius: 5px;
            border-width: 3px;
            border-style: solid;
            border-color: rgb(0,255,0);""")
        ls = []
        con = myc.connect(user = 'root',password = '1551734',host = 'localhost',database ="Cinema")
        kursor = con.cursor()
        kursor.execute("SELECT id from kino")
        res = kursor.fetchall()
        for x in res:
            ls.append(str(x[0]))
        self.change_id.addItems(ls)
        
        self.lb89 = QLabel(f"{self.change_value.currentText()}ni kiriting: ",self.update)
        self.lb89.setFont(QFont("Poor Richard",24))
        self.lb89.setGeometry(900,40,400,50)
        self.lb89.setStyleSheet("color: rgb(0,0,255);")
        
        self.change_val = QLineEdit(self.update)
        self.change_val.setFont(QFont("Poor Richard",24))
        self.change_val.setGeometry(1310,40,300,50)
        self.change_val.setStyleSheet("""color: rgb(0,0,255);
            background-color: rgb(250,235,215);
            border-radius: 15px;
            border-width: 3px;
            border-style: solid;
            border-color: rgb(0,255,0);""")
        self.change_val.setAlignment(Qt.AlignmentFlag(20)) 
        
        self.update_btn = QPushButton("Update cinema",self.update)
        self.update_btn.setFont(QFont("Poor Richard",24))
        self.update_btn.setGeometry(1310,100,300,50)
        self.update_btn.setStyleSheet("""color: rgb(0,0,255);
            background-color: rgb(128,128,128);
            border-radius: 15px;
            border-width: 3px;
            border-style: solid;
            border-color: rgb(0,255,0);""")
        self.update_btn.clicked.connect(self.update_data) 

        
    def add_databases(self,database = 'Cinema'):
        con = myc.connect(user = 'root',password = '1551734',host = 'localhost')
        kursor = con.cursor()
        kursor.execute(f"Create database if not exists {database}")
        
    def add_table(self,database ='Cinema',table = 'kino'):
        con = myc.connect(user = 'root',password = '1551734',host = 'localhost',database =f"{database}")
        kursor = con.cursor()
        kursor.execute(f"""Create table if not exists {table} 
                    (id int primary key auto_increment,
                    name varchar(30),rejisor varchar(30),
                    EX_date  date, cinema_genre varchar(30),
                    count_actor int, Oscar_laureate bool);""")
        
    def insert_tab(self):
        #self.insert.setStyleSheet("background-color: rgb(255,153,153);")
        
        self.lb = QLabel("Kino nomi: ",self.insert)
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

        self.lb1 = QLabel("Kino rejissori: ",self.insert)
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

        self.lb3 = QLabel("Kino janri: ",self.insert)
        self.lb3.setFont(QFont("Poor Richard",24))
        self.lb3.setGeometry(800,160,250,50)
        self.lb3.setStyleSheet("color: rgb(0,0,255);")
        
        self.cinema_type = QComboBox(self.insert)
        self.cinema_type.setFont(QFont("Poor Richard",24))
        self.cinema_type.setGeometry(1060,160,250,50)
        self.cinema_type.setStyleSheet("""color: rgb(0,0,255);
            background-color: rgb(250,235,215);
            border-radius: 5px;
            border-width: 3px;
            border-style: solid;
            border-color: rgb(0,255,0);""")
        ls = ["Komediya","Fantastik","Drama","Romantik","Detektiv","Hujjatli","Jangari"]
        self.cinema_type.addItems(ls)
        
        self.lb4 = QLabel("Aktyorlar soni: ",self.insert)
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

        self.lb5 = QLabel("Oscar yutganmi: ",self.insert)
        self.lb5.setFont(QFont("Poor Richard",24))
        self.lb5.setGeometry(800,220,250,50)
        self.lb5.setStyleSheet("color: rgb(0,0,255);")
        
        self.rdb = QRadioButton("Ha",self.insert)
        self.rdb.setGeometry(1060,220,100,50)
        self.rdb.setStyleSheet("color: rgb(0,0,255);")
        self.rdb.setFont(QFont("Poor Richard",24))
        
        self.rdb1 = QRadioButton("Yo'q",self.insert)
        self.rdb1.setGeometry(1200,220,100,50)
        self.rdb1.setStyleSheet("color: rgb(0,0,255);")
        self.rdb1.setFont(QFont("Poor Richard",24))
        
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
    
    def delete_data(self):
        con = myc.connect(user = 'root',password = '1551734',host = 'localhost',database ="Cinema")
        kursor = con.cursor()
        sql = f"""Delete from kino 
                where '{self.del_id.currentText} = {self.del_val.text()}"""
        kursor.execute(sql)
        con.commit()
        os.system("cls")
        print("Bazadan o'chdi")
        self.show_table_delete()
    
    def show_table_delete(self):
        self.table_update.setVisible(True)
        self.table_update.setGeometry(100,350,1600,600)
        self.table_update.setFont(QFont("Poor Richard",20))
        con = myc.connect(user = 'root',password = '1551734',host = 'localhost',database ="cinema")
        kursor = con.cursor()
        kursor.execute("Select * from kino")
        res = kursor.fetchall()
        rw_c = len(res)
        cl_c = 7
        
        self.table_update.setRowCount(rw_c)
        self.table_update.setColumnCount(cl_c)
        self.table_update.horizontalHeader().setFont(QFont("Poor Richard",20))
        ls = ["ID: ","Name ","Rejissor","Expration date","Genre ","Count actors","Oscar Laureate"]
        self.table_update.setHorizontalHeaderLabels(ls)
        st = ","*rw_c
        self.table_update.setVerticalHeaderLabels(st.split(","))
        sch = 0
        header = self.table_update.horizontalHeader()
        # for x in range(7):
            # header.setSectionResizeMode(x,QHeaderView.ResizeToContents)
        for x in res:
            self.table_update.setItem(sch,0,QTableWidgetItem(str(x[0])))
            self.table_update.setItem(sch,1,QTableWidgetItem(x[1]))
            self.table_update.setItem(sch,2,QTableWidgetItem(x[2]))
            self.table_update.setItem(sch,3,QTableWidgetItem(str(x[3])))
            self.table_update.setItem(sch,4,QTableWidgetItem(x[4]))
            self.table_update.setItem(sch,5,QTableWidgetItem(str(x[5])))
            if x[6]:
                self.table_update.setItem(sch,6,QTableWidgetItem("True"))
            else:
                self.table_update.setItem(sch,6,QTableWidgetItem("False"))
            sch += 1
    
    def show_table(self):
        self.table.setVisible(True)
        self.table.setGeometry(100,350,1600,600)
        self.table.setFont(QFont("Poor Richard",20))
        con = myc.connect(user = 'root',password = '1551734',host = 'localhost',database ="cinema")
        kursor = con.cursor()
        kursor.execute("Select * from kino")
        res = kursor.fetchall()
        rw_c = len(res)
        cl_c = 7
        
        self.table.setRowCount(rw_c)
        self.table.setColumnCount(cl_c)
        self.table.horizontalHeader().setFont(QFont("Poor Richard",20))
        ls = ["ID: ","Name ","Rejissor","Expration date","Genre ","Count actors","Oscar Laureate"]
        self.table.setHorizontalHeaderLabels(ls)
        st = ","*rw_c
        self.table.setVerticalHeaderLabels(st.split(","))
        sch = 0
        header = self.table.horizontalHeader()
        # for x in range(7):
            # header.setSectionResizeMode(x,QHeaderView.ResizeToContents)
        for x in res:
            self.table.setItem(sch,0,QTableWidgetItem(str(x[0])))
            self.table.setItem(sch,1,QTableWidgetItem(x[1]))
            self.table.setItem(sch,2,QTableWidgetItem(x[2]))
            self.table.setItem(sch,3,QTableWidgetItem(str(x[3])))
            self.table.setItem(sch,4,QTableWidgetItem(x[4]))
            self.table.setItem(sch,5,QTableWidgetItem(str(x[5])))
            if x[6]:
                self.table.setItem(sch,6,QTableWidgetItem("True"))
            else:
                self.table.setItem(sch,6,QTableWidgetItem("False"))
            sch += 1
            
            
    def show_table_update(self):
        self.table_update.setVisible(True)
        self.table_update.setGeometry(100,350,1600,600)
        self.table_update.setFont(QFont("Poor Richard",20))
        con = myc.connect(user = 'root',password = '1551734',host = 'localhost',database ="cinema")
        kursor = con.cursor()
        kursor.execute("Select * from kino")
        res = kursor.fetchall()
        rw_c = len(res)
        cl_c = 7
        
        self.table_update.setRowCount(rw_c)
        self.table_update.setColumnCount(cl_c)
        self.table_update.horizontalHeader().setFont(QFont("Poor Richard",20))
        ls = ["ID: ","Name ","Rejissor","Expration date","Genre ","Count actors","Oscar Laureate"]
        self.table_update.setHorizontalHeaderLabels(ls)
        st = ","*rw_c
        self.table_update.setVerticalHeaderLabels(st.split(","))
        sch = 0
        header = self.table_update.horizontalHeader()
        # for x in range(7):
            # header.setSectionResizeMode(x,QHeaderView.ResizeToContents)
        for x in res:
            self.table_update.setItem(sch,0,QTableWidgetItem(str(x[0])))
            self.table_update.setItem(sch,1,QTableWidgetItem(x[1]))
            self.table_update.setItem(sch,2,QTableWidgetItem(x[2]))
            self.table_update.setItem(sch,3,QTableWidgetItem(str(x[3])))
            self.table_update.setItem(sch,4,QTableWidgetItem(x[4]))
            self.table_update.setItem(sch,5,QTableWidgetItem(str(x[5])))
            if x[6]:
                self.table_update.setItem(sch,6,QTableWidgetItem("True"))
            else:
                self.table_update.setItem(sch,6,QTableWidgetItem("False"))
            sch += 1    
            
            
            
            
        
        
    def ishla_qani(self):
        self.lb89.setText(f"{self.change_value.currentText()}ni kiriting: ")  
        
    
    def delete_tab(self):
        self.del_id = QComboBox(self.delete)
        self.del_id.setFont(QFont("Poor Richard",24))
        self.del_id.setGeometry(360,100,100,50)
        self.del_id.setStyleSheet("""color: rgb(0,0,255);
            background-color: rgb(250,235,215);
            border-radius: 5px;
            border-width: 3px;
            border-style: solid;
            border-color: rgb(0,255,0);""")
        ls = ["ID", "Name", "Rejisor", "EX_date", "Cinema_Genre", "count_actor", "oscar_laureate"]
        self.del_id.addItems(ls)

        self.lbdel = QLabel(f"{self.del_id.currentText()}ni kiriting: ",self.delete)
        self.lbdel.setFont(QFont("Poor Richard",24))
        self.lbdel.setGeometry(700,100,300,50)
        self.lbdel.setStyleSheet("color: rgb(0,0,255);")
        
        self.del_val = QLineEdit(self.delete)
        self.del_val.setFont(QFont("Poor Richard",24))
        self.del_val.setGeometry(900,100,300,50)
        self.del_val.setStyleSheet("""color: rgb(0,0,255);
            background-color: rgb(250,235,215);
            border-radius: 15px;
            border-width: 3px;
            border-style: solid;
            border-color: rgb(0,255,0);""")
        self.del_val.setAlignment(Qt.AlignmentFlag(20)) 
        
        self.del_btn = QPushButton("Delete cinema",self.delete)
        self.del_btn.setFont(QFont("Poor Richard",24))
        self.del_btn.setGeometry(600,200,600,60)
        self.del_btn.setStyleSheet("""color: rgb(0,0,255);
            background-color: rgb(128,128,128);
            border-radius: 15px;
            border-width: 3px;
            border-style: solid;
            border-color: rgb(0,255,0);""")
        self.del_btn.clicked.connect(self.delete_data)

        
    def show_tab(self):
        self.show_d.setStyleSheet("background-color: rgb(255,228,205);")
        
        
        
    
    def insert_data(self):
        
        self.add_databases()
        self.add_table()
        con = myc.connect(user = 'root',password = '1551734',host = 'localhost',database ="Cinema")
        kursor = con.cursor()
        sql=("Insert into kino (name,rejisor,EX_date, cinema_genre,count_actor, Oscar_laureate) Values (%s,%s,%s,%s,%s,%s);")
        name = self.name.text()
        author= self.author.text()
        ex_date = self.ex_date.text()
        janr = self.cinema_type.currentText()
        count_d = int(self.count_d.text())
        if self.rdb.isChecked() == True:
            res = True
        else:
            res = False
        value = (name,author,ex_date,janr,count_d,res)
        kursor.execute(sql,value)
        con.commit()
        self.name.clear()
        self.author.clear()
        self.ex_date.clear()
        self.count_d.clear()
        self.show_table()
        os.system("cls")
        print("Ma'lumot qo'shildi")
    
    def update_data(self):
        con = myc.connect(user = 'root',password = '1551734',host = 'localhost',database ="Cinema")
        kursor = con.cursor()
        sql = f"""Update kino set {self.change_value.currentText()} = "{self.change_val.text()}" 
        where id = {self.change_id.currentText()}"""
        kursor.execute(sql)
        con.commit()
        os.system("cls")
        print("Baza o'zgardi")
        self.show_table_update()
app = QApplication(sys.argv)
ilova= project()
ilova.show()
sys.exit(app.exec())