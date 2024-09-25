from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1, idx2 = m - 1, n - 1
        while idx1 >= 0 and idx2 >= 0:
            if nums1[idx1] > nums2[idx2]:
                nums1[idx1 + idx2 + 1] = nums1[idx1]
                idx1 = idx1 - 1
            else:
                nums1[idx1 + idx2 + 1] = nums2[idx2]
                idx2 = idx2 - 1

        if idx1 < 0:
            nums1[:idx2 + 1] = nums2[:idx2 + 1]


# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6] 
# n = 3

# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1

# nums1 = [2, 0]
# m = 1
# nums2 = [1]
# n = 1

# nums1 = [4,5,6,0,0,0]
# m = 3
# nums2 = [1, 2, 3]
# n = 3

# soln = Solution()
# soln.merge(nums1, m, nums2, n)
# print(nums1)