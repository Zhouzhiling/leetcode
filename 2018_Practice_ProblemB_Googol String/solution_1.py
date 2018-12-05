import numpy as np
import math
output = open("./out_large.txt", 'w+')

with open('./B-large-practice.in') as fp:
    T = int(fp.readline())
    cur_rd = 1
    total = ''
    while cur_rd <= T:
        key = 'Case #'+str(int(cur_rd))+': '
        k = int(fp.readline())
        t = pow(10, 100)
        # St and k
        flag = 0
        while 1:
            # if middle
            if math.log(k, 2) == t-1 or k==0:
                break
            # if left part
            elif math.log(k, 2) < t-1:
                t = math.ceil(math.log(k+1, 2))
            elif math.log(k, 2) > t-1:
                # if right part
                k = pow(2, t) - k
                if k == 0:
                    break
                t -= 1
                if flag == 1:
                    flag = 0
                else:
                    flag = 1
            # print('t = ',str(t), '; k = ',str(k))
        print(key + str(int(flag)))
        print('{0}'.format(key+str(int(flag))), file=output)
        cur_rd += 1
    blank = fp.readline()
