class Solution(object):
    def maxArea(self, height):
        n=len(height)-1
        j=0
        max=0
        while n>j:
            if(max<(n-j)*min(height[j],height[n])):
                max=(n-j)*min(height[j],height[n])
            elif(height[j]<height[n]):   
                j+=1
            else:
                n-=1
        return max
        

Sol=Solution()
Sol.maxArea([1,8,6,2,5,4,8,3,7])
        