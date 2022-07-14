import re
# input
text = input()

# 先將所有,-.變成空白
# 解決, or . 後面沒空白的狀況
# 以及視-前後為個別詞彙
comma_dot_pt = re.compile('[\.\,\-:?!]')
text = re.sub(comma_dot_pt, ' ', text)
# print(text)

# 用來蒐集字首的list
prefix_list = []

text_list = text.split()
for i, string in enumerate(text_list):
    # 檢查是否有['"-]
    for sign in ['\'', '\"', '(', ')']:
        first_index = string.find(sign)
        if first_index != -1:
            # 繼續檢查是否有第二個' "
            second_index = string.find(sign, first_index+1)
            if second_index != -1:
                # exaple: 'D', 'fader'
                # !假設沒有'he'is 這種狀況
                n_between_alpha = second_index - first_index - 1
                if n_between_alpha <= 1:
                    continue
                else:
                    # 將前後變成空白
                    # 'fader' -> fader
                    text_list[i] = string.replace(sign,'')
            else:
                # 'Python -> Python
                # fader' -> fader
                text_list[i] = string.replace(sign,'')
            # 處理完一樣要取大寫字首
            prefix_list.append(text_list[i].capitalize()[0])
        # 這是一般情況, ex: Python
        else:
            continue
    # 假設都沒出現以上四種sign
    if len(prefix_list) < i+1:
        prefix_list.append(text_list[i].capitalize()[0])
        
# print(text_list)
# print(prefix_list)

# 用來存放count的list
count_list = []
for ascii_code in range(65, 90 + 1):
    alpha = chr(ascii_code)
    count_list.append(prefix_list.count(alpha))
# print(count_list)
# 位數決定怎麼對齊
n_digits = len(str(max(count_list)))

# 用來存放字母出現次數不為0的清單
alpha_count_list = []
for ascii_code in range(65, 90 + 1):
    alpha = chr(ascii_code)
    count = prefix_list.count(alpha)
    alpha_count_list.append([alpha, count])

# print(alpha_count_list)
# [['A', 10], ['B', 2], ['C', 4], ['D', 4], ['E', 1], ['F', 2], ['I', 7], ['L', 3], ['N', 1], ['O', 6], ['P', 7], ['R', 1], ['S', 5], ['T', 7], ['U', 1], ['W', 2]]

# 用來存放結果的list
result_list = []
# 目標是找到前3多的alpha並輸出，
# 如果次數等於當前最大的次數，就append，
# 因為alpha_count_list已經照順序排列了，
# 所以只要用for迴圈照順序append就好
while len(result_list) < 3:
    max_count = max(count_list)
    for i in range(len(alpha_count_list)):
        if alpha_count_list[i][1] == max_count:
            result_list.append(alpha_count_list[i])
            count_list[i] = -1
            # 長度等於3就停
            if len(result_list) == 3:
                break
        else:
            continue

# 印出結果
for alpha, count in result_list:
    if n_digits == 1:
        print('{}:{:>1d}'.format(alpha, count))
    elif n_digits == 2:
        print('{}:{:>2d}'.format(alpha, count))
    elif n_digits == 3:
        print('{}:{:>3d}'.format(alpha, count))
    else:
        print('{}:{:>4d}'.format(alpha, count))