string = input("Enter a string: ")
vowels = "aeiou"
a = 0
e = 0
i = 0
o = 0
u = 0

for char in string.lower():
    if char == 'a':
        a += 1
    elif char == 'e':
        e += 1
    elif char == 'i':
        i += 1
    elif char == 'o':
        o += 1
    elif char == 'u':
        u += 1

print("Frequency of vowels:")
print("a:", a)
print("e:", e)
print("i:", i)
print("o:", o)
print("u:", u)
