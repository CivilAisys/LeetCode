import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []

        # 將數組元素加入最小堆
        for num in nums:
            heapq.heappush(heap, num)

            # 如果堆大小超過k 移除堆頂元素  這樣可保證最後的堆頂元素為第k大的元素
            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)
