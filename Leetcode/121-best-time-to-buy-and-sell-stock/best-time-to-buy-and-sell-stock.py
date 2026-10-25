class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #bruteforce,TC:O(n^2)
        # maxm=0
        # for l in range(len(prices)):
        #     for r in range(l+1,len(prices)):
        #         if prices[r]>prices[l]:
        #             profit=prices[r]-prices[l]
        #             maxm=max(maxm,profit)
        # return maxm

        maxm=0
        minm=prices[0]
        for i in range(len(prices)):
            if prices[i]<minm:
                minm=prices[i]
            profit=prices[i]-minm
            maxm=max(maxm,profit)
        return maxm
            
        
            
        
            



