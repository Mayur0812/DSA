class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def check_nodes(node1, node2):
    if node1 == None or node2== None:
        return False
    if (node1.key==node2.key and node1.left.key == node2.left.key) or (node1.key==node2.key and node1.right.key == node2.right.key) or check_nodes(node1.left, node2) or check_nodes(node1,node2.right):
        print(f"substrees detected for nodes: {node1.key} and {node2.key}")
        return True

def duplicate_st(root):
    if root is None:
        return False
    if check_nodes(root.left, root.right):
        print("Yes subtree exists")
    else:
        print("No is doesnt")
    
if __name__ == '__main__':
     
    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')
    root.right.right = Node('B')
    root.right.right.right = Node('E')
    root.right.right.left= Node('D')
 
    duplicate_st(root)