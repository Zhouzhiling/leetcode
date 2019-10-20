# Caesar Cipher Encrpytion 

**Question 1:**
Caesar Cipher Encrpytion
You are given a list of string, group them if they are same after using Ceaser Cipher Encrpytion.
Definition of "same", "abc" can right shift 1, get "bcd", here you can shift as many time as you want, the string will be considered as same.



**Example:**



```
Input: ["abc", "bcd", "acd", "dfg"]
Output: [["abc", "bcd"], ["acd", "dfg"]]
```



## Code

```python
# Caesar Cipher Encrpytion
def CaesarEncrpytion(words):
    record = {}
    for word in words:
        length = len(word)
        keylist = []
        for i in range(length):
            keylist.append(str(ord(word[i])-ord(word[0])))
        key = "".join(keylist)
        if key in record:
            record[key].append(word)
        else:
            record[key] = [word]
    return record.values()

words = ["abc", "bcd", "acd", "dfg"]
print(CaesarEncrpytion(words))
```

