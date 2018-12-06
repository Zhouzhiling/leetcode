import numpy as np
import string

output = open("./A-small-practice.out", 'w+')
with open('A-small-practice.in') as fp:
    T = int(fp.readline())
    cur_rd = 1
    while cur_rd <= T:
        key = 'Case #'+str(int(cur_rd))+': '
        cur_rd += 1
        list = fp.readline().strip('\n')
        [s, e] = [int(n) for n in list.split()]
        count = 0
        for i in range(s, e+1):
            digit_sum = 0
            arr = str(i)
            if arr.find('9') != -1:
                continue
            for n in range(0, len(arr)):
                digit_sum += int(arr[n])
            if digit_sum % 9 != 0:
                count += 1
        count_str = str(count)
        print(key + count_str)
        print('{0}'.format(key+count_str), file=output)
