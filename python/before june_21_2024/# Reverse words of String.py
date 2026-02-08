# Reverse words of String

class solution(object):
    def reverseVovelOfString(word):
        l=list(word)
        rev=[]
        print(l)
        n=0
        m=0
        i=len(l)-1
        for i in range(i,0,-1):
            revword=revword+l[i]
            if l[i]==' ':
                
                break
        rev=rev+revword
        
        return rev
                
    
    
    
    word=(input("Enter the Word : "))
    rev=reverseVovelOfString(word)
    print(rev)