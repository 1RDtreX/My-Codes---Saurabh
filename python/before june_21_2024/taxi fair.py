# write a python code to take distance and calculate the amout to be paid
# Taxi fair
# Start --->

name=""
amou=0
distance=0
mob=0
address=0

name=(input("Enter your name : "))
address=input("ENTER your address : ")
mob=(input("Enter your mobile number : "))
x=len(mob)
if(x>10):
   mob=input("Enter a valid Phone number : ")
elif(x<10):
   mob=input("Enter a valid Phone number : ")
mob=float(mob)
  
distance=float(input("ENTER the distance : "))

if(distance<=5):
    amou=distance*10
elif(distance<=10):
    amou=50+((distance-5)*15)
else:
    amou=125+((distance-10)*20)
    
print("customer name = ",name)
print("customer adresss = ",address)
print("Distance travelled = ",distance)
print("customer mobile number = ","+91",(int)(mob))
print("Amout to be paid = ","$",amou)