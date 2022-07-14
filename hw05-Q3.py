# Define function
def find_next_new(unvisited, dst, cur):
    '''consider next two loc, find the minimun sum dst
    and return the next loc and dst'''
    if len(unvisited) == 1:
        next_loc = unvisited[0]
        min_dst = dst[next_loc][cur]
    else:
        next_loc = -1
        min_total_dst = 999
        for next1 in unvisited:
            for next2 in filter(lambda x: x != next1, unvisited):
                if dst[cur][next1] + dst[next1][next2] < min_total_dst:
                    next_loc = next1
                    min_total_dst = dst[cur][next1] + dst[next1][next2]
                    min_dst = dst[cur][next1]
    return next_loc, min_dst


def find_next(unvisited, dst, cur):
    '''just greedy algorithm'''
    next_loc = -1
    min_dst = 999
    for j in unvisited:
        if dst[cur][j] < min_dst:
            next_loc = j
            min_dst = dst[cur][j]
    return next_loc, min_dst


# if there is a new algorithm, we can directly add it here
def choose_algorithm(algorithm):
    '''choose which algorithm we want'''
    algorithm_list = ['', find_next, find_next_new]
    return algorithm_list[algorithm]


# set up the distance matrix
n_v_list = [int(i) for i in input().split(' ')]
n_loc = n_v_list[0]
algorithm = n_v_list[1]
dst = [[int(j) for j in input().split(' ')] for _ in range(n_loc)]

# set up the origin
origin = 0

# tour: a list that will contain the solution
# tour_len: the total distance of the solution
# unvisited: a list that contains those
# unvisited locations at any time
tour = [origin]
tour_len = 0
unvisited = []
for i in range(n_loc):
    unvisited.append(i)
unvisited.remove(origin)

# The algorithm
cur = origin
for i in range(n_loc - 1):
    # find the next location to visit
    next_loc, min_dst = choose_algorithm(algorithm)(unvisited, dst, cur)
    # move "next" from unvisited to tour
    unvisited.remove(next_loc)
    tour.append(next_loc)
    tour_len += min_dst
    # run the next iteration from the next location
    cur = next_loc
# complete the tour
tour.append(origin)
tour_len += dst[cur][origin]

# print out the solution
print(','.join(str(i) for i in tour), tour_len, sep=';')
