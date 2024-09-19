# Initial and discounted prices 
cover_price = 24.95
store_price = cover_price * 0.6

# Buying cost 
no_books = 60
book_cost = no_books * store_price

# Shipping cost
ship_cost = 3 + (.75 * (no_books - 1))

# Total cost 
total_cost = book_cost + ship_cost
print(f'The total cost is ${round(total_cost, 2)}')
