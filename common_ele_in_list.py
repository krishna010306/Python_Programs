l1 = []
l2 = []
n = int(input("enter the lenth of List:"))
for i in range(0,n):
    v = int(input("Enter the 1st list element="))
    l1.append(v)
for i in range(0,n):
    v = int(input("Enter the 2nd list element="))
    l2.append(v)
common = []
for item in l1:
    if item in l2 and item not in common:
        common.append(item)
print("Common List:",common)