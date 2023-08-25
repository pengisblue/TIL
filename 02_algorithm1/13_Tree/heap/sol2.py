# from queue import PriorityQueue
import heapq
arr = [7, 2, 5, 3, 4, 6]
# que = PriorityQueue()
# for num in arr:
#     que.put(num)

heapq.heapify(arr)
print(arr)