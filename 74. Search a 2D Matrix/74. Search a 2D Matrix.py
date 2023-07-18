# 將二維矩陣看做為一維數組並進行二分查找
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])  # 矩陣列行
        left, right = 0, rows * cols - 1  # 初始化左右指針

        while left <= right:
            mid = left + (right - left) // 2
            row = mid // cols  # 該中間元素在二維矩陣中的列索引
            col = mid % cols  # 該中間元素在二維矩陣中的行索引

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1  # 已經排出等於的可能性故需mid + 1
            else:
                right = mid - 1  # 能進到這裡表示mid已經被排除 故為right - 1

        return False
