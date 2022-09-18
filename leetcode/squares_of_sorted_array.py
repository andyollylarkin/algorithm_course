from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            res.append((i)**2)
        return sorted(res)

sol = Solution()
print(sol.sortedSquares([-4,1,0,3,10]))