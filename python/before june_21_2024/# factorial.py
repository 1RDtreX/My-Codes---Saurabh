# factorial

def factorial(n):
    fact = 1
    i=1
    for i in range (n,0,-1):
        fact=fact*i
    return fact
n=(int(input("Enter the number to find the factorial : ")))
x=factorial(n)
print(x)