from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows = len(grid)
        cols = len(grid[0])

        q = deque()

        # 第一步：找到所有宝箱
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        # 第二步：定义上下左右四个方向
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        # 第三步：开始 BFS
        while q:

            r, c = q.popleft()

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # 判断是否越界
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                # 只访问还没有计算距离的陆地
                if grid[nr][nc] != 2147483647:
                    continue

                # 更新距离
                grid[nr][nc] = grid[r][c] + 1

                # 加入队列
                q.append((nr, nc))