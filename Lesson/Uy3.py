import os
os.system("cls")

#1
class Book:

    def __init__(self, name, author, price, publisher):
        self.name = name
        self.author = author
        self.price = price
        self.publisher = publisher

    def set_info(self, lst):
        self.name = input("Name: ")
        self.author = input("Author: ")
        self.price = int(input("Price: "))
        self.publisher = input("Publlisher: ")
        lst.append(Book(self.name, self.author, self.price, self.publisher))

    def get_info(self):
        return f'''
        Name: {self.name}
        Author: {self.author}
        Price: {self.price}
        Publisher: {self.publisher}'''

book1 = Book("Queen of Fire", "Devika Rangachari", 100, "Pearson")
book2 = Book("Hear Yourself", "Prem Rawat", 80, "Harper Collins")
book3 = Book("Tomb of Sand", "Geetanjali Shree's", 120, "Simon")
book4 = Book("Monsoon", "Sahitya Akademi", 90, "Schuster")
book5 = Book("The Little Book of Joy", "Dalai Lama & Desmond Tutu", 120, "Macmillan")
lst = [book1, book2, book3, book4, book5]
book5.set_info(lst)

for i in lst:
    if i.publisher[0] >= "A" and i.publisher[0] <= "H":
        print(i.get_info())



#2
# class PC:

#     def __init__(self, name, ram, price, processor):
#         self.name = name
#         self.ram = ram
#         self.price = price
#         self.processor = processor

#     def set_info(self, lst):
#         self.name = input("Name: ")
#         self.ram = int(input("Ram: "))
#         self.price = int(input("Price: "))
#         self.processor = input("Processor: ")
#         lst.append(PC(self.name, self.ram, self.price, self.processor))

#     def get_info(self):
#         return f'''
#         Name: {self.name}
#         Ram: {self.ram}
#         Price: {self.price}
#         Processor: {self.processor}'''

# PC1 = PC("Asus", 32, 1200, "Core i9-12th")
# PC2 = PC("Acer", 16, 1000, "Core i7-12th")
# PC3 = PC("HP", 12, 800, "Core i5-12th")
# PC4 = PC("Lenovo", 8, 700, "Core i3-12th")
# lst = [PC1, PC2, PC3, PC4]
# PC4.set_info(lst)

# for i in lst:
#     if i.ram > 4 and i.ram < 16:
#         print(i.get_info())



#3
# class Club:

#     def __init__(self, name, team, trainer, capitan):
#         self.name = name
#         self.team = team
#         self.trainer = trainer
#         self.capitan = capitan

#     def set_info(self, clubs):
#         self.name = input("Name: ")
#         self.team = input("Team: ")
#         self.trainer = input("Trainer: ")
#         self.capitan = input("Captain: ")
#         clubs.append(Club(self.name, self.team, self.trainer, self.capitan))

#     def get_info(self):
#         return f'''
#         Name: {self.name}
#         Team: {self.team}
#         Trainer: {self.trainer}
#         Capitan: {self.capitan}'''

#     def sorting(self, clubs):
#         clubs.sort(key=lambda i: i.name)
#         for i in clubs:
#             print(i.get_info())

#     def new_club(self, clubs, search):
#         os.system("cls")
#         for i in clubs:
#             if i.name == search:
#                 print(i.get_info())
#                 exit(1)
#         print(f"{search} doesn't exist")

# club1 = Club("Real Medrid", 12, "Wunchi", "Duchon")
# club2 = Club("Marcelona", 15, "Kurman", "Yemen")
# club3 = Club("United Chester", 13, "Derman", "Bob")
# club4 = Club("Julentus", 12, "Fernando", "Solah")
# club5 = Club("Maroco", 14, "Gun Mi", "John")
# clubs = [club1, club2, club3, club4, club5]
# club5.set_info(clubs)

# club1.sorting(clubs)
# club1.new_club(clubs, input("\nEnter the name of a club -> "))