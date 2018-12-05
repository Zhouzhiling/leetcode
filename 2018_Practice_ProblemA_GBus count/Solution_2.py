# https://github.com/alexwaweru/kickstart_practice_2018/blob/master/kickstart_practice_round_2018/GBus_count/solution.py
import numpy as np

output = open("./out_small_2.txt", 'w+')
with open('A-small-practice.in') as fp:
    T = int(fp.readline())
    cur_rd = 1
    while cur_rd <= T:
        key = 'Case #'+str(int(cur_rd))+':'
        cur_rd += 1
        bus_num = int(fp.readline())

        bus_stop_list = fp.readline()
        bus_stop = [int(n) for n in bus_stop_list.split()]

        stop_start = [bus_stop[k] for k in range(0, len(bus_stop), 2)]
        stop_end = [bus_stop[k] for k in range(1, len(bus_stop), 2)]
        test_num = int(fp.readline())
        count = 0
        test_arr = np.zeros(test_num)
        while count < test_num:
            test_arr[count] = int(fp.readline())
            count = count + 1

        count = 0
        total = ''
        while count < test_num:
            cur_city = int(test_arr[count])
            value = 0
            for item in range(0, len(stop_start)):
                if stop_end[item] >= cur_city >= stop_start[item]:
                    value += 1

            total = total + ' ' + str(int(value))
            count += 1

        print(key + total)
        print('{0}'.format(key+total), file=output)
        blank = fp.readline()


