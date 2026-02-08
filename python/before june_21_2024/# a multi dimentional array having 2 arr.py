# a multi dimentional array having 2 array who is going top be multiply diagonally
# Start --->

# a four digit array
array_1=[[ 1, 2, 3],[4,5,6],[7,8,9]]

def show(array_1):
    for i in range((len(array_1))):
        # for j in range (len(array_1)):
            print(array_1[i])
            
def diagonal_from_left_to_right(array_1):
    for i in range(len(array_1)):
            print(array_1[i][i])
            
def diagonal_from_right_to_left(array_1):
    x=reversed(array_1)
    print(x)
    x=len(array_1)-1
    # for x in range((len(array_1)),1,-1):
    #     print(array_1[x][x])
            
show(array_1)
diagonal_from_left_to_right(array_1)
diagonal_from_right_to_left(array_1)