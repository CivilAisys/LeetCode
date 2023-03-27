# 解法1 快慢指針
# 可將數組看作為一個有向圖，其中每個數字 i 作為一個節點，其對應的值 nums[i] 作為向其連接的邊。
# 由於數組中至少存在一個重複的數字，因此這個圖中一定存在一個環。
# 此題使用 Floyd Cycle Detection Algorithm 找出環的起點
# 步驟1: 快慢指針相撞 並將慢指針指回頭 此時快指針在環內  步驟2 快慢指針都只走1步 直到相撞  只時相撞點即為環的起點(重複數字)
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # 快慢指針
        slow, fast = nums[0], nums[0]
        # 每個數字為1節點 其對應的值為指向的索引
        while True:
            slow = nums[slow] # 走一格
            fast = nums[nums[fast]] #　走兩格
            if slow == fast:
                break
        
        #重置慢指針為頭 並且快慢指針都一步一步走  直到碰撞即為環的起點 亦為重複得值
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow
    
# 解法2 使用set判斷是否重複
class Solution1:
    def findDuplicate(self, nums: list[int]) -> int:
        s= set()
        for num in nums:
            if num in s:
                return num
            s.add(num)


test = Solution()
test.findDuplicate([1,3,4,2,2])
