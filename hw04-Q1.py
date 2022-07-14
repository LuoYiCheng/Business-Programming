# input variables
mnc_list = [int(i) for i in input().split(',')]
n_class = mnc_list[0]
n_product = mnc_list[1]
cur_class = mnc_list[2]
proba_list = [int(p) for p in input().split(',')]
class_list = [int(c) for c in input().split(',')]

# we copy proba_list becuz we change the list element below
proba_list_origin = proba_list.copy()

# find the first two product's index
recommand_list = []  # store in recommand_list
while len(recommand_list) < 2:
    max_proba = max(proba_list)
    for i in range(n_product):
        if proba_list[i] == max_proba:
            recommand_list.append(i+1)  # remember plus 1
            proba_list[i] = 0  # sometimes we need to find second max num
            # ! important!! remember we just need first two index
            if len(recommand_list) == 2:
                break
        else:
            continue
proba_list = proba_list_origin  # recovery proba_list

# find the thrid product's index
ncur_max_proba = 0
ncur_class_nums = 0  # number of not in current class
for i in range(n_product):
    # i + 1 is true index in this question
    if ((i + 1) not in recommand_list) & (class_list[i] != cur_class):
        if proba_list[i] > ncur_max_proba:
            ncur_max_proba = proba_list[i]
            third_index = i + 1  # store product's index
            ncur_class_nums += 1
        else:
            continue
    else:
        continue

# append the third index to recommand_list
if ncur_class_nums != 0:
    recommand_list.append(third_index)
else:
    recommand_list.append(-1)

# outcome
print(','.join([str(i) for i in recommand_list]))
