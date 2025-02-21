from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        left, mid, right = 0, 0, 0
        nums.sort()
        triplets = list()
        if nums[0] > 0 or nums[-1] < 0:   # if min > 0 or max < 0, there must exist no soln.
            return triplets
        
        while left < n - 2:   # fix 1, search for the other 2 numbers
            cur_left = nums[left]
            mid, right = left + 1, n - 1
            while mid < right:
                cur_mid, cur_right = nums[mid], nums[right]
                cur_sum = cur_left + cur_mid + cur_right
                if cur_sum == 0:
                    triplets.append([cur_left, cur_mid, cur_right])
                    while mid < right and nums[right] == cur_right:
                        right -= 1
                    while mid < right and nums[mid] == cur_mid:
                        mid += 1
                elif cur_sum > 0:
                    while mid < right and nums[right] == cur_right:
                        right -= 1
                else:
                    while mid < right and nums[mid] == cur_mid:
                        mid += 1
            while left < n - 2 and nums[left] == cur_left:
                left += 1
        return triplets
