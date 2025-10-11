#using slicing concept
def pallincheck(x):
    if(x==x[::-1]):
        print("it a pallindrome")
    else:
        print("not pallindrome")
        
x= "12321"
pallincheck(x)

