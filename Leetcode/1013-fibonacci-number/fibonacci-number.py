class Solution(object):
    def fib(self, n):
        # if n<=1:
        #     return n 
        # return self.fib(n-1) + self.fib(n-2)
        if n <= 1:
            return n
        dp=[-1]*(n+1)

        dp[0]=0
        dp[1]=1

        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[-1]

        
        
        