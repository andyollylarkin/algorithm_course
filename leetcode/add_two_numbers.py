#!/usr/local/bin/python3
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        res = '[' + str(self.val)
        current = self
        while current.next is not None:
            current = current.next
            res = res + ',' + str(current.val) 
        res = res + ']'
        return res


class Solution:
    """ Time complexity O(max(n,m)) """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_list = None
        current1 = l1
        current2 = l2
        carry = False
        
        while (current1.next is not None or current1.val is not None) or (current2.next is not None or current2.val is not None) or carry:
            l1_val = current1.val if current1.val is not None else 0
            l2_val = current2.val if current2.val is not None else 0
            val = l1_val + l2_val
            if carry:
                val += 1
                carry = False
            if val > 9:
                carry = True
                val -= 10
            if result_list is None:
                result_list = ListNode(val)
            else:
                new_node = ListNode(val)
                tmp = result_list
                while tmp.next is not None:
                    tmp = tmp.next
                tmp.next = new_node

            current1 = current1.next if current1.next is not None else ListNode(None)
            current2 = current2.next if current2.next is not None else ListNode(None)
        return result_list



a = Solution()