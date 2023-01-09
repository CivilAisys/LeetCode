# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#解法1
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    #創建鏈結
    merge = ListNode()
    #創建head指針  最後回傳head.next即可
    head = merge

    #當list1 and list2皆還有值時才繼續做比對
    while list1 and list2:
        #值小的先加入merge內並將對應list及merge移動指針
        if list1.val < list2.val:
            merge.next = ListNode(list1.val)
            list1 = list1.next
        else:
            merge.next = ListNode(list2.val)
            list2 = list2.next
        #移動merge
        merge = merge.next
    
    #需考慮list1 and list2長度不一致的情況  會導致長的list會有剩下
    #故剩下的直接加在merge後面
    if not list1:
        merge.next = list2
    if not list2:
        merge.next = list1
    
    return head.next