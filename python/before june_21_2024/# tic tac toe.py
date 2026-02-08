wincheck="no"
row1=["1","2","3"]
row2=["4","5","6"]
row3=["7","8","9"]
def board(row1,row2,row3):
    
    print(row1[0],"|",row1[1],"|",row1[2])
    print("---------")
    print(row2[0],"|",row2[1],"|",row2[2])
    print("---------")
    print(row3[0],"|",row3[1],"|",row3[2])
    print("---------")

# Gameplay for X

def chance_x(row1,row2,row3):  
     x=(int(input("Enter X : ")))
     if x<=3:
         row1[x-1] ="X"
     elif (3<x and x<=6):
         row2[x-1]="X"
     elif (6<x and x<=9):
         row3[x-1] ="X"
    
# Gameplay for O

def chance_x(row1,row2,row3):  
     x=int(input("Enter X (1-9): "))
     if x<1 or x>9:
         print("Invalid input. Please enter a number between 1 and 9.")
         return
     if x<=3:
         row1[x-1] ="X"
     elif (3<x and x<=6):
         row2[x-4]="X"
     elif (6<x and x<=9):
         row3[x-7] ="X"

# Check for win

def win(row1,row2,row3):
    # for X
    if row1[0]==row1[1]==row1[2]=="X" or row2[0]==row2[1]==row2[2]=="X" or row3[0]==row3[1]==row3[2]=="X":
        print("X win        🏆")
        wincheck="X"
    elif row1[0]==row2[1]==row3[2]=="X" or row1[2]==row2[1]==row3[0]=="X":
        print("X win        🏆")
        wincheck="X"
    elif row1[0]==row1[1]==row1[2]=="O" or row2[0]==row2[1]==row2[2]=="O" or row3[0]==row3[1]==row3[2]=="O":
        print("O win        🏆")
        wincheck="O"
    elif row1[0]==row2[1]==row3[2]=="O" or row1[2]==row2[1]==row3[0]=="O":
        print("O win        🏆")
        wincheck="O"

# Now for gameplay

def gameplay(row1, row2, row3):
    for i in range(10):
        chance_x(row1, row2, row3)
        board(row1, row2, row3)
        win(row1, row2, row3)
        if wincheck == "X" or wincheck == "O":
            break

        chance_o(row1, row2, row3)
        board(row1, row2, row3)
        win(row1, row2, row3)
        if wincheck == "X" or wincheck == "O":
            break

    if wincheck == "no":
        print("It's a tie!")

print("Welcome to the game")
board(row1, row2, row3)
gameplay(row1, row2, row3)