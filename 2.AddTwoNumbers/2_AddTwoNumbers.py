# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    # 建立listNode
    result = ListNode()
    # 用於指針移動  最後應回傳result.next
    head = result
    # 進位值
    carry = 0

    while l1 != None or l2 != None or carry != 0:
        # 加總
        sum = 0

        # l1不為None 加總並移動至l1.next
        if l1 != None:
            sum += l1.val
            l1 = l1.next
        # l2不為None 加總並移動至l1.next
        if l2 != None:
            sum += l2.val
            l2 = l2.next
        # 加總進位值
        sum += carry
        # sum >= 10 時  取餘數並進位  <10進位為0
        if sum >= 10:
            sum %= 10
            carry = 1
        else:
            carry = 0

        # 創建新的listNode並移動指針
        head.next = ListNode(sum)
        head = head.next

    # 回傳result.next  應result.val為0  創建的初始值
    return result.next
