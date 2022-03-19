class Solution(object):
    def isValid(self, s):
        stack=[]
        # using Python dictionary to avoid switch-case:
        dict={')':'(',']':'[','}':'{'}
        for ch in s:
            if ch in dict:
                if len(stack)>0 and dict[ch]==stack[-1]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(ch)
        if(len(stack)==0):
            return True
        else:
            return False
 