mn_list = [int(i) for i in input().split(',')]
machines = mn_list[0]
works = mn_list[1]
worktime_list = [int(t) for t in input().split(',')]
deadline_list = [int(dl) for dl in input().split(',')]
diff_list = [worktime_list[i] - deadline_list[i] for i in range(works)]

# save time list for ti, default is 0
machine_time_list = [0 for _ in range(machines)]

# loop: decide how many times we need to run (given works)
total_delay = 0
for i in range(works):
    # ! decrease for loop increase efficiency!!
    next_machine = machine_time_list.index(min(machine_time_list))
    next_work = diff_list.index(min(diff_list))
    delay = machine_time_list[next_machine] + diff_list[next_work]
    machine_time_list[next_machine] += worktime_list[next_work]  # update the machine's work time which we choose
    diff_list[next_work] = 9999999999  # avoid us repeat do the same work
    # calculate delay time
    if delay > 0:
        total_delay += delay
# outcome
print(total_delay)
