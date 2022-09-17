from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        containsMap = {}
        i = 0
        while i <= len(nums) - 1:
            if nums[i] in containsMap:
                return True
            else:
                containsMap[nums[i]] = 1
            i += 1
        return False

a = Solution()
a.containsDuplicate([3,3])