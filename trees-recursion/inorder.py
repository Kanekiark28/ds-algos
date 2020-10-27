"""
Inorder traversal of BST
Order: LNR
"""

class Node:
    
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
    
    #Insert Node
    def insert(self, val):
        
        if self.val:
            if val < self.val:
                if not self.left:
                    #Create a new node on left st
                    self.left = Node(val)
                else:
                    #Insert to left val
                    self.left.insert(val)
            elif val > self.val:
                if not self.right:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = Node(val)
    
    def inorder(self, root):
        res = []
        self.recurse(root,res)
        return res
    
    def recurse(self, root,res):
        if root:
            self.recurse(root.left,res)
            res.append(root.val)
            self.recurse(root.right,res)
            
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inorder(root))

        
                
                    