class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_sum = sum(nums[:k])
        maxi = window_sum
        for i in range(k, len(nums)):
            
            window_sum = window_sum - nums[i-k] + nums[i]
            maxi = max(maxi, window_sum)

        return float(maxi) / k

            



            
