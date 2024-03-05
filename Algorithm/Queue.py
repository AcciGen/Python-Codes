import queue
import os
os.system("cls")
navbat = queue.Queue(maxsize = 3)
num = queue.Queue(maxsize = 3)
ls = [False, True, "False", "True", "14", 14, 14.08]
for x in ls:
    navbat.put(x)

while navbat.empty() == False:
    n = navbat.get()

    if type(n) == str and n.isdigit() or type(n) in [int, float]:
        num.put(n)
        print(n)

# while 1:
#     x = input("Keyingi mijoz Nameni kiriting: ")
#     navbat.put(x, block = False, timeout = 3.0)
    # res = navbat.get(timeout = 25)
