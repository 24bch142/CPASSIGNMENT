data = [("Amit", "Rahul"), "Priya", ("Raj", "Vikram"), "Neha", "Sita"]

boys = sum(1 for item in data if isinstance(item, tuple))
girls = sum(1 for item in data if isinstance(item, str))

print("Number of Boys:", boys)
print("Number of Girls:", girls)
