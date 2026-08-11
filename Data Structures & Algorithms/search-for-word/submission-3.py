class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        #先确定行 和 列，行就是元素个数，列就是单个元素中有多少
        Rows = len(board)
        Cols = len(board[0])

        def dfs(r, c ,i):
            #先写清楚：什么时候算通过
            if i== len(word):
                return True
            
            #再写清楚边界以及错误情况
            if( r<0 or c<0 or r>= Rows or c>= Cols or word[i]!=board[r][c] or board[r][c] == "#"):
                return False
            
            #下面是匹配过程正常的情况
            board[r][c] = "#"
            
            res = (dfs(r+1, c  ,i+1) or dfs(r-1, c, i+1) or dfs(r, c+1 ,i+1) or dfs(r,c-1,i+1))
            

            board[r][c] = word[i]# 这一步很重要（你不复原，下次从别的地方出发路过这里，还以为这里用过了）
            

            return res
        
        for r in range(Rows):
            for c in range(Cols):
                if dfs(r,c,0):
                    return True
        return False
        