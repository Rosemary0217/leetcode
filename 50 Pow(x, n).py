class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(base, exp):
            if exp == 0:
                return 1
            elif exp % 2 == 0:
                return power(base * base, exp // 2)
            else:
                return base * power(base * base, exp // 2)
        
        if x == 0:
            return 0
        if x == 1 or n == 0:
            return 1
        if n == 1:
            return x
        if n > 0:
            return power(x, n)
        else:
            return 1.0 / power(x, -n)