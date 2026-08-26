class Solution(object):
    def Odd(self,k):
        if(k%2!=0):
            return True
        else :
            return False
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        x=self.Odd(low)
        y=self.Odd(high)
        count=0

        if(low<=10**9 and low>=0 and high<=10**9 and high>=0 ):
            if(x==True and y==True):count=((high-low)/2)+1
            elif(x==True and y==False or x==False and y==False):count=((high-low)+1)//2
            elif(x==False and y==True):count=((high-low)//2)+1
        return count
            
                

        return count

            
            

            
