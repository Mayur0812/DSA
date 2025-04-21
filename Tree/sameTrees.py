class Solution:
    def sameTree(self, p, q):
        if p==None and q == None:
            return True
        
        if p == None or q == None:
            return False
        
        if p.val!=q.val:
            return False
        

        left = self.sameTree(p.left, q.left)
        right = self.sameTree(p.right, q.right)

        return left and right