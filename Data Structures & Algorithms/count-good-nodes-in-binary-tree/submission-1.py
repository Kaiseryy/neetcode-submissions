# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxval):
            
            #先写终止条件：
            if not node:
                return 0
            
            current = 1 if node.val >= maxval else 0
            newmaxval = max(maxval,node.val)
            current+= dfs(node.left,newmaxval)
            current+=dfs(node.right,newmaxval)

            return current
        
        return dfs(root,root.val)

            

        