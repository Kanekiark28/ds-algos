import heapq

arr = [99,88,66,223,12,33,10,25]
type(arr)
heapq.heapify(arr)
print(arr)
heapq.heappush(arr,787878)
print(arr)
type(arr)