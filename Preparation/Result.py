import os
os.system("cls")

# Lift
# lift = list()
# for i in range(11, 0, -1):
#     lst = input().split(",")
#     lift.extend(lst)
# os.system("cls")

# for i in range(11, 0, -1):
#     cnt = 0
#     for j in range(len(lift)):

#         if f"{i-1}" == lift[j]:

#             if cnt > 0:
#                 print(f",{lift[j]}", end="")
#             else:
#                 print(lift[j], end="")
#                 cnt += 1

#     if cnt == 0:
#         print("-", end="")
#     print()

# Next Bigger Number
# num = int(input())
# res = -1
# s = ""
# lst = list(str(num))

# for i in range(len(lst)-1, 0, -1):

#     lst[i], lst[i-1] = lst[i-1], lst[i]

#     for i in lst:
#         s += i

#     if int(s) > num:
#         res = int(s)
#         break
#     else:
#         s = ""

# print(res)

# Like or Dislike
inpt = input()
lst = []
for i in inpt:
    if i.isupper():
        if i == 'D':
            lst.append('Dislike')
        elif i == 'L':
            lst.append("Like")

natija = 'Nothing'

for i in range(len(lst)):
    if lst[i]!=natija:
        natija = lst[i]
    elif lst[i]==natija:
        natija = 'Nothing'
        
print(natija)