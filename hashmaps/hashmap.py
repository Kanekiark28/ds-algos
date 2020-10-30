"""
HashMaps:
    - Put O(1)
    - Delete O(1)
    - Get O(1)
    
    What makes a good hashing function?
        - Deterministic
        - Elements need to be spread out
        
    When collisions happen:
        - Chaining
"""


"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

diff = 7
d[7] = 0
9-7 = 2
    return [d[2],7

"""


def two_sum(nums,target):
    d = {}
    
    for i in range(len(nums)):
        diff = target - nums[i]
        if nums[i] in d:
            return [d[nums[i]],i]
        else:
            d[diff] = i
            
"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.


"""


class Node:
    
    def __init__(self,val,next,random):
        self.val = val
        self.next = next
        self.random = random
        
def deep_copy(head):
    d = {}
    curr = head
    while curr:
        d[curr] = Node(curr.val)
        curr = curr.next
        
    curr = head
    while curr:
        d.get(curr).next = d.get(curr.next)
        d.get(curr).random = d.get(curr.random)
        curr = curr.next
        
    return d.get(head)


"""

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

def group_anagrams(strs):

    d = {}
    for word in strs:
        anagram = "".join(sorted(word))
        if anagram in d:
            d[anagram].append(word)
        else:
            d[anagram] = []
            d[anagram].append(word)
            
    return d.values()
            
print(two_sum([2,7,11,15],9))