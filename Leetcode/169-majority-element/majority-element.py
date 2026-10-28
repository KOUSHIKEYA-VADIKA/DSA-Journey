class Solution(object):
    def majorityElement(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        size=len(nums)
        for num in nums:
            if num not in d:d[num]=1
            else:d[num]=d[num]+1
        for i in d:
            if d[i] > size/2 :return i
            