from single_number import Solution

def test_single_number():
    sol = Solution()
    assert sol.singleNumber([2,2,1]) == 1
    assert sol.singleNumber([3,3,1,1,2,2,4,5,4,5,8]) == 8