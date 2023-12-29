def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Get user input for the number
num = int(input("Enter a non-negative integer to calculate its factorial: "))

# Check if the number is non-negative
if num < 0:
    print("Please enter a non-negative integer.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
