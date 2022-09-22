function ListNode(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
}
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function (head) {
    let lenght = 1;
    let current = head;
    // count nodes
    while (current.next !== null) {
        lenght += 1;
        current = current.next;
    }
    if (lenght == 1) {
        return head;
    }
    // middle position of all nodes
    const middle = Math.round(lenght / 2);
    current = head;
    i = 0;
    // lookup middle node
    while (current.next !== null && i < middle - 1) {
        i += 1;
        current = current.next;
    }
    // if divided with the remainder, then there will be two middle nodes, we return the second
    if (lenght % 2 == 0) {
        return current.next;
    }
    return current;
};

node = middleNode(
    new ListNode(
        1,
        new ListNode(
            2,
            new ListNode(3, new ListNode(4, new ListNode(5, new ListNode(6))))
        )
    )
);

console.log(node.val);
