# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False

       #剩下都不为空或者都为空的情况。那就从头开始匹配，根结点，左右子树，一直匹配下去。
       #从根节点起完全匹配
        if self.sameTree(root, subRoot):
            return True
       #往下找左右子树
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right ,subRoot))
    
    def sameTree(self, root: Optional[TreeNode],subRoot:Optional[TreeNode])-> bool:
        #这个是递归的终止条件（正向）
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left,subRoot.left)and self.sameTree(root.right,subRoot.right))
            
        return False
        


        