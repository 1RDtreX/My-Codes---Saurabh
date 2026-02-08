# Move Zeroes
class solution(object):
    def moveZeroes(nums):
        for j in range (len(nums)):
            for i in range(len(nums)-1):
                if nums[i]==0:
                    k=nums[i+1]
                    nums[i+1]=nums[i]
                    nums[i]=k
        print(nums)
            
    def moveZeroes2(nums):
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        
        print(nums)

             
         
         
    nums=[0,1,0,3,12]
    moveZeroes2(nums)
    
   
    
    