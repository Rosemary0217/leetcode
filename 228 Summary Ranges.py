from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = list()
        n = len(nums)
        if n == 0:
            return res
        elif n == 1:
            return [str(nums[0])]
            
        start, end = nums[0], nums[0]
        for num in nums[1:]:
            if num == end + 1:   # continuous
                end += 1
            else:
                if start == end:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{end}")
                start, end = num, num
        # the last interval
        if start == end:   
            res.append(str(num))
        else:
            res.append(f"{start}->{end}")     
        return res
    
sol = Solution()
# nums = [0,1,2,4,5,7]
nums = [0,2,3,4,6,8,9]
print(sol.summaryRanges(nums))