#how to swap a number

x = 5
y = 7

#1st way
x = x+y 
y = x - y 
x = x - y 
print(x,y)

#2nd way
x,y = y,x

#3rd way
temp = x
x = y 
y = temp
