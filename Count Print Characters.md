# Count Print Characters



```python
from collections import defaultdict
import sys


if __name__ == '__main__':
    sign_stack = [sys.stdin.readline().strip()]
    lines = [sign_stack[0]]
    while sign_stack:
        line = sys.stdin.readline().strip()
        lines.append(line)
        cmd = line.strip().split()
        if cmd[0] == 'LOOP':
            sign_stack.append(line)
        if cmd[0] == 'END':
            sign_stack.pop()

    stack = []
    dict = defaultdict(int)
    for line in lines[1:-1]:
        cmd = line.split(' ')
        if cmd[0] == 'LOOP':
            if not stack:
                if cmd[1] == 'n':
                    stack.append((1, 1))
                else:
                    stack.append((int(cmd[1]), 0))
            else:
                if cmd[1] == 'n':
                    stack.append((stack[-1][0], stack[-1][1] + 1))
                else:
                    stack.append((int(cmd[1]) * stack[-1][0], stack[-1][1]))
        if cmd[0] == 'END':
            stack.pop()
        if cmd[0] == 'PRINT':
            if not stack:
                dict[0] = len(cmd[1])
            else:
                tmp = (stack[-1][0] * len(cmd[1]), stack[-1][1])
                dict[stack[-1][1]] += tmp[0]

    val = []
    dict = sorted(dict.items(), key=lambda x: x[0], reverse=True)
    for k, v in dict:
        if k == 0:
            val.append(str(v))
        elif k == 1:
            val.append(str(v) + '*n')
        else:
            val.append(str(v) + '*n^' + str(k))

    print '+'.join(val)
```

