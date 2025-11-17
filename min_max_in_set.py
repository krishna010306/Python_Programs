n = int(input("Enter the length set: "))
numbers = set()
for i in range(n):
    num = int(input("Enter a number: "))
    numbers.add(num)  
max_value = max(numbers)
min_value = min(numbers)
print("Maximum value:", max_value)
print("Minimum value:", min_value)