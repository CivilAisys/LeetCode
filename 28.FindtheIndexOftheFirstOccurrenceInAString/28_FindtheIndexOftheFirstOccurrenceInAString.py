# 解法1 暴力比對  時間複雜度為O(nm) n為hatstack.length m為needle.length
def strStr(haystack: str, needle: str) -> int:
    mainStrLength = len(haystack)
    patternLength = len(needle)

    for index in range(mainStrLength):
        # 從主字串發起點與比對字串首位開始嘗試比對
        a = index
        b = 0
        while b < patternLength and haystack[a] == needle[b]:
            a += 1
            b += 1
            if a == mainStrLength:
                break
        # 當比對字串的索引與其長度一樣時  表示完整比對到  回傳index
        if b == patternLength:
            return index
        
    return -1
