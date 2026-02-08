# a simple ATM interface

def intro():
    print("WELCOME TO RED BANK : \nwhere dreams come True")
    
def ch1():
    choice=0
    try:
        choice=int(input("1. Saving Acount \n2. Credit Account\n---> "))
    except:
        choice=int(input("Please Enter numbers only\n---> "))
    
    if choice==1:
        pass
    elif choice==2:
        pass
    else:
        choice=int(input("Please enter a valid Number\n---> "))
        
def saving():
    choice=int(input("1. Widrawl \n2. Add\n---> ")) 
    choice=0
    try:
        choice=int(input("1. Widrawl \n2. Add\n---> "))
    except:
        choice=int(input("please enter a number\n1. Widrawl \n2. Add\n---> "))
    
    if choice==1:
        pass
    elif choice==2:
        pass
    else:
        choice=int(input("Please enter a valid Number\n---> "))
            

intro()
ch1()
    
    