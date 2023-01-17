#  解法1  將str內字串進行list化並排序  並已排序後的list在串回字串作為key值並將其結果紀錄 
#  並依序對strs內字串做同樣動作  關鍵點為Anagram內字母都會一樣只是順序不同  故排序後會一樣 可聚合在一起
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    #結果
    result = {}
    
    for string in strs:
        #字串轉陣列並排序在串回字串
        arr = list(string)
        arr.sort()
        new_String = "".join(arr)
        # mead new_String is one of keys in result
        if new_String in result:
            result[new_String].append(string)
        else:
            result[new_String] = [] 
            result[new_String].append(string)

    return result.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))