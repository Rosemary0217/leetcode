class Solution(object):
    def twoSum(self, nums, target):
        hash={}
        for i,elem in enumerate(nums):
            if target-elem not in hash:
                hash[elem]=i
            else:
                return [hash.get(target-nums[i]),i]
        return []

"""note:
(1)for dictionary, the IN keyword is used to check whether the KEY is in it, not the value.
(2)for dictionary, the dict.get(key,default=NONE) returns the value with that particular key. """

def main():
    myList=[2,7,11,15]
    soln=Solution()
    print(soln.twoSum(myList,9))

main()