t1=[]
a =  int(input("Enter the Length of Tuple:"))
for k in range(0,a):
    v = int(input("Enter the list element="))
    t1.append(v)
t=tuple(t1)
maxi = max(t)
mini = min(t)
print("Maximum Number: ",maxi)
print("Minimum Number: ",mini)