class solution(object):
    def merge(self,s1,s2):
        max_len=0
        j=""
        small=len(s1)
        if len(s1)>len(s2):
            max_len=len(s1)
            small=len(s2)
            j=s1
        else : 
            max_len=len(s2)
            j=s2
        
        print(max_len)
        final=""
        for i in range(max_len):
            if i<=small:
                final=final+s1(i)+s2(i)
            else :
                final=j(i)
        
        return final
        
        
    x=merge(1,"Heys","Man")
    print(x)
    