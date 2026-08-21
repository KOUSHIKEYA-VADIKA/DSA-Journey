class Solution(object):
    def addDigits(self, num):
        sum=0
        if(num==0):
            return 0
        while(num>0):
            last=num%10
            sum+=last
            num//=10
        if len(str(abs(sum))) == 1:
            return sum
        else :
            return self.addDigits(sum)
        
            
        

                    


                




        
        