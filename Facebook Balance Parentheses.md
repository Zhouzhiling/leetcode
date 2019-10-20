# # Facebook | Balance Parentheses

 Given a string `str` consisting of parentheses `(`, `)` and alphanumeric characters. Remove minimum number of paranthesis to make the string valid and return **any** valid result. In a valid string for every opening/closing parentheses there is a matching closing/opening one. 

**Example 1:**



```
Input: "ab(a(c)fg)9)"
Output: "ab(a(c)fg)9" or "ab(a(c)fg9)" or "ab(a(cfg)9)"
```



**Example 2:**



```
Input: ")a(b)c()("
Output: "a(b)c()"
```



**Example 3:**



```
Input: ")("
Output: ""
```



**Example 4:**



```
Input: "a(b))"
Output: "a(b)"
```



**Example 5:**



```
Input: "(a(c()b)"
Output: "a(c()b)" or "(ac()b)" or "(a(c)b)"
```



**Example 6:**



```
Input: "(a)b(c)d(e)f)(g)"
Output: "(a)b(c)d(e)f(g)"
```



## Code

```python
def BalanceParentheses(s):
    stack = []
    # -1 means left parentheses
    # 1 means right parentheses
    for i, c in enumerate(s):
        if c == '(':
            stack.append([i, -1])
        elif c == ')':
            if stack and stack[-1][1] == -1:
                stack.pop()
            else:
                stack.append([i, 1])
        else:
            continue
    # print(stack)
    invalid_list = [stack[i][0] for i in range(len(stack))]
    valid_list = [s[i] for i in range(len(s)) if i not in invalid_list]
    return "".join(valid_list)


s = "(a)b(c)d(e)f)(g)"
print(BalanceParentheses(s))
```

