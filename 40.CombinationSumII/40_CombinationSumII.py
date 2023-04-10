#解法1 candidates內之值  只有兩種可能  選或不選  遞迴條件為將當前加入並且索引+1  或是直接索引+1
def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    #結果
    result = []
    #需先排序
    candidates = sorted(candidates)
    combinationDFS(candidates,target, [], result)
    return result

# 此DFS算法會將target - candidate[curIndex] 並持續下向搜索可能結果 path為當前可能結果集 target為當前剩餘數值 
def combinationDFS(candidates: list[int], target: int, path: list[int], totalResult: list[list[int]]):
    # 終止條件為 target == 0
    if target == 0:
        totalResult.append(path)
    # 迴圈模擬選與不選  
    for index in range(len(candidates)):
        # 此條件非常重要  避免重複
        if index >= 1 and candidates[index] == candidates[index - 1]:
            continue
        # 若candidates[index] > target  後續都不需要比對  因為candidates為sorted list
        if candidates[index] > target:
            break
        # candidates會越來越少  path + [candidates[index]] 會回傳新陣列  不改變原path
        combinationDFS(candidates[index+1:], target - candidates[index], path + [candidates[index]], totalResult)


combinationSum2([10,1,2,7,6,1,5], 8)
    