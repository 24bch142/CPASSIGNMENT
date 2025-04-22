import random 
numbers = [random.randint(-50, 50) for _ in range(30)] 
print("Original List:", numbers)

positive_numbers = [num for num in numbers if num > 0]
negative_numbers = [num for num in numbers if num < 0]

print("Positive Numbers:", positive_numbers)
print("Negative Numbers:", negative_numbers)
