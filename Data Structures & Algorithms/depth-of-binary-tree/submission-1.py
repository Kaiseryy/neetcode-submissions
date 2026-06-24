# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #初始化栈
        stack = [[root,1]]
        res = 0

        while stack:
            #先获取stack的信息
            node,depth = stack.pop()

            if node:
                #如果节点不为空，res就可以更新深度
                res = max(res,depth)
             
                 
                #继续加入两边的节点，然后深度也先假设存在（一会儿循环会验证）
                stack.append([node.left,depth+1])
                stack.append([node.right,depth+1])
              
        return res
    
        