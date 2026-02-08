def greet(fx):
    def greet1():
        print("Hello ")
        fx()
        print("bye")
    return greet1
        
        

def namaste():
    print("worked")

greet(namaste)()