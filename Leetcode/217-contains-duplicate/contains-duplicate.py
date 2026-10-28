class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d={}
        count=0
        for num in nums:
            if num not in d:
                d[num]=1
            else :
                d[num]=d[num]+1
        for i in d:
            if d[i]>=2:
                return True
            elif d[i]==1:
                count+=1
        if count==len(nums):
            return False
