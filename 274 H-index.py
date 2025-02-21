from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
            The h-index is defined as the maximum value of h such that 
            the given researcher has published at least h papers that have 
            each been cited at least h times.
        """
        h_index = 0
        n = len(citations)
        citations.sort()
        for i in range(n):
            if citations[n - 1 - i] >= i + 1:
                h_index = i + 1
            else:
                break
        return h_index

sol = Solution()
nums = [1]
print(sol.hIndex(nums))