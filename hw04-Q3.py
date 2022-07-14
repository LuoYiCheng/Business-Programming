mn_list = [int(i) for i in input().split(',')]
machines = mn_list[0]
works = mn_list[1]
worktime_list = [int(t) for t in input().split(',')]
deadline_list = [int(dl) for dl in input().split(',')]

# save time list for ti, default is 0
machine_time_list = [0 for _ in range(machines)]

# First loop: decide how many times we need to run (given works)
# Second and third loop: calculate for all the combinations for work and machine
total_delay = 0
works_done = []
for i in range(works):
    min_delay = 99999999999999999  # each loop we reset delay time
    for work in range(works):
        if work in works_done:  # skip done work
            continue
        else:
            for machine in range(machines):
                #! efficiency
                if machine_time_list[machine] != min(machine_time_list):
                    continue
                else:
                    delay = machine_time_list[machine] + worktime_list[work] - deadline_list[work]
                    if delay < min_delay:
                        min_delay = delay
                        next_work = work
                        next_machine = machine
    # update the work_done list
    works_done.append(next_work)
    # update the machine's work time which we choose 
    machine_time_list[next_machine] += worktime_list[next_work]
    # calculate delay time
    if min_delay > 0:
        total_delay += min_delay
#     print('本次安排工作{work}於機台{machine},並更新t{machine}為{time}'.\
#         format(work=next_work+1, machine=next_machine+1, time=machine_time_list[next_machine]))
# print('總延遲時間{}分鐘'.format(total_delay))
print(total_delay)
