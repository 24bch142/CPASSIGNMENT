string = input("Enter a string: ")
string = string.lower()
vowels = "aeiou"
count = 0
for char in string:
    if char in vowels:
        count += 1
print("Number of vowels in the string:", count)
