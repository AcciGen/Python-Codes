import os
from abc import *
os.system("cls")

# class Computer(ABC):
# 	def __init__(self, model, price):
# 		self.model = model
# 		self.price = price
# 	@abstractclassmethod
# 	def show_info(self):
# 		pass

# 	@abstractclassmethod
# 	def check_graph(self):
# 		pass

# 	def working(self):
# 		pass

# class Laptop(Computer):
# 	def __init__(self, model, price, vc = None, ram = 16):
# 		super().__init__(model, price)
# 		self.vc = vc
# 		self.ram = ram

# 	def show_info(self):
		# print(f"Name: {self.model}\nPrice: {self.price}\nVideocard: {self.vc}\nRam: {self.ram}")

# 	def check_graph(self):
# 		if self.vc is None:
# 			print("This laptop is not for games")
# 		else:
# 			print("Press F to play the game")

# nt = Laptop("Asus", 1200, "RTX 3060", 32)
# nt.show_info()
# nt.check_graph()



# class Application(ABC):
# 	def __init__(self, name, users, establishment, inventer):
# 		self.name = name
# 		self.users = users
# 		self.establishment = establishment
# 		self.inventer = inventer

# 	@abstractclassmethod
# 	def show_info(self):
		# print(f"Name: {self.name}\nUsers: {self.users}\nEstablishment: {self.establishment}\nInventer: {self.inventer}")

# 	def month_income(self):
# 		if self.users >= 1000000:
# 			print(f"{self.name} har oy {self.users * 2}")
# 		elif self.users >= 10000000:
# 			print(f"{self.name} har oy {self.users * 4}")
# 		elif self.users < 1000000:
# 			print(f"Sizda yetarli client mavjud emas")
# 		else:
# 			print(f"{self.name} har oy {self.users * 5}")

# class YouTube(Application):
# 	def __init__(self, name, users, establishment, inventer):
# 		super().__init__(name, users, establishment, inventer)

# 	def show_info(self):
# 		super().show_info()

# yt = YouTube("YouTube", 23000000000, 2005, "Javod Karim")
# # yt.show_info()
# yt.month_income()



# class Countries(ABC):
# 	def __init__(self, name, independence, population, language):
# 		self.name = name
# 		self.independence = independence
# 		self.population = population
# 		self.language = language

# 	@abstractclassmethod
# 	def show_info(self):
# 		pass

# 	@abstractclassmethod
# 	def getIndepend(self):
# 		pass

# class Country(Countries):
# 	def __init__(self, name, independence, population, language):
# 		super().__init__(name, independence, population, language)

# 	def show_info(self):
# 		print(f"Name: {self.name}\nIndependence: {self.independence}\nPopulation: {self.population}\nLanguage: {self.language}")

# 	def getIndepend(self):

# class Counter_Strike(0:0)
# 	method attack(str->body(4,5), -0, )


class Person:
	def __init__(self):
		self.name = None
		self.__id = 0
	
	@property
	def person(self):
		return f"Name -> {self.name}  ID -> {self.__id}"
	
	@person.setter
	def person(self, nd):
		self.name = nd[0]
		self.__id = nd[1]

	@person.deleter
	def person(self):
		print("Name and ID was deleted")
		del self.name
		del self.__id

pers = Person()
pers.person = ["John", 14618]
print(pers.person)
del pers.person
print(pers.name)