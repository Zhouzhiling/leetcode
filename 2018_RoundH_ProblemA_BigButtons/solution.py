from __future__ import division
import numpy as np
output = open("./A-large-practice.out", 'w+')
with open('A-large-practice.in') as fp:
    T = int(fp.readline())
    cur_rd = 1
    while cur_rd <= T:
        key = 'Case #'+str(int(cur_rd))+': '
        cur_rd += 1
        NP = fp.readline().strip('\n')
        [N, P] = [int(n) for n in NP.split()]

        count = 0
        suffix = []
        while count < P:
            count = count + 1
            print('Count:\t', count)
            cur = fp.readline().strip('\n')
            flag = 1
            if len(suffix) == 0:
                suffix.append(cur)
                print('Add:\t', cur)
            else:
                for suf in suffix:
                    if cur.startswith(suf):
                        flag = 0
                        break
                    elif suf.startswith(cur):
                        suffix.remove(suf)
                        print('Rem:\t', suf)
                if flag is 1:
                    suffix.append(cur)
                    print('Add:\t', cur)


        # then calculate the number of possible combinations
        total = pow(2, N)
        for suf in suffix:
            cur_len = len(suf)
            total -= pow(2, N-cur_len)

        total_str = str(total)
        print(key + total_str)
        print('{0}'.format(key+total_str), file=output)
