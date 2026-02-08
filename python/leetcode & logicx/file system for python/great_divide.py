# binary to decimal


def binary_to_decimal():
    print()
    x=(int(input("ENter the binary number : ")))
    x=str(x)
    x=[int(m) for m in x]
    x=x[::-1]
    print(x)
#  binary=[1,2,4,8,16,32,64,124,512,1024,2048] 1101
    n=0
    sum=0
    for i  in range(len(x)):
        if x[i]==1:
            sum=sum+pow(2,n)
        n+=1
    print(sum)

def decimal_to_binary():

    x=(int(input("ENter the binary number : ")))
    boolean=True
    binary_digits = []
    while x > 0:
        binary_digits.append(x % 2)
        x = x // 2
    
    print(binary_digits)
    
dec=(int(input("1 : binary to decimal conversion \n2 : decimal to binary conversion \nEnter : ")))

if dec==1:
    binary_to_decimal()
elif dec==2:
    decimal_to_binary()
else:
    print("Please Enter a Valid number")
