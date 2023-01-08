def longestCommonPrefix(strs: list[str]) -> str:
    #結果　以第一個字串做為比對基準
    prefix = strs[0]

    #迴圈進行比對 每次while loop若是沒比對到 prefix就長度就必須-1
    #!=0 因為比對結果應該從開頭 比對到的值索引必須為0 表示為開頭 
    for index in range(len(strs)):
        while strs[index].find(prefix) != 0:
            prefix = prefix[:len(prefix) - 1]

    return prefix