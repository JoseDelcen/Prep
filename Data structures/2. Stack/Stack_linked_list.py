# Basic stack implementation using linked lists in Python 3

# Node class
class Node:
    # Each node will contain a value and a pointer to the next node of the linked list
    def __init__(self, value=None):
        self.value = value
        self.next = None
        
# Stack (linked list) class
class Stack:
    
    # Initialization of the stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0
    
    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
    
    def pop(self):
        if self.isEmpty:
            raise Exception("Stack is empty")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value