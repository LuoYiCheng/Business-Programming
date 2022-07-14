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

bring_input = input()
bring_list = []
for i in bring_input.split(','):
    bring_list.append(int(i))

total_weight = 0
total_utility = 0
for i in range(n_items):
    total_weight += weight_list[i] * bring_list[i]
    total_utility += utility_list[i] * bring_list[i]

if total_weight > weight_limit:
    print(-1)
else:
    print(total_weight, total_utility, sep=',')