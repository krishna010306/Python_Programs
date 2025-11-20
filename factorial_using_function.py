def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    print(f"Factorial of {num} is {factorial(num)}")