items_prices = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}

top_three_items = sorted(items_prices.items(), key=lambda x: x[1], reverse=True)[:3]

print("Top three items in the shop:")
for item, price in top_three_items:
    print(f'{item} {price}')
