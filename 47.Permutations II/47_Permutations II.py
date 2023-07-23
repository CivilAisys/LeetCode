# 解法1  使用backTracking進行窮舉  將所有可能組合列出  但組合不能夠重複
class Solution:
    def permuteUnique(self,nums: list[int]) -> list[list[int]]:
        #結果集
        result = []
        numsLength = len(nums)

        #nums為當前決策可以選擇的數值 numsLength為最外層初始nums的長度  path為已決策的陣列 滿足條件為result
        def permuteUniqueDFS(nums: list[int], path: list[int]):
            #決策中止條件
            if numsLength == len(path):
                result.append(path)

            #將可決策數進行去重
            new_List = list(set(nums))
            #需要注意  為避免重複  當前決策只能選不相同的數字 故使用去重後陣列new_List
            for index in range(len(new_List)):
                #下回可決策數列 為nums - nums[index]
                numsCopy = nums.copy()
                numsCopy.remove(new_List[index])
                permuteUniqueDFS(numsCopy, path + [new_List[index]])

        permuteUniqueDFS(nums, [])
        return result

