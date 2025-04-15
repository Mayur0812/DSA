class Tree:
    def __init__(self , key) -> None:
        self.left = None
        self.right = None
        self.key = key


    def preOrder_traverse_tree(self,node):
        if node:
            print(node.key, end = " ")
            self.preOrder_traverse_tree(node.left)
            self.preOrder_traverse_tree(node.right)

    def calculate_height(self, root):
        if root is None:
            return 0
        
        lheight = 1 + self.calculate_height(root.left)
        rheight = 1 + self.calculate_height(root.right)
        
        return lheight if lheight > rheight else rheight
        
            
    def BFS(self,node):
        """
        This function is to print BFS
        """
        queue = []


        

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)

ht = root.calculate_height(root)
print(ht)