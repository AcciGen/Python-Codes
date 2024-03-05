import os
os.system("cls")
import random as r

def isPrime(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.insert(0, item)

    def pop_item(self):
        return self.stack.pop(0)
    
    def empty(self):
        return len(self.stack) == 0
    
    def top(self):
        return self.stack[0]

st = Stack()
stJ = Stack()
stT = Stack()
n = 10

while n:
    x = r.randint(10, 99)
    st.push(x)
    print(x)
    n -= 1

while st.empty() == False:
    num = st.top()
    if num % 2 == 0:
        print(num, "juftga qo'shildi")
        stJ.push(num)
    else:
        print(num, "toqga qo'shildi")
        stT.push(num)

    st.pop_item()