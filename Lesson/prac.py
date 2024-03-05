import os
os.system("cls")
import random

# lst = [random.randint(1, 9) for i in range(8)]
# lst.sort()
# print(lst)
# lst.reverse()

# if len(lst) == 2:
#     if lst[0] == lst[1]:
#         print("None")
#         exit()

#     else:
#         print(lst[0])
#         exit()

# elif len(lst) == 1:
#     print("None")
#     exit()

# max = lst[0]
# i = 0
# while max == lst[i]:

#     i += 1

# if lst[i] == lst[i+1]:
#     print("None")

# else:
#     print(lst[i])


# lst = [random.randint(1, 9) for i in range(6)]
# print(lst)

# n, m = map(int, input("Qaysi 2ta oraliq teskari qilinsin: ").split(" "))
# i = n
# new = []

# while i <= m:

#     new.append(lst[i])
#     i += 1

# new.reverse()

# for i in range(len(lst)):

#     if i >= n and i <= m:
#         lst[i] = new[i-n]

# print(lst)


# lst = [random.randint(1, 100) for i in range(20)]
# lst.sort()
# print(lst)

# i = 0
# while i != len(lst):

#     if lst[i] >= 40 and lst[i] <= 60:

#         lst.pop(i)
#         i -= 1

#     i += 1

# print(lst)


# lst = []

# for i in range(3):

#     typo = input("Qandey ma'lumot kiritasiz (s/i/f) >> ")

#     if typo in 's':
#         num = input(f"{i+1} ma'lumotni kiriting: ")

#     elif typo in 'i':
#         num = int(input(f"{i+1} ma'lumotni kiriting: "))

#     elif typo in 'f':
#         num = float(input(f"{i+1} ma'lumotni kiriting: "))

#     lst.append(num)

# print(lst)

# i = 0
# while i != len(lst):

#     if type(lst[i]) == int or type(lst[i]) == float:

#         lst.pop(i)
#         i -= 1

#     i += 1

# print(lst)



# lst = [random.randint(1, 100) for i in range(20)]
# new = []
# lst.sort()
# print(lst)

# cnt = 1

# for i in range(len(lst)):

#     cnt = 2
#     if lst[i] > 1:
#         for j in range(2, lst[i]):

#             if lst[i] % j == 0:
#                 cnt += 1

#         if cnt == 2:
#             new.append(lst[i])

# print(new)



# n = int(input())
# lst = list(map(int, input().strip().split()))[:n]

# f = 0
# while True:

#     mn = min(lst)
#     mx = max(lst)
#     i1 = lst.index(mn)
#     i2 = lst.index(mx)

#     if i1 == len(lst)-1:
#         lst.pop(i1)
#     elif i1 < i2:
#         f = mx - mn
#         break
#     elif i1 > i2:
#         lst.pop(i2)

# print(f)

# def birja(nums):
#     n = min(nums)
#     if len(nums) < 2:
#         return False
#     if n == nums[-1]:
#         nums.pop()
#     return max(nums[min(nums):]) - min(nums)
# n = int(input())
# nums = list(map(int,input().split()))[:n]

# print(birja(nums))


