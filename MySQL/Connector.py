import os
import mysql.connector as myc
os.system("cls")

def create_database(database_home):
    connect = myc.connect(user = "root", password = "1551734", host = "localhost")
    kursor = connect.cursor()
    kursor.execute(f"Create database if not exists {database_home}")
    if kursor:
        print(f"{database_home} nomli baza qo'shildi")

def create_table(database_name, table_name):
    connect = myc.connect(user = "root", password = "1551734", host = "localhost", database = f"{database_name}")
    kursor = connect.cursor()
    kursor.execute(f"""Create table if not exists {table_name}(id int primary key auto_increment, name varchar(25), inventer varchar(30), profit float, nationality varchar(30))""")
    connect.commit()
    print(f"{table_name} nomli table qo'shildi")

def input_data(database_name = "Famous_Person", table_name = "FM"):
    connect = myc.connect(user = "root", password = "1551734", host = "localhost", database = f"{database_name}")
    kursor = connect.cursor()
    sql = f"insert into {table_name}(name, inventer, profit, nationality) Values (%s %s %s %s)"
    values = ("Ilon Mask", "Space X", 254.6, "USA")
    kursor.execute(sql, values)
    connect.commit()
    print("Done")


# create_database("Famous_Person")
# create_table("Famous_Person", "FM")
# input_data()
