import time

user=0
to_do=["Eat : ✅","drink : ❌"]


def show(self,user,to_do,loopcontrol):
    print("1 Show List :")
    print("2 Mark      :")
    print("3 Add       :")
    print("4 Delete    :")
    print("5 Done      :")
    try:
        user=(int(input("Enter the option : ")))
    except Exception as e:
        user=(int(input("Please enter a Valid Number : ")))
        
    if user==1:
        showlist(to_do)
    elif user==2:
        mark(to_do)
    elif user==3:
        add(to_do)
    elif user==4:
        delete(to_do)
    elif user==5:
        done(loopcontrol)
    else:
        print("Please Enter a Valid Number 😡")
    
def showlist(to_do):
    
    i=1
    for x in to_do:
        print(f"{i}: {x}")
        i+=1

def mark(to_do):
    showlist(to_do)
    oper=(int(input("Enter the work to mark : ")))
    
    marker=(int(input("Enter : 1 for ✅ and 2 for ❌")))
    if marker==1:
        to_do[oper-1]=to_do[oper-1].split(":")[0]+" : ✅"
    elif marker==2:
        to_do[oper-1]=to_do[oper-1].split(":")[0]+" : ❌"
    else:
        print("Invalid number Entered")
    

def add(to_do):
    
    new=(input("Enter the Work To Do : "))
    to_do.append(new)
    more=(int(input("Wanna Add more : 1 for yes 2 for no : ")))
    if more==1:
        add(to_do)
    else:
        exit

def delete(to_do):
    showlist(to_do)
    remove=(int(input("Enter the work you want to delete : ")))
    del to_do[remove-1]

def done(loopcontrol):
    loopcontrol=False
    exit
loopcontrol=True
while loopcontrol:
    show(0,user,to_do,loopcontrol)
    print("---------------")