# to do list
import time

d=[]
# no_do=[]hjgj
done="done"
daa=0
dlt=0
# To show options
def show():
    print("1. To Show List")
    print("2. To add TO DO")
    print("3. To Mark done")
    print("4. Delete to do")
    print("5. to EXIT")
    
# To show data
def data(d,):
    print()
    x=1
    if (len(d)>0):
        print("new TO DO : ")
        for i in d:
            print(x,". ",i)
            x+=1
    else:
        print("No Work To Do 🥺")
    print()
    
# To Add Data
def add(d):
    print()
    list_add=(input("Enter To Do : "))
    d=d.append(list_add)
    
# Done
def do(d,done,daa):
    x=d[daa]
    d[daa]=x+" : "+done
    
def delete(d,dlt):
    d[dlt]=""
    
# Main
while True:
    show()
    user=(int(input("Enter : ")))e
    if user==1:
        time.sleep(.5)
        data(d)
    elif user ==2:
        add(d)
        data(d)
    elif user ==3:
        data(d)
        daa=(int(input("Enter the Number : ")))
        daa=daa-1
        do(d,done,daa)
    elif user == 4:
        dlt=(int(input("Enter to Delete : ")))
        data(d)
        delete(d,dlt)
    elif user==5:
        break

data(d)