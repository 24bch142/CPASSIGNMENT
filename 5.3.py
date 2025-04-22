import random
numbers = [random.randint(1, 30) for _ in range(50)]
print("Original List:", numbers)

unique_numbers = list(set(numbers)) 
print("List after Removing Duplicates:", unique_numbers)
