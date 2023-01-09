class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#解法1
def swapPairs(head: ListNode) -> ListNode:
    #若head == None  or head.next == None   return head
    if head == None or head.next == None:
        return head
    
    #最後回傳result.next
    result = ListNode()
    result.next = head
    
    #需要檢查當前及下一個皆有值時才進行調換
    while head != None and head.next != None:


    
    return result.next


swapPairs(ListNode(1, ListNode(2)))

        
    