import os
import mysql.connector as my

class myDatabase:
    def __init__(self, database):
        self.con = my.connect(user = 'root', password = '1551734', host = 'localhost')
        self.curs = self.con.cursor()
        self.curs.execute(f"Create database if not exists {database}")

    def addTable(self, database, tableName):
        self.con = my.connect(user = 'root', password = '1551734', host = 'localhost', database = f'{database}')
        self.curs = self.con.cursor()
        self.curs.execute()
