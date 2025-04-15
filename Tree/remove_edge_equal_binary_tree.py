class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def countNodes(root):
    """
    """
    if root == None:
        return 0
    return (1 + countNodes(root.left) + countNodes(root.right))


def remEdge(root):
    """
    
    """
    if root == None:
        return False
    
    if(countNodes(root.right)==(countNodes(root.left)-1)) or (countNodes(root.left)==(countNodes(root.right)-1)):
        print("Yes")
    else:
        print("False")

if __name__=='__main__':
    root = Node(5) 
    root.left = Node(1) 
    root.right = Node(6) 
    root.left.left = Node(3) 
    root.right.left = Node(7) 
    root.right.right = Node(4)
    remEdge(root.right)
