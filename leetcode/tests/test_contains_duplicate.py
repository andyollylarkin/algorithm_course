from contains_duplicate import Solution


def test_contains_duplicate():
    sol = Solution()
    assert sol.containsDuplicate([1,2,3,1]) == True
    assert sol.containsDuplicate([1,2,3,4]) == False
    assert sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True
    assert sol.containsDuplicate([1]) == False
    assert sol.containsDuplicate([3,3]) == True