string_input = input("Enter a string: ")
alphabets = sum(c.isalpha() for c in string_input)
digits = sum(c.isdigit() for c in string_input)

print("Alphabets count:", alphabets)
print("Digits count:", digits)
