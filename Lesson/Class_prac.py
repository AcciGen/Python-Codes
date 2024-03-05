# class Cat:
    
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#         print("Salom")

#     def move_forward(self):
#         print("move forward")
    
#     def move_left(self):
#         print("Move left")

#     def move_right(self):
#         print("Move right")


# tom = Cat("Tom", "Blue")
# jerry = Cat("Jerry", "Black")



# class Circle:

#     def __init__(self, radius, color):
#         self.radius = radius
#         self.color = color

#     def get_radius(self):
#         return self.radius

#     def set_radius(self):
#         self.radius = int(input("Enter the new radius -> "))

#     def get_color(self):
#         return self.color

#     def set_color(self):
#         self.color = input("Enter the new color -> ")

#     def get_area(self):
#         yuza = 3.14 * self.radius**2
#         return yuza

#     def get_circumference(self):
#         uzunlig = 2 * 3.14 * self.radius
#         return uzunlig
    
#     def get_info(self):
#         return f'''
#     Radius: {self.radius}
#     Color: {self.color}
#     Yuza: {self.get_area()}
#     Uzunlig: {self.get_circumference()}
#     '''


# circle = Circle(12, "White")
# print("Radius:", circle.get_radius())
# circle.set_radius()
# print("Color:", circle.get_color())
# circle.set_color()
# print("Yuza:", circle.get_area())
# print("Uzunlig:", circle.get_circumference())
# print(circle.get_info())


# class Animal:

#     def __init__(self, name, weight, color):
#         self,name=name
#         self.weight = weight
#         self.color = color

# class Bird(Animal):
#     name = "Araman"
#     color = "Blue"
#     weight = 1.12
#     wings_color = "Red"


#     def fly(self):
#         print("Bird is fly")

#     def walk(self):
#         print("Bird walk")

#     def twit(self):
#         print("Bird twit")

#     def eat(self):
#         print("Bird eat")

#     def sleep(self):
#         print("Bird sleep")

#     def hunt(self):
#         print("Bird hunt")


# class Fish:
#     name = "Name"
#     color = "Orange"
#     weight = 3.56


# class Market:

#     def __init__(self):
#         self.database = []

#     def add_product(self, name, price):
#         self.database.append({
#             "name":name,
#             "price":price
#         })

#     def get_products(self):
#         for i in self.database:
#             print(f"\nName -> {i['name']}")
#             print(f"Price -> {i['price']}\n")

#     def remove_product(self, name):
#         for i in self.database:
#             if i['name'] == name:
#                 self.database.remove(i)


# makro = Market()
# makro.add_product("Pepsi", 13000)
# makro.add_product("Coca-Cola", 12000)
# makro.add_product("Non", 3000)
# makro.remove_product("Non")
# makro.get_products()
