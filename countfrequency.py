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
