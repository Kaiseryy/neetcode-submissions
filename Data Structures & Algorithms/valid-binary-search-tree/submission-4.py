# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node,left,right):
            #递归的终点
            if not node:
                return True
            
            #每次都中间的节点都会验证然后才继续看它的两个子节点
            if not (left< node.val <right):
                return False
            
            #同时左子节点和右子节点都满足
            return valid(node.left, left, node.val) and valid(node.right, node.val, right) 

        return valid(root, float("-inf"), float("inf"))
        