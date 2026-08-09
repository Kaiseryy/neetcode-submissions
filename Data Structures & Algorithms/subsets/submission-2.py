class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = [] 

        def dfs(i):
            #终止条件
            if i >= len(nums):
                #只记录当时那个subset的内容
                res.append(subset.copy())
                return
            
            subset.append(nums[i])# 决定"要"：记下来
            dfs(i+1)  # 去处理下一个元素
            subset.pop()# 撤掉，恢复原状决定"不要"
            dfs(i+1)  # 决定"不要"：直接去处理下一个
        
        
        dfs(0)
        return res
            

            
        