def selfDividingNumbers(left, right):
        list2=[]
        while(left<=right):
            original=left
            temp=left
            content=True
            while(temp>0):
                digit=temp%10
                if(digit==0):
                     content=False
                     break
                if(original%digit!=0):
                    content=False
                temp//=10
            if(content==True):
                 list2.append(left)
            left=left+1
        return list2
k=selfDividingNumbers(47,85)
print(k)


            

                
                

            
            
            


        