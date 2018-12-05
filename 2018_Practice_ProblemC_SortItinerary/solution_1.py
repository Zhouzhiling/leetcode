import numpy as np


def get_keys(d, value):
    return [k for k, v in d.items() if v == value]


output = open("./out-large.txt", 'w+')
with open('C-large-practice.in') as fp:
    T = int(fp.readline())
    cur_rd = 1
    while cur_rd <= T:
        key = 'Case #'+str(int(cur_rd))+':'
        cur_rd += 1
        ticket_num = int(fp.readline())
        info = dict()
        total = ''
        cur = 0
        start_sp = np.zeros(ticket_num)
        stop_sp = np.zeros(ticket_num)
        for cur in range(0, ticket_num):
            start_name = fp.readline().strip('\n')
            stop_name = fp.readline().strip('\n')
            if not info.__contains__(start_name):
                info[start_name] = 2*cur
            if not info.__contains__(stop_name):
                info[stop_name] = 2*cur+1
            start_sp[cur] = info[start_name]
            stop_sp[cur] = info[stop_name]

        # find start city
        for t in range(0, 2*cur+1):
            if sum(start_sp == t) == 1 and sum(stop_sp == t) == 0:
                start_city = t
                start_city_id = np.where(start_sp == start_city)[0]

        cur_id = start_city_id
        for t in range(0, ticket_num):
            end_city = stop_sp[cur_id]
            total = total + ' ' + get_keys(info, start_sp[cur_id])[0] + '-' + get_keys(info, stop_sp[cur_id])[0]
            cur_id = np.where(start_sp == end_city)[0]

        print(key + total)
        print('{0}'.format(key+total), file=output)
        # blank = fp.readline()
