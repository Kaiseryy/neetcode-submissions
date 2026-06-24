# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #初始化一个栈
        stack = [[p,q]]

        while stack:
            #把栈里的东西取出
            node1 ,node2 = stack.pop()

            #如果p和q都为空，那直接跳过这轮（这个是识别到末尾了）
            if not node1 and not node2:
                continue
            
            #设置识别的条件(其中一个为空，或者值不一样都是false)
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            #继续取子节点
            stack.append([node1.left,node2.left])
            stack.append([node1.right,node2.right])

        
        return True
            
        