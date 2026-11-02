class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new=[]
        for i in nums:
            new.append(i)
        return nums+new


    