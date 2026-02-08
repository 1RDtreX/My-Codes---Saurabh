# secret Code
# program to make and read Sercret treX code
opt=0
data=""
def write(data):
    jd=""
    ii=len(data)-1
    for ii in range(1,0,-1):
        jd=jd+data[ii]
        
    return jd
    
    
try:
    opt=(int(input("1. Write \n2. Read\n-> ")))
except Exception as e:
    opt=(int(input("Enter in numbers : ")))

if opt==1:
    print("Welcome to Writter :")
    data=(input("Enter the Word :\n-> "))
    write(data)
    
jd=write(data)
print(jd)
    
