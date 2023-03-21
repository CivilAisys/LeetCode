from collections import defaultdict
# 解法1 使用兩個dict 分別記錄p的字符個數和s中前p字符長度的字符個數並進行比較
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        #m1 m2 分別記錄著s 和 p 每個字符出現的次數
        result, m1, m2 = [], defaultdict(int), defaultdict(int)
        length_s, lenght_p = len(s), len(p)
        # 計算p字符出現的次數
        for i in range(0,lenght_p):
            m2[p[i]] += 1
        # 加尾減頭 且i需要大於等於p的長度
        for i in range(0, length_s):
            m1[s[i]] += 1
            if i >= lenght_p:
                m1[s[i - lenght_p]] -= 1
                # 若-1後該鍵的值為0  將其刪除以利後續比對
                if m1[s[i - lenght_p]] == 0:
                    m1.pop(s[i - lenght_p])
            if m1 == m2:
                result.append(i - lenght_p + 1)
                
        return result
    
test = Solution()
test.findAnagrams("cbaebabacd","abc")