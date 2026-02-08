# this is a simple python game
# between user and computer
# it is a dise agme where random is used
# first working game in python
import random


def rand():
  
    x=random.randint(1,6)
    return x

def welcome():
    print("welcome to the game")
def chance():
    chance=(int(input("How much chance you would like to play : ")))
    return chance
    
def user():
    user=(int(input("Enter the number : ")))
    return user
win=0
welcome()

ch=chance()
for i in range (ch):
  use=user() 
  ai=rand()
  if ai==use:
    print("You win the round 🏆")
    win+=1
  else:
      print("ohh you loose because ai has choosen - ",ai)

if win>(ch/2):
    print("you won the match woooooooooooooo")
else:
    print("ohh you loose the match naaaaaaaaaaaaaaaaaaaa")