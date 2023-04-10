#解法1  先算出 nums的總和  再算0-len(nums)應該要的總和  相減及為答案
def missingNumber(nums: list[int]) -> int:
    sum, length = 0, len(nums)
    #計算nums總和
    for num in nums:
        sum += num
    
    return int(0.5*length*(length + 1) - sum)


#解法2 

