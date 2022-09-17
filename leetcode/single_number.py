from typing import Dict, List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor

sol = Solution()
sol.singleNumber([4,1,2,1,2])
