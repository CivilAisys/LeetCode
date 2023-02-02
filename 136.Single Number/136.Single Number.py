#解法1  題目要求 時間:O(n) 空間O(1) 故使用位元互斥判斷
#被同一個數XOR(^=)兩次會變回自己  題目敘述  只有一個數字是出現一次  其餘皆兩兩成對 故最後回XOR回單獨的那個數字
#且因為XOR具有交換律  故先後順序並不影響
def singleNumber(nums: list[int]) -> int:
    #結果
    result = 0
    for num in nums:
        result ^= num
    
    return result

singleNumber([2,1,2])