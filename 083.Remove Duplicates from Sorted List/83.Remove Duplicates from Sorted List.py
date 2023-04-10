# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#解法1使用dict來確認值是否出現過
def deleteDuplicates(head: ListNode) -> ListNode:
    #count保存出現次數
    count = {}
    #創立一個結果的鏈結 保存new_head 最後回傳new_head.next即可 cur是用來插入新鏈結的指針 
    new_head = ListNode()
    cur = new_head
    #遍歷head
    while head:
        if head.val in count:
            head = head.next
        else:
            count[head.val] = 1
            cur.next = ListNode(head.val)
            cur = cur.next
    
    return new_head.next