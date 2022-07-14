input1 = input()
input_list = []
for i in input1.split(','):
    input_list.append(int(i))
n_items = input_list[0]
weight_limit = input_list[1]  # B

weight_input = input()
weight_list = []
for i in weight_input.split(','):
    weight_list.append(int(i))

utility_input = input()
utility_list = []
for i in utility_input.split(','):
    utility_list.append(int(i))

k_tries = int(input())
try_list = []
for k in range(k_tries):
    bring_input = input()
    bring_list = bring_input.split(',')
    for i in range(len(bring_list)):
        bring_list[i] = int(bring_list[i])
    try_list.append(bring_list)  
# print(try_list)

#演算法
max_utility = 0
weight = 0
number = 9999999999999
for k in range(k_tries):    # 我們一共要試k次
    total_weight = 0
    total_utility = 0
    # 先計算第k次的效用及負重
    for i in range(n_items):
        total_weight += weight_list[i] * try_list[k][i+1]   # 因為try_list[0]為編號
        total_utility += utility_list[i] * try_list[k][i+1]
    # print(try_list[k][0], total_weight, total_utility, sep=',')

    if total_weight > weight_limit: # 如果超出負重就直接跳出迴圈
        continue
    else:
        # 先檢查當總效用一樣大時，我們要選編號較小的那一組
        if (total_utility == max_utility) and (try_list[k][0] < number):
            number = try_list[k][0]
            max_utility = total_utility
            weight = total_weight
        # 就算沒有滿足上面條件，我們仍要將具有較大效用的代入
        elif total_utility > max_utility:
            number = try_list[k][0]
            max_utility = total_utility
            weight = total_weight

#印出結果
print(number, weight, max_utility, sep=',')
        
