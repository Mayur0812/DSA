class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def level(root, node,lev):
    """
    will return level of each node
    """
    if root == None:
        return 0
    #print(f"Solving level for: {root.key} with value of level: {lev} and node: {node}")
    if root.key == node:
        print(f"----- Found node : {root.key} at level: {lev}")
        return lev
    lev +=1
    
    return max(level(root.left, node, lev),level(root.right, node , lev))

def isSibling(root, node1, node2):
    """
    chekcing if two nodes are sibling or not
    """
    if root is None:
        return False
    
    if (root.left.key==node1 and root.right.key==node2) or (root.left.key==node2 and root.right.key==node1) or isSibling(root.left, node1, node2) or isSibling(root.right, node1,node2):
        return True


def is_cousins(root, node1, node2):
    """
    approach:
        1. If they are at the same level
        2. different paranets
    """
    if root == None or node1 == None or node2 == None:
        return False
    level1 = level(root,node1,0)
    level2 = level(root,node2,0)
    print(f"Level of {node1} is {level1} and level of :{node2} is {level2}")
    if (level1 == level2):
        if (isSibling(root,node1,node2)):
            print("No they are not siblings")
        else:
            print("Both are siblings")
    else:
        print("Both are not siblings")

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(15)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)

    is_cousins(root,4,5)