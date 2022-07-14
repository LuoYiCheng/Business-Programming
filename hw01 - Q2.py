# 讀數、指派變數
p_chicken = int(input())
p_fries = int(input())
p_drieddofu = int(input())
q_chicken = int(input())
q_fries = int(input())
q_drieddofu = int(input())
discount_threshold_1 = int(input())    
discount_amount_1 = int(input())
discount_threshold_2 = int(input())    
discount_amount_2 = int(input())

TOTAL_COST = p_chicken*q_chicken + p_fries*q_fries + p_drieddofu*q_drieddofu
discounted_cost = p_chicken*q_chicken + p_fries*q_fries + p_drieddofu*q_drieddofu

after_first_discounted = discounted_cost - discount_threshold_1
after_second_discounted = after_first_discounted - (after_first_discounted//discount_threshold_2)*discount_threshold_2

if after_first_discounted >= 0:
    if after_first_discounted//discount_threshold_2 > 0:
        discounted_cost -= (discount_amount_1 + (after_first_discounted//discount_threshold_2)*discount_amount_2) 
    else:
        discounted_cost -= discount_amount_1
        

#印出結果
print(str(TOTAL_COST) + ',' + str(discounted_cost))