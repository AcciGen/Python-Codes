import os
from abc import *
from math import *
os.system("cls")


# class Shape(ABC):
# 	@abstractclassmethod
# 	def area(self):
# 		pass

# 	@abstractclassmethod
# 	def perimetr(self):
# 		pass


# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def area(self):
#         p = self.perimetr()/2
#         S = p * (p - self.a) * (p - self.b) * (p - self.c)
#         return sqrt(S)

#     def perimetr(self):
#         return self.a + self.b + self.c


# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def area(self):
#         return self.a * self.b
    
#     def perimetr(self):
#         return 2 * (self.a + self.b)


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2
    
#     def perimetr(self):
#         return 2 * 3.14 * self.radius

# triangle = Triangle(6, 8, 10)
# print(triangle.area())



# class Time:
# 	def __init__(self, hour, minut, sekund):
# 		self.hour = int(hour)
# 		self.minut = int(minut)
# 		self.sekund = int(sekund)
			
# 	def minutLeft(self):
# 		hour = 23 - self.hour
# 		minut = 60 - self.minut
# 		if hour > 0:
# 			minut += hour * 60
# 		print(f"{minut} minut qoldi")

# 	def add100(self):
# 		self.minut += 100
# 		while self.minut > 59:
# 			self.minut -= 60
# 			self.hour += 1
# 			self.hour %= 24
# 		self.showTime()

# 	def showTime(self):
# 		print("{:02d}:{:02d}:{:02d}".format(self.hour, self.minut, self.sekund))

# time1 = list(input("Enter a time -> ").split(":"))
# time = Time(time1[0], time1[1], time1[2])
# time.minutLeft()
# time.add100()




# class Time:
# 	def __init__(self, hour, minut, sekund):
# 		self.hour = hour
# 		self.minut = minut
# 		self.sekund = sekund


# class Mobile(Time):
# 	def __init__(self, hour, minut, sekund, surname, operator, real_time):
# 		super().__init__(hour, minut, sekund)
# 		self.surname = surname
# 		self.operator = operator
# 		self.real_time = real_time

# 	def abonent(self):
# 		if self.real_time < "00:00:00" or self.real_time > "23:59:59":
# 			print("Error!")
# 		elif self.real_time >= "08:00:00" and self.real_time <= "18:00:00":
# 			print("Abonent band!")
# 		elif self.real_time <= "05:00:00" or self.real_time >= "22:00:00":	
# 			print("Abonent uxlayapti!")
# 		else:
# 			print("Abonent bo'sh")

# ps = Mobile(16, 30, 30, "Anatoliy", "TELE2", "22:10:00")
# ps.abonent()


# lst, Score, Uzb, Enm = ["3:1", "2:2", "1:5", "4:0"], 0, 0, 0
# for i in lst:
#     if i[0] > i[-1]: Score += 3
#     elif i[0] < i[-1]: Score += 0
#     elif i[0] == i[-1]: Score += 1
#     Uzb += int(i[0])
#     Enm += int(i[-1])
# print(f"{Score} scores {Uzb}:{Enm}")


