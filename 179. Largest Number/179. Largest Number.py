import functools
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def compare(x, y):
            # 自定義比較函式  將兩數字轉換成字符串後型比較
            # 如果 x+y > y+x，則 x 應該排在 y 的前面
            if int(x + y) > int(y + x):
                return -1
            elif int(x + y) < int(y + x):
                return 1
            else:
                return 0

        # 將數字列表轉換成字符串列表
        nums = [str(num) for num in nums]
        # 進行排序
        nums.sort(key=functools.cmp_to_key(compare))

        # 如果排序後的第一個元素是 '0'，則返回 '0'
        if nums[0] == '0':
            return '0'

        # 否則，將排序後的字符串列表拼接起來並返回
        return ''.join(nums)
