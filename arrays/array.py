"""
Lists/Arrays
    Complexities:
        - Append: O(1)
        - Indexing: O(1)
        - Insert: O(N)
        - Popping: O(1) if the end of the list, else O(N)
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

arr = [-1,0,1,2,-1,-4]
print(three_sum(arr))

