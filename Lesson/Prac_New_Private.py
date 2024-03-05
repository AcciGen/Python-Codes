import os
os.system("cls")

# class Ekundalik:
# 	def __init__(self, name, age, sinf, gpa, password):
# 		self.name = name
# 		self.age = age
# 		self.sinf = sinf
# 		self.password = password
# 		self.__gpa = gpa

# 	def __str__(self):
# 		return f"Name -> {self.name}\nAge -> {self.age}\nClass -> {self.sinf}\nPassword -> {self.password}\nGPA -> {self.__gpa}"
	
# 	def change_gpa(self, input_gpa, check_ps):
# 		n = input(f"Enter to change GPA from {self.__gpa} to {input_gpa}: ")
# 		if n == "" and check_ps == self.password:
# 			self.__gpa = input_gpa
# 		else:
# 			print("Error!")

# 	def get_gpa(self):
# 		print(f"GPA -> {self.__gpa}")

	
# kundalik1 = Ekundalik("Nuriddin", 18, 12, 5, 1235)
# print(kundalik1)
# kundalik1.change_gpa(4.5, 1235)
# kundalik1.get_gpa()



class Date:
	def __init__(self, day, month, year):
		self.__day = day
		self.__month = month
		self.__year = year

	def isLeapYear(self):
		if self.__year % 4 == 0 and self.__year % 100 != 0 or self.__year % 400 == 0:
			print("Leap Year")
		else:
			print("Not Leap Year")

	def isValidDate(self):
		if self.__day > 0 and self.__day < 32 and self.__month > 0 and self.__month < 13 and self.__year > 0 and self.__year < 10000:
			print("True")
		else:
			print("False")

date = Date(14, 8, 2005)
date.isLeapYear()
date.isValidDate()
