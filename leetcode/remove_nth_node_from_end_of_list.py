from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return ListNode()

        list_length = 1
        current = head
        while current.next is not None:
            current = current.next
            list_length += 1

        if list_length == n:
            return head.next

        search_pos = list_length - (n - 1)

        i = 1
        current = head
        while i < search_pos - 1:
            current = current.next
            i += 1
        current.next = current.next.next
        return head



a = Solution()
res = a.removeNthFromEnd(ListNode(1, ListNode(2)), 1)
# res = a.removeNthFromEnd(ListNode(1, ListNode(2)), 2)
# res = a.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)