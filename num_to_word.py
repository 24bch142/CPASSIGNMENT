num_to_word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
               "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
               "eighteen", "nineteen"]
num = int(input("Enter a number (0-19): "))
if 0 <= num <= 19:
    print(num_to_word[num])
else:
    print("Invalid input")
