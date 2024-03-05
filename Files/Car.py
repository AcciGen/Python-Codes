import os
os.system("cls")
os.chdir("C:\\Codes\\Py_Codes\\Files")

#1
# try:
#     file = open("car.txt", "r")

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


#2
# try:
#     file = open("car.txt", "r")

# except FileNotFoundError:
#     print("404 Not Found")
#     exit(1)

# else:
#     data = file.readlines()
#     file.close()
#     data.pop(0)

# data = list(map(lambda i: i[:-1].split(","),data))
# data.sort(key=lambda x: x[2],reverse=True)
# for i in data:
#     print(i[1], i[-1], i[2])
