from collections import deque
# #第一阶段：准备工作
#     │
#     ├── 获取地图的行数、列数
#     ├── 创建 visit
#     └── 创建队列 q
#     │
#     ▼
# 第二阶段：找到所有宝箱
#     │
#     ├── 遍历整个 grid
#     └── 把所有宝箱加入队列
#     │
#     ▼
# 第三阶段：BFS
#     │
#     ├── 从队列取出格子
#     ├── 更新它距离宝箱的距离
#     ├── 把四周可以访问的格子加入队列
#     └── 按层重复，直到队列为空

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        Rows = len(grid)
        Cols = len(grid[0])
        visit = set()

        q = deque()
        #统计所有没有探索过的岛屿（宝藏已经探索过了）
        def addCell(r,c):
            if (min(r,c)<0 or r==Rows or c== Cols or (r,c) in visit or grid[r][c]==-1):
                return
            
            #如果visit过了一遍了，下一次再过它的时候就要直接跳过了，不能继续排队了。
            visit.add((r,c))
            #没有到边界的岛屿可以继续加入队列排队，一直等到最后找到
            q.append([r,c])

        #收集宝藏
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] ==0:
                    q.append([r,c])
                    visit.add((r,c))
        
        dist = 0 
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] =dist
                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c+1)
                addCell(r,c-1)
            dist+=1



