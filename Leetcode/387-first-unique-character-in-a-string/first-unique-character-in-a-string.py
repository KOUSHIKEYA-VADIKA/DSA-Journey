class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        k={}
        #s=list(s)
        for ch in s:
            if ch not in d:
                d[ch]=1
            else:d[ch]=d[ch]+1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1



        
