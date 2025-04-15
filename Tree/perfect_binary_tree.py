class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def depth(root):
    """
    """
    d = 0
    if root is None:
        return 0
    while (root!=None):
        d +=1
        root = root.left
    return d


def pbt(root,level):
    """
    """
    if (root == None):
        return True

    if (root.left != None and root.right == None) or (root.right != None and root.left == None):
        return False
    
    d = depth(root)

    if(root.left==None and root.right==None and d==level):
        return True
    if(root.left==None and root.right==None and d+1!=level):
        print(f"Not at same level: {root.key,d,level}")
        return False
   
    return (pbt(root.left,level+1) and pbt(root.right,level+1))


if __name__ == '__main__':
    root = Node(10) 
    root.left = Node(20) 
    root.right = Node(30) 
 
    root.left.left = Node(40) 
    root.left.right = Node(50) 
    root.right.left = Node(60) 
    root.right.right = Node(70)
    root.right.right.left = Node(30)
    if(pbt(root,0)):
        print("Yes")
    else:
        print("No")
        