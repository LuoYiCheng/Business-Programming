n_stop = int(input()) # n個車站
max_sits = int(input()) # 每台巴士最大load

total_passenger = 0
total_stop = n_stop  # 保持total_stop不變

# 因為n會隨題目給定而不同，在無法使用List的情況下我選擇列出所有的條件 (題目限制1 <= n <= 10)，如此一來可避免找不到變數的Bug
if n_stop > 0:
    stop_1_remaining = int(input())
    total_passenger += stop_1_remaining
    n_stop -= 1
if n_stop > 0:
    stop_2_remaining = int(input())
    total_passenger += stop_2_remaining
    n_stop -= 1
if n_stop > 0:
    stop_3_remaining = int(input())
    total_passenger += stop_3_remaining
    n_stop -= 1
if n_stop > 0:
    stop_4_remaining = int(input())
    total_passenger += stop_4_remaining
    n_stop -= 1
if n_stop > 0:
    stop_5_remaining = int(input())
    total_passenger += stop_5_remaining
    n_stop -= 1
if n_stop > 0:
    stop_6_remaining = int(input())
    total_passenger += stop_6_remaining
    n_stop -= 1
if n_stop > 0:
    stop_7_remaining = int(input())
    total_passenger += stop_7_remaining
    n_stop -= 1
if n_stop > 0:
    stop_8_remaining = int(input())
    total_passenger += stop_8_remaining
    n_stop -= 1
if n_stop > 0:
    stop_9_remaining = int(input())
    total_passenger += stop_9_remaining
    n_stop -= 1
if n_stop > 0:
    stop_10_remaining = int(input())
    total_passenger += stop_10_remaining
    n_stop -= 1

# print(total_passenger, total_stop)

# (提醒自己)要考慮到剛好整除的狀況才不會多算一輛巴士
if total_passenger % max_sits == 0:
    n_buses = total_passenger // max_sits
else:
    n_buses = total_passenger // max_sits + 1
# print('巴士數: ', n_buses)

available_sits = 0
# 需要幾台巴士就跑幾個迴圈
for bus in range(n_buses):
    available_sits = max_sits  # 新的迴圈代表巴士乘載量又回復了
    n_stop =  total_stop 
    if n_stop > 0:
        # 狀況一：巴士剩餘座位能夠承載該站人數，就直接印出該站人數就好
        # 狀況二：如果不夠減就印出巴士人數
        if (available_sits - stop_1_remaining) >= 0:
            print(stop_1_remaining, end='')           
            available_sits -= stop_1_remaining
            stop_1_remaining = 0
        else:
            print(available_sits, end='')
            stop_1_remaining -= available_sits
            available_sits = 0
        n_stop -= 1


    if n_stop > 0:
        print(',', end='')  # 在印出下一個數字之前先印逗號
        if (available_sits - stop_2_remaining) >= 0:
            print(stop_2_remaining, end='')           
            available_sits -= stop_2_remaining
            stop_2_remaining = 0
        else:
            print(available_sits, end='')
            stop_2_remaining -= available_sits
            available_sits = 0
        n_stop -= 1

    if n_stop > 0:
        print(',', end='')
        if (available_sits - stop_3_remaining) >= 0:
            print(stop_3_remaining, end='')           
            available_sits -= stop_3_remaining
            stop_3_remaining = 0
        else:
            print(available_sits, end='')
            stop_3_remaining -= available_sits
            available_sits = 0
        n_stop -= 1

    if n_stop > 0:
        print(',', end='')
        if (available_sits - stop_4_remaining) >= 0:
            print(stop_4_remaining, end='')           
            available_sits -= stop_4_remaining
            stop_4_remaining = 0
        else:
            print(available_sits, end='')
            stop_4_remaining -= available_sits
            available_sits = 0
        n_stop -= 1

 
    if n_stop > 0:
        print(',', end='')
        if (available_sits - stop_5_remaining) >= 0:
            print(stop_5_remaining, end='')           
            available_sits -= stop_5_remaining
            stop_5_remaining = 0
        else:
            print(available_sits, end='')
            stop_5_remaining -= available_sits
            available_sits = 0
        n_stop -= 1


    if n_stop > 0:
        print(',', end='')
        if (available_sits - stop_6_remaining) >= 0:
            print(stop_6_remaining, end='')           
            available_sits -= stop_6_remaining
            stop_6_remaining = 0
        else:
            print(available_sits, end='')
            stop_6_remaining -= available_sits
            available_sits = 0
        n_stop -= 1


    if n_stop > 0:
        print(',', end='')
        if (available_sits - stop_7_remaining) >= 0:
            print(stop_7_remaining, end='')           
            available_sits -= stop_7_remaining
            stop_7_remaining = 0
        else:
            print(available_sits, end='')
            stop_7_remaining -= available_sits
            available_sits = 0
        n_stop -= 1


    if n_stop > 0:
        print(',', end='')
        if (available_sits - stop_8_remaining) >= 0:
            print(stop_8_remaining, end='')           
            available_sits -= stop_8_remaining
            stop_8_remaining = 0
        else:
            print(available_sits, end='')
            stop_8_remaining -= available_sits
            available_sits = 0
        n_stop -= 1


    if n_stop > 0:
        print(',', end='')
        if (available_sits - stop_9_remaining) >= 0:
            print(stop_9_remaining, end='')           
            available_sits -= stop_9_remaining
            stop_9_remaining = 0
        else:
            print(available_sits, end='')
            stop_9_remaining -= available_sits
            available_sits = 0
        n_stop -= 1


    if n_stop > 0:
        print(',', end='')
        if (available_sits - stop_10_remaining) >= 0:
            print(stop_10_remaining, end='')           
            available_sits -= stop_10_remaining
            stop_10_remaining = 0
        else:
            print(available_sits, end='')
            stop_10_remaining -= available_sits
            available_sits = 0
        n_stop -= 1
    print('') # 每輛公車跑完後要換行