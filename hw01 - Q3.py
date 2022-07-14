# 讀數、指派變數
p_chicken = int(input())
p_fries = int(input())
p_drieddofu = int(input())
q_chicken = int(input())
q_fries = int(input())
q_drieddofu = int(input())
discount_threshold = int(input())    #  滿t元先折s元
discount_amount = int(input())

NONDIS_TOTAL_COST = p_chicken*q_chicken + p_fries*q_fries + p_drieddofu*q_drieddofu  #  固定常數，假設並未多採購所需花費
expected_cost = p_chicken*q_chicken + p_fries*q_fries + p_drieddofu*q_drieddofu      #  可操作變數
final_cost = 0   #  最後所需花費 (Anwser)

# 如果原本採購金額已超過t，直接計算總花費
if expected_cost > discount_threshold:
    final_cost += expected_cost - discount_amount
# 否則先計算達到t需要多買幾份豆干
else:
    extra_q_drieddofu = (discount_threshold-expected_cost)//p_drieddofu + 1  
    expected_cost += extra_q_drieddofu * p_drieddofu - discount_amount
    #  比較多買豆乾的方案是否能夠達到較低花費
    if expected_cost < NONDIS_TOTAL_COST:
        q_drieddofu += extra_q_drieddofu
        final_cost += expected_cost
    else:
        final_cost = NONDIS_TOTAL_COST
    
#印出結果
print(q_chicken, q_fries, q_drieddofu, final_cost, sep=',')