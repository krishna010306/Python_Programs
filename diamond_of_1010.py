n = 7 
for i in range(0, n, 2):
    for j in range(i):  
        print(" ", end="")
    for j in range(n - i):  
        print("1" if j % 2 == 0 else "0", end="")
    print()