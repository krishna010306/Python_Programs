l1=[]
n = int(input("enter the lenth of List:"))
for i in range(0,n):
    v = int(input("Enter the 1st list element="))
    l1.append(v)
print("Even Numbers in List:")
for item in l1:
    if item%2==0:
        print(item,", ",end="")