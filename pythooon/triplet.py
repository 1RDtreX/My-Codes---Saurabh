class Solution(object):
    def increasingTriplet(self, nums):
        i=len(nums)-1
        if nums[i-1]<nums[i] and nums[i]<nums[0]:
            return True
        #elif  nums[i]<nums[0] and nums[0]<nums[1]:
            return True
        i=0
        for i in range(0,len(nums)-2):
            if nums[i]<nums[i+1] and nums[i+1]<nums[i+2]:
                return True
                break
            
        return False
            
        
        
s=Solution()
b=s.increasingTriplet([20,100,10,12,5,13])
print(b)