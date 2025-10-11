# When a function calling itself again and again till it met any condition is called recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test the function
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")

#normal using loop
def factorial_iterative(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial

# Example usage
number = 3
print(f"The factorial of {number} is {factorial_iterative(number)}")
