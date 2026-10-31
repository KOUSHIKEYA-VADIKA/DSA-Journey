class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen=set()
        left=0
        right=0
        maxlength=0
        for right in range(len(s)):
            if s[right] in seen:
                while s[right] in seen:
                    seen.remove(s[left])
                    left+=1
            seen.add(s[right]) 
            if maxlength<(right-left+1):
                maxlength=(right-left+1)
        return maxlength



        