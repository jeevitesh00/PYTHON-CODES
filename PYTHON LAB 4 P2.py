# Q2. WAP to demonstrate built in functions of Strings

text = "Hello, World!"
print("text in all uppercase is",text.upper())
print("text in all lowercase is",text.lower())
print("text in first letter capital is",text.capitalize())
print("text in capital is i.e. first letter of every word capital is",text.title())
print("text is found at",text.find("World"))
print("text in replaced from world to python",text.replace("World", "Python"))
print("text is split by a space character",text.strip())
print("text is split with , character",text.split(","))
print("text is checked to be all digits",text.isdigit())
print("text is checked to be all alphabets",text.isalpha())
print("text is checked to be all digits and alphabets",text.isalnum())
print("text is checked to be all uppercase",text.isupper())
print("text is checked to be all lowercase",text.islower())
print("text is counted for number of characters",len(text))
print("text first character is",text[0])
