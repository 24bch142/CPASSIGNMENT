list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [2, 4, 6, 8]

list3 = [num for num in list1 if num not in list2]

print("List 1:", list1)
print("List 2:", list2)
print("List 3 (Elements not in List 2):", list3)
