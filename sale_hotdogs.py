# Task

# Complete function saleHotdogs/SaleHotDogs/sale_hotdogs, function accepts 1 parameter:n,
# n is the number of hotdogs a customer will buy, different numbers have different prices
# (refer to the following table), return how much money will the customer spend to buy that number of hotdogs.

# solution
# Time: 477ms
def sale_hotdogs(n):
    return n * 100 if n < 5 else n * 95 if n < 10 else n * 90


print(sale_hotdogs(7))
