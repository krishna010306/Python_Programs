n = int(input("Enter the length set: "))
numbers = set()
for i in range(n):
    num = int(input("Enter a number: "))
    numbers.add(num) 
print("Length of Set: ",len(numbers))