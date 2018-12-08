from __future__ import division
import numpy as np


def delete_duplicate(c_digit):
    output = []
    for n in c_digit:
        if output.count(n) == 0:
            output.append(n)
    return output


output = open("./B-small-practice.out", 'w+')
with open('B-small-practice.in') as fp:
    T = int(fp.readline())
    cur_rd = 1
    while cur_rd <= T:
        key = 'Case #'+str(int(cur_rd))+': '
        cur_rd += 1
        NP = fp.readline().strip('\n')
        [N, K, P] = [int(n) for n in NP.split()]

        count = 0
        suffix = []
        c_digit = []
        result = []
        for k in range(N):
            result.append('0')

        while count < K:
            count = count + 1
            cur = fp.readline().strip('\n')
            [A, B, V] = [int(n) for n in cur.split()]
            result[A-1] = str(V)
            c_digit.append(A)
            c_digit = delete_duplicate(c_digit)
            total = pow(2, N - len(c_digit))

            sequence = bin(P-1)[2:]
            sequence = '0' * (N - len(c_digit) - len(sequence)) + sequence
            idx = 0
            for t in range(N):
                if c_digit.count(t+1) == 0:
                    # if idx >= len(sequence):
                    #     result[t] = '0'
                    # else:
                    result[t] = sequence[idx]
                    idx += 1

            result_str = ''.join(result)
        print(key + result_str)
        print('{0}'.format(key+result_str), file=output)
