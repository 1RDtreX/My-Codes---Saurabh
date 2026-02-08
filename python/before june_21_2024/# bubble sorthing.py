# bubble sorthing

a=[9,4,1,7,2,5,8,6,3,0]
timer=0
for j in range(len(a)):
  timer+=1
  print(a,'=',timer)
  for i in range(len(a)-1):
    if a[i]>a[i+1]:
        k=a[i]
        a[i]=a[i+1]
        a[i+1]=k