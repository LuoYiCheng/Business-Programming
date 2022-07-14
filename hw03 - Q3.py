# Input & Create variable
n_K_str = input()
n_K_list = [int(i) for i in n_K_str.split(',')]
n_stop = n_K_list[0]
maximum_load = n_K_list[1]

# Input & Create passenger list
passenger_list = [int(p) for p in input().split(',')]

# Let's compute!
total_passengers = sum(passenger_list)

# we need n buses
n_bus = total_passengers // maximum_load
if total_passengers % maximum_load != 0:
    n_bus += 1

# One more bus means we need to print one more line, therefore, we  loop n_bus times first!
# Then we go through each stop to decide whether carry passengers at that station.
for bus in range(n_bus):
    available_seats = maximum_load  # new bus, maximum load!
    carry_list = []  # record this bus carry how many passengers at each stop
    for stop in range(n_stop):
        # Just append 0 to list when there are no passenger at stop.
        if passenger_list[stop] == 0:
            carry_list.append(0)  
            continue

        # when bus do not have enough seat, we carry passenger until no available seats.
        if available_seats < passenger_list[stop]:
            carry_list.append(available_seats)
            passenger_list[stop] -= available_seats
            available_seats = 0
            break  # the current bus don't have any available seat, just BREAK.
        # We can carry all passenger at this stop!
        else:
            carry_list.append(passenger_list[stop])
            available_seats -= passenger_list[stop]
            passenger_list[stop] = 0
    # We must append 0 if that bus didn't go through remaining stop
    while len(carry_list) < n_stop:
        carry_list.append(0)
    print(','.join(str(_) for _ in carry_list))