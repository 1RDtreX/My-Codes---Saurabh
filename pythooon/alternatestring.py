
class Solution(object):
    def mergeAlternately(self, word1, word2):
        res=""
        l1,l2=len(word1),len(word2)
        min=l1 if l1<l2 else l2
        max=l1 if l1>l2 else l2
        print(min, max)
        
        for i in range (min):
            if word1[i]==word2[i]:
                res=res+word1[i]
            else:
                res=res+word1[i]+word2[i]
        
        if(len(word1)>len(word2)):
            for i in range (max):
                if i>=min:
                    res=res+word1[i]
        else:
            
            for i in range (max):
                if i>=min:
                    res=res+word2[i]
        
       
        return res
sol=Solution()
sol.mergeAlternately("be","bab")
        