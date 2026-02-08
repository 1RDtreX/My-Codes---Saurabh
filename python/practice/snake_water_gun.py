
# stone paper scissor game 

import random


def ai():
    r= random.randint(1,3)
    if r==1:
        print("AI has choosen STONE")
    elif r==2:
        print("AI has choosen PAPER")
    elif r==3:
        print("AI has choosen SCISSOR")
    return r
    
def player():
    try:
        c= int(input("Enter \n1 for stone \n2 for paper\n3 for scissor\n"))
    except :
        c=int(input("Please enter a number and nothing else : "))
    
    if c<1 or c>3:
        player()
    
    return c
    
    
    
    
    

def logic(self,c,p):
    points=0
    com=c
    play=p
    if play==com:
        print("TIE")
    elif play==1 and com==2:
        print("LOOSE")
        points-=1
    elif play==2 and com==3:
        print("LOOSE")
        points-=1
    elif play==3 and com==1:
        print("LOOSE")
        points-=1    
    elif com==1 and play==2:
        print("WIN")
        points+=1
    elif com==2 and play==3:
        print("WIN")
        points+=1
    elif com==3 and play==1:
        print("WIN")
        points+=1
    return points
    

def gameplay():
    p=player()
    c=ai()
    print()
    p=logic(0 ,c,p)
    print()
    return p
    
    
print("Welcome to the ultimate Competetion : ")
chance=int(input("Enter how many chances you want play : "))

winpo=0

for i in range(chance):
    po=gameplay()
    winpo=winpo+po

print("SCORE :")
print(winpo,"/",chance)
winper=(winpo/chance)*100
print("win percentage = ",winper,"%")
if winper<50:
    print("YOU LOOSE \nSuggestion : go and learn to play MF")
elif winper==50:
    print("This is a Tie Match")

elif winper>50:
    print("YOU WON THE MATCH hurrey")


