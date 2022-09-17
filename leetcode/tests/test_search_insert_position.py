from search_insert_position import Solution

def test_search_insert_position():
    sol = Solution()
    assert sol.searchInsert([1,3,5,6], 5) == 2 
    assert sol.searchInsert([1], 0) == 0
    assert sol.searchInsert([0,3], 1) == 1