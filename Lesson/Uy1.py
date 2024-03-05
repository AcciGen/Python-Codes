import os
os.system("cls")
from itertools import permutations

#1
# def res(lst, lst1, lst2):
#     ls = []
#     dc = dict()

#     for i in range(4):
#         dc[lst[i]] = {lst1[i] : lst2[i]}

#     ls.append(dc)
#     return ls

# lst = ['S001', 'S002', 'S003', 'S004']
# lst1 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# lst2 = [85, 98, 89, 92]
# print(res(lst, lst1, lst2))


#2
# word = input("Satr kiriting: ")
# d = dict()
# for i in list(word):
#     d.setdefault(i, list(word).count(i))
# print(d)


#3
# dict1 = {1:'ABC', 2:'DEF', 3:'GHI', 4:'JKL', 5:'MNO', 6:'PRS'}

# for i in range(len(dict1.values())):
#     if i % 2 != 0:
#         dict1[i], dict1[i+1] = dict1[i+1], dict1[i]
        
# print(dict1)


#4
# text = input()
# sentences = text[:-1].split(".")
# text = text.replace(".", "")
# words = text.split()
# print("Words:", words)
# print("Sentences:", sentences)


#5
# nums = [61, 228, 9]
# elems = list()
# for i in permutations(nums):
#     i = int(''.join(list(map(str, i))))
#     elems.append(i)
# print(max(elems))


#6
# lst = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# dc = {}

# for i in range(len(lst)):
#     dc.setdefault(lst[i][0], [lst[i][1], lst[i][2]])

# print(dc)


#7
# lst = list(map(int, input().split()))
# for i in lst:
#     num = i
#     while num > 10:
#         num //= 10
#     if num % 2 == 0:
#         print(i, end=" ")


#8
# dic1 = {1:10, 2:20}
# dic2 = {3:30, 4:40}
# dic3 = {5:50, 6:60}
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)


#9
# n = int(input())
# dic = {}

# for i in range(1, n):

#     dic.setdefault(i, i**2)

# print(dic)


#10
# dic = {2:20, 1:10, 3:30, 4:40, 6:60, 5:50}

# ls = list(dic.items())
# ls.sort()
# ls.remove(ls[0])
# ls.remove(ls[-1])
# dic.clear()
# dic.update(ls)
# print(dic)


#11
# n = int(input("Nechta key kiritasiz >> "))
# dic = {}

# while n != 0:

#     s = int(input("Key >> "))
#     s1 = int(input("Value >> "))
#     dic.update({s:s1})
#     n -= 1

# lst = list(dic.values())
# lst.sort()
# lst2 = [lst[-1], lst[-2], lst[-3]]
# lst1 = list(dic.keys())

# for i in range(len(lst1)):
#     j = 0

#     while j != 3:

#         if dic.get(lst1[i]) == lst2[j]:
#             print(lst1[i])
#         j += 1


#12
# lst = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
# new_lst = []

# for i in lst:
#     cnt = 0
#     for x in list(i):
#         cnt += x
#     new_lst.append(cnt)

# print(new_lst)


#13
# lst = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]

# for i in range(len(lst)):
#     lst[i] = list(lst[i])

# print(lst)


#14
# d1 = {'a':100, 'b':200, 'c':300}
# d2 = {'a':300, 'b':200, 'd':400}

# for i in d2.keys():

#     if i in d1:
#         d1[i] += d2[i]
#     else:
#         d1[i] = d2[i]

# print(d1)