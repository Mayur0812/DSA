class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def mirror(root1, root2):
    if root1==None and root2 ==None:
        return True
    if root1 == None or root2 == None:
        return False
    
    return ((root1.key == root2.key)  and mirror(root1.left, root2.right) and mirror(root1.right, root2.left))

if __name__=='__main__':
    root1 = Node(1)
    root2 = Node(1)
    
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    
    root2.left = Node(3)
    root2.right = Node(2)
    root2.right.left = Node(5)
    root2.right.right = Node(4)
    
    if mirror(root1, root2):
        print ("Yes its a mirror tree ")
    else:
        print ("No, its not a mirror tree")
