# # ##########Prime Number#############
def is_prime(num):
    for i in range(2,num-1): # for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    else:
        return True
    
for i in range(2,101):
    value = is_prime(i)
    if value == True:
        print(i)


# # ##########Prime Number#############
#TO check if a number is prime or not
def is_prime(num):
    for i in range(2,num-1):
        if num % i == 0:
            return False
    else:
        return True
    
num = 18
value = is_prime(num)
if value == True:
    print("prime")
else:
    print("Not prime")
acr-bepd-aah
