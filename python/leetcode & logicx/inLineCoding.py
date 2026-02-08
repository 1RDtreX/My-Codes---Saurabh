# can place flower
class Solution(object):
    def canPlaceFlowers(self,pot,n):
        
        for i in range(len(pot)-1):
          if pot[i]==0:
            if pot[i+1]==0 and pot[i-1]==0:
                n=n-1
                pot[i]==1
        print(pot)
        return n==0

    x=canPlaceFlowers(1,[1,0,0,0,0,1],2)
    print(x)