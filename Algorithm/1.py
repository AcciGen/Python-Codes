import os
import random as r
os.system("cls")

# def linearSearch(lst):
#     left = lst[0]
#     right = lst[-1]
#     for i in range(len(lst)):
#         if lst[i] > left and lst[i] < right and lst[i] % 2 == 0:
#             return lst[i]
#     return -1

# os.system("cls")
# lst = [r(10, 50) for x in range(6)]
# print(lst)
# print("Result:", linearSearch(lst))


# def checkTub(n):
#     j = 2
#     while j * j <= n:
#         if n % j == 0:
#             return False
#         j += 1
#     return True

# def linearSearch(index, lst):
#     if index == -1:
#         return index
#     if (checkTUb(lst[index]) == True):
#         pass

# os.system("cls")
# nums = [r(1, 30) for x in range(9)]
# print(nums)


# def binarySearch(ls, item):
#     start = 0
#     end = len(ls) - 1
    # while start <= end:
    #     middle = (start + end) // 2
    #     if ls[middle] == item:
    #         return middle
    #     elif ls[middle] > item:
    #         end = middle - 1
    #     else:
    #         start = middle + 1
    # return -1

# def findItems(ls):
#     res = list()
#     for x in range(min(ls) + 1, max(ls)):
#         if binarySearch(ls, x) == -1:
#             res.append(x)
#     return res

# lst = list(map(int, input("List elementlarini kiriting: ").split()))

# result = findItems(lst)
# for x in result:
#     if x != result[-1]:
#         print(x, end = " + ")
#     else:
        # print(x, end = " = ")

# ls = [r(1, 20) for i in range(8)]
# print(ls)
# ls.sort()
# cnt = 0
# for i in range(len(ls)):



# def bubbleSort(ls):
#     for i in range(len(ls)):
#         check = False
#         for j in range(len(ls) - i - 1):
#             if ls[j] > ls[j+1]:
#                 ls[j], ls[j+1] = ls[j+1], ls[j]
#                 check = True

#         if check == False:
#             break
#     return ls

# os.system("cls")
# ls = list(map(int, input().split()))

# print(ls)
# print(bubbleSort(ls))

# def selectionSort(ls):
#     for i in range(len(ls)):
#         minI = i
#         for j in range(i+1, len(ls)):
#             if ls[minI] < ls[j]:
#                 minI = j
#         if minI != i:
#             ls[minI], ls[i] = ls[i], ls[minI]
#     return ls

# result = list()
# for i in range(10):
#     result.append(r.uniform(10, 50))




# def selectionSort(ls):
#     for i in range(len(ls)):
#         minI = i
#         for j in range(i+1, len(ls)):
#             if ls[minI] > ls[j]:
#                 minI = j
#         if minI != i:
#             ls[minI], ls[i] = ls[i], ls[minI]
#     return ls

# def count(ls, num):
#     lst = selectionSort(ls)
#     cnt = 0
#     for i in range(len(lst)):
#         if num == lst[i]:
#             cnt += 1
#         if num == lst[i-1] and lst[i] != num:
#             return cnt
#     return cnt

# lst = [7, 4, 2, 8, 1, 2, 4, 6, 7, 1, 2, 0, 5, 3]
# print(lst)
# print(count(lst, int(input("Choose the number: "))))



