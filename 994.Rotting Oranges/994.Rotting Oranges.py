# 解法1 BFS 0為空 1為新鮮 2為腐爛
# 先統計出新鮮橘子個數 並將腐爛的座標放入一個佇列quene並進行while迴圈
# 迴圈條件為佇列不為空且freshLeft>0
import collections
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # result為題目代表的分鐘數
        result, m, n, freshLeft = 0, len(grid), len(grid[0]), 0
        # 使用deque輔助遍歷 以及dir為上下左右的方向
        q = collections.deque()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # 遍歷矩陣計算新鮮橘子個數並將腐爛的橘子座標放入佇列中
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshLeft += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        # 開始遍歷  條件為佇列不為空且新鮮橘子還有剩餘
        while q and freshLeft > 0:
            # 層歷
            for index in range(len(q)):
                cur = q.popleft()
                # 上下左右遍歷
                for dir in dirs:
                    x, y = cur[0] + dir[0], cur[1] + dir[1]
                    # 若越界 or 非空或腐爛即跳過
                    if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != 1:
                        continue
                    # 將新鮮變腐爛並加入佇列中
                    grid[x][y] = 2
                    q.append((x, y))
                    freshLeft -= 1
            # 每層遍歷完 分鐘數+1
            result += 1
        # 若沒有新鮮橘子剩下  即返回分鐘數 除此-1
        return -1 if freshLeft > 0 else result


test = Solution()
test.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
