class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(idx,path,cur):
            if cur == target:
                res.append(path.copy())
                return
            
            for i in range(idx,len(candidates)):
                #这个还挺难理解的，跳过同层的2
                if i>idx and candidates[i] == candidates[i-1]:
                    continue

                if cur + candidates[i]> target:
                    break
                
                path.append(candidates[i])
                dfs(i+1,path,cur+candidates[i])
                path.pop()
        
        dfs(0,[],0)
        return res

        