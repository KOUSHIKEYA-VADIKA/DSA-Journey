class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        

        #tc=O(n)
        maxm=0
        minm=prices[0]
        for i in range(len(prices)):
            if prices[i]<minm:
                minm=prices[i]
            profit=prices[i]-minm
            maxm=max(maxm,profit)
        return maxm
            
        
            
        
            



