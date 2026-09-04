class Solution(object):
    def maxArea(self, height):
        width=0
        left=0
        right=len(height)-1
        maxwater=0
        arr=height
        while(left<right):
            minimum=min(arr[left],arr[right])
            width=right-left
            area=abs(width*minimum)
            if(area>maxwater):
                maxwater=area
            if(arr[left]<=arr[right]):left+=1
            else :right-=1
        return maxwater
        

        




        


        