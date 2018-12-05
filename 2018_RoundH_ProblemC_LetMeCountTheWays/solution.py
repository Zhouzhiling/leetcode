import numpy as np
import math

# 算半个小时也没算出来公式
# 于是找了答案，哎
# 放在高考前我一定能半小时算出这个排列组合的><
# 算公式的方法在large数据集上超时了emmm
# todo: 之后看懂计算公式 + 不超时的方法


def c(m, n):
    return int(math.factorial(m) / (math.factorial(n) * math.factorial(m - n)))


output = open("./C-large-practice.out", 'w+')
with open('./C-large-practice.in') as fp:
    T = int(fp.readline())
    cur_rd = 1
    while cur_rd <= T:
        key = 'Case #'+str(int(cur_rd))+': '
        cur_rd += 1
        NM = fp.readline().strip('\n')
        [N, M] = [int(n) for n in NM.split()]
        L = 2 * N
        flag = -1
        total = 0
        for i in range(M+1):
            flag = -flag
            a = c(M, i)
            b = int(math.factorial(L-i))
            d = 2 ** i
            total += int(int(flag) * a * b * d)
            total -= (total // 1000000007) * 1000000007

        total = int(total % 1000000007)

        total_str = str(total)
        print(key+total_str)
        print('{0}'.format(key+total_str), file=output)
