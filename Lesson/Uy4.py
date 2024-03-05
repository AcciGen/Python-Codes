import os
os.system("cls")

#1
class Animal:

    def __init__(self, name, color, hunger, aggressive):
        self.name = name
        self.color = color
        self.hunger = hunger
        self.aggressive = aggressive

class Beast(Animal):

    def HungryOrNot(self):
        if self.hunger:
            print("Yirtqich ayni vaqt och! O'lja qidirmoqda!")
        else:
            print("Yirtqich ayni vaqt to'q")

    def AggressiveOrNot(self):
        if self.aggressive:
            print("Yirtqich ayni vaqt tashlanadi! Go'sht yeyishi kerak!")
        else:
            print("Yirtqich ayni vaqt tinch")

    def showInfo(self):
        print(f"Info:\n Name: {self.name}\n Color: {self.color}\n Hunger: {self.hunger}\n Aggressive: {self.aggressive}")


class Herbivorous(Animal):

    def HungryOrNot(self):
        if self.hunger:
            print("O'txo'r ayni vaqt och! U yem qidirmoqda!")
        else:
            print("O'txo'r ayni vaqt to'q")

    def AggressiveOrNot(self):
        if self.hunger and self.aggressive:
            print("O'txo'r ayni vaqt tashlanadi! Tezroq yem berish kerak!")
        else:
            print("O'txo'rni qorni tinch, seni esa boshing tinch")

    def showInfo(self):
        print(f"Info:\n Name: {self.name}\n Color: {self.color}\n Hunger: {self.hunger}\n Aggressive: {self.aggressive}")
    
lion = Beast("Lion", "Dark Yellow", True, True)
horse = Herbivorous("Horse", "Brown", False, False)
lion.showInfo()
lion.HungryOrNot()
lion.AggressiveOrNot()
horse.showInfo()
horse.HungryOrNot()
horse.AggressiveOrNot()



#2
# class Int:

#     def __init__(self, Int):
#         self.lst = [Int]

#     def show(self):
#         print(self.lst)

# class IntFloat(Int):

#     def __init__(self, Int, Float):
#         super().__init__(Int)
#         self.lst.append(Float)

# class IntFloatBool(IntFloat):

#     def __init__(self, Int, Float, Bool):
#         super().__init__(Int, Float)
#         self.lst.append(Bool)

# class IntFloatBoolStr(IntFloatBool):

#     def __init__(self, Int, Float, Bool, Str):
#         super().__init__(Int, Float, Bool)
#         self.lst.append(Str)

# a = Int(12)
# a.show()
# b = IntFloat(10, 14.5)
# b.show()
# c = IntFloatBool(14, 45.12, True)
# c.show()
# d = IntFloatBoolStr(42, 12.25, False, "Accepted")
# d.show()



#3
# class Printer:

#     def __init__(self):
#         self.ps = []

#     def inputPS(self, model, speed, price, type, year):
#         self.model = model
#         self.speed = speed
#         self.price = price
#         self.type = type
#         self.year = year
#         self.ps.append([self.model, self.speed, self.price, self.type, self.year])

#     def show(self):
#         print("Info:")
#         for i in self.ps:
#             print(f" Model: {i[0]}\n Speed: {i[1]}\n Price: {i[2]}\n Type: {i[3]}\n Year: {i[4]}\n")

    # def sortPrice(self):
    #     res = sorted(self.ps, key = lambda x: x[2])
    #     self.ps = res.copy()
    #     self.show()

#     def sortYearAndType(self, year, type):
#         for i in self.ps:
#             if i[-1] == year and i[-2] == type:
#                 print(f"\n Model: {i[0]}\n Speed: {i[1]}\n Price: {i[2]}\n Type: {i[3]}\n Year: {i[4]}\n")

# printers = Printer()
# printers.inputPS("HEP", 95, 30, "Line", 2012)
# printers.inputPS("Canon", 155, 75, "Laser", 2023)
# printers.inputPS("Canyon", 100, 40, "Ink", 2015)
# printers.inputPS("Next", 140, 65, "Thermal", 2022)
# printers.inputPS("Gren", 120, 50, "Laser", 2018)

# printers.show()
# print("-----After Sorting Price-----")
# printers.sortPrice()
# year = int(input("Year -> "))
# type = (input("Type -> "))
# printers.sortYearAndType(year, type)



#4
# class Counter:

#     def __init__(self, num):
#         self.num = num

#     def plus(self):
#         if self.num >= 0:
#             self.num += 1
#         else:
#             print("Son 0dan kichik")

#     def minus(self):
#         if self.num > 0:
#             self.num -= 1
#         elif self.num == 0:
#             print("Son 0ga teng. Ayirishda Error!")
#         else:
#             print("Son 0dan kichik. Ayirishda Error!")
    
#     def getCounter(self):
#         print(self.num)

# num = Counter(0)
# num.plus()
# num.getCounter()
# num.minus()
# num.getCounter()
# num.minus()