class Solution(object):

    def selfDividingNumbers(self,left, right):
        list2=[]
        while(left<=right):
            original=left
            temp=left
            content=True
            while(temp>0):
                digit=temp%10
                if(digit==0 or original%digit!=0):
                     content=False
                     break
                temp//=10
            if(content==True):list2.append(left)
            left+=1
        return list2