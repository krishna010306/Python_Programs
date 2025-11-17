l1 = []
n = int(input("enter the lenth of List:"))
for i in range(0,n):
    v = int(input("Enter the list element="))
    l1.append(v)
large = l1[0]
len = len(l1)
for i in range(1,len):
    if large < l1[i]:
        large=l1[i]
print(large," is the largest number among of all")