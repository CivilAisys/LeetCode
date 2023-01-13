# 解法1  使用窮舉  backtracking 遍歷所有可能 對每個可選擇的數值只有兩種可能  選 或 不選
# 中止條件為拿出數字減剩餘數值 < 0
def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    # 結果
    result = []
    combinationSumDFS(candidates, 0, [], target, result)
    return result

# candidates 為可選值  curIndex表示當前選擇應決定的索引 curCandidates為目前尚有可能之結果 target為目標結果 totalResult為所有可能結果
def combinationSumDFS(candidates: list[int], curIndex: int, curCandidates: list[int], target: int, totalResult: list[list[int]]):
    # 決策中止條件為 curCandidates內數值加總 == target  or curIndex = len(candidates) or 加總 > target
    if sum(curCandidates) == target:
        totalResult.append(curCandidates)
        return
    elif curIndex == len(candidates):
        return
    elif sum(curCandidates) > target:
        return

    # 兩個可能  選擇當前index數值並加入至curCandidates內 or index+1
    newList = curCandidates.copy()
    newList.append(candidates[curIndex])
    combinationSumDFS(candidates, curIndex, newList, target, totalResult)
    combinationSumDFS(candidates, curIndex + 1, curCandidates, target, totalResult)

print(combinationSum([2,3,6,7], 7))