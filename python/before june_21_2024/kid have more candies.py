# leet : kid with greatest number of candies\
class Solution(object):
    def kidsWithCandies(b, candies, extraCandies,n):

        def equal(candies,b,extra):
            for i in range(n):
                greater=True
                for j in range(n):
                    if (candies[i]+extraCandies)<=candies[j]:
                        greater=False
                        break
        
                b.append(greater)

        equal(candies,b,extraCandies)      
        return b
    
    n=(int(input("Enter the  number of Kids : ")))
    candies=[]
    b=[]    
    for i in range(n):
            print("Enter the number of candies",(i+1),"kid have ")
            num=(int(input(": ")))
            candies=candies+[num]
    extraCandies=(int(input("Enter the Extra Candies You have : ")))

    b=kidsWithCandies(b, candies, extraCandies,n)
    print(b)
