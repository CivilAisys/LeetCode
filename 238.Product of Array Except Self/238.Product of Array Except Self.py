# 解法1
# 對於某一個數位，如果我們知道其前面所有數位的乘積，同時也知道後面所有的數乘積，那麼二者相乘就是我們要的結果，
# 所以我們只要分別創建出這兩個陣列即可，分別從陣列的兩個方向遍歷就可以分別創建出乘積累積陣列
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0 for _ in range(n)]
        fwd, bwd = [0 for _ in range(n)], [0 for _ in range(n)]
        fwd[0], bwd[n-1] = 1, 1
        # fwd[0] 必為1  fwd[index]代表 index前的所有乘積
        for index in range(1, n):
            fwd[index] = fwd[index - 1] * nums[index - 1]
        # fwd[-1] 必為1 bwd[index]代表 index後的所有乘積
        for index in range(n - 2, -1, -1):
            bwd[index] = bwd[index + 1] * nums[index + 1]
        
        # res[index] = fwd[index] * bwd[index] 表示除index本身外  前後所有的乘積
        for index in range(n):
            res[index] = fwd[index] * bwd[index]
        
        return res

test = Solution()
test.productExceptSelf([1,2,3,4])