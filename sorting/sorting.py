"""
Quick Sort: Average Case: O(nlogn)
Space: Inplace O(1)
"""


def quickSort(nums,low,high):
    if low < high:
        #partition takes high as pivot and sorts the elements around it, returning the pivot
        partition_idx = partition(nums,low,high)
        quickSort(nums,low,partition_idx-1)
        quickSort(nums,partition_idx+1,high)
    

def partition(nums,low,high):
    
    #take the last element as pivot
    pivot = nums[high]
    i = (low-1)
    
    for j in range(low,high):
        
        if nums[j] <= pivot:
            i += 1
            nums[i],nums[j] = nums[j],nums[i]
    
    nums[i+1],nums[high]= nums[high],nums[i+1]
    return (i+1)

arr = [10,80,30,90,40,50,70,412412,3,2,31,321,4,12,51,613,6,16,13,52,4,123,12,312,4,6,4,5,5,3,45,2,342,34,2,32,32,142,41,241,4,12,41,4,1,42,14,214,12,412,31,312,31,3123]
quickSort(arr,0,len(arr)-1)
print(arr)