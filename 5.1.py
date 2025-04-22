import random

odd_list = random.sample(range(1, 50, 2), 5)  
even_list = random.sample(range(2, 50, 2), 4)  

print("Odd List:", odd_list)
print("Even List:", even_list)

odd_list[2] = even_list  
print("After Replacement:", odd_list)

flattened_list = [item for sublist in odd_list for item in (sublist if isinstance(sublist, list) else [sublist])]
print("Flattened List:", flattened_list)

flattened_list.sort()
print("Sorted List:", flattened_list)
