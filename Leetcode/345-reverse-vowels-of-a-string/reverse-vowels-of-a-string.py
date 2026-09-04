class Solution(object):
    def reverseVowels(self, s):
        right=len(s)-1
        left=0
        s=list(s)
        while(left<right):
            if s[left] in "aeiouAEIOU" and s[right] in "aeiouAEIOU":
                s[left],s[right]=s[right],s[left]
                right-=1
                left+=1
            elif s[left] not in "aeiouAEIOU":
                left+=1
            elif s[right] not in "aeiouAEIOU":
                right-=1
        s=''.join(s)
        return s
        
            
            




        
    



























        
        