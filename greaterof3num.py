n1 = int(input("Enter 1st Number="))
n2 = int(input("Enter 2st Number="))
n3 = int(input("Enter 3st Number="))
if(n1>n2):
    if(n1>n3):
        print(n1," is Greatest")
    else:
        print(n3," is Greatest")
else:
    if(n2>n3):
        print(n2,"is Greatest")
    else:
        print(n3,"is Greatest")