# Input & Create essential variable
nmc1c2_list = [int(i) for i in input().split(',')]
product1_price_choices = nmc1c2_list[0]
product2_price_choices = nmc1c2_list[1]
product1_cost = nmc1c2_list[2]
product2_cost = nmc1c2_list[3]

# Input & Create list of price for each product
product1_price_list = [int(p) for p in input().split(',')]
product2_price_list = [int(p) for p in input().split(',')]

# Input & Create list of sales for each product at all price combinations.
sales_list = [[[int(unit) for unit in input().split(',')]
               for n in range(product1_price_choices)]
              for i in range(2)]
# print(sales_list)

# Let's compute!
# first loop: depend on how many product1_price_choices
# second loop: depend on how many product2_price_choices
# third loop: We have two product
max_profit = -99999
for i in range(product1_price_choices):
    for j in range(product2_price_choices):
        # Now, we get sales for each product
        product1_sales = sales_list[0][i][j]
        product2_sales = sales_list[1][i][j]
        profit = (product1_price_list[i]-product1_cost)*product1_sales +\
            (product2_price_list[j]-product2_cost)*product2_sales
        if profit > max_profit:
            max_profit = profit
            bpop1 = product1_price_list[i]  # Best price of product 1
            bpop2 = product2_price_list[j]  # Best price of product 2
        elif profit == max_profit:
            if product1_price_list[i] < bpop1:
                bpop1 = product1_price_list[i]
                bpop2 = product1_price_list[j]
            elif (product1_price_list[i] == bpop1) & (product2_price_list[j] < bpop2):
                bpop2 = product2_price_list[j]

# Print outcome
print(bpop1, bpop2, max_profit, sep=',')
