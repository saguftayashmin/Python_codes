#using slicing concept
def pallincheck(x):
    if(x==x[::-1]):
        print("it a pallindrome")
    else:
        print("not pallindrome")
        
x= "12321"
pallincheck(x)

#using function concept
def reverse(str):
    rev=""
    for i in str:
        rev=i+rev
    return rev.strip()
    
def pallindromcheck(str):
    if str == reverse(str):
        print("Its pallindrom")
    else:
        print("Not pallindrome")

str="sagufta"   
pallindromcheck(str)


