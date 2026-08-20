class Solution(object):
    def isPalindrome(self, x):
        if(x>2**31 - 1 and x<-2**31):
            return 0
        num=x
        original=num
        rev=0
        while(num>0):
            lastdigit=num%10
            rev=(rev*10)+lastdigit
            num//=10
        if(original<0):
            return False
        elif(original==rev):
            return True
        else :
            return False
        