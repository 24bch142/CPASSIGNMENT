food_items = [("Burger", 150), ("Pizza", 300), ("Pasta", 200), ("Sandwich", 120)]

sorted_food_items = sorted(food_items, key=lambda x: x[1], reverse=True)

print("Sorted Food Items:", sorted_food_items)

