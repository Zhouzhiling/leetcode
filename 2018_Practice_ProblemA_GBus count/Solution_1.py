# https://github.com/alexwaweru/kickstart_practice_2018/blob/master/kickstart_practice_round_2018/GBus_count/solution.py
import numpy as np

output = open("./out_large.txt", 'w+')
with open('A-large-practice.in') as fp:
    T = int(fp.readline())
    cur_rd = 1
    while cur_rd <= T:
        key = 'Case #'+str(int(cur_rd))+':'
        cur_rd += 1
        bus_num = int(fp.readline())

        bus_stop_list = fp.readline()
        bus_stop = [int(n) for n in bus_stop_list.split()]

        test_num = int(fp.readline())
        count = 0
        test_arr = np.zeros(test_num)
        while count < test_num:
            test_arr[count] = int(fp.readline())
            count = count + 1

        max_num = np.max(bus_stop)
        bus_num_arr = np.zeros([max_num+1])
        for t in range(0, len(bus_stop)):
            if t % 2 == 1:
                continue
            for i in range(bus_stop[t], bus_stop[t+1]+1):
                bus_num_arr[i] = bus_num_arr[i]+1

        count = 0
        total = ''
        while count < test_num:
            cur_city = int(test_arr[count])
            if cur_city > max_num:
                value = 0
            else:
                value = bus_num_arr[cur_city]
            total = total + ' ' + str(int(value))
            count += 1

        print(key + total)
        print('{0}'.format(key+total), file=output)
        blank = fp.readline()


