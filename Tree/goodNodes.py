class Solution:
    def goodNodes(self, root):
        def traverse(node, maxSoFar):
            if not node:
                return 0
            
            left = traverse(node.left, max(maxSoFar, node.val))
            right = traverse(node.right, max(maxSoFar, node.val))

            ans = left + right

            if node.val > maxSoFar:
                ans +=1

            return ans
        traverse(root, float("-inf"))


            