import os
os.system("cls")

# def check_tub(n):
#     j = 2
#     while j * j <= n:
#         if n % j == 0:
#             return False
#         j += 1
#     return True

# n = int(input())

# while check_tub(n)==False:

#     n += 1
# print(n)



# n = input()
# for i in range(len(n)):
#     cnt = n.count(n[i])
#     print(int(cnt), end="")



# def function(n:int)->None:
#     cnt = 0
#     while str(n) != str(n)[::-1]:
#         n += int(str(n)[::-1])
#         cnt += 1
#     print(cnt, n)

# n = int(input())
# function(n)


n = int(input())

for i in range(n):
    if i == 0 or i == n-1:
        print("1"*n)
    elif i == 1:
        print("0"*(n-1), "1", sep="")
    elif i == n - 2:
        print("1", "0"*(n-2), "1", sep="")
    elif i == 2:
        print("1"*(n-2), "0", "1", sep="")
    elif i == n // 2:
        print("1", "0"*(n-4), "1", "0", "1", sep="")
    else:
        print("1", "0", "1"*(n-4), "0", "1", sep="")