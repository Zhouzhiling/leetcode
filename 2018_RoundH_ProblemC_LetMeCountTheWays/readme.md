### Problem

To celebrate the anniversary of Googleland, **N** couples are going to go for a boat ride in a rowboat. The rowboat is very long, but it is only one person wide, so the people will sit in a line from front to back.

However, during a rehearsal of the voyage, the boat did not move! After investigating, the organizers found that some newlywed couples were not rowing, but writing love poems for each other the whole time. Specifically, there are **M** pairs of newlywed couples. If the two members of a newlywed couple are sitting next to each other, they will be so busy writing poems that they will not row.

Now the organizers have come to you, the smartest person in Googleland, to ask, how many possible ways are there to arrange all 2**N** people on the rowboat, such that for each of the **M** newlywed couples, the two members are not sitting next to each other? Two ways are different if there is some position in the boat at which the two ways use different people. Notice that for the purpose of counting the number of ways, the two members of a couple are not considered to be interchangeable. Since the number can be very large, the organizers only want to know the value of the answer modulo 1000000007(109+7).

### Input

The first line of the input gives the number of test cases, **T**. **T** test cases follow. Each test case consists of one line with two integers **N** and **M** as described above.

### Output

For each test case, output one line containing `Case #x: y`, where `x` is the test case number (starting from 1) and `y` is the number of possible arrangements, modulo 1000000007(109+7).

### Limits

1 ≤ **T** ≤ 100.

#### Small dataset

1 ≤ **M** ≤ **N** ≤ 100.

#### Large dataset

1 ≤ **M** ≤ **N** ≤ 100000.

### Sample

Input

```
5
2 1
2 2
3 1
3 2
10 5
```

Output

```
Case #1: 12
Case #2: 8
Case #3: 480
Case #4: 336
Case #5: 560963525
```

In Sample Case #1, there are 2 couples. To make the description simpler, we use the characters `A` and `a` to represent the newlywed couple, and `B` and `b` to represent the other couple. Per the rules of the problem, `A` and `a` cannot be adjacent. There are 12 ways to arrange the four people:
`ABab` `ABba` `AbaB` `AbBa`
`aBAb` `aBbA` `abAB` `abBA`
`BAba` `BabA` `bABa` `baBA`

In Sample Case #2, both two couples are newlywed couples, so `A` and `a` cannot be adjacent, and `B` and `b` cannot be adjacent. They can be arranged in the following 8 ways:
`ABab` `AbaB` `aBAb` `abAB`
`BAba` `BabA` `bABa` `baBA`