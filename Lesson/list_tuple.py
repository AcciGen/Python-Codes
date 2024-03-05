import os
os.system("cls")

# list = [12, 10, 25, 36, 42, 13]
# list[0] = 10
# list[1] = 12
# list.append(20)
# list.insert(5, 14)
# son = list.pop(5)
# list.pop(0)
# print(son)
# list.append("My world")
# print(list)

# lt = ["Hello", "Good", "Time"]
# list.extend(lt)
# print(list)
# list.remove(36)
# for i in range(len(list)):

#     if (list[i] % 2 == 0):
#         print("Juft son >> ", list[i])

#     elif (list[i] % 2 != 0):
#         print("Toq son >> ", list[i])



# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list)

# for i in range(0, len(list), 1):

#     select = int(input("Select the index to rewrite >> "))
#     write = input("What you write there (s/n/f) >> ")
#     if write == 's':
#         rewrite = input("Write the string >> ")

#     elif write == 'n':
#         rewrite = int(input("Write the number >> "))

#     elif write == 'f':
#         rewrite = float(input("Write the float number >> "))

#     list.insert(select, rewrite)
#     print(list)



# list = []
# n = int(input("Nechta ma'lumot kiritilsin >> "))

# for i in range(n):
#     type = input("Ma'lumot >> ")
#     list.append(type)

# print(list)



# list = ["Hello", "World", "Good", "Day"]
# print(list)
# for i in range(0, len(list), 1):

#     if i % 2 != 0:
#         type = list.pop(i)
#         print(type, end = " ")

# print(list)


# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# cop = list.copy()

# print(list)
# print(cop)


# list = [100, 45, 80, 12, 14, 42]
# list.sort()
# list.reverse()
# print(list)
# list.clear()
# print(list)


# tuple = ('x', 'a', 'm', 'm', 'a') # don't have permission to retype or rewrite (delete or remove)
# print(tuple.index('x'))
# cnt = tuple.count('a')
# print(cnt)


a, b = map(int, input().split(" "))
list = []

for i in range(a, b, 1):

    if (i % 2 == 0):
        list.append(a)
    a += 1

print(list)