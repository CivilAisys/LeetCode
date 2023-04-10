# 解法1 
# 一位一位的疊加，比如對於題目中例子 [1，2，3] 來說，最開始是空集，那麼我們現在要處理1，就在空集上加1，為 [1]，
# 現在我們有兩個自己 [] 和 [1]，下面我們來處理2，我們在之前的子集基礎上，每個都加個2，可以分別得到 [2]，[1， 2]，
# 那麼現在所有的子集合為 []， [1]， [2]， [1， 2]，同理處理3的情況可得 [3]， [1， 3]， [2， 3]， [1， 2， 3]， 再加上之前的子集就是所有的子集合了
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # 結果集  初始為空集合
        result = [[]]
        # 將nums進行排序
        nums.sort()

        #進行迴圈計算子集
        for num in nums:
            # 先將result陣列裡的值再推入result內(需使用copy 因為result內的值為list)  在對原result值進行append
            for i in range(len(result)):
                result.append(result[i].copy())
                result[i].append(num)
        return result
    
test = Solution()

test.subsets([1,2,3])