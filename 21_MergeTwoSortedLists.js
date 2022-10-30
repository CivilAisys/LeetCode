/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
//解法1
const mergeTwoLists = function (list1, list2) {
    //創建鏈結
    let merge = new ListNode()
    //創建head指針 然後最後回傳head.next即可
    let head = merge;

    //當list1 && list2皆存在可以比對時才繼續做比對合併
    while (list1 && list2) {
        //小的先放
        if (list1.val < list2.val) {
            //放進去後創建node塞入merge內 並移動到下一個node 
            merge.next = new ListNode(list1.val);
            list1 = list1.next;
        } else {
            merge.next = new ListNode(list2.val)
            list2 = list2.next;
        }

        //移動merge
        merge = merge.next;

    }
    /**需考慮兩個linklist長度不同　　因為在前面while比對　
     * 一定會對list1 or list2指針移動到其中一個為null為止　
     * 此時若長度不一致　　就表示變數merge尚未串接完成　　
     * 直接將剩餘的list1 or list2 塞到merge後面**/
    if (!list1) merge.next = list2;
    if (!list2) merge.next = list1;

    return head.next;
};

function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}