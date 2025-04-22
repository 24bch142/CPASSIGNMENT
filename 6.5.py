tuples_list = [(1, 2), (), (3, 4, 5), (), (6, 7, 8), ()]

filtered_list = [t for t in tuples_list if t]

print("List after Removing Empty Tuples:", filtered_list)
