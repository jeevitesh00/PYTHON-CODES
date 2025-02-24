# Q5. WAP to accept two strings from the user and display the common words.

str1 = input("Enter first string: ").split()
str2 = input("Enter second string: ").split()

common_words = [word for word in str1 if word in str2]

print("Common words:", common_words)
