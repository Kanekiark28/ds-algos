"""
Linked Lists

Append - O(1)
Lookup - O(1)
Removal - O(1)

"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def reverse_linked_list(head):
    
    prev = None
    curr = head
    while curr:
        head = head.next
        curr.next = prev
        prev = curr
        curr = head
    return prev

"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:
"""

def find_intersection(h1,h2):
    p1 = h1
    p2 = h2
    
    while p1 != p2:
        
        if not p1:
            p1 = h2
        else:
            p1 = p1.next
            
        if not p2:
            p2 = h1
        else:
            p2 = p2.next
            
    return p1


def remove_from_nth(head,n):
    
    #if only one element, return None
    if not head.next:
        return None
    
    slow = head
    fast = head
    
    for i in range(n):
        #move fast to n position
        fast = fast.next
        
    #if n == len(list)    
    if not fast:
        return head.next
    
    #move fast and slow together
    while fast:
        fast = fast.next
        slow = slow.next
    
    #connnect slow to the element after nth remoal    
    slow.next = slow.next.next
    
    return head

def add_two_numbers(l1,l2):
    
    l3 = Node(None)
    new_head = l3
    carry = 0
    
    while l1 or l2:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        ans = l1_val + l2_val + carry
        carry = ans % 10
        ans = ans // 10
        new_node = Node(ans)
        l3.next = new_node
        l3 = l3.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
            
    if carry:
        new_node = Node(carry)
        l3.next = new_node
        l3 = l3.next
    
    return new_head.next


def even_odd_list(head):
    
    if not head:
        return None
    
    even = head.next
    odd = head
    even_head = even
    
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        
        even.next = odd.next
        even = even.next
        
        
    odd.next = even.head
    
    return head
        