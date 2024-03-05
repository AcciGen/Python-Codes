import os
os.system("cls")

# def factorial(n):
#     lst = []

#     for i in range(len(n)):
#         cnt = 1
#         x = 1
#         while x != n[i]+1:
#             cnt *= x
#             x += 1
#         lst.append(cnt)

#     return lst

# num = int(input("Nechta son kiritasiz -> "))
# if num < 5:
#     print("Error! n < 5!")
#     exit()

# n = list(map(int, input("Enter the number -> ").split()))[:num]
# print(factorial(n))

# def num_index(lst):

#     cube = []
#     sum = 0
#     for i in range(len(lst)):
#         if i % 2 == 0:
#             cube.append(int(lst[i])*int(lst[i]))
#         else:
#             sum += int(lst[i])

#     print("Juftlarni kvadrati -> ", cube)
#     print("Toqlarni yig'indisi -> ", sum)

# lst = list(input())
# num_index(lst)

# def isupdown(str):

#     up = 0
#     down = 0

#     for i in str:
#         if i.isupper():
#             up += 1
#         elif i.islower():
#             down += 1

#     print("Up -> ", up)
#     print("Down -> ", down)

# str = input()
# isupdown(str)


# def max(lst):

#     max = 0
#     for i in lst:
#         if i > max:
#             max = i

#     return max


# n = int(input("Nechta son kiritasiz -> "))
# lst = list(map(int, input(f"Listga {n}ta son kiriting -> ").split()))[:n]
# print(max(lst))


# def is_prime(n):

#     k = 2
#     while  k * k <= n:
#         if n % k == 0:
#             return False
#         k = k + 1
#     return True

# n = int(input())
# lst = []

# for i in range(1, n):

#     if is_prime(i):
#         lst.append(i)

# print(lst)


lst = list(input())

if len(lst) % 2 == 0:
    for i in range(len(lst)//2, len(lst)):

        lst[i] = lst[i].upper()
else:
    for i in range(len(lst)//2+1, len(lst)):

        lst[i] = lst[i].upper()
        
str = ''
for i in lst:

    str += i

print(str)