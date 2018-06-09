prices = {}

prices["banana"] = 4
prices["apple"] = 2
prices["orange"] = 1.5
prices["pear"] = 3

stock = {}

stock["banana"] = 6
stock["apple"] = 0
stock["orange"] = 32
stock["pear"] = 15

print()
print("Fruits's price and stock information:")
print()

for price in prices:
    print(price)
    print("price:", prices[price])
    print("stock:", stock[price])
    print()

print()

print("Bill:")
print()

total = 0

for price in prices:
    print(price, end=": ")
    multi = prices[price] * stock[price]
    print(float(multi))
    total += multi

print()

print("Total:", total)
