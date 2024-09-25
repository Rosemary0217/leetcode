from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 1
        idx = 1
        cnt = 1
        prev_val = nums[0]
        while ptr < len(nums):
            if nums[ptr] == prev_val and cnt == 2:   
                ptr += 1
            else:   
                nums[idx] = nums[ptr]
                idx += 1
                if nums[ptr] == prev_val and cnt < 2:  # same number appears  than twice, keep it in the list
                    cnt += 1
                else:    # a new value
                    prev_val = nums[ptr]
                    cnt = 1
                ptr += 1
        return idx