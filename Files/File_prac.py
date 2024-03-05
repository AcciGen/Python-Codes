import os
os.system("cls")
import random
os.chdir("C:\\Codes\\Py_Codes\\Files")

# with open("people_cnt.txt", "r") as file:

#     lst = file.readlines()
    # for i in lst:
        # fname, lname, gen, age, cty = i.split(",")
        
        # if gen == "Male":
        #     print(fname, lname, cty, end="")

# file.close()



# try:
#     file = open("popularity.txt","r")

# except FileNotFoundError:
#     print("404 Not found!")
#     exit(1)

# else:
#     data = file.readlines()
#     file.close()

# for i in data:
#     town, pop, country = i.split(",")

#     if int(pop) >= 1000000:
#         print(town, pop, country)



# try:
#     file = open("product.txt","r")

# except FileNotFoundError:
#     print("404 Not found!")
#     exit(1)

# else:
#     data = file.readlines()
#     file.close()

# for i in data:
#     id, ucode, material, price, avail = i.split(',')
#     price = price.removeprefix("$")

#     if float(price) < 1000:
#         if avail == "false\n":
#             print(material)



# try:
#     file = open("cinema.txt","r", encoding="utf8")

# except FileNotFoundError:
#     print("404 Not found!")
#     exit(1)

# else:
#     data = file.readlines()
#     file.close()

# for i in data:
#     id, movie, genre, year, cinema, starts_at = i.split(',')
#     starts_at = starts_at.split(":")

#     if int(starts_at[0]) > 17:
#         if genre == "Horror":
#             print(id)



# try:
#     file = open("server_speed.txt","r")

# except FileNotFoundError:
#     print("404 Not found!")
#     exit(1)

# else:
#     data = file.readlines()
#     file.close()

# for i in data:
#     id, app, ver, server, server_test = i.split(',')
#     server = server.split(".")

#     if int(server[0]) > 150 and int(server[1]) > 150:
#         if float(server_test) > 5.0:
#             print(f"BU SERVER UZOQDA, LEKIN TEZLIGI {server_test}")
#         else:
#             print("BU SERVER UZOQDA\n")



try:
    file = open("phonenum.txt","r")

except FileNotFoundError:
    print("404 Not found!")
    exit(1)

else:
    data = file.readlines()
    file.close()

for i in data:
    country, code, first, sec, third = i.split()
    cnt = len(first+sec+third)
    if cnt == len(set(first+sec+third)):
        print(i)
