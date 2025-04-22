names_set = set()

names_set.update(["Alice", "Bob", "Charlie", "David", "Eve"])  # Add 5 names

names_set.discard("Charlie")  # Remove a name
names_set.add("Carlos")  # Modify by adding new name

names_set.difference_update({"Alice", "Eve"})  # Delete two names

print("Updated Set:", names_set)
