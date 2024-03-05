import os
import mysql.connector as my
os.system("cls")


#1
class myDB:
    def __init__(self, database):
        self.con = my.connect(user = 'root', password = '1551734', host = 'localhost')
        self.curs = self.con.cursor()
        self.curs.execute(f"CREATE database if not exists {database}")
    
    def table(self, database, table):
        self.con = my.connect(user = "root", password = "1551734", host = "localhost", database = f"{database}")
        self.curs = self.con.cursor()
        self.curs.execute(f"CREATE table if not exists {table}(id int primary key auto_increment, name varchar(30), course int, studentship int)")
        self.con.commit()

    def inputData(self, database, table):
        self.con = my.connect(user = "root", password = "1551734", host = "localhost", database = f"{database}")
        self.curs = self.con.cursor()
        sql = f"INSERT into {table}(name, course, studentship) Values (%s, %s, %s)"
        value1 = ("John", 2, 3500)
        value2 = ("Davron", 1, 2000)
        value3 = ("Mike", 3, 3500)
        value4 = ("Katie", 3, 3500)
        value5 = ("Tony", 4, 4000)
        value6 = ("Ibrohim", 1, 2000)
        value7 = ("Anvar", 3, 2000)
        value8 = ("Pak", 2, 4000)
        value9 = ("Park", 3, 3500)
        value10 = ("Durdona", 2, 2500)
        self.curs.execute(sql, value1)
        self.curs.execute(sql, value2)
        self.curs.execute(sql, value3)
        self.curs.execute(sql, value4)
        self.curs.execute(sql, value5)
        self.curs.execute(sql, value6)
        self.curs.execute(sql, value7)
        self.curs.execute(sql, value8)
        self.curs.execute(sql, value9)
        self.curs.execute(sql, value10)
        self.con.commit()
    
    def showData(self, database, table):
        self.con = my.connect(user = "root", password = "1551734", host = "localhost", database = f"{database}")
        self.curs = self.con.cursor()
        self.curs.execute(f"SELECT SUM(studentship) as 'studentshipSum' FROM {table} WHERE course = 2;")
        result = self.curs.fetchall()
        for x in result:
            print(f"Sum >>  {x[0]}\n")

        self.curs.execute(f"SELECT name, course, studentship FROM {table} WHERE LENGTH(name) < 5 order by course desc;")
        result = self.curs.fetchall()
        for x in result:
            print(f"Name >>         {x[0]}")
            print(f"Course >>       {x[1]}")
            print(f"Studentship >>  {x[2]}")
            print("\n----------------------\n")


University = myDB('maktab')
University.table('maktab', 'student')
University.inputData('maktab', 'student')
University.showData('maktab', 'student')



#2
# class myDB:
#     def __init__(self, database):
#         self.con = my.connect(user = 'root', password = '1551734', host = 'localhost')
#         self.curs = self.con.cursor()
#         self.curs.execute(f"CREATE database if not exists {database}")
    
#     def table(self, database, table):
#         self.con = my.connect(user = "root", password = "1551734", host = "localhost", database = f"{database}")
#         self.curs = self.con.cursor()
#         self.curs.execute(f"CREATE table if not exists {table}(id int primary key auto_increment, name varchar(30), birth date, points int)")
#         self.con.commit()

#     def inputData(self, database, table):
#         self.con = my.connect(user = "root", password = "1551734", host = "localhost", database = f"{database}")
#         self.curs = self.con.cursor()
#         sql = f"INSERT into {table}(name, birth, points) Values (%s, %s, %s)"
#         value1 = ("John", "2002-12-14", 4)
#         value2 = ("Davron", "2001-01-31", 5)
#         value3 = ("Mike", "2000-05-27", 2)
#         value4 = ("Katie", "2004-07-14", 4)
#         value5 = ("Tony", "2001-03-17", 4)
#         value6 = ("Ibrohim", "2004-12-31", 5)
#         value7 = ("Anvar", "2002-06-05", 2)
#         value8 = ("Pak", "2003-04-13", 5)
#         value9 = ("Park", "2004-12-24", 3)
#         value10 = ("Durdona", "2001-02-25", 2)
#         self.curs.execute(sql, value1)
#         self.curs.execute(sql, value2)
#         self.curs.execute(sql, value3)
#         self.curs.execute(sql, value4)
#         self.curs.execute(sql, value5)
#         self.curs.execute(sql, value6)
#         self.curs.execute(sql, value7)
#         self.curs.execute(sql, value8)
#         self.curs.execute(sql, value9)
#         self.curs.execute(sql, value10)
#         self.con.commit()
    
