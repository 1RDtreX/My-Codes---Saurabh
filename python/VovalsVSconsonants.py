# to extract vovel and display it first with the same series

def extraction(name):
    name=name
    consonants=""
    print(name)
    for i in name:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            print(i,end="")
        else:
            consonants=consonants+i
    print(end="  ")
    print(consonants)

extraction("saurabh vishwakarma")