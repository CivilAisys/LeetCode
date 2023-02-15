# 解法1 DFS
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        # 長寬
        m, n = len(grid), len(grid[0])
        # 與grid長寬一樣的矩陣紀錄該位置是否被遍歷過
        visited = [[False]*n for _ in range(m)]
        # 島嶼數量
        result = 0
        # 開始遍歷
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0" or visited[i][j]:
                    continue
                helper(grid, visited, i, j)
                result += 1
        return result
# DFS遞歸 向該節點上下左右遍歷直到越界or遇到便利過的or為0的
def helper(grid: list[list[str]], visited: list[list[str]], x :int, y: int)->None:
    # 終止條件 1.越界 2.為0 3.已遍歷過的
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == "0" or visited[x][y]:
        return
    visited[x][y] = True
    # 上下左右
    helper(grid, visited, x-1, y)
    helper(grid, visited, x+1, y)
    helper(grid, visited, x, y-1)
    helper(grid, visited, x, y+1)
















test = Solution()
test.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])