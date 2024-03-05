# Caesar Cipher
# s = input("Text -> ")
# n = int(input("Key -> "))
# new = ""

# i = 0
# while i < len(s):
#     if s[i] == " ":
#         new += " "

#     elif ord(s[i]) > 64 and ord(s[i]) < 91:
#         if ord(s[i]) + n < 91:
#             new += chr(ord(s[i])+n)
#         else:
#             new += chr((ord(s[i])+n)-26)

#     elif ord(s[i]) > 96 and ord(s[i]) < 123:
#         if ord(s[i]) + n < 123:
#             new += chr(ord(s[i])+n)
#         else:
#             new += chr((ord(s[i])+n)-26)
#     i += 1

# print(new)


# Matrix
# file = open("matrix.txt", "w")
# n = int(input())

# for i in range(n):
#     for j in range(n):
#         if i == j or i + j == n - 1:
#             file.write("1 ")
#         else:
#             file.write("0 ")
#     file.write("\n")
# file.close()


# Facebook Likes
# names = list(map(str, input().split()))
# n = len(names)

# if not names:
#     print("no one likes this")
# elif n == 1:
#     print(f"{names[0]} likes this")
# else:
#     txt = ""
#     for i in range(n - 2):
#         txt += f"{names[i]}, "
#     txt += f"{names[-2]} and {names[-1]} like this"
#     print(txt)


# Reduce
# from functools import reduce
# lst = [1, 2, 3, 4]
# # 3 3 4
# # 6 4
# # 10
# print(reduce(lambda a, b: a + b, lst))
# print(reduce(lambda a, b: a if a < b else b, lst))


# Yes No
# lst = list(map(int, input().split()))
# n = len(lst)
# for i in range(n):
#     check = True
#     for j in range(i):
#         if lst[j] == lst[i]:
#             print("Yes")
#             check = False
#             break
#     if check:
#         print("No")



# Balloons
# def check(nums):
#     res = list()
#     cnt = 1
#     f_index = 0
#     i = 0
#     while i < len(res):
#         print(i)
#         if nums[i] == nums[i-1]:
#             cnt += 1
#         else:
#             if cnt > 2:
#                 while cnt > 0:
#                     res.append(nums.pop(f_index))
#                     cnt -= 1
#                 i = 0
#             cnt = 0
#             f_index = i
#     print(res)


# n = int(input("Numbers count -> "))
# lst = list(map(int, input("Enter the numbers with spaces -> ").split()))[:n]
# print(check(lst))



# AB or CD remove
# s = "ABFCACDB"
# lst = list()

# for i in s:
#     if i == "B" and lst[-1] == "A":
#         lst.pop()
#     elif i == "D" and lst[-1] == "C":
#         lst.pop()
#     else:
#         lst.append(i)
# print(len(lst))



# Cake
# name = input("name = ")
# age = int(input("age = "))
# n = f" {age} Happy Birthday {name}! {age} "

# if age % 2 == 0:
#     for i in range(len(n)+2):
#         print("#", end="")
#     print(f"\n#{n}#")
#     for i in range(len(n)+2):
#         print("#", end="")

# else:
#     for i in range(len(n)+2):
#         print("*", end="")
#     print(f"\n*{n}*")
#     for i in range(len(n)+2):
#         print("*", end="")


# Phone Number
# num = input()
# if num[0] == "(" and num[4] == ")" and num[8] == "-" and num[12] == "-" and num[15] == "-" and len(num) == 18:
#     print(True)
# else:
#     print(False)


# 609 = 609
# s, res = input(), ''

# for i in s[::-1]:
#     if i == "6":
#         res += "9"
#     elif i == "9":
#         res += "6"
#     elif i == "0":
#         res += "0"

# print(res == s)



# Draw
# draw = list(map(str, input().split()))
# cnt = 2
# i = 1
# while i < len(draw):
#     if draw[i].lower() != draw[i-1].lower():
#         cnt += 3
#     else:
#         cnt += 2
#     i += 1
# print(cnt)



# ?
# def pal(s):
#     if len(s) <= 2:
#         return s[0]
#     ans = ''
#     for i in range(len(s)):
#         p = ''
#         res = ''
#         for j in range(i, len(s)):
#             p += s[j]
#             print(len(p), len(res))
#             if p == p[::-1] and len(p) > len(res):
#                 res = p
#         ans = res
#     return ans

# print(pal("accb"))



# 13th Friday
# from datetime import datetime as dt, timedelta as td

# date_str = input("Current date >> ")
# date = dt.strptime(date_str, "%d.%m.%Y")

# while date.weekday() != 4:
#     date += td(days=1)

# while date.day != 13:
#     date += td(weeks=1)

# print("Next 13th Friday is", date.strftime("%d.%m.%Y"))



# from 16 to 2
# def daraja(a, b):
#     res = 1
#     for x in range(b):
#         res = res * a
#     return res

# def printBinary(num):
#     res = 0
#     num = num.upper()
#     dic = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
#     cnt = 0
#     for x in num:
#         cnt += 1
#         if x.isdigit() and x != "0":
#             res = res + int(x) * daraja(16, len(num) - cnt)
#         elif x in ("A", "B", "C", "D", "E", "F"):
#             res = res + dic[x] * daraja(16, len(num) - cnt)

#     return res

# def printBinar(num):
#     if num == 0:
#         return
#     printBinar(num//2)
#     print(num % 2, end = "")

# num = input("Sonni kiriting: ")
# printBinar(printBinary(num))



# Robot Translate
# def binary(num):
#     if num == 0:
#         return "0"
    
#     bin = ''
#     while num > 0:
#         rem = num % 2
#         bin = str(rem) + bin
#         num //= 2
    
#     return str(bin)

# s = input()
# bin_s = ''
# num = 0
# cnt = 0
# for i in range(len(s)):
#     if s[i].isdigit():
#         if cnt > 0:
#             num = num*10 + int(s[i])
#         else:
#             num = int(s[i])
#             cnt += 1
#     else:
#         if cnt > 0:
#             bin_s += binary(num)
#             num = 0
#             cnt = 0
#         bin_s += s[i]
# print(bin_s)



# Camelcase and Snakecase
# s = input()
# new = ''

# for i in range(len(s)):
# 	if s[i].isupper():
# 		new += "_"+s[i].lower()
# 	elif s[i] == "_":
# 		continue
# 	elif s[i-1] == "_":
# 		new += s[i].upper()
# 	else:
# 		new += s[i]
# print(new)



# Sum Only Nums
# def sumInStr(s):
#     num, sum = 0, 0
#     for i in range(len(s)):
#         if s[i].isdigit():
#             num = num*10 + int(s[i])
#         else:
#             if num != 0:
#                 sum += num
#                 num = 0
        
#         if i == len(s)-1:
#             if num != 0:
#                 sum += num
#     return sum

# s = input()
# print(sumInStr(s))



