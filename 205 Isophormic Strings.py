class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map = dict()  # key: ch in s, value: ch in key mapped to ch in t
        for i in range(128):
            hash_map[i] = -1   # not decided yet
        total_len = len(s)
        for i in range(total_len):
            s_idx, t_idx = ord(s[i]), ord(t[i])
            if hash_map[s_idx] == -1:
                hash_map[s_idx] = t_idx
            elif hash_map[s_idx] != t_idx:
                return False
        cnt = [0] * 128
        for v in hash_map.values():
            cnt[v] += 1
            if v >=0 and cnt[v] > 1:
                return False   #  no two characters may map to the same character
        return True
    
sol = Solution()
s = "badc"
t = "baba"
sol.isIsomorphic(s, t)