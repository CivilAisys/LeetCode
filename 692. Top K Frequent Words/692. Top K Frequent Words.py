import heapq
from collections import Counter
# 解法1 使用優先佇列 python對應為head quene
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        # 使用Counter來統計單詞出現的頻率 key:word value:times 
        # Counter中排序預設為頻率高低 頻率相同則依照key值進行排序
        count = Counter(words)

        #headq為最小推積 將freq變成負則變成最大推積 
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap) #依照推最小積定義排序 若鎮列為元組陣列  會依照第一個進行排序
        return [heapq.heappop(heap)[1] for _ in range(k)]

test = Solution()
test.topKFrequent(["i","love","leetcode","i","love","coding"],2)