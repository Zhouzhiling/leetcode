# # Amazon | OA 2019 | Movies on Flight

I had 2 question on my online assesment, however I remeber only the first one. My code passed only 10 test out of 13. I did a sorting and then found the best pair with 2 for loops



**Question:**
You are on a flight and wanna watch two movies during this flight.
You are given `List<Integer> movieDurations` which includes all the movie durations.
You are also given the duration of the flight which is `d` in minutes.
Now, you need to pick two movies and the total duration of the two movies is less than or equal to `(d - 30min)`.



Find the pair of movies with the longest total duration and return they indexes. If multiple found, return the pair with **the longest movie**.



**Example 1:**



```
Input: movieDurations = [90, 85, 75, 60, 120, 150, 125], d = 250
Output: [0, 6]
Explanation: movieDurations[0] + movieDurations[6] = 90 + 125 = 215 is the maximum number within 220 (250min - 30min)
```



## Code

```python
def MoviesFlight(md, d):
    d -= 30
    md = [[m, i] for i, m in enumerate(md)]
    md.sort()
    st = 0
    ed = len(md)-1
    res = [0, 0]
    cursum = 0
    while st < ed:
        cur = md[st][0] + md[ed][0]
        if cur == d:
            return [md[st][1], md[ed][1]]
        elif cur < d:
            if cur > cursum:
                cursum = cur
                res = [md[st][1], md[ed][1]]
                st += 1
        elif cur > d:
            ed -= 1
    print(cursum)
    return res


movieDurations = [90, 85, 75, 60, 120, 150, 125]
d = 250
print(MoviesFlight(movieDurations, d))
```

