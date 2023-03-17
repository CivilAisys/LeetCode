# 解法1 DFS 並搭配使用一個visited的矩陣來做輔助
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        # 矩陣的長寬
        m, n = len(board), len(board[0])
        # 輔助用visited矩陣 與傳入矩陣大小一致
        visited = [[False]*n for _ in range(m)]
        
        # 對矩陣中的每個字母進行DFS查詢
        for i in range(m):
            for j in range(n):
                if(self.search(board,word,0,i,j,visited)):
                    return True

        return False
    #idx 為word要比對的索引 
    def search(self, board, word, idx, i, j, vistied) -> bool:
        m, n = len(board), len(board[0])
        # 終止條件
        # 查找的idx已經超過了word本身 回傳true
        if idx == len(word):
            return True
        # 越界 or 已經被查找過 or 查找到的不符合 回傳False
        if i < 0 or j < 0 or i >= m or j >= n or vistied[i][j] or word[idx] != board[i][j]:
            return False
        # 標記為已遍歷過
        vistied[i][j] = True
        # 上下左右只要一個符合遍回傳True
        result = self.search(board, word, idx+1, i-1, j, vistied) or self.search(board, word, idx+1, i+1, j,
                vistied) or self.search(board, word, idx+1, i, j-1, vistied) or self.search(board, word, idx+1, i, j+1, vistied)
        # 全部遍歷完後重新標記為False  已讓後續能夠繼續重複使用
        vistied[i][j] = False
        return result
        
test = Solution()
print(test.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))