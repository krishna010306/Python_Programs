t1=[]
comm=[]
a =  int(input("Enter the Length of Tuple:"))
for k in range(0,a):
    v = int(input("Enter the list element="))
    t1.append(v)
t=tuple(t1)
for i in t:
    if t.count(i) > 1 and i not in comm:
        comm.append(i)
print(tuple(comm))