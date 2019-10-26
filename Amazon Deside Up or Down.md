 Coding: 一个数字stream，如果有增减趋势的变化就加一个UP或者DOWN，挺简单的，e.g. input 1 10 23 18 15 20，output 1 10 23 DOWN 18 15 UP 20（LZ是菜鸡本鸡，基本上我说简单就是真的简单hh） 

 [https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=561888&extra=page%3D4%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3046%5D%5Bvalue%5D%3D5%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311%26orderby%3Ddateline](https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=561888&extra=page%3D4%26filter%3Dsortid%26sortid%3D311%26searchoption[3046][value]%3D5%26searchoption[3046][type]%3Dradio%26sortid%3D311%26orderby%3Ddateline) 



## Code

```python

# Amazon full-time round 2
# 1 10 23 DOWN 18 15 UP 20
nums = [1,10,23,18,15,20]
length = len(nums)
if length <= 2:
    print(nums)
else:
    first = 0
    second = 1
    third = 2
    res = nums[0:2]
    while third < length:
        if nums[first] < nums[second] and nums[second] > nums[third]:
            res.append('DOWN')
        elif nums[first] > nums[second] and nums[second] < nums[third]:
            res.append('UP')

        res.append(nums[third])
        first += 1
        second += 1
        third += 1
print(res)
```

