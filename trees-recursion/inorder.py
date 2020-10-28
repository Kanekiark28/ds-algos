"""
Inorder traversal of BST
Order: LNR
"""

from collections import deque

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
    
    def max_depth(self,root):
        if not root:
            return 0
        
        leftHeight = self.max_depth(root.left)
        rightHeight = self.max_depth(root.right)
        
        return max(leftHeight,rightHeight)+1
    
    def isSymmetric(self, root):
        #if not root == isSymmetric!
        if not root:
            return True
        
        return self.isSymmetricLeftRight(root.left,root.right)
    
    def isSymmetricLeftRight(self,left,right):
        #check if both are none or tree is unbalanced
        if not left or not right:
            return left == right
        #if left == right check if left.left == right.right
        elif left.val == right.val and self.isSymmetricLeftRight(left.left,right.right) and self.isSymmetricLeftRight(left.right,right.left):
            return True
        
    def isSameTree(self,p,q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
            return True
        
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        
        lHeight = self.max_depth(root.left)
        rHeight = self.max_depth(root.right)
        lDiameter = self.diameterOfBinaryTree(root.left)
        rDiameter = self.diameterOfBinaryTree(root.right)
        
        return max((lHeight+rHeight),max(lDiameter,rDiameter))
    
    def validateBST(self,root):
        return self.validate(root,None,None)
    
    def validate(self,root,minimum,maximum):
        if not root:
            return True
        elif not minimum and root.val<=minimum or not maximum and root.val >= maximum:
            return False
        else:
            return self.validate(root.left,minimum,root.val) and self.validate(root.right,root.val,maximum)
    
    def levelOrder(self,root):
        res = []
        if not root:
            return res
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            currlevel = []
            for i in range(size):
                item = q.popleft()
                currlevel.append(item.val)
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
            res.append(currlevel)
        return res
    
    def rightSidedView(self,root):
        res = []
        if not root:
            return res
        
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                if i == size - 1:
                    res.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        
        return res
    
    def kthSmallest(self,root,k):
        res = []
        self.kinorder(root,k,res)
        return res[k-1]
    
    def kinorder(self,root,k,res):
        if root:
            self.kinorder(root.left,k,res)
            res.append(root.val)
            self.kinorder(root.right,k,res)

    
arr = [1,2,3,5,4]
root = Node(1)
root.right = Node(3)
root.left = Node(2)
root.left.right = Node(5)
root.right.right = Node(4)
print(root.rightSidedView(root))
    
        


        
                
                    