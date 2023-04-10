# 解法1 使用Frequency Counter計算每個數出現次數  次數 > 1 return True else false
def containsDuplicate(nums: list[int]) -> bool:
    # 計算數值出現次數
    dic_of_count = {}

    for num in nums:
        if num in dic_of_count:
            # 若出現過代表超過兩次  直接回傳True
            return True
        else:
            dic_of_count[num] = 1

    return False

#解法2 將nums set化 並與其原先比對長度是否一致  一致 return False else True
def containsDuplicate1(nums: list[int]) -> bool:
    #用set過濾不重複
    set_of_nums = set(nums)

    #比較nums and set長度是否一致
    a = len(nums)
    b = len(set_of_nums)

    if a == b:
        return False
    else:
        return True





