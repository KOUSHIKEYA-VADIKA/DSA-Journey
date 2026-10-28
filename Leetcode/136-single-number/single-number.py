class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for num in nums:
            if num not in d:
                d[num]=1
            else :
                d[num]=d[num]+1
        for i in d:
            if d[i]<=1:
                return i
        
            



            
    

