params_list = []
for i in input().split(','):
    params_list.append(int(i))
n_applies = params_list[0]  # n
n_conditions = params_list[1]  # m
load_outcome = params_list[2]  # ci
new_persons = params_list[4]

coordinate_list = []
for i in range(n_applies):
    record_list = []
    for j in input().split(','):
        record_list.append(int(j))
    coordinate_list.append(record_list)

# 算距離
result = []
for i in range(new_persons):
    new = []
    for c in input().split(','):
        new.append(int(c))
    dis_dict = dict()
    # 每個迴圈分別計算
    for n in range(n_applies):
        # 不知道有幾個個人條件分數
        dis_square = 0
        for m in range(n_conditions):
            dis_square += (new[m] - coordinate_list[n][m]) ** 2
        dis = round(dis_square ** 0.5, 2)
        # 如果該key值未出現，則預設Value為一個List，之後再append信貸分類結果
        dis_dict.setdefault(dis, list())
        dis_dict[dis].append(str(coordinate_list[n][n_conditions]))

    # 排序結果
    dis_dict = dict(sorted(dis_dict.items(), key=lambda kv: kv[0]))

    # 建立一個依照距離排序好(最近->最遠)的信貸分類結果清單
    values = list(dis_dict.values())
    values_list = []
    for i in values:
        for j in i:
            values_list.append(j)

    # 處理是否需要拓展k的問題
    kvtuple_list = []
    for key, values in dis_dict.items():
        for value in values:
            kvtuple_list.append((key, value))
    # print(kvtuple_list)
    # 如在取第k近的紀錄時有複數筆平手，則往下繼續找
    # 直到下一個距離
    k_NN = params_list[3]
    while k_NN + 1 < n_applies:
        if kvtuple_list[k_NN - 1][0] == kvtuple_list[k_NN][0]:
            k_NN += 1
        else:
            break
    # print('k_NN :{}'.format(k_NN))

    # 決定該用戶分類
    # k_NN表示取距離最近的數目
    from collections import Counter
    k_value_list = []
    for i in values_list[:k_NN]:
        k_value_list.append(int(i))
    class_counter = Counter(k_value_list)
    # 先依value降冪，再依key升冪排序
    # class_list : [(分類, 數量), (分類, 數量))]
    class_list = sorted(class_counter.items(), key=lambda kv: (-kv[1], kv[0]))
    result.append(class_list[0][0])

# 印結果
print(','.join(str(i) for i in result))
