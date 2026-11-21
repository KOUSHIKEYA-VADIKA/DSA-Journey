class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        def solve(nums):
            if len(nums)==1:
                return nums[0]
            dp=[-1]*(len(nums))
            dp[0]=nums[0]
            dp[1]=max(nums[0],nums[1])

            for i in range(2,len(nums)):
                dp[i]=max(dp[i-1],nums[i]+dp[i-2])
            return dp[-1]
        case1=solve(nums[1:])
        case2=solve(nums[:-1])
        return max(case1,case2)

        
        