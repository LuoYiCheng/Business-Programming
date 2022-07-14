n_t = input()
n_t_list = [int(i) for i in n_t.split(',')]
n_food = n_t_list[0]         # There are  n category food 
dis_threshold = n_t_list[1]  # Once meet this threshold, customer could get a coupon!

# Input and Create price list
price_str = input()
price_list = [int(i) for i in price_str.split(',')]

# Input and Create food unit list
food_str = input()
food_list = [int(i) for i in food_str.split(',')]

# Let's compute
total_amount = 0
for i in range(n_food):
    total_amount += price_list[i] * food_list[i]

coupon = total_amount // dis_threshold

# Outcome
print(total_amount, coupon, sep=',')