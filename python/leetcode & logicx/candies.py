class Solution(object):
    def kidsWithCandies(self,a,can):
        
        
        max_can=max(a)
       
        b=[]

        for i in range(len(a)):
          b=b+[False]
          if (a[i]+can)>=max_can:
              b[i]=True
        return b
        
        print(b)
    
    
    