from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        def reverse(nums: List[int], start: int, end: int) -> None:
            mid = (start + end + 1) // 2
            for offset in range(mid - start):
                nums[start + offset], nums[end - offset] = nums[end - offset], nums[start + offset]

        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)