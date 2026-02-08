# febonacci series
# write a python code to rpitn febonacci series
n=5
def febo(n):
    x=0
    for i in range (n):
       
            if i==n:
                y=(i-2)+(i-1)
                print(y)
                return y
            else:
                continue
febo(5)
