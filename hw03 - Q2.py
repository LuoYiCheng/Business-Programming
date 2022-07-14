n_m_t = input()
n_m_t_list = [int(i) for i in n_m_t.split(',')]
n_food = n_m_t_list[0]         # There are  n category food 
n_customers = n_m_t_list[1]     # We have m customers
dis_threshold = n_m_t_list[2]  # Once meet this threshold, customer could get a coupon!

# Input and Create price list
price_str = input()
price_list = [int(i) for i in price_str.split(',')]

# Input and Create food unit list, Nestlist: m x n
food_list = [[int(i) for i in input().split(',')] for m in range(n_customers)]


# Let's compute
total_amount = 0
coupon = 0
for m in range(n_customers):  # Because We need to calculate each consumer's amount of consupmtion,
                              # so first loop is determined by n_customers.
    amount_of_consupmtion = 0
    
    for i in range(n_food):   # i represent type of food
        amount_of_consupmtion += price_list[i] * food_list[m][i]
    
    coupon += amount_of_consupmtion // dis_threshold
    total_amount += amount_of_consupmtion

# Outcome
print(total_amount, coupon, sep=',')