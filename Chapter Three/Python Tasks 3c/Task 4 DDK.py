# a total of three different arrays to store values for later
items = []
prices = []
tax = []

# this basically just asks the user for an item, then a price for said item, and then once that is done, everything gets added to the arrays.

# every single product name, goes into the items array. every single product price, into the prices array.

# however, for taxes, it's calculating the price * 0.06, and then adds that value to the tax array.
for i in range(1, 4):
    item_product = input(f"Enter item {i}: ")
    item_price = float(input(f"Enter price {i}: "))
    items.append(item_product)
    prices.append(item_price)
    product_tax = item_price * 0.06
    tax.append(product_tax)

# finally, this is a for loop to print out all the statistics for the items requested.
for i in range(3):
    print(items[i], "costs $", round(prices[i], 2), "with tax $", round(tax[i], 2))