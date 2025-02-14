from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for num in nums:
            if farthest < 0:
                return False
            farthest = max(farthest, num)
            farthest -= 1

        return True
