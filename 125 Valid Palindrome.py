### sol1: convert then compare ###
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = [ch.lower() for ch in s if ch.isalnum()]
        return all(s1[i] == s1[-i - 1] for i in range(len(s1)//2))  #也可以用s1[~i]
    

### sol2: 2 ptrs ###
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        head, tail = 0, n-1
        while head < tail:
            if not s[head].isalnum():
                head += 1
                continue
            if not s[tail].isalnum():
                tail -= 1
                continue
            if s[head].lower() != s[tail].lower():
                return False
            head += 1
            tail -= 1
        return True