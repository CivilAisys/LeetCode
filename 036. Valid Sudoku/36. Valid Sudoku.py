# 解法1
# 滿足數獨矩陣的條件為 1.行列數字皆不重複 2. 3*3的方格內的數字不重複
# 用 set 來判斷行、列和宮內是否有重複的數字
# 步驟:1.遍歷每一個格子，對於每個格子，分別記錄它所在的行、列和宮內的數字，如果有重複的數字，直接返回 False。
# 2.如果整個數狀都遍歷完了，都沒有返回 False，則返回 True。
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row_set = [set() for _ in range(9)]  # 紀錄每列的數字
        col_set = [set() for _ in range(9)]  # 紀錄每行的數字
        block_set = [set() for _ in range(9)]  # 紀錄每個九宮格的數字

        # 開始遍歷數獨矩陣  遇到.(空格)跳過 i為列 j為行
        for i in range(9):
            for j in range(9):
                num = board[i][j]  # 讀數字
                # 判斷是否為空
                if num != ".":
                    # 將之視為9個九宮格(索引0-8) (i//3)*3為確認在哪列的九宮格開頭上 j//3為要右移幾格
                    block_index = (i//3)*3 + j//3
                    # 判斷是否在行列.九宮格內有相同數字
                    if num in row_set[i] or num in col_set[j] or num in block_set[block_index]:
                        return False
                    # 加入數字至行列.九宮格內
                    row_set[i].add(num)
                    col_set[j].add(num)
                    block_set[block_index].add(num)
        return True
