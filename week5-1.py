unit_cost = int(input())
unit_price = int(input())
demand = int(input())
resale_price = int(input())
list_prob = []
for prob in range(demand + 1):
    list_prob.append(float(input()))

max_profit = -99999999999
expected_profit = 0
best_order_amount = 0

# 最外層迴圈為尋找最佳進貨量，內圈則計算在給定的進貨量下的預期收益
for current_q in range(demand + 1):
    expected_sales = 0
    excepted_remaining_q = 0
    for assumption_demand in range(demand + 1):  #  "假設"需求逐漸增加，大於當前進貨量時最多也只能賣出current_q單位
        if assumption_demand < current_q:
            expected_sales += list_prob[assumption_demand] * assumption_demand
            excepted_remaining_q += list_prob[assumption_demand] * (current_q - assumption_demand)
        else:
            expected_sales += list_prob[assumption_demand] * current_q
    #  print('current_q : ' + str(current_q), 'assumption_demand : ' + str(assumption_demand), 'expected_sales : ' + str(expected_sales), sep='  ') => For Check
    expected_profit = unit_price*expected_sales - unit_cost*current_q + resale_price*excepted_remaining_q
    if expected_profit > max_profit:
        max_profit = expected_profit
        best_order_amount = current_q
    
print(best_order_amount, int(max_profit), sep=' ')