#解法1 
#題目為到達陣列末端所需最少次數  陣列內數值代表一次最多跳幾格
#解題思路  貪婪演算法  直接求解當前index可跳最大路徑 ex nums[i] = 4 直接跳4格
def jump(nums: list[int]) -> int:
    #跳躍次數
    jump = 0
    #當前可跳到最遠的索引
    curFarthest = 0
    #當前所在位置
    cur_pos = 0

    #不包含nums的最後一個索引 故為range(len(nums) - 1)
    for index in range(len(nums) - 1):
        #可跳到最遠的索引
        curFarthest = max(index + nums[index], curFarthest)
        #當index == cur_pos  代表需要進行跳躍  並進行可能之最大跳躍
        #當索引值等於當前位置時 將cur_pos = curFarthest(移動到可移動最大索引) 並jump += 1
        if index == cur_pos:
            cur_pos = curFarthest
            jump += 1

    return jump



jump([1,1,1,1])