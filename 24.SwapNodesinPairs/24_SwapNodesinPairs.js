/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
//解法1
const swapPairs = function(head) {
    
    //若是head === null or head.next === null  就可直接回傳;
    if(head === null || head.next === null) return head;

    let dummy = new ListNode();
    dummy.next = head;
    let result = dummy;

    //檢查下一個及下下一個是否有值(起始點前插入一個空的node)  有值才調換  調換後移動當前頭的位置再進行檢查及調換
    while (dummy.next && dummy.next.next) {
        //將p設置為1  q為2
        let p = dummy.next, q = dummy.next.next;
        //將1 設置為2
        dummy.next = q;
        //將1的下一個設置為3
        p.next = q.next;    
        //將2的下一個設置為1
        q.next = p; 
        //將節點移動至1
        dummy = p
    }

    return result.next;
};

function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

swapPairs( new ListNode(1,new ListNode(2,new ListNode(3, new ListNode(4, undefined)))))