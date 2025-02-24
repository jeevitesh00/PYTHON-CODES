# Q8. Write a python program to read a number, if it is an even number , print the square of that number and if it is odd number print cube of that number.

num=int(input("Enter number: "))
if num%2==0:
    print(num**2)
elif num%2!=0:
    print(num**3)
else:
    print("Error")
