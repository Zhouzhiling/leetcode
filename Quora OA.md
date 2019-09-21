

## Question 1. GoodTuples

Example：
Input: a = [1, 1, 2, 1, 5, 3, 2, 3]
Output: 3
Explain:
[1, 1, 2] -> two 1 and one 2(O)
[1, 2, 1] -> two 1 and one 2(O)
[2, 1, 5] -> one 2, one 1 and one five(X)
[1, 5, 3] -> (X)
[5, 3, 2] -> (X)
[3, 2, 3] -> (O)

```python
a = [1, 1, 2, 1, 5, 3, 2, 3]
length = len(a)
count = 0
for i in range(1, length-1):
    if a[i-1] == a[i] and a[i] == a[i+1]:
        continue
    elif a[i-1] == a[i] or a[i] == a[i+1] or a[i-1] == a[i+1]:
        count += 1
print(count)
```



## 第二题：remove One digit:

input1：ab12c
input:2: 1zzz456

任意remove 两个input中其中的一个数字，使得input1 的alphabet order 小于 input2 的alphabet order
a = "ab12c"
b = "1zzz456"

```python
lena = len(a)
lenb = len(b)
flag = False
for i in range(lena):
    if a[i].isnumeric():
        if i < lena-1 and a[i] > a[i+1]:
            if a[:i]+a[i+1:] < b:
                flag = True
            break
        elif a[:i]+a[i+1:] < b:
            flag = True
            break
if flag:
    print("Yes!")

for i in range(lenb):
    if b[i].isnumeric():
        if i < lenb-1 and b[i] < b[i+1]:
            if b[:i]+b[i+1:] > a:
                flag = True
            break
        elif b[:i] + b[i + 1:] > a:
            flag = True
            break

print(flag)
```



## Question 3. Rotate matrix among Diagnals

