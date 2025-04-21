## TargetSUm: Need to pass this information

class Solution:
    def hasPath(self, root, targetSum):
        def traverse(root, curr):
            if not root:
                return False
            
            if root.left == None and root.right == None:
                return curr+root.val == targetSum
            
            curr += root.val
            left = traverse(root.left, curr)
            right = traverse(root.right, curr)

            return left or right
        
        return traverse(root, 0)