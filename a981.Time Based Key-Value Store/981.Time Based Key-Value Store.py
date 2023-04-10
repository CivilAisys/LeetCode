import collections
import heapq
# 解法1 使用headq(堆積佇列)
class TimeMap:

    def __init__(self):
        # default值以list產生
        self.times = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # 為最小堆積(MinHeap)
        heapq.heappush(self.times[key], (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # 從最大開始便利  符合條件的第一個便是最靠近的
        for i in range(len(self.times[key])-1, -1, -1):
            t, v = self.times[key][i]
            if t <= timestamp:
                return v
        return ''