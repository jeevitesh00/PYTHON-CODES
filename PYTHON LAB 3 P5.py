# Q5. Write a python program to read three numbers and find the smallest among them

num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
num3=int(input("Enter number 3: "))
if (num1<num2) and (num1<num3):
    print("Smallest value is: ",num1)
elif (num2<num1) and (num2<num3):
    print("Smallest value is: ",num2)
elif (num3<num2) and (num3<num1):
    print("Smallest value is: ",num3)
else:
    print("Error")
