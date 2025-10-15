#Bubble Sorting Technique

def bubble_sort(elements):
    n = len(elements) #6
    for i in range(n - 1):
        print(f'Iteration Number{i}')
        for j in range(n - i - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
    return elements

# Test the function
elements = [3,5,2,7,9,4]
print(bubble_sort(elements))
