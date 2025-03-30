class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = dict()
        for ch in magazine:
            if ch in freq.keys():
                freq[ch] += 1
            else:
                freq[ch] = 1
        for ch in ransomNote:
            if ch not in freq.keys() or freq[ch] == 0:
                return False
            else:
                freq[ch] -= 1
        return True
    
# Note: 也可以用ch与‘a’的ascii差值直接构建26个key，可以降低运行时间