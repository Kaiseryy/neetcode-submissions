# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            #积累：先写最边界的条件，就是在末尾None的时候 return什么
            if not root:
                return [True,0]
            
            left , right = dfs(root.left),dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1]-right[1])<=1
            #积累：在常规迭代阶段，是返回什么
            return [balanced, 1+max(left[1],right[1])]
        return dfs(root)[0]
    
    
        