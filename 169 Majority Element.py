from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:   # Moore Voting algorithm
        candidate, cnt = 0, 0
        for num in nums:
            if candidate == num:
                cnt += 1
                continue
            if cnt == 0:
                candidate = num
                cnt += 1
            else:
                cnt -= 1
        return candidate