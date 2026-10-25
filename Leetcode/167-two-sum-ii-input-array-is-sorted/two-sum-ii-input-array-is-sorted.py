class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=0
        r=len(numbers)-1
        while(l<r):
            total=numbers[l]+numbers[r]
            if total==target:
                return [l+1,r+1]
            elif total<target:
                l+=1
            else:
                r-=1

       
         


        