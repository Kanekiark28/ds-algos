"""
Lists/Arrays
    Complexities:
        - Append: O(1)
        - Indexing: O(1)
        - Insert: O(N)
        - Popping: O(1) if the end of the list, else O(N)
        
Problem Types:
    - Two Pointers
    - Case by Case Analysis
    - 2D Matrix Manipulation
    - 
    
"""

def max_three_elements(array):
    if len(array) < 3:
        return array
    a = b = c = -float('inf')
    for elem in array:
        if elem > c:
            a = b
            b = c
            c = elem
        elif elem > b:
            a = b
            b = elem
        elif elem > a:
            a = elem
    return [a,b,c]

def max_area(height):
    
    start = 0
    end = len(height)-1
    area = 0
    
    while start <= end:
        
        pivot = min(height[start],height[end])
        area = max(area, pivot*(end-start))
        
        if height[start] > height[end]:
            end -= 1
        else:
            start += 1
    return area

def three_sum(array):
    res = []
    array.sort()
    
    for i in range(len(array)):
        if i == 0 or (i > 0 and array[i] != array[i-1]):
            low = i + 1
            high = len(array)-1
            comp = 0 - array[i]
            while low < high:
                if comp == array[low]+array[high]:
                    res.append([array[low],array[high],array[i]])
                    while low < high and array[low] == array[low+1]:
                        low += 1
                    while low < high and array[high] == array[high-1]:
                        high -= 1
                    low += 1
                    high -= 1
                elif comp < array[low]+array[high]:
                    high -= 1
                elif comp > array[low]+array[high]:
                    low += 1
    return res

def next_permutation(nums):
    k = len(nums) - 2
    
    while k >= 0 and nums[k+1] <= nums[k]:
        k -= 1
        
    if k == -1:
        reverseList(0,len(nums)-1,nums)
        return nums
    
    for i in range(len(nums)-1,-1,-1):
        if nums[i] > nums[k]:
            temp = nums[i]
            nums[i] = nums[k]
            nums[k] = temp
            break
    
    reverseList(k+1,len(nums)-1,nums)
    return nums
    
def reverseList(start,end,nums):
    while start <= end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start += 1
        end -= 1
    

"""
Given a 2D array rotate it 90 degrees
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
"""

def rotate_ninety(matrix):
    
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    
    for i in range(len(matrix)):
        for j in range(len(matrix)//2):
            matrix[i][j],matrix[i][len(matrix)-1-j] = matrix[i][len(matrix)-1-j],matrix[i][j]
    return arr
arr = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate_ninety(arr))



