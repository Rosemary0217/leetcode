from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = dict()
        for idx, v in enumerate(nums):
            hmap[v] = idx   # if same elem in more than one place, record the largest index
        for idx, v in enumerate(nums):
            if target - v in hmap.keys() and idx != hmap[target - v]:   # search from small index, no repeat
                return [idx, hmap[target - v]]    
        """
            Note: we can also do it with one-pass hash table
        """