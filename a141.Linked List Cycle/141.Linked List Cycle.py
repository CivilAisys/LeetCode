class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 這道題是快慢指標的經典應用。只需要設兩個指標，
# 一個每次走一步的慢指標和一個每次走兩步的快指標，如果鏈表裡有環的話，兩個指標最終肯定會相遇。
def hasCycle(head: ListNode) -> bool:
    try:
        #快慢指標
        slow, fast = head,head
        #快慢指標皆不為None時
        while slow and fast:
            slow = slow.next
            fast = fast.next.next

            #相撞時代表鏈結內有循環
            if slow == fast:
                return True
    except:
        #fast = fast.next.next 可能在fast.next就為None None.next不存在  故噴錯
        return False
    return False
