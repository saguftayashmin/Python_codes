lis = [1,2,32,43,13,54,76,99,234,553,125,6]


def largestElem(lis):
    maxItem = 0
    
    for i in range(len(lis)):
        if  lis[i] > maxItem:
            maxItem = lis[i]
    return maxItem
    
print(largestElem(lis))
