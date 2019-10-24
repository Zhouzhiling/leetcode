# [⭐] Uber Follow-up of 122. Best Time to Buy and Sell Stock II

122. Best Time to Buy and Sell Stock II 的变题。

 第一題的followup: 假如改成一個2D array 每個row代表一個時間點, 每個column不同stock price。每次最多持有一支股票，求最大profit?
例如a[0][1] 就是第一天第二支stock的價格 



## Solution

因为不限制购买次数，所以



## Code

```python
# 122 follow up
def maxProfit(prices):
    day_num = len(prices)
    stock_num = len(prices[0])
    min_price = prices[0]
    res = 0
    for day in range(1, day_num):
        curmax = 0
        curidx = 0
        for i in range(stock_num):
            if prices[day][i] - min_price[i] > curmax:
                curmax = prices[day][i] - min_price[i]
                curidx = i
        print(curmax)
        res += curmax
        min_price = prices[day]
    return res

prices = [[1,2,1,7],[2,2,4,6],[1,2,4,5],[4,2,4,4]]
print(maxProfit(prices))
```

