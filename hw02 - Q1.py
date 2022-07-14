n_foods = int(input())
list_price = [] # 用來儲存每種食物價格的List
list_count = [] # 用來儲存每種食物個數的List

# 讀數價格與數量時同時計算花費
total_cost = 0
for i in range(n_foods):
    price_i = int(input())
    count_i = int(input())
    total_cost += price_i * count_i    

discount_threshold = int(input())

n_coupons = total_cost // discount_threshold # 計算折價券張數

print(total_cost, n_coupons, sep=',') # 印出結果
# Used Memory (kb)：2948
# Used Time (ms) ：444

# 清單的解法
# for n in range(n_foods):
#     price_food = int(input())
#     count_food = int(input())
#     list_price.append(price_food)
#     list_count.append(count_food)


# total_cost = 0
# for i in range(n_foods):
#     total_cost += list_price[i] * list_count[i]
