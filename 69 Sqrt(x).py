class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 1, x
        while left <= right:
            mid = (left + right + 1) // 2
            sq = mid ** 2
            if sq == x:
                return mid
            elif sq < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
    
# sol = Solution()
# num = 6
# print(sol.mySqrt(num))