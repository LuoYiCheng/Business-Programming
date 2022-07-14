n_works = int(input())
worktime_list = [[int(t)] for t in input().split(',')]
deadline_list = [int(dl) for dl in input().split(',')]

# 先把worktime變成一個[t, 原本工作編號]的Nest List
for i in range(n_works):
    worktime_list[i].append(i)
    worktime_list[i].append(deadline_list[i])
# [[5, 0, 19], [8, 1, 12], [4, 2, 15], [1, 3, 6], [3, 4, 4]]

# 案deadline時間做排序
worktime_list = sorted(worktime_list, key=lambda work: work[2])
# [[3, 4, 4], [1, 3, 6], [8, 1, 12], [4, 2, 15], [5, 0, 19]]
deadline = []
for i in range(n_works):
    deadline.append(worktime_list[i].pop(2))
# worktime_list: [[3, 4], [1, 3], [8, 1], [4, 2], [5, 0]]
# deadline: [4, 6, 12, 15, 19]

# 開始排工作流程
cur_t = 0  # 從t=0出發
workflow = []  # 用來裝工作順序的list
skip = []  # 用來裝略過工作的清單
for i in range(n_works):
    if cur_t + worktime_list[i][0] <= deadline[i]:
        workflow.append(worktime_list[i][1])
        cur_t += worktime_list[i][0]
    else:
        skip.append(worktime_list[i])

# 最後再把沒有運行的工作加到工作流程中
delay_t = 0
for i in range(len(skip)):
    workflow.append(skip[i][1])
    cur_t += skip[i][0]
    delay_t += cur_t - deadline_list[skip[i][1]]

# 印出結果
print(','.join(str(i+1) for i in workflow) + ';' + str(delay_t))

# for i in range(n_works):
#     if cur_t + worktime_list[i] <= deadline_list[i]:
#         workflow.append(i)
#         cur_t += worktime_list[i]
#     else:
#         skip.append(i)

# # 最後再把沒有運行的工作加到工作流程中
# for i in skip:
#     workflow.append(i)

# print(','.join(str(i+1) for i in workflow) + ';' + str(len(skip)))


# for dl in deadline_list:
#     for work in range(n_works):
#         if worktime_list[work] == 0:  # 如果該工作已執行完，就直接往下一個找
#             continue
#         # 如果該工作不會延遲，則執行它，工作時間歸0以免之後重複做
#         if cur_t + worktime_list[work] <= dl:
#             cur_t += worktime_list[work]
#             worktime_list[work] = 0
