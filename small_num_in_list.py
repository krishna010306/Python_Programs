l1 = []
n = int(input("enter the lenth of List:"))
for i in range(0,n):
    v = int(input("Enter the list element="))
    l1.append(v)
small = l1[0]
len = len(l1)
for i in range(1,len):
    if small > l1[i]:
        small=l1[i]
print(small," is the smallest number among of all")