# from datetime import datetime as dt, timedelta as td

# data_str = input("Current date >> ")
# date = dt.strptime(data_str, "%d.%m.%Y")

# while date.weekday() != 4:
#     date += td(days=1)

# while date.day != 13:
#     date += td(weeks=1)

# print("Next 13th Friday is", date.strftime("%d.%m.%Y"))



# Maze
# def isReachable(grid):
#     rows = len(grid)
#     cols = len(grid[0])

#     current_row = 0
#     current_col = 0

#     # Пока мы не достигли нижнего правого угла
#     while current_row < rows - 1 or current_col < cols - 1:
#         # Если можно двигаться вниз и следующая ячейка равна 0
#         if current_row < rows - 1 and grid[current_row + 1][current_col] == 0:
#             current_row += 1
#         # Если можно двигаться вправо и следующая ячейка равна 0
#         elif current_col < cols - 1 and grid[current_row][current_col + 1] == 0:
#             current_col += 1
#         else:
#             # Если нельзя двигаться ни вниз, ни вправо, значит мы не смогли достичь нижнего правого угла
#             return False

#     return True

# maze1 = [[0,1,1,1,1,1,1],
#          [0,0,1,1,0,1,1],
#          [1,0,0,0,0,1,1],
#          [1,1,1,1,0,0,1],
#          [1,1,1,1,1,0,0]]

# maze2 = [[0,1,1,1,1,1,1],
#          [0,0,1,0,0,1,1],
#          [1,0,0,0,0,1,1],
#          [1,1,0,1,0,0,1],
#          [1,1,0,0,1,1,1]]

# maze3 = [[0,1,1,1,1,0,0],
#          [0,0,0,0,1,0,0],
#          [1,1,1,0,0,0,0],
#          [1,1,1,1,1,1,0],
#          [1,1,1,1,1,1,1]]

# maze4 = [[0,1,1,1,1,0,0],
#          [0,0,0,0,1,0,0],
#          [1,1,1,0,0,0,0],
#          [1,0,0,0,1,1,0],
#          [1,1,1,1,1,1,0]]

# print(isReachable(maze1))
# print(isReachable(maze2))
# print(isReachable(maze3))
# print(isReachable(maze4))



# Left And Right Hand
# import os
# os.system("cls")
# os.chdir("C:\\Codes\\PyCodes\\Preparation")

# def countLeftRightHand(s):
#     left = ["1","2","3","4","5","q","w","e","r","t","a","s","d","f","g","z","x","c","v","b"]
#     right = ["6","7","8","9","0","y","u","i","o","p","h","j","k","l",";","n","m",",",".","/"]
#     lcnt = 0
#     rcnt = 0
#     for i in s:
#         if i in left:
#             lcnt += 1
#         elif i in right:
#             rcnt += 1

#     print(f"Left Count: {lcnt}")
#     print(f"Right Count: {rcnt}")


# try:
#     file = open("handwrite.txt", "r")

# except FileNotFoundError:
#     print("404 Not Found")
#     exit(1)

# else:
#     data = file.readline()

# countLeftRightHand(data)



# Animals
# animals = ["dog", "cat", "bat", "cock", "cow", "pig", "fox", "ant", "bird",
#            "lion", "wolf", "deer", "bear", "frog", "hen", "mole", "duck", "goat"]

# s = list(input().lower())
# ans_cnt = 0
# ans = []

# for animal in animals:

#     rs = s.copy()
    
#     check = True
#     while check:

#         count = 0
#         for char in animal:
#             if char in rs:
#                 count += 1
#                 rs.remove(char)
#             else:
#                 check = False

#         if count == len(animal):
#             if animal not in ans:
#                 ans.append(animal)
#             ans_cnt += 1

#         if not rs:
#             check = False            

# print(ans_cnt, *ans)



# MySQL
# import mysql.connector as mys
# class Database:
#     def __init__(self, database):
#         try:
#             self.con = mys.connect(user = 'root', password = '1551734', host = 'localhost')
#             self.curs = self.con.cursor()
#             self.curs.execute(f"CREATE database if not exists {database}")

#         except Exception as error:
#             print(error)

#         else:
#             print('Database created and connected')

#     def table(self, database, table):
#         try:
#             self.con = mys.connect(user = "root", password = "1551734", host = "localhost", database = f"{database}")
#             self.curs = self.con.cursor()
#             self.curs.execute(f"CREATE table if not exists {table}(order_number int, customer_number int)")
        
#         except Exception as error:
#             print(error)

#         else:
#             self.con.commit()
#             print("Table created")

#     def inputData(self, database, table):
#         try:
#             self.con = mys.connect(user = "root", password = "1551734", host = "localhost", database = f"{database}")
#             self.curs = self.con.cursor()
#             sql = f"INSERT into {table}(order_number, customer_number) Values (%s, %s)"
#             val = [(1, 1),
#                    (2, 2),
#                    (3, 3),
#                    (4, 3)]
#             self.curs.executemany(sql, val)
        
#         except Exception as error:
#             print(error)
        
#         else:
#             self.con.commit()
#             print("Inserted")
    
#     def showData(self, database, table):
#         try:
#             self.con = mys.connect(user = "root", password = "1551734", host = "localhost", database = f"{database}")
#             self.curs = self.con.cursor()
#             self.curs.execute(f"SELECT * FROM {table}")
#             result = self.curs.fetchall()
#             for x in result:
#                 print(f"Order >>     {x[0]}")
#                 print(f"Customer >>  {x[1]}")
#                 print("\n------------------\n")

#             self.curs.execute(f"SELECT customer_number FROM {table} GROUP BY customer_number ORDER BY COUNT(customer_number) desc limit 1;")
#             result = self.curs.fetchall()
#             print("\n----------------------\n")
#             print(f"Customer >>  {result[0][0]}")
#             print("\n----------------------\n")
        
#         except Exception as error:
#             print(error)

# Market = Database('market')
# Market.table('market', 'product')
# Market.inputData('market', 'product')
# Market.showData('market', 'product')



# 0 and 1
# dic = {"nol": 0, "bir": 1}

# s = input().lower().split()

# if len(s) % 8 == 0:
#     for i in s:
#         print(dic[i], end="")
# else:
#     print()



# Google
# n = int(input())
# print("G", end="")
# while n > 0:
#     print("o", end="")
#     n -= 1
# print("gle")



# Matching pair
# s = input().split()
# cnt = 0
# for i in range(len(s)):
#     for j in range(i+1, len(s)):
#         if s[i] == s[j]:
#             cnt += 1
# print(cnt)



# 