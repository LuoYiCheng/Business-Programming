# define function
def print_mode(mode:str):
    '''用來決定要以哪一種模式輸出的函數'''
    line = 0
    if mode == 'C':
        for key, value in cid_consumption_dict.items():
            if line < 3:
                print(key, value, sep=',')
                line += 1
    else:
        for key, value in pid_cust_dict.items():
            if line < 3:
                print(key, value, sep=',')
                line += 1
    return


# Get path
# path = 'homework\week_homework\example1.csv'
path = input()
n_row = int(input())
mode = input()

# Read file
with open(path, 'r', encoding='utf-8') as file:
    data_list = []
    for line in file:
        # 將換行字元消除
        data_list.append(line.replace('\n', ''))
for i in range(len(data_list)):
    data_list[i] = data_list[i].split(',')

# delete first raw
# ['CID', 'PID', 'QTY', 'UNIT_PRICE']
del data_list[0]

# build dict to summary our info
cid_consumption_dict = dict()
pid_cust_dict = dict()

# Append details
for record in data_list:
    cid = int(record[0])
    pid = record[1]
    qty = int(record[2])
    unit_price = int(record[3])
    # 處理顧客金額
    if cid in cid_consumption_dict:
        cid_consumption_dict[cid] += qty * unit_price
    else:
        cid_consumption_dict[cid] = qty * unit_price
    # 處理產品個數
    try:
        if cid not in pid_cust_dict[pid]:
            pid_cust_dict[pid].add(cid)
        else:
            continue
    except KeyError:
        pid_cust_dict[pid] = {cid}
# print(pid_cust_dict)
# 計算產品購買顧客數
for key in pid_cust_dict.keys():
    pid_cust_dict[key] = len(pid_cust_dict.get(key))
# 排序
cid_consumption_dict = dict(sorted(cid_consumption_dict.items(), key = lambda kv: (-kv[1], kv[0])))
# cid_consumption_dict = dict(sorted(cid_consumption_dict.items(), key = lambda kv: kv[1], reverse=True))
pid_cust_dict = dict(sorted(pid_cust_dict.items(), key = lambda kv: (-kv[1], kv[0])))
# pid_cust_dict = dict(sorted(pid_cust_dict.items(), key = lambda kv: kv[1], reverse=True))

# # 輸出
# print('cid_consumption_dict:{}'.format(cid_consumption_dict))
print_mode(mode)