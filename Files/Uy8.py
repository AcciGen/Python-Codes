import os
os.system("cls")
os.chdir("C:\\Codes\\Py_Codes\\Files")

try:
    file = open("person's.txt", "r")

except FileNotFoundError:
    print("404 Not Found")
    exit(1)

else:
    data = file.readlines()
    file.close()
    data.pop(0)

filetrue = open("Ishli.txt", "w")
filefalse = open("Ishsiz.txt", "w")

for i in data:
    if 'true' in i:
        filetrue.write(i)
    elif 'false' in i:
        filefalse.write(i)

#2
# try:
#     file = open("person's.txt", "r")

# except FileNotFoundError:
#     print("404 Not Found")
#     exit(1)

# else:
#     data = file.readlines()
#     file.close()
#     data.pop(0)

# dic = {}
# country = list(map(lambda i : i[:-1].split(",")[2],data))
# st = set(country)

# for i in st:
#     value = 0
#     value = country.count(i)
#     dic.setdefault(i, value)

# for i in sorted(dic):
#     print(i, dic[i], sep=" -> ")