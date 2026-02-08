# who is going to be millioner game
# 5 question and 4 options
# for every answer $ 100 will be awarded
import random
que=["taple is : ","national bird of India : ","easy programing language : ","best game : ","20 + 60 = "]
ans=["immutable","peacock","python","cod",80]
amount=0

i=0
for i in range (5):
    ranint=random.randint(0,4)
    print(ranint)
    print(que[ranint])
    user=(input("Enter the answer"))
    if user==ans[ranint]:
        print("Sahi jawab + $100")
        amount+=100
    else:
        print("Galat jawab")
print("You hacve won",amount)
        