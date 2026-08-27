class Solution(object):
    def sortedSquares(self, nums):
        l=[]
        for i in range(len(nums)):l.append(nums[i]**2)
        l.sort()
        return l
        

       