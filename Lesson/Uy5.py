import os
from datetime import datetime
os.system("cls")

#1
# class Book:
#     def __init__(self):
#         self.lst = []

#     def addBook(self):
#         self.__name = input("Name: ")
#         self.page = int(input("Pages: "))
#         self.price = int(input("Price: "))
#         self.lst.append([self.__name, self.page, self.price])

#     def showBooks(self):
#         for i in self.lst:
#             print(f"\nName- -> {i[0]}\nPages- -> {i[1]}\nPrice- -> {i[2]}\n")

#     def priceX2(self):
#         for i in self.lst:
#             if "Programming" in i[0]:
#                 i[2] *= 2
#         self.showBooks()

#     def PagePrice(self):
#         cntPage = 0
#         cntPrice = 0
#         for i in self.lst:
#             cntPage += i[1]
#             cntPrice += i[2]

#         print(f"Barcha kitoblarni 1ta pageni o'rtacha narxi -> {cntPage/cntPrice}")
#         print()

# books = Book()
# while 1:
#     op = int(input("Press 1 if you will add a book: "))
#     if op != 1:
#         os.system("cls")
#         break
#     os.system("cls")
#     books.addBook()

# print("--Before The Raising Of Prices--")
# books.showBooks()
# input("Press Enter To Continue\n")
# os.system("cls")
# print("--After The Raising Of Prices--")
# books.priceX2()
# books.PagePrice()



#2
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

class Drug(Date):
    def __init__(self, drug_name, date_create, company_name):
        self.drug_name = drug_name
        self.date_create = date_create
        self.company_name = company_name

    def daysBetween(self):
        release_date = datetime(year=int(self.date_create[2]), month=int(self.date_create[1]), day=int(self.date_create[0]))
        today = datetime.now()
        days_passed = (today - release_date).days
        print(f"Passed days: {days_passed}")

    def show(self):
        print(f"\nDrug name: {self.drug_name}\nDate of creation: {self.date_create[0]}/{self.date_create[1]}/{self.date_create[2]}\nCompany name: {self.company_name}")

name = input("Drug name -> ")
date = list(input("Date of creation -> ").split("."))
company = input("Company name -> ")
drug1 = Drug(name, date, company)
drug1.show()
drug1.daysBetween()



#3
# class Card:
#     def __init__(self):
#         self.lst = []

#     def addCard(self, password = 5555):
#         self.person = input("Person: ")
#         self.__number = int(input("Card number: "))
#         self._expiration = input("Expiration: ")
#         self.cash = int(input("Cash: "))
#         self.password = password
#         self.lst.append([self.person, self.__number, self._expiration, self.cash, self.password])

#     def changePassword(self, person):
#         verification = int(input("Enter the default password -> "))
#         for i in self.lst:
#             if person in i[0]:
#                 if verification == self.password:
#                     new = int(input("Enter new password -> "))
#                     i[4] = new
#                     print("Changed successfully")
#                 else:
#                     print("Error)")
    
#     def sortCash(self):
        # res = sorted(self.lst, key = lambda x: x[3], reverse=True)
#         self.lst = res.copy()
#         self.showCards()

#     def showCards(self):
#         print()
#         for i in self.lst:
#             print(f"Person: {i[0]} Number: {i[1]} Expiration: {i[2]} Cash: {i[3]} Password: {i[4]}")

# cards = Card()
# while 1:
#     op = int(input("Press 1 if you will add a book: "))
#     if op != 1:
#         os.system("cls")
#         break
#     os.system("cls")
#     cards.addCard()

# name = input("Name -> ")
# cards.changePassword(name)
# cards.sortCash()         