class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l=0
        r=len(s)-1
        if(s==""):return True
        flag=False
        while(l<=r):
            if(s[l]==s[r]):flag=True
            else :return False
            l+=1
            r-=1
        if(flag==True):return True
        else:return False

