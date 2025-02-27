from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        expand = True
        for idx, digit in enumerate(digits):
            expand = True if expand == True and digit == 9 else False
        l = idx + 1    # total number of digits
        if expand == True:
            digits[0] = 1
            for i in range(1, l):
                digits[i] = 0
            digits.append(0)
        else:
            carry = (digits[l-1] + 1) // 10
            digits[l-1] = (digits[l-1] + 1) % 10
            for i in range(l-2, -1, -1):
                s = digits[i] + carry   # data dependency here
                digits[i] = s % 10 
                carry = s // 10
        return digits
    
    
sol = Solution()
nums = [8,9,9,9]
print(sol.plusOne(nums))