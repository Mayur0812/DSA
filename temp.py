class Tree:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

    def preOrder_traverse_tree(self,node):
        if node:
            print(node.key, end = " ")
            self.preOrder_traverse_tree(node.left)
            self.preOrder_traverse_tree(node.right)



root = Tree(3)
root.left = Tree(1)
root.right = Tree(4)
root.preOrder_traverse_tree(root)