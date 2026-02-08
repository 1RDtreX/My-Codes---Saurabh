# to make anthings Table

number=(int(input("Enter te number : ")))
i=0
choice=(int(input("Enter 1 for 'for' and 2 for 'while'")))
if choice==1:
  for i in range(10):
    print(number,"*",(i+1),"=",number*(i+1))
  print("for loop close")
# with while loop

elif choice==2:
    i=0
    while(i<10):
        print(number,"*",(i+1),"=",number*(i+1))
        i+=1
    print("wihle loop close")