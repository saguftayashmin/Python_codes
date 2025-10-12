nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4] 

def frequencyCount(nums):
    
    dic = {}
    
    for i in range(len(nums)):
        if nums[i] not in dic.keys():
            dic[nums[i]] = 1
        else:
            dic[nums[i]] = dic[nums[i]]+1
            
    return dic
    
print(frequencyCount(nums))


str = "aaabbbbccdddd"
#a3b4c2d4

str = "aaabbbbccdddd"
#a3b4c2d4

def frequencyCount(str):
    dic = {}
    for i in str:
        if i in dic:
            dic[i] = dic[i]+1
        else: 
            dic[i] = 1

    result = ''
    for k,v in dic.items():
        result = result + f'{k}{v}'
    return result
    
print(frequencyCount(str))

#2nd way
def frequencyCount(str):
    lis = list(str)
    dic = {}
    
    for i in range(len(lis)):
        
        if lis[i] not in dic.keys():
            dic[lis[i]] = 1
        else:
            dic[lis[i]] = dic[lis[i]] + 1
    
    result = ''
    for k, v in dic.items():
        result = result + f'{k}{v}'
            
    return result    
    
print(frequencyCount(str))

str = "a3b4c2d4"
#"aaabbbbccdddd"
#print("a"*3+"b"*4+"c"*2+"d"*4)

def frequencyCountReverse(str):
    final = ""
    result = ""
    for i in str:
        if i.isalpha():
            result = result+i
        else:
            result = result * int(i)
            final += result
            result = ""
    return final
            
    
print(frequencyCountReverse(str))


