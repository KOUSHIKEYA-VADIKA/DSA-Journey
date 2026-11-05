class Solution(object):
    def isSubsequence(self, s, t):
        j=0
        seen=[]
        for i in range(len(t)):
            if j<len(s):
                if s[j]==t[i]:
                    seen.append(s[j])
                    j+=1
        seen="".join(seen)
        if s in seen:
            return True
        else:return False

        



         

        
        

        
            



        
            
        











    
         



        
        