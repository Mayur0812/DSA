class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.key = key

def sum(root):
    if (root == None):
        return 0
    total_sum = sum(root.left) + root.key + sum(root.right)
    return total_sum
    
def sum_tree(root):
    if root == None or (root.left == None and root.right == None):
        return True
    ls = sum(root.left)
    rt = sum(root.right)

    if (root.key == ls + rt) and sum_tree(root.left) and sum_tree(root.right):
        return True
    
    return False    
        

if __name__ == '__main__':
    root = Node(26)
    root.left = Node(10)
    root.right = Node(6)
    if(sum_tree(root)):
        print("Balanced")
    else:
        print("Not balanced")