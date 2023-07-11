class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0  # 最長子串的長度
        max_count = 0  # 最大重複字符的字數
        start = 0  # 　滑動窗口的起始點
        char_count = {}  # 計算字符的字典

        for end in range(len(s)):
            # 字符計數增加
            char_count[s[end]] = char_count.get(s[end], 0) + 1
            # 更新最大重複字數 與當前s[end]字符計數比較
            max_count = max(max_count, char_count[s[end]])

            # 檢查窗口需要替換的字符數量 end-start+1為窗口大小
            # 條件為窗口大小-當前最大重複自符大於可替換次數k 便將窗口Start+1
            if (end - start + 1) - max_count > k:
                char_count[s[start]] -= 1  # 窗口最左端右移1 故start對應計數-1
                start += 1

            max_length = max(max_length, end-start+1)

        return max_length

test = Solution()
test.characterReplacement(s = "AABABBA", k = 1)