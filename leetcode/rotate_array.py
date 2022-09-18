from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        i = 0
        while i < k:
            val = nums[-1]
            del nums[-1]
            nums.insert(0, val)
            i += 1

sol = Solution()
# sol.rotate([1,2,3,4,5,6,7], 3)
sol.rotate([-1,-100,3,99], 2)