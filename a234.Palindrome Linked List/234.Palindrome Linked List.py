# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 解法1 遍歷至尾部並用stack保存其值  在遍歷head比對stack內的值是否相同
# 時間:O(2n) -> O(n)  空間O(n)
def isPalindrome(head: ListNode) -> bool:
    # 輔助比對的stack
    stack = []
    # 遍歷至尾部的指針並將值塞入stack內
    cur = head
    while cur:
        stack.append(cur.val)
        cur = cur.next

    # 遍歷head指針與stack內值一一比對
    while head:
        if head.val != stack.pop():
            return False
        head = head.next

    return True


# 解法2  要符合題目follow up 要求  需要先用快慢指針找出中間點 
# 在將後半段鏈表進行頭插法反轉
# 時間:O(2n) -> O(n)  空間O(1)
def isPalindrome(head: ListNode) -> bool:
    # 表示只有head自己一個節點存在  直接回傳
    if not head.next:
        return True
    #使用快慢指針來找出"中間的節點" 慢指針一次一步 快指針一次兩步
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    #使用頭插法來進行後半段鏈結的反轉
    new_head, old_head = slow ,slow.next
    while old_head.next:
        #保存old_head的下個節點
        temp = old_head.next
        #將下個節點的下個節點給old_head
        old_head.next = temp.next
        #將temp.next更新為new_head.next
        temp.next = new_head.next
        #將新的頭節點更新為temp
        new_head.next = temp
    
    #從head與slow.next開始進行比對
    while slow.next:
        slow = slow.next
        if slow.val != head.val:
            return False
        head = head.next

    return True
