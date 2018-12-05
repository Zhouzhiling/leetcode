import numpy as np

output = open("./D-out-large.txt", 'w+')
with open('D-large-practice.in') as fp:
    T = int(fp.readline())
    cur_rd = 1
    while cur_rd <= T:
        key = 'Case #'+str(int(cur_rd))+':'
        total = ''
        cur_rd += 1
        list = fp.readline().strip('\n').split(' ')
        N = int(list[0])
        Q = int(list[1])
        array_list = fp.readline().strip('\n')
        ini_array = [int(n) for n in array_list.split()]
        array = np.zeros(int(N*(N+1)/2))
        count = 0
        for t in range(0, len(ini_array)):
            for tt in range(t, len(ini_array)):
                array[count] = sum(ini_array[t:tt+1])
                count += 1
        array.sort()
        count = 0
        start_arr = np.zeros(Q)
        end_arr = np.zeros(Q)
        while count < Q:
            tmp = fp.readline().strip('\n')
            [st, ed] = [int(n) for n in tmp.split()]
            count = count + 1
            cur = sum(array[st-1:ed])
            total = total + '\n' + str(int(cur))

        print(key + total)
        print('{0}'.format(key+total), file=output)
        # blank = fp.readline()
