#解法1 解題思路同45題  貪心演算法  求解每次可跳最大次數
#與45題不同點在於 45題假設一定可跳至最後  只是求最少跳躍次數  此題應為可能跳躍不到最後索引  故多出許多判斷
def canJump(nums: list[int]) -> bool:
    #nums長度
    nums_length = len(nums)
    #長度為1  一定為True
    if nums_length == 1:
        return True

    #當前位置
    cur_pos = 0
    #當前可跳最遠索引
    cur_farthest = 0
    #不包含最後一個元素  
    for index in range(nums_length - 1):
        cur_farthest = max(index + nums[index], cur_farthest)
        #當index == cur_pos  代表需要進行跳躍  並進行可能之最大跳躍
        #當索引值等於當前位置時 將cur_pos = curFarthest(移動到可移動最大索引) 並jump += 1
        if index == cur_pos:
            #當可跳躍最遠>= nums_length - 1 表示可跳至最後索引所在  直接回傳True
            if cur_farthest >= nums_length - 1:
                return True
            #需要跳躍時  當前值為0且  cur_pos >= cur_farthest return False
            if (cur_pos < nums_length and nums[cur_pos] == 0) and cur_pos >= cur_farthest: 
                return False

            cur_pos = cur_farthest

    return False

print(canJump([1,1,2,2,0,1,1]))