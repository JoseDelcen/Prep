# Basic Doubly linked list implementation in Python 3

# Node class
class Node:
    # Each node will contain a value and a pointer to the next node of the linked list
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None
        
# Singly linked list class
class singlyLinkedList:
    
    # Initialization defining the head and tail of the list
    def __init__(self):
        self.head = None
        self.tail = None 
        
    # Iteration function
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    # Insert function
    def insertNode(self, value, location):
        newNode = Node(value)
        
        if self.head is None: # Empty list
            self.head = newNode
            self.tail = newNode
            
        else: # List not empty
            if location == 0: # First node
                newNode.next = self.head
                self.head = newNode
            elif location == 1: # Last node
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                nextNode = currentNode.next
                currentNode.next = newNode
                newNode.next = nextNode
    
    # Traverse list
    def traverse(self):
        if self.head is None:
            print("List does not exist")
        else:
            node_num = 0
            node = self.head
            while node is not None:
                print("Value of node ", node_num, " is " node.value)
                node_num += 1
                node = node.next
    
    # Search for a specific value in the list
    def searchValue(self, target):
        node = self.head
        if self.head is None:
            print("List is empty")
        else:
            while node is not None:
                if node.value == target:
                    return "Value appears in the list"
                node = node.next
            return "Values does not appear in the list"
        
    def deleteNode(self, location):
        if self.head is None:
            print("List does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        #node = node.next
                        node.next = None
                        self.tail = node
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                nextNode = currentNode.next
                currentNode.next = nextNode.next