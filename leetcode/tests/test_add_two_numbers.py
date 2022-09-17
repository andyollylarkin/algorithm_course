from add_two_numbers import Solution
from add_two_numbers import ListNode

def test_addTwoNumbers():
    sol = Solution()
    set1 = [ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))]
    set2 = [ListNode(9, ListNode(9, ListNode(9))), ListNode(8, ListNode(8, ListNode(8)))]
    set3 = [ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))), ListNode(9, ListNode(9, ListNode(9, ListNode(9))))]
    set4 = ListNode(0), ListNode(1, ListNode(2))
    set5 = ListNode(0), ListNode(0)

    assert sol.addTwoNumbers(set1[0], set1[1]).__str__() == '[7,0,8]'
    assert sol.addTwoNumbers(set2[0], set2[1]).__str__() == '[7,8,8,1]'
    assert sol.addTwoNumbers(set3[0], set3[1]).__str__() == '[8,9,9,9,0,0,0,1]'
    assert sol.addTwoNumbers(set4[0], set4[1]).__str__() == '[1,2]'
    assert sol.addTwoNumbers(set5[0], set5[1]).__str__() == '[0]'