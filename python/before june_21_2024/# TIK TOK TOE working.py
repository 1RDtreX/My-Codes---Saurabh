# TIK TOK TOE

# main rows and column
x="🥺"
o="😈"
n=0

r1=["1","2","3"]
r2=["4","5","6"]
r3=["7","8","9"]

def board(r1,r2,r3):
    print(r1[0],"|",r1[1],"|",r1[2])
    print("---------")
    print(r2[0],"|",r2[1],"|",r2[2])
    print("---------")
    print(r3[0],"|",r3[1],"|",r3[2])
    
def X(r1,r2,r3,x):
    user=(int(input("Enter for X :")))
    if user>0 and user<4:
        r1[user-1]=x
    elif user>3 and user<7:
        r2[user-4]=x
    elif user>6 and user<10:
        r3[user-7]=x

def O(r1,r2,r3,o):
    user=(int(input("Enter for O :")))
    if user>0 and user<4:
        r1[user-1]=o
    elif user>3 and user<7:
        r2[user-4]=o
    elif user>6 and user<10:
        r3[user-7]=o

def logic(r1,r2,r3,x,o,n):
    # for X
    if r1[0] == r1[1] == r1[2] == "X" or r2[0] == r2[1] == r2[2] == "X" or r3[0] == r3[1] == r3[2] == "X" or \
        r1[0] == r2[0] == r3[0] == "X" or r1[1] == r2[1] == r3[1] == "X" or r1[2] == r2[2] == r3[2] == "X" or \
        r1[0] == r2[1] == r3[2] == "X" or r1[2] == r2[1] == r3[0] =="X":
        print("X is winner")
        n=1
        
        
    # for O
    elif r1[0] == r1[1] == r1[2] == "O" or r2[0] == r2[1] == r2[2] == "O" or r3[0] == r3[1] == r3[2] == "O" or \
            r1[0] == r2[0] == r3[0] == "O" or r1[1] == r2[1] == r3[1] == "O" or r1[2] == r2[2] == r3[2] == "O" or \
            r1[0] == r2[1] == r3[2] == "O" or r1[2] == r2[1] == r3[0] == "O":
        print("O is winner")
        n=1
    
    
def gameplay(r1,r2,r3,x,o,n):
    for i in range (10):
        if n==0:
            X(r1,r2,r3,x)
            logic(r1,r2,r3,x,o,n)
            if n==1:
                break
        if n==0:
            board(r1,r2,r3)
            O(r1,r2,r3,o)
            logic(r1,r2,r3,x,o,n)
            if n==1:
                break
            
        elif n==1:
            winner()
        board(r1,r2,r3)
    if n==1:
        winner()
    
def winner():
    print("HEY YOU WON THE MATCH")
    
    
board(r1,r2,r3)
gameplay(r1,r2,r3,x,o,n)