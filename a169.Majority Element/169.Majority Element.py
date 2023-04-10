# 解法1 使用hash table計算各數字出現次數  再比對其是否大於 nums的長度
# 時間: O(n) 空間: O(n)
def majorityElement(nums: list[int]) -> int:
    # 陣列長度 dic用來記錄出現次數
    majority = len(nums) / 2
    dic = {}

    # 計算各數值出現次數
    for num in nums:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1

    for key in dic:
        if dic[key] > majority:
            return key


# 解法2 摩爾投票法(此演算法前提是必須有過半數的值存在)
# 這是一種先假設候選者，然後再進行驗證的演算法。
# 現將數位中的第一個數假設為過半數，然後進行統計其出現的次數，
# 如果遇到同樣的數，則計數器自增1，否則計數器自減1，如果計數器減到了0，則更換下一個數位為候選者
# 時間O(n) 空間 O(1)
def majorityElement(nums: list[int]) -> int:
    result, count = 0, 0
    for num in nums:
        if count == 0:
            result = num
            count += 1
        elif num == result:
            count += 1
        elif num != result:
            count -= 1

    return result
