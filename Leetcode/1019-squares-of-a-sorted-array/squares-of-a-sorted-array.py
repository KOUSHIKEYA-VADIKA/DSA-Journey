class Solution(object):
    def sortedSquares(self, nums):
        left=0
        right=len(nums)-1
        pos=len(nums)-1
        result = [0] * len(nums)
        while(left<=right):
            if(abs(nums[left])>abs(nums[right])):
                result[pos]=nums[left]**2
                left+=1
            else : 
                result[pos]=nums[right]**2
                right-=1
            pos-=1
        return result
            
           
            

        
        

       