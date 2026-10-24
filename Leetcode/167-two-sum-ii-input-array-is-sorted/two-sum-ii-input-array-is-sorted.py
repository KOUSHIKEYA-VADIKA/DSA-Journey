class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i in range(len(numbers)):
            need=target-numbers[i]
            if need in d:
                return [d[need]+1,i+1]
            d[numbers[i]]=i

       
         


        