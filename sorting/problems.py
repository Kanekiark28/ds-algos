"""

Given a collection of intervals, merge all overlapping intervals.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

"""

def merge_intervals(intervals):
    
    stack = []
    
    intervals.sort(key=lambda x: x[0])
    
    for interval in intervals:
        
        if not stack or (stack[-1][-1] <= interval[0]):
            stack.append(interval)
        else:
            stack[-1][-1] = max(stack[-1][-1], interval[1])
            
    return stack

"""
Given a list of non-negative integers nums, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.

Input: nums = [10,2]
Output: "210"

"""
from functools import cmp_to_key

def largest_number(nums):
    if not any(nums):
        return "0"
    
    #convert to strings
    nums = list(map(str,nums))
    #sort by concatenation of strings
    nums.sort(key=cmp_to_key(lambda x,y: 1 if x+y > y+x else -1 if x+y < y+x else 0),reverse=True)
    return "".join(nums)

print(largest_number([10,2]))


"""

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:

Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?
 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

nums = [2,0,2,1,1,0]
        s
        i
                  e   

"""

def sort_colors(nums):
    
    start = 0
    end = len(nums)-1
    idx = 0
    
    while start <= end and idx <= end:
        if nums[idx] == 0:
            nums[idx] = nums[start]
            nums[start] = 0
            start += 1
            idx += 1
        elif nums[idx] == 2:
            nums[idx] = nums[end]
            nums[end] = 2
            end -= 1
        else:
            idx += 1
    return nums


nums = [2,0,2,1,1,0]
print(sort_colors(nums))          
    