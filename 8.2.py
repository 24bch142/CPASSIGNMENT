import random

num_set = {random.randint(15, 45) for _ in range(10)}
count_less_30 = sum(1 for num in num_set if num < 30)

num_set = {num for num in num_set if num <= 35}  # Remove numbers > 35

print("Random Set:", num_set)
print("Count of numbers < 30:", count_less_30)
