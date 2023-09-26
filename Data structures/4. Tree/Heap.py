# Basic binary tree implementation in Python 3

import heapq

_list = [3,4,1,2,5]

heapq.heapify(_list)

print("Heap: ")
print(list(_list))

heapq.heappush(_list,6)

print("Modified heap: ")
print(list(_list))

print("Smallest element in heap is: ")
print(heapq.heappop(_list)) 