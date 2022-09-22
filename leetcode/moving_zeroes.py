from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        r = len(nums) - 1
        zeroes = []
        i = 0
        while i < len(nums) - 1:
            if nums[i] == 0:
                zeroes.append(nums.pop(i))
                continue
            i += 1
        for i in zeroes:
            nums.append(i)

sol = Solution()
sol.moveZeroes([0,1,2,3,0,12,13,0,4,5])