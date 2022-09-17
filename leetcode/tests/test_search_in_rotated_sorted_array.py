from rotated_sorted_array import Solution

def test_search():
    sol = Solution()
    assert sol.search([4,5,6,7,0,1,2], 0) == 4
    assert sol.search([4,5,6,7,0,1,2], 3) == -1
    assert sol.search([1], 0) == -1
    assert sol.search([0], 0) == 0