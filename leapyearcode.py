yr = int(input("Enter the year="))
if((yr%4==0 and yr%100!=0) or yr%400==0):
    print(yr,"is leap year")
else:
    print(yr,"is not leap year")