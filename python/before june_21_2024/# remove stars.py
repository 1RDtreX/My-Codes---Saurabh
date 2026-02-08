# remove stars 

class Solution(object):
    self=input("Enter The Word : ")
    s=""
    
    def removeStars(self, s):
        fles=""
        star=0
        for i in self:
            if i=="*":
                star=star+1
                print(i)
        return star
    x=removeStars(self,s)
    print(x)