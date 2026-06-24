# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre = ind = 0

        def dfs(limit):
            nonlocal pre,ind
            
            #两个终止条件
            if pre >= len(preorder):
                return None
            
            #子树的末尾是None，那它的上一个是真实的最后一个 也就是中序的第一个值
            if inorder[ind] == limit:
                ind +=1
                return None
            

            #递归的核心机制
            root = TreeNode(preorder[pre])
            pre +=1
            #左子树的上界就是上一个中间点
            root.left = dfs(root.val)
            #其实这一步是最难理解的，中序遍历来说，小子树的右边最后一个的上界是往上的一个树的左子节点
            root.right = dfs(limit)
            return root
        
        return dfs(float("inf"))

        
        