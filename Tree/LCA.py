class LCA:
    def findLCA(self, root,p,q):
        ## base conditions
        if not root:
            return None

        if p==root or q==root:
            return root
        
        left = self.findLCA(root.left, p,q)
        right = self.findLCA(root.right, p ,q)

        if left:
            return left
        
        return right


