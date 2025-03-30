# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.
# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = dict()
        for i in range(26):
            cnt[i] = 0
        for ch in s:
            cnt[ord(ch)-ord('a')] += 1  # function ord() returns the integer that represents the character
        for ch in t:
            cnt[ord(ch)-ord('a')] -= 1
        for i in range(26):
            if cnt[i] != 0:
                return False
        return True
