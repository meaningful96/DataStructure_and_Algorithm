# Deep Learning for AI engineer
"""
Created on Youminkk


Nil sine magno vitae labore dedit mortalibus
"""

class Node:
    def __init__(self,key):
        self.key = key
        self.parent = self.right = self.left = None
    
    def __str__(self):
        return str(self.key)

a = Node(6)
b = Node(9)
c = Node(1)
d = Node(5)
a.left = b
a.right = c
b.parent = c.parent = a
b.left = d
d.paren = b