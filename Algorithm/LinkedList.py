import os
from random import randint as r
os.system("cls")


# class Node:
#     def __init__(self, data = None):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def show(self):
#         x = self.head
#         while x is not None:
#             print(x.data, end = " -> ")
#             x = x.next
#         print("None")

#     def left_add(self, item):
#         node = Node(item)
#         if self.head == None:
#             self.head = node
#             return
#         x = self.head
#         node.next = self.head
#         self.head = node

#     def right_add(self, item):
#         node = Node(item)
#         if self.head == None:
#             self.head = node
#             return
#         x = self.head
#         while x is not None:
#             last = x
#             x = x.next
#         last.next = node

#     def between_add(self, node, item):
#         nd = Node(item)
#         if self.head == None:
#             print(f"{node} mavjud emas")
#             self.head = nd
#             return
#         x = self.head
#         while x.data != node.data:
#             last = x
#             x = x.next
#             if x is None:
#                 print("Berilgan Node mavjud emas")
#             last.next = nd
#             nd.next = x
    
#     def delete_data(self, node):
#         x = self.head
#         if x.data == node.data:
#             self.head = x.next
#             print(f"{node.data} LinkedListdan o'chirildi")
#             x = None
#             return
#         while x is not None:
#             if x.data == node.data:
#                 break
#             last = x
#             x = x.next

#         if x is None:
#             print(f"{node.data} topilmadi")
#             return
#         last.next = x.next
#         x = None
#         print(f"{node.data} LinkedListdan o'chirildi")

#     def Max(self):
#         x = self.head
#         mx = x.data
#         while x is not None:
#             if x.data > mx:
#                 mx = x.data
#             x = x.next
#         return Node(mx)

# LL = LinkedList()

# node1 = Node(r(1, 30))
# node2 = Node(r(1, 30))
# node3 = Node(r(1, 30))
# node4 = Node(r(1, 30))

# LL.head = node1
# node1.next = node2
# node2.next = node3
# node3.next = node4

# LL.show()
# LL.delete_data(LL.Max())
# LL.show()


lst = [1, 2]
print(lst == lst[::-1])
print(int("101", 2))