# Q4. Write a python program to read three numbers and if any two variables are equal, print that number.

num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
num3=int(input("Enter number 3: "))
if (num1==num2):
    print("There is a same value: ",num1)
elif (num1==num3):
    print("There is a same value: ",num3)
elif (num2==num3):
    print("There is a same value: ",num2)
else:
    print("No same values")
