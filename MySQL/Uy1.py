import os
import mysql.connector as mys
os.system("cls")

# 1
def createDatabase(newDatabase = "Computers"):
    connect = mys.connect(user = "root", password = "1551734", host = "localhost")
    cur = connect.cursor()
    cur.execute(f"Create database if not exists {newDatabase}")
    if cur:
        print(f"{newDatabase} database created successfully!")

def createTable(newDatabase = "Computers", newTable = "Laptops"):
    connect = mys.connect(user = "root", password = "1551734", host = "localhost", database = f"{newDatabase}")
    cur = connect.cursor()
    cur.execute(f"Create table if not exists {newTable}(id int primary key auto_increment, name varchar(35), style varchar(35), processor varchar(25), ram varchar(12), videoCard varchar(25), price int)")
    connect.commit()
    print(f"{newTable} table created successfully!")

def inputData(newDatabase = "Computers", newTable = "Laptops"):
    connect = mys.connect(user = "root", password = "1551734", host = "localhost", database = f"{newDatabase}")
    cur = connect.cursor()
    sql = f"insert into {newTable}(name, style, processor, ram, videoCard, price) Values (%s, %s, %s, %s, %s, %s)"
    value1 = ("MSI Stealth 17 Studio", "Gaming Laptop", "Intel® Core™ i9-13900H", "64GB DDR5", "GeForce RTX™ 4080 NVIDIA®", "2999")
    value2 = ("Lenovo IdeaPad 5 PRO", "Office Laptop", "Intel® Core™ i5-11300H", "8GB DDR4", "GeForce MX450 NVIDIA®", "750")
    value3 = ("Asus ZenBook 14 DUO OLED", "Ultra Laptop", "Intel® Core™ i7-13700H", "16GB DDR5", "GeForce RTX™ 4050 NVIDIA®", "2100")
    value4 = ("Lenovo LOQ 16", "Gaming Laptop", "Intel® Core™ i5-13420H", "32GB DDR5", "GeForce RTX™ 4050 NVIDIA®", "900")
    value5 = ("HP Pavilion 15 Gold", "Office Laptop", "AMD Ryzen™ 3-5300U", "8GB DDR4", "AMD® Radeon Graphics", "450")
    cur.execute(sql, value1)
    cur.execute(sql, value2)
    cur.execute(sql, value3)
    cur.execute(sql, value4)
    cur.execute(sql, value5)
    connect.commit()
    print("New data added successfully!")

def showData(newDatabase = "Computers", newTable = "Laptops"):
    connect = mys.connect(user = "root", password = "1551734", host = "localhost", database = f"{newDatabase}")
    cur = connect.cursor()
    cur.execute(f"Select * from {newTable} order by price asc;")
    res = cur.fetchall()
    for x in res:
        print(f"Id >>           {x[0]}")
        print(f"Name >>         {x[1]}")
        print(f"Style >>        {x[2]}")
        print(f"Processor >>    {x[3]}")
        print(f"Ram >>          {x[4]}")
        print(f"Video Card >>   {x[5]}")
        print(f"Price >>        {x[6]}")
        print("\n")

# createDatabase()
# createTable()
# inputData()
showData()



# 2
# def createDatabase(newDatabase = "Phones"):
#     connect = mys.connect(user = "root", password = "1551734", host = "localhost")
#     cur = connect.cursor()
#     cur.execute(f"Create database if not exists {newDatabase}")
#     if cur:
#         print(f"{newDatabase} database created successfully!")

# def createTable(newDatabase = "Phones", newTable = "Types"):
#     connect = mys.connect(user = "root", password = "1551734", host = "localhost", database = f"{newDatabase}")
#     cur = connect.cursor()
#     cur.execute(f"Create table if not exists {newTable}(id int primary key auto_increment, name varchar(40), processor varchar(40), memory varchar(8), price int)")
#     connect.commit()
#     print(f"{newTable} table created successfully!")

# def inputData(newDatabase = "Phones", newTable = "Types"):
#     connect = mys.connect(user = "root", password = "1551734", host = "localhost", database = f"{newDatabase}")
#     cur = connect.cursor()
#     sql = f"insert into {newTable}(name, processor, memory, price) Values (%s, %s, %s, %s)"
#     value1 = ("Apple Iphone 15 Pro Max", "A17 Pro", "1TB", "36000000")
#     value2 = ("Xiaomi Redmi Note 10 Pro", "Qualcomm Snapdragon 732G", "128GB", "3680000")
#     value3 = ("Samsung Galaxy Z Fold 2", "Qualcomm Snapdragon 865+", "256GB", "14230000")
#     value4 = ("Samsung Galaxy S20 FE", "Exynos 990", "128GB", "6800000")
#     value5 = ("Oppo A52", "Qualcomm Snapdragon 665", "64GB", "1850000")
#     cur.execute(sql, value1)
#     cur.execute(sql, value2)
#     cur.execute(sql, value3)
#     cur.execute(sql, value4)
#     cur.execute(sql, value5)
#     connect.commit()
#     print("New data added successfully!")

# def showData(newDatabase = "Phones", newTable = "Types"):
#     connect = mys.connect(user = "root", password = "1551734", host = "localhost", database = f"{newDatabase}")
#     cur = connect.cursor()
#     cur.execute(f"Select * from {newTable} order by price desc;")
#     res = cur.fetchall()
#     for x in res:
#         print(f"Id >>           {x[0]}")
#         print(f"Name >>         {x[1]}")
#         print(f"Processor >>    {x[2]}")
#         print(f"Ram >>          {x[3]}")
#         print(f"Price >>        {x[4]}")
#         print("\n")

# createDatabase()
# createTable()
# inputData()
# showData()