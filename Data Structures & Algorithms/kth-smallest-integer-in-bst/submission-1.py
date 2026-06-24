# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        arr = []

        
        def dfs(node):
            #递归的精髓就在于设置好结束条件
            if not node:
                return
            #递归的原则，依据二叉搜索树的原则，先左边小的，然后看中间的，再看右边大的
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)
        return arr[k-1]
        