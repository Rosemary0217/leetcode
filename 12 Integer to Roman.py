class Solution:
    def intToRoman(self, num: int) -> str:
        s = ""
        quo, rem = 0, num
        symbols = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        vals = [1000, 500, 100, 50, 10, 5, 1]
        for idx, v in enumerate(vals):
            if idx % 2 == 0:   # if v is power of 10, can append
                quo = rem // v
                rem = rem % v
                if quo > 3:   # append at most 3 times, otherwise use value starts with 5
                    continue
                for _ in range(quo):
                    s += symbols[v] 
            else:   # use the substractive form, take v=500 for example
                if rem // vals[idx + 1] == 4:     # e.g. convert 4xx to 'CD'
                    s += symbols[vals[idx + 1]]
                    s += symbols[v]
                elif rem // vals[idx + 1] == 9:   # e.g. convert 9xx to 'CM'
                    s += symbols[vals[idx + 1]]
                    s += symbols[vals[idx - 1]]
                else:      # e.g. cnonvert 7xx to 'D' first, then look at 100
                    quo = rem // v    
                    for _ in range(quo):
                        s += symbols[v]
                rem = rem % v
        return s
    

"""
    The above solution's runtime only beats 49%. Here's an answer soln. I saw in discussion.

    class Solution:
    def intToRoman(self, num: int) -> str:
        # Creating Dictionary for Lookup
        num_map = {
            1: "I",
            5: "V",    4: "IV",
            10: "X",   9: "IX",
            50: "L",   40: "XL",
            100: "C",  90: "XC",
            500: "D",  400: "CD",
            1000: "M", 900: "CM",
        }
        
        # Result Variable
        r = ''
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            # If n in list then add the roman value to result variable
            while n <= num:
                r += num_map[n]
                num-=n
        return r
"""