import random
# 使用前綴和及二分查找
class Solution:

    def __init__(self, w: list[int]):
        self.prefix_sum = []
        prefix_sum = 0
        # 計算前綴和
        for weight in w:
            prefix_sum += weight
            self.prefix_sum.append(prefix_sum)
        # 總和
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        # target為 1到total_sum任意數字  這樣每個索引被取得機率就會與權重成比例
        target = random.randint(1, self.total_sum)

        left, right = 0, len(self.prefix_sum) - 1

        # 進行二分查找 若條件為 left <= right  裡面的right要調整為 right = mid - 1  不然會有無線迴圈
        while left < right:
            # 此為向下取整  故二分查找條件不能使left = mid  不會有infinite loop
            mid = left + (right - left) // 2

            if target <= self.prefix_sum[mid]:
                right = mid
            else:
                left = mid + 1

        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
