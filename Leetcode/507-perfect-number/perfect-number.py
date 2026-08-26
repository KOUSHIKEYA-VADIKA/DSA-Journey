import math
class Solution(object):
    def checkPerfectNumber(self,num):

        p=0
        l=[]
        sum,original=0,num
        if(num<=10**8 and num>=1):
            if(num==1):return False
            for i in range(2,int(math.sqrt(num))+1):
                if(num%i==0):
                    l.append(i)
                    p=original//i
                    if(p not in l):
                        l.append(p)
                        sum+=i+p
        sum=sum+1
        if(sum==original):
            return True
        else :
            return False
       
