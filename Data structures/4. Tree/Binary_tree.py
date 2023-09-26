# Basic binary tree implementation in Python 3

# Node class. Each node will have a particualr value and pointers to the left and right childs
class Node():
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
        
if __name__ == "__main__":
    # Create root
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    
    """ 1 
       / \
      2   3
     / \ / \
    N  N N  N
    """
    