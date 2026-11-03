class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        seen={}
        for arr in nums:
            for num in set(arr):
                if num not in seen:
                    seen[num]=1
                else :
                    seen[num]+=1
        result=[]
        for num in seen:
            if seen[num]==len(nums):
                result.append(num)
        result.sort()
        return result
            



        