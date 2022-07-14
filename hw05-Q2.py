# 定義一個時間運算的函數
def time_elapsed(hour, minute, second, duration, unit = 's'):
    '''Given an event start time and event duration,
    a function that can calculate the event end time.'''
    if unit == 's':
        second += duration
    elif unit == 'm':
        minute += duration
    else:
        hour += duration
    while second >= 60:
        second -= 60
        minute += 1
    while minute >= 60:
        minute -= 60
        hour += 1
    while hour >= 24:
        hour -= 24
    return hour, minute, second 

# 再定義一個檢查輸入格式的函數
def check_input(hour, minute, second, duration, unit):
    '''assure input format is eligible'''
    condition1 = (0 <= hour <= 23) and (0 <= (minute or second) <= 59)
    condition2 = duration >= 0
    condition3 = unit in ['s', 'm', 'h']
    return condition1 and condition2 and condition3
    
# Input variables
time_list = [int(i) for i in input().split(',')]
hour = time_list[0]
minute = time_list[1]
second = time_list[2]
n_events = int(input())


# 演算法
is_legal = True
for event in range(n_events):
    input_list = [i for i in input().split(',')]
    duration = int(input_list[0])
    unit = input_list[1]
    # 先檢查輸入格式
    if check_input(hour, minute, second, duration, unit) == True:
        hour, minute, second = time_elapsed(hour, minute, second, duration, unit)
    else:
        is_legal = False
        continue

# 判定我們要印出的答案
if is_legal == True:    
    result = ':'.join(str(i) for i in [hour, minute, second])
else:
    result = -1

# 印出結果
print(result)