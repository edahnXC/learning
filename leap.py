year=int(input("year: "))
if year%4==0:
    if year%100!=0 or year%400==0:
        print("leap year")
    else:
        print("it is not a leap year")
else: 
    print("the given year is not leap year")