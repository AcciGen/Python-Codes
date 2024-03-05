import os
os.system("cls")
os.chdir("C:\\Codes\\Py_Codes\\Files")

#1
# try:
#     file = open("Internet.txt", "r")

# except FileNotFoundError:
#     print("404 Not Found")
#     exit(1)

# else:
#     data = file.readlines()
#     file.close()

# for i in data:
#     e, fn, macA, dv = i.split(",")
#     macA = macA.split("-")
#     count = 0
#     for j in macA:
#         if not j.isdigit():
#             count += 1
#     if count == len(macA):
#         print(e, fn)



#2
# try:
#     file = open("Internet.txt", "r")

# except FileNotFoundError:
#     print("404 Not Found")
#     exit(1)

# else:
#     data = file.readlines()
#     file.close()

# dic = {}
# data = list(map(lambda i : i[:-1].split(',')[-1],data))
# st = set(data)

# for i in st:
#     value = 0
#     value = data.count(i)
#     dic.setdefault(i, value)

# for i in sorted(dic):
#     print(i, dic[i], sep=" -> ")



#3
# try:
#     file = open("Karta.txt", "r")

# except FileNotFoundError:
#     print("404 Not Found")
#     exit(1)

# else:
#     data = file.readlines()
#     file.close()

# dic = {}
# data = list(map(lambda i : i[:-1].split(",")[-1],data))
# st = set(data)

# for i in st:
#     value = 0
#     value = data.count(i)
#     dic.setdefault(i, value)

# for i in sorted(dic):
#     print(i, dic[i], sep=" -> ")



#4
# try:
#     file = open("Karta.txt", "r")

# except FileNotFoundError:
#     print("404 Not Found")
#     exit(1)

# else:
#     data = file.readlines()
#     file.close()

# data = list(map(lambda i : i[:-1].split(","),data))
# value = ["visa", "visa-electron"]
# lst = []

# for i in data:
#     if i[1] in value:
#         lst.append(i[-1])

# for i in set(lst):
#     print(i)



#5
# try:
#     file = open("Karta.txt", "r")

# except FileNotFoundError:
#     print("404 Not Found")
#     exit(1)

# else:
#     data = file.readlines()
#     file.close()

# data = list(map(lambda i : i[:-1].split(","),data))

# for i in data:
#     if len(sorted(set(i[0]))) == 10:
#         print(i[0], i[5], i[2], i[4])