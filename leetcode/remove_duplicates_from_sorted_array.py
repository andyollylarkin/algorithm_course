from typing import List


class Solution:
    """ NOT WORK """
    def removeDuplicates(self, nums: List[int]) -> int:
        b_pointer = 0
        f_pointer = 1
        ln = len(nums)
        i = 0
        while i <= ln and len(nums) > 1:
            if nums[b_pointer] == nums[f_pointer]:
                del nums[b_pointer]
                if b_pointer - 1 >= 0 and f_pointer - 1 >= 1:
                    b_pointer = 0 
                    f_pointer = 1
                continue
            if len(nums) > 2 and f_pointer + 1 <= len(nums) - 1:
                b_pointer += 1
                f_pointer += 1
            i += 1



        
a = Solution()
a.removeDuplicates([0,0,1,1,1,2,2,3,3,4])