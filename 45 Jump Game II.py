from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        n = len(nums)
        farthest_from_here, farthest_all = 0, 0
        for i in range(n - 1):
            farthest_from_here = max(farthest_from_here, i + nums[i])  # farthest position reachable from here with current number of jumps
            if i == farthest_all:      # i is always included in [0, farthest_from_here]
                farthest_all = farthest_from_here
                jump += 1    # when the farthest is n-2, need an extra jump to n-1; otherwise we don't jump. If include n-1 in for loop, would cause one more jump
        return jump
    
# sol = Solution()
# nums = [2,3,1,1,4]
# print(sol.jump(nums))