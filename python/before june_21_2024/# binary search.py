# binary search

user=[1,2,3,4,5,6,7,10]
upper_bound=(len(user))
lower_bound=0

search=(int(input("Enter the number you want to search : ")))

found=False

for i in upper_bound>lower_bound:
    mid=lower_bound+upper_bound/2
    if mid == search:
        print("Item found at",(int(mid)))
        found = True
        break
    elif mid>search:
        upper_bound=mid+1
    elif mid<search:
        lower_bound=mid-1
