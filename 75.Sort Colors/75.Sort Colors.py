# 只有 0 1 2  使用雙指針  遍歷陣列  碰到0  與頭指針交換並+1  尾指針碰到2交換並-1  碰到1不管(放中間)
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 當前指針及頭尾指針 
        cur = 0
        head, tail = 0, len(nums) - 1
        
        # 遍歷nums
        while cur <= tail:
            if nums[cur] == 0:
                # 交換
                nums[head], nums[cur] = nums[cur], nums[head]
                head += 1
            elif nums[cur] == 2:
                # 與tail交換後  需要將當前指針-1 最後會+1  等於固定於原地確認被調換的數值是多少
                # 交換
                nums[tail], nums[cur] = nums[cur], nums[tail]
                tail -= 1
                cur -= 1
            # 當前指針+1
            cur += 1    
test = Solution()
test.sortColors([2,0,1])