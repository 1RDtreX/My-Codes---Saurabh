# to print a spade
# by users input 

n=(int(input("Enter the size foe amarald : ")))
reserve_size=n

for i in range (n,0,-1):
    x=reserve_size
    for j in range (n):
        print(" ",end="")
    for m in range(x-j):
        print("*",end="")
    for m in range(x-j):
        print("*",end="")
    for j in range (n):
        print(" ",end="")
    n-=1
    print()
n=reserve_size+1
for i in range (n):
    x=reserve_size+1
    for j in range(i):
        print(" ",end="")
    for m in range(x-i):
        print("*",end ="")
    for m in range(x-i):
        print("*",end ="")
    for j in range(i):
        print(" ",end="")
    print()