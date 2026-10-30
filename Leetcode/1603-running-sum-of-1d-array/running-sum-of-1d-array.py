class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum=0
        k=[]
        for i in range(len(nums)):
            if i==0:
                sum=nums[i]
                k.append(sum) 
            else:
                sum+=nums[i]
                k.append(sum)
        return k
                


        