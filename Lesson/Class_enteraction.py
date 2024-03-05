import os
import random
from accessify import*
os.system("cls")
# class Car:
#     def __init__(self):
#         self.lst = []

#     def addCar(self, model, price, __distance):
#         self.model = model
#         self.price = price
#         self.__distance = __distance
#         self.__change_distance()
#         self.lst.append([self.model, self.price, self.__distance])

#     def __change_distance(self):
#         self.__distance += random.randint(8, 12)

#     def get_distance(self):
#         return self.__distance
    
#     def sort(self):
#         res = sorted(self.lst, key = lambda x: x[2])
#         self.lst = res.copy()

#     def show(self):
#         for i in self.lst:
#             print(f" Model {i[0]}\n Price {i[1]}\n Distance {i[2]}\n")

# cars = Car()
# while 1:
#     op = int(input("1: "))
#     if op != 1:
#         break
#     os.system("cls")
#     model = input("Model: ")
#     price = int(input("Price: "))
#     cars.addCar(model, price, 0)

# print(cars.show())
# print("\n")
# print(cars.sort())
# print(cars.show())




# class Student:
#     def __init__(self, name, card, contract, sub_credit = 6):
#         self.name = name
#         self.student_card = card
#         self.sub_credit = sub_credit
#         self.contract = contract
#         self.__missed_lessons = 0

#     def check_attention(self, hour = None, minute = None):
#         self.__check_lesson(hour, minute)
#         if self.__missed_lessons >= 5:
#             self.__missed_lessons -= 5
#             pay = self.contract / 60 * self.sub_credit
#             self.student_card -= pay
#             print(f"Sizni kartezdan {pay} so'm yechildi")
#         else:
#             print(f"Qoldirilgan darslar soni {self.__missed_lessons}")

#     def __check_lesson(self, hour, minute):
#         if hour is None:
#             self.__missed_lessons += 3
#         elif minute > 30 and hour > 7 and hour < 10:
#             self.__missed_lessons += 1
#         elif minute > 0 and hour > 10 and hour < 12:
#             self.__missed_lessons += 2
#         else:
#             self.__missed_lessons += 3

#     def show_info(self):
#         print(f"{self.name}  {self.sub_credit}  {self.student_card}")

# student1 = Student("Den", 14000000, 7200000)
# student1.check_attention()
# student1.check_attention(11, 25)
# student1.check_attention(8, 45)

# student1.show_info()
