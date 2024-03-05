import os
from random import randint as r
os.system("cls")

# Binar daraxtda ma'lumotlar chiqarishni(Traversal o'tish) 2 xil ko'rinishda amalga oshirsa bo'ladi:
# 1. InorderTraversal left -> root -> right ->
# 2. PreorderTraversal root -> left -> right ->
# 3. PostorderTraversal left -> right -> root ->


# class Node:
#     def __init__(self, data):
#         self.left = None
#         self.data = data
#         self.right = None

#     def printTree(self):
#         if self.left:
#             self.left.printTree()
#         print(self.data, end = " -> ")
#         if self.right:
#             self.right.printTree()

#     def addRoot(self, item):
#         if self.data > item:
#             if self.left is None:
#                 self.left = Node(item)
#             else:
#                 self.left.addRoot(item)

#         elif self.data < item:
#             if self.right is None:
#                 self.right = Node(item)
#             else:
#                 self.right.addRoot(item)
        
#         else:
#             self.data = item

# root = Node(r(1, 50))
# root.addRoot(r(1, 50))
# root.addRoot(r(1, 50))
# root.addRoot(r(1, 50))
# root.addRoot(r(1, 50))
# root.addRoot(r(1, 50))
# root.addRoot(r(1, 50))
# root.addRoot(r(1, 50))
# root.addRoot(r(1, 50))
# root.addRoot(r(1, 50))
# root.printTree()




class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data, end = " -> ")
        if self.right:
            self.right.printTree()

    def addRoot(self, item):
        if self.data > item:
            if self.left is None:
                self.left = Node(item)
            else:
                self.left.addRoot(item)
        elif self.data < item:
            if self.right is None:
                self.right = Node(item)
            else:
                self.right.addRoot(item)
        else:
            self.data = item
    
    def findRoot(self, item):
        if self.data > item:
            if self.left is None:
                print("404 Not Found")
            else:
                self.left.findRoot(item)
        elif self.data < item:
            if self.right is None:
                print("404 Not Found")
            else:
                self.right.findRoot(item)
        print("Root Found")
        

def inorder_Traversal(root):
    res = list()
    if root:
        res = inorder_Traversal(root.left)
        res.append(root.data)
        res = res + inorder_Traversal(root.right)
    return res

def preorder_Traversal(root):
    res = list()
    if root:
        res.append(root.data)
        res = res + preorder_Traversal(root.left)
        res = res + preorder_Traversal(root.right)
    return res

def postorder_Traversal(root):
    res = list()
    if root:
        res = res + postorder_Traversal(root.left)
        res = res + postorder_Traversal(root.right)
        res.append(root.data)
    return res


root = Node(25)
root.addRoot(13)
root.addRoot(r(1, 20))
root.addRoot(r(1, 20))
root.addRoot(r(1, 20))
root.addRoot(r(1, 20))
root.addRoot(r(1, 20))
root.addRoot(r(1, 20))
root.findRoot(13)
root.printTree()
print()
print(inorder_Traversal(root))
print(preorder_Traversal(root))
print(postorder_Traversal(root))