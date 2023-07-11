# 使用二分查找即滑動窗口找到k個值的最左側邊界
class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        # 左右兩端點 右邊斷點-k為保證 mid+k不會越界
        left = 0
        right = len(arr) - k
        # 左右兩端點為滑動窗口最左側的候選
        while left < right:
            mid = (left + right) // 2
            # 比較 mid 和 mid+k 看誰離x比較近 離mid+k較近 代表mid不可能包含於最左側故left=mid+1
            if x - arr[mid] > arr[mid+k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left+k]

test = Solution()
test.findClosestElements(arr = [1,2,3,4,5], k = 4, x = -1)