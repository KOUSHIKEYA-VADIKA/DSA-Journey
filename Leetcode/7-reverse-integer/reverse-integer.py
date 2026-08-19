class Solution(object):
    def reverse(self, x):
        reverse=0
        sign=1
        if(x<0):
            sign=-1
            x=x*sign
        while(x>0):
            lastdigit=x%10
            reverse=(reverse*10)+lastdigit
            x//=10
        reverse=reverse*sign
        if(reverse<(2**31 - 1) and reverse > (-2**31)):
            x=reverse
            return x
        else :
            return 0
        

        