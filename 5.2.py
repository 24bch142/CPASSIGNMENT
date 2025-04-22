import random
numbers = random.sample(range(1, 100), 20)
print("List:", numbers)

num = int(input("Enter a number: "))
positions = [i for i, val in enumerate(numbers) if val == num]
print(f"Positions of {num}:", positions if positions else "Not found")
