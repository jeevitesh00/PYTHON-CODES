# Q3. Check whether an entered year is leap year or not.

year=int(input("Enter a year: "))
if (year%4==0) or (year%100==0) and (year%400==0):
    print("It is a leap year.")
elif (year%100==0) and (year%400!=0):
    print("Not a leap year.")
else:
    print("It is not a leap year.")
