import os
os.system("cls")

# from collections import Counter
# lst = list(map(str, input().split()))
# print(Counter(lst))


# class projector:

#     def __init__(self):
#         self.model = ""
#         self.price = 0

#     def input_data(self, m, p):
#         self.model = m
#         self.price = p

#     def show_projector(self):
#         print(f"{self.model} <-> {self.price}")

# nvm = projector()
# nvm.input_data(input("Model :> "), int(input("Price :> ")))
# nvm.show_projector()



class phone:

    def __init__(self, m, p, r, b, cm):
        self.model = m
        self.price = p
        self.ram = r
        self.battery = b
        self.camera = cm

    def show(self):
        print(f"{self.model} <-> {self.price} <-> {self.ram} <-> {self.battery} <-> {self.camera}")

phones = []
num = int(input("Number of phones -> "))
for x in range(num):
    m = input("Model: ")
    p = int(input("Price: "))
    r = input("Ram: ")
    b = input("Battery: ")
    c = input("Camera: ")
    phones.append(phone(m, p, r, b, c))

os.system("cls")
for i in range(len(phones)-1):
    for j in range(i+1, len(phones)):
        if phones[i].model < phones[j].model:
            phones[i], phones[j] = phones[j], phones[i]

for x in phones:
    x.sho



