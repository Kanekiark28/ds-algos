"""
Implementation of Trees

"""

class Node:
    
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
        
def insert_left(self,child):
    if self.left is None:
        self.left = child
    else:
        child.left = self.left
        self.left = child
        
def insert_right(self,child):
    if self.right is None:
        self.right = child
    else:
        child.right = self.right
        self.right = child
        
root = Node('a')
root.val  # => 'a'
root.left  # => None

root.insert_left(Node('b'))
root.left  # => <__main__.Node object>
root.left.val  # => 'b'

root.insert_right(Node('c'))
root.right  # => <__main__.Node object>
root.right.val  # => 'c'

root.right.val = 'hello'
root.right.val  # => 'hello'    