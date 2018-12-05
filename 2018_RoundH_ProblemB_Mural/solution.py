import numpy as np
import math

# 想清楚之后就是找最大连续子列的问题
# 洪水无法侵蚀已经画过的墙，所以找到子列以后一定可以全部画满

# 时间复杂度O(N)
output = open("./B-large-practice.out", 'w+')
with open('./B-large-practice.in') as fp:
    T = int(fp.readline())
    cur_rd = 1
    while cur_rd <= T:
        key = 'Case #'+str(int(cur_rd))+': '
        cur_rd += 1
        N = int(fp.readline().strip('\n'))
        wall = fp.readline().strip('\n')
        paint_num = int((len(wall)+1)/2)
        cur = sum([int(n) for n in wall[0:paint_num]])
        total = cur
        for t in range(0, len(wall)-paint_num):
            cur = cur - int(wall[t]) + int(wall[paint_num+t])
            total = max(total, cur)
        total_str = str(total)
        print(key+total_str)
        print('{0}'.format(key+total_str), file=output)
