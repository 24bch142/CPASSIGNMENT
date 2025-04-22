def to_lower(char):
    if 'A' <= char <= 'Z':  
        return chr(ord(char) + 32)  
    return char  

# Function to convert a character to uppercase
def to_upper(char):
    if 'a' <= char <= 'z':  
        return chr(ord(char) - 32)  
    return char  

# Function to toggle case of a character
def toggle_case(char):
    if 'A' <= char <= 'Z':  
        return chr(ord(char) + 32)
    elif 'a' <= char <= 'z':  
        return chr(ord(char) - 32)
    return char  

# Function to convert a string to lowercase
def custom_lower(string):
    result = ""
    for char in string:
        result += to_lower(char)
    return result

# Function to convert a string to uppercase
def custom_upper(string):
    result = ""
    for char in string:
        result += to_upper(char)
    return result

# Function to toggle case in a string
def custom_toggle(string):
    result = ""
    for char in string:
        result += toggle_case(char)
    return result

# Accept input from the user
user_string = input("Enter a string: ")

# Convert and display the results
print("Lowercase:", custom_lower(user_string))
print("Uppercase:", custom_upper(user_string))
print("Toggle Case:", custom_toggle(user_string))
