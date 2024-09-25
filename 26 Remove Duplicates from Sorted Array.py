from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 1
        idx = 1
        prev_val = nums[0]
        while ptr < len(nums):
            if nums[ptr] == prev_val:
                ptr += 1
            else:
                nums[idx] = nums[ptr]
                prev_val = nums[ptr]
                idx += 1
                ptr += 1
        return idx