#     def showData(self, database, table):
#         self.con = my.connect(user = "root", password = "1551734", host = "localhost", database = f"{database}")
#         self.curs = self.con.cursor()
#         self.curs.execute(f"SELECT * FROM {table} WHERE MONTH(birth) in (12, 1, 2);")
#         result = self.curs.fetchall()
#         for x in result:
#             print(f"ID >>       {x[0]}")
#             print(f"Name >>     {x[1]}")
#             print(f"Birth >>    {x[2]}")
#             print(f"Points >>   {x[3]}")
#             print("\n----------------------\n")

#         self.curs.execute(f"DELETE FROM {table} WHERE points = 2;")
#         self.curs.execute(f"SELECT * FROM {table}")
#         result = self.curs.fetchall()
#         print("\nStudents with points 2 were deleted!\n")
#         for x in result:
#             print(f"ID >>       {x[0]}")
#             print(f"Name >>     {x[1]}")
#             print(f"Birth >>    {x[2]}")
#             print(f"Points >>   {x[3]}")
#             print("\n----------------------\n")


# University = myDB('maktab')
# University.table('maktab', 'student')
# University.inputData('maktab', 'student')
# University.showData('maktab', 'student')



#3
# class myDB:
#     def __init__(self, database):
#         self.con = my.connect(user = 'root', password = '1551734', host = 'localhost')
#         self.curs = self.con.cursor()
#         self.curs.execute(f"CREATE database if not exists {database}")
    
#     def table(self, database, table):
#         self.con = my.connect(user = "root", password = "1551734", host = "localhost", database = f"{database}")
#         self.curs = self.con.cursor()
#         self.curs.execute(f"CREATE table if not exists {table}(id int primary key auto_increment, model varchar(40), processor varchar(30), ram int, monitorFreq int, videoCard bool, price int);")
#         self.con.commit()

#     def inputData(self, database, table):
#         self.con = my.connect(user = "root", password = "1551734", host = "localhost", database = f"{database}")
#         self.curs = self.con.cursor()
#         sql = f"INSERT into {table}(model, processor, ram, monitorFreq, videoCard, price) Values (%s, %s, %s, %s, %s, %s)"
#         value1 = ("MSI Stealth 17 Studio", "Intel® Core™ i9-13900H", 32, 240, 1, 2999)
#         value2 = ("Lenovo IdeaPad 5 PRO", "Intel® Core™ i5-11300H", 16, 60, 0, 850)
#         value3 = ("Asus ZenBook 14X OLED", "Intel® Core™ i7-13700H", 16, 60, 0, 900)
#         value4 = ("MSI Crosshair 15", "Intel® Core™ i7-12700H", 16, 144, 1, 1400)
#         value5 = ("HP Pavilion 15 Gold", "AMD® Ryzen™ 3-5300U", 8, 60, 0, 420)
#         value6 = ("Asus VivoBook 16", "AMD® Ryzen™ 5-7530U", 8, 60, 0, 500)
#         value7 = ("Asus Rog Strix Scar G733", "AMD® Ryzen™ 9-7945HX", 32, 240, 1, 3100)
#         value8 = ("Lenovo LOQ 16", "Intel® Core™ i5-13420H", 16, 165, 1, 900)
#         value9 = ("Dell Alienware M18", "AMD® Ryzen™ 7-7745HX", 16, 165, 1, 1700)
#         value10 = ("Acer Predator Helios 18", "Intel® Core™ i7-13700HX", 16, 165, 1, 1650)
#         self.curs.execute(sql, value1)
#         self.curs.execute(sql, value2)
#         self.curs.execute(sql, value3)
#         self.curs.execute(sql, value4)
#         self.curs.execute(sql, value5)
#         self.curs.execute(sql, value6)
#         self.curs.execute(sql, value7)
#         self.curs.execute(sql, value8)
#         self.curs.execute(sql, value9)
#         self.curs.execute(sql, value10)
#         self.con.commit()
    
