import os
os.system("cls")
import math

# class Triangle:
    # def __init__(self, a, b, c):
    #     self.a = a
    #     self.b = b
    #     self.c = c

    # def perimetr(self):
    #     return self.a + self.b + self.c

    # def yuza(self):
    #     p = self.perimetr()/2
    #     S = p * (p - self.a) * (p - self.b) * (p - self.c)
    #     return S ** (1/2)

# class Circle:
    # def __init__(self, radius):
    #     self.radius = radius

    # def perimetr(self):
    #     return (2 * 3.1415 * self.radius)

    # def yuza(self):
    #     return 3.1415 * self.radius ** 2
    
# class Rectangle:
    # def __init__(self, a, b):
    #     self.a = a
    #     self.b = b

    # def perimetr(self):
    #     return 2 * (self.a + self.b)

    # def yuza(self):
    #     return self.a * self.b
    

# shape = input("Shakl nomini kiriting -> ")
# match (shape):
#     case "triangle":
#         uchbur = Triangle(3, 4, 5)
#         print("Perimetr triangle: ", uchbur.perimetr())
#         print("Yuza triangle: ", uchbur.yuza())
    
#     case "circle":
#         aylana = Circle(3)
#         print("Perimetr circle: ", aylana.perimetr())
#         print("Yuza circle: ", aylana.yuza())

#     case _:
#         print("Error!")


class Subject:
    def __init__(self):
        self.subs = []

    def addSubjects(self):
        self.name = input("Name: ")
        self.credit = int(input("Credit: "))
        self.score = int(input("Score: "))
        ms = int(input("Modern Subject -> Yes(1) No(0): "))
        if ms:
            self.modernSubject = True
        else:
            self.modernSubject = False

        self.subs.append([self.name, self.credit, self.score, self.modernSubject])

    def changeSubjects(self, name):
        for i in range(len(self.subs)):
            if self.subs[i][0] == name:
                print(f"Previous Credit -> {self.subs[i][1]}")
                self.subs[i][1] = int(input("New Credit: "))

    def removeSubject(self, name):
        check = False
        for i in self.subs:
            if i[0] == name:
                check = True
                self.subs.remove(i)
                break
        if check == True:
            print("Removed")
        else:
            print("Not in this list!")

    def viewSubjects(self):
        for i in self.subs:
            print(f" {self.name}\n {self.credit}\n {self.score}\n {self.modernSubject}")

    def sortSubjects(self):
        res = sorted(self.subs, key = lambda x: x[1])
        self.subs = res.copy()
        for i in self.subs:
            print(f" {self.name}\n {self.credit}\n {self.score}\n {self.modernSubject}")
        
sub = Subject()
while 1:
    op = int(input("To add subject press 1: "))
    if op != 1:
        break
    sub.addSubjects()

os.system("cls")
sub.viewSubjects()
sub.changeSubjects("History")
print("-----After changes-----")
sub.viewSubjects()
print("After Sorting")
sub.sortSubjects()
name = input("Subject name: ")
sub.removeSubject(name)













