# made by my first mechanical keyboard

c=0
def add(a,b):
    c=a+b
    return c
def subtract(a,b):
    c=a-b
    return c
def divide(a,b):
    c=a/b
    return c
def multiply(a,b):
    c=a*b
    return c 

x=0

choice=(input("Enter + , - , * , / "))

a=(int(input("Enter the number : ")))
b=(int(input("Enter the number : ")))
if(choice=="+"):
    x=add(a,b)
if(choice=="-"): 
    x=subtract(a,b)
if(choice=="/"): 
    x=divide(a,b)
if(choice=="*"): 
    x=multiply(a,b)

print("result = ",x)