#     def showData(self, database, table):
#         self.con = my.connect(user = "root", password = "1551734", host = "localhost", database = f"{database}")
#         self.curs = self.con.cursor()
#         self.curs.execute(f"SELECT * FROM {table} WHERE videoCard = 1;")
#         result = self.curs.fetchall()
#         for x in result:
#             print(f"ID >>               {x[0]}")
#             print(f"Model >>            {x[1]}")
#             print(f"Processor >>        {x[2]}")
#             print(f"Ram >>              {x[3]}")
#             print(f"Monitor Freq >>     {x[4]}")
#             print(f"Video Card >>       {x[5]}")
#             print(f"Price >>            {x[6]}")
#             print("\n----------------------\n")

#         self.curs.execute(f"UPDATE {table} set model = 'Dell' WHERE price > 1000 and model like 'A%';")
#         self.curs.execute(f"SELECT * from laptop;")
#         result = self.curs.fetchall()
#         print("\n\nSecond Change!\n")
#         for x in result:
#             print(f"ID >>               {x[0]}")
#             print(f"Model >>            {x[1]}")
#             print(f"Processor >>        {x[2]}")
#             print(f"Ram >>              {x[3]}")
#             print(f"Monitor Freq >>     {x[4]}")
#             print(f"Video Card >>       {x[5]}")
#             print(f"Price >>            {x[6]}")
#             print("\n----------------------\n")

# PC = myDB('pc')
# PC.table('pc', 'laptop')
# PC.inputData('pc', 'laptop')
# PC.showData('pc', 'laptop')



#4
# class myDB:
#     def __init__(self, database):
#         self.con = my.connect(user = 'root', password = '1551734', host = 'localhost')
#         self.curs = self.con.cursor()
#         self.curs.execute(f"CREATE database if not exists {database}")
    
#     def table(self, database, table):
#         self.con = my.connect(user = "root", password = "1551734", host = "localhost", database = f"{database}")
#         self.curs = self.con.cursor()
#         self.curs.execute(f"CREATE table if not exists {table}(id int primary key auto_increment, name varchar(30), birth date, points int)")
#         self.con.commit()

#     def inputData(self, database, table):
#         self.con = my.connect(user = "root", password = "1551734", host = "localhost", database = f"{database}")
#         self.curs = self.con.cursor()
#         sql = f"INSERT into {table}(name, birth, points) Values (%s, %s, %s)"
#         value1 = ("John", "2002-02-14", 4)
#         value2 = ("Tony", "2001-01-31", 5)
#         value3 = ("Mike", "2000-05-27", 3)
#         value4 = ("Katie", "2004-07-14", 4)
#         value5 = ("Tony", "2001-02-21", 4)
#         value6 = ("Ibrohim", "2004-12-31", 5)
#         value7 = ("John", "2002-06-05", 3)
#         value8 = ("Pak", "2003-04-13", 5)
#         value9 = ("Pak", "2004-12-24", 5)
#         value10 = ("Katie", "2001-02-25", 4)
#         self.curs.execute(sql, value1)
#         self.curs.execute(sql, value2)
#         self.curs.execute(sql, value3)
#         self.curs.execute(sql, value4)
#         self.curs.execute(sql, value5)
#         self.curs.execute(sql, value6)
#         self.curs.execute(sql, value7)
#         self.curs.execute(sql, value8)
#         self.curs.execute(sql, value9)
#         self.curs.execute(sql, value10)
#         self.con.commit()
    
#     def showData(self, database, table):
#         self.con = my.connect(user = "root", password = "1551734", host = "localhost", database = f"{database}")
#         self.curs = self.con.cursor()
#         self.curs.execute(f"SELECT name, COUNT(*) FROM {table} GROUP BY name HAVING COUNT(*) > 1;")
#         result = self.curs.fetchall()
#         for x in result:
#             print(f"Name >>         {x[0]}")
#             print(f"Similarities >> {x[1]}")
#             print("\n----------------------\n")

#         self.curs.execute(f"UPDATE {table} set points = 5 WHERE points = 4 and MONTH(birth) in (2)")
#         print("\n\nStudents with points 4 were changed to 5!\n")
#         self.curs.execute(f"SELECT * FROM {table}")
#         result = self.curs.fetchall()
#         for x in result:
#             print(f"ID >>       {x[0]}")
#             print(f"Name >>     {x[1]}")
#             print(f"Birth >>    {x[2]}")
#             print(f"Points >>   {x[3]}")
#             print("\n----------------------\n")

# University = myDB('maktab')
# University.table('maktab', 'student')
# University.inputData('maktab', 'student')
# University.showData('maktab', 'student')