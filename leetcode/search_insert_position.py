from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Edge cases
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                return mid

        return left

sol = Solution()
sol.searchInsert([1,3,5,6], 2)