# Write a Python program to find the common elements between two lists.

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

common_elem = []
for i in list_a:
    if i in list_b:
        common_elem.append(i)
print(common_elem)
