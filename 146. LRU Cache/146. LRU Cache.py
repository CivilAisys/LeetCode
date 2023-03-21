# 雙向鏈表
class ListNode:
    def __init__(self, key=0, value=0) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
# 解法1 使用雙向鏈表 + hashtable 實現LRU Cache
# 雙向鏈表為維護順序的資結  剛使用的放到鏈表頭部  一直未被使用的放到鏈表尾部 當達到容量時  從尾部刪除
# 鏈表的get時間複雜度為 O(N)  故使用hashtable進行優化為題目要求的O(N)
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0



    def get(self, key: int) -> int:

    def put(self, key: int, value: int) -> None:
