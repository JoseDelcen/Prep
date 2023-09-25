# Basic queue implementation using the Queue module in Python 3

from queue import Queue

q = Queue(maxsize=3)

q.put("a")
q.put("b")
q.put("c")

print("Is the queue full?: ", q.full())

print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())

print("\nIs the queue empty?: ", q.empty())

