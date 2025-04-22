prices = {"apple": 100, "banana": 40, "milk": 50, "bread": 30}
quantities = {"apple": 2, "banana": 5, "milk": 1, "bread": 3}

total_bill = sum(prices[item] * quantities[item] for item in prices if item in quantities)

print("Total Bill:", total_bill)
