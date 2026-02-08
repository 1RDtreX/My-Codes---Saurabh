# lenear search

user_input=[0,0,0,0,0,0]
print(type(user_input))

for i in range(5):
    user=(int(input("Enter the element at ")))
    user_input[i]=user
    
search=(int(input("Enter the number you want to search : ")))

for i in range(5):
    if search==user_input[i]:
        print("Item at",(i+1))