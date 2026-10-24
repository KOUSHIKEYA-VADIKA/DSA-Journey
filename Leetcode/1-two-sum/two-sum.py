class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i in range(len(nums)):
            need=target-nums[i]
            if need in d:
                return [d[need],i]
            d[nums[i]]=i