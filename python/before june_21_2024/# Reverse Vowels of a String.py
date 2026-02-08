# # Reverse Vowels of a String
a="jadu"
k=""
a=(list(a))
for i in a:
    if i=='a'or i=='e'or i=='i'or i=='o'or i=='u':
        
        k=i
        for j in range((len(a)),0,-1):
            if j=='a'or j=='e'or j=='i'or j=='o'or j=='u':
                a[i]=j
                a[j]=k
print(a)        