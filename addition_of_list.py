l1 = []
n = int(input("enter the lenth of List:"))
for i in range(0,n):
    v = int(input("Enter the list element="))
    l1.append(v)
sum=0
len = len(l1)
for i in range(0,len):
    sum +=l1[i]
print(sum," is the sum of all items in list")