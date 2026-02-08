a=int(input("Enter First number : "))
b=int(input("Enter Second number : "))
i=0
c=input("Enter + , - , * , / : ")
result=0


if c=="+":
    result=a+b

elif c=="-":
    result=a-b
    
elif c=="*":
    result=a*b
    
elif c=="/":
    result=a/b
    
else:
    result=str("error")

print("Result = ",result)


    