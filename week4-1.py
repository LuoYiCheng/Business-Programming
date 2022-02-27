unit_cost = int(input())
unit_price = int(input())
demand = int(input())
order_amount = int(input())
list_prob = []
for prob in range(demand + 1):
    list_prob.append(float(input()))

# 先算出期望銷售量
expected_sales = 0

for i in range(demand + 1):
    if i < order_amount:
        expected_sales += list_prob[i] * i
    else:  #  當需求量大於進貨量，最多也只會賣出進貨量
        expected_sales += list_prob[i] * order_amount

expected_profit = unit_price * expected_sales - order_amount * unit_cost

print(int(expected_profit))