Example：
[[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
-->
[[1, 4, 3],
[8, 5, 2],
[7, 6, 9]]

[[1,2,3,4,5],
[6,7,8,9,10],
[11,12,13,14,15],
[16,17,18,19,20],
[21,22,23,24,25]]
-->
[[1,16,11,6,5],
[22,7,12,9,2],
[23,18,13,8,3],
[24,17,14,19,4],
[21,20,15,10,25]]

```python
def swap(a,i1,j1,i2,j2):
    a[i1][j1], a[i2][j2] = a[i2][j2], a[i1][j1]

a = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]]
length = len(a)
times = (length-1)//2
if length <= 1:
    print("...")
for t in range(times):
    for i in range(1, length-1-t*2):
        swap(a, t, i+t, length-1-i-t, t)

    for i in range(1, length-1-t*2):
        swap(a, i+t, t, length-1-i-t, length-1-t)

    for i in range(1, length-1-t*2):
        swap(a, length - 1 - t, i + t, i+t, t)

print(a)
```



## 第四题：等差数组

input A:[0, 4, 8, 16]
input B:[0, 2, 6, 12, 14, 20]
output: 新的A 的长度
从B中最多能选几个数字使得 A 变成一个任意两个数之间的差是相等的数组， 例如：[0, 4, 8, 12, 16, 20]

```python
A = [0, 4, 8, 16]
B = [0, 2, 6, 12, 14, 20]
setA = set(A)
setB = set(B)
lena = len(A)
minA = min(A)
maxA = max(A)
diffs = [A[i]-A[i-1] for i in range(1, lena)]
upper = min(diffs)
output = -1

# find common factor
possibilities = []
for i in range(1,upper+1):
    flag = True
    for diff in diffs:
        if diff % i != 0:
            flag = False
            break
    if flag:
        possibilities.append(i)

print(diffs)
print(possibilities)

for cur in possibilities:
    miniCount = sum(diff//cur-1 for diff in diffs)
    if miniCount > len(B):
        continue

    num = minA
    flag = True
    while num <= maxA:
        if num not in setA:
            if num not in setB:
                flag = False
                break
        num += cur
        
# 还有负向也要考虑
    if flag:
        while num in setB:
            miniCount += 1
            num += cur
        output = max(output, miniCount)
print(output)
```



## Find how many numbers have even digit in a list.

Ex.
Input: A = [12, 3, 5, 3456]
Output: 2

```python
# Output: 2
A = [12, 3, 5, 3456]
count = 0
for num in A:
    num = abs(num)
    while num > 0:
        if (num%10)%2==1:
            count += 1
            break
        num = num / 10
print(count)
```



## Question 1. frameWindow

Given an int n, print the *** window frame of the number;
Example: input -> n = 6
output -> [
"********", --> 8 *
"*           *", -> 2 * 加 六个 ' ' (space)
"*           *",
"*           *",
"*           *",
"********"
]

```python
n = 2
output = []
if n == 1:
    output.append("*")
else:
    output.append("*"*n)
    for i in range(n-2):
        output.append("*"+" "*(n-2)+"*")
    output.append("*"*n)

print(output)
```



## divisorSubstrings

Give a number n and digit number k find all serial substring is able to divisible n.
Input: n = 120, k = 2
Output: 2
Explain:
120 -> 12 and 20
120 % 12 == 0 (O)
120 % 20 == 0 (O)

```python
n = 12439750
k = 2
factor = pow(10, k-1)
sub = set()
cur = 0
num = n
count = 0
cur = n % pow(10, k)
num = num // pow(10, k)
while 1:
    print(cur)
    if n % cur == 0:
        count += 1
    cur = cur // 10 + (num%10)*factor
    if num == 0:
        break
    num = num // 10
print(count)
```



## [coolFeature](https://leetcode.com/discuss/interview-question/349634/Quora-or-Online-Assessment-with-CodeSignal)

```python
a = [1, 2, 3]
b = [3, 4]
seta = set(a)
query = [[1, 5], [1, 1, 1], [1, 5]]
res = []
for que in query:
    if len(que) == 3:
        idx = que[1]
        num = que[2]
        b[idx] = num
    else:
        count = 0
        total = que[1]
        for num in b:
            if total-num in seta:
                count += 1
        res.append(count)
print(res)
```



## Cut Pork

Ex.
Input: A = [1, 2, 3, 4, 9], k = 5
Output: 3

Explanat‍‌‌‍‌‌‍‍‍‌‌‍‌‌‍‍‍‌‌ion:
if size = 1, then we have 19 parts
if seize = 2, then we have 8 parts
if size = 3, then we have 5 parts
if size = 4, then we have 3 parts, which is not enough.
So return the max size = 3.

Sol.
Use binary search to find the size of ribbon to reach the time limit.

```python
def calculate_count(size):
    count = 0
    for pork in A:
        count += pork // size
    return count


A = [3,3,6,6]
k = 4
totalLength = sum(A)
st = 1
ed = totalLength // k
while st < ed:
    mid = (st + ed + 1)//2
    count = calculate_count(mid)
    if count >= k:
        st = mid
    elif count < k:
        ed = mid - 1
print(st)
```



## If two strings are close enough.

Given two rules to define two strings are close enough.

1. you can swap neighbor char any times. Ex. "abb" -> "bba"
2. If two strings have the same character, then you can change the character into another.
    Ex. If both strings contain "a" and "b", you can change all "a"s in the first string or change all "b"s in the first string. same as the second string
Ex.
Input: S1 = "babzccc", S2 = "abbzczz"
Output: True
Sol.
Use a dictionary to record the frequency of characters.
Remove the same part in dictionaries
try to find the pair that have different character but with the same frequency

```python
s1 = "babzcck"
s2 = "abbzczz"
record1 = {}
record2 = {}
chrset = set(ch for ch in s1)
length = len(s1)
if length != len(s2):
    print(False)
for ch in s1:
    record1[ch] = record1.get(ch, 0) + 1
for ch in s2:
    record2[ch] = record2.get(ch, 0) + 1

for ch in chrset:
    if ch not in record1 and ch not in record2:
        continue
    if ch in record1 and ch in record2:
        count1 = record1[ch]
        count2 = record2[ch]
        if count1 == count2:
            record1.pop(ch)
            record2.pop(ch)
        else:
            flag = False
            for ch2 in record2:
                if record2.get(ch2, 0) == count1 and record1.get(ch2,0) == count2:
                    flag = True
                    record1.pop(ch)
                    record1.pop(ch2)
                    record2.pop(ch)
                    record2.pop(ch2)
                    break
            if not flag:
                print("False")
                break
    else:
        print("False")
print("True")
```

