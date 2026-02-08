class Solution(object):
    def productExceptSelf(self, nums):
        ss=[1]*len(nums)
        for i in range (len(nums)):
            for j in range(len(nums)):
                if i != j:
                    ss[i] *= nums[j]
           
        return ss
        
    
s=Solution()
m=s.productExceptSelf([1,2,3,4])
for i in m:
    print(i)