set1=set()
n = int(input("Enter the Length of Set: "))
for i in range(n):
    num = int(input("Enter Number: "))
    set1.add(num)
print("Set is: ",set1)
i = int(input("Enter the number to remove:"))
set1.remove(i)
print("Updated Set is: ",set1)