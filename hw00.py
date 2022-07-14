#讀數、指派變數
x1 = int(input())
x2 = int(input())
x3 = int(input())

Total_Cost = 50*x1 + 40*x2 + 30*x3

coupon_count = Total_Cost // 100

#印出結果
print(str(Total_Cost) + ',' + str(coupon_count))