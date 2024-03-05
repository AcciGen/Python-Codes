import os
os.system("cls")

#1
# def azbukamorse(lst):

#     morze = {
#         "-----":"0",
#         ".----":"1",
#         "..---":"2",
#         "...--":"3",
#         "....-":"4",
#         ".....":"5",
#         "-....":"6",
#         "--...":"7",
#         "---..":"8",
#         "----.":"9"
#     }

#     for i in range(len(lst)):

#         print(morze[lst[i]], end="")


# azbuka = list(map(str, input("Azbuka Morzeni kiriting\n").strip().split()))
# azbukamorse(azbuka)


#2
# def time(t):

#     print("{:02d}:{:02d}:{:02d}".format(t//3600,(t%3600)//60,t%60))

# t = int(input("Enter the time -> "))
# time(t)


#3
# def mukammal_son(n):
#     lst = []
#     for i in range(1, n//2 + 1):
#         if n % i == 0:
#             lst.append(i)

#     if sum(lst) == n:
#         return True
#     else:
#         return False

# num = int(input("Enter the number -> "))
# if mukammal_son(num):
#     print("Mukammal son")
# else:
#     print("Mukammal son emas")


#4
# def change(k, n):

#     add = n[::-1] + k
#     return add[::-1]

# n = input("Enter the number -> ")
# k = input("Enter the addable number -> ")
# print(int(change(k, n)))


#5
# def swap(x, y):

#     x, y = y, x
#     return (x, y)

# x = float(input("Enter the 1st number -> "))
# y = float(input("Enter the 2nd number -> "))
# print((x, y))
# print(swap(x, y))


#6
# def degree(n, k):

#     i = 1
#     x = k
#     while x < n:

#         x = x * k
#         i += 1

#     return i if x == n else "Berilgan son k soninig darajasi emas"

# n, k = map(int, input("Enter the n and k -> ").split())
# print(degree(n, k))


#7
# def cube(lst):

#     new_lst = []
#     for i in range(len(lst)):

#         n = lambda x: x*x
#         new_lst.append(n(lst[i]))

#     return new_lst

# lst = list(map(int, input("Listga sonlarni kiriting\n").split()))
# print(cube(lst))


#8
# def filt(lst):

#     res = sorted(lst, key = lambda x: x[1])

#     return res

# lst = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# print(filt(lst))


#9
# def split(lst):

#     juft = list(filter(lambda x: (x % 2 == 0), lst))
#     toq = list(filter(lambda y: (y % 2 != 0), lst))

#     print(juft)
#     print(toq)

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(lst)
# split(lst)


#10
# def null(str, cnt = 0):
#     if str[cnt] != '0':
#         return cnt
#     return null(str, cnt+1)

# str = input("Enter the number -> ")
# print(null(str))


#11
# def convert_date(in_date):

    # months_dict = {
    #     "01": "January",
    #     "02": "February",
    #     "03": "March",
    #     "04": "April",
    #     "05": "May",
    #     "06": "June",
    #     "07": "July",
    #     "08": "August",
    #     "09": "September",
    #     "10": "October",
    #     "11": "November",
    #     "12": "December"
    # }

#     date, time = in_date.split()
#     day, month, year = date.split(".")
#     hours, minutes = time.split(":")

#     day = int(day)
#     month = months_dict[month]
#     year = int(year)
#     hours = int(hours)
#     minutes = int(minutes)

#     return f"{day} {month} {year} year {hours} hours {minutes} minutes"

# in_date = input()
# print(convert_date(in_date))