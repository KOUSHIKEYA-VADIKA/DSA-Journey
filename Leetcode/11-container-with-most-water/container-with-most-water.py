class Solution(object):
    def maxArea(self, height):
        width,left=0,0
        right=len(height)-1
        maxwater=0
        while(left<right):
            minimum=min(height[left],height[right])
            width=right-left
            area=abs(width*minimum)
            if(area>maxwater):
                maxwater=area
            if(height[left]<=height[right]):left+=1
            else :right-=1
        return maxwater


        