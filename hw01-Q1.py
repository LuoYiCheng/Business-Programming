# 讀數、指派變數
p_chicken = int(input())
p_fries = int(input())
p_drieddofu = int(input())
q_chicken = int(input())
q_fries = int(input())
q_drieddofu = int(input())
discount_threshold = int(input())    #  滿t元就送折價券

Total_Cost = p_chicken*q_chicken + p_fries*q_fries + p_drieddofu*q_drieddofu

coupon_count = Total_Cost // discount_threshold

#印出結果
print(str(Total_Cost) + ',' + str(coupon_count))