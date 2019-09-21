Given an array of positive integers `a`, your task is to calculate the sum of every possible `a[i] ∘ a[j]`, where `a[i] ∘ a[j]` is the concatenation of the string representations of `a[i]` and `a[j]` respectively.

Example

- For `a = [10, 2]`, the output should be `concatenationsSum(a) = 1344`.

  - `a[0] ∘ a[0] = 10 ∘ 10 = 1010`,
  - `a[0] ∘ a[1] = 10 ∘ 2 = 102`,
  - `a[1] ∘ a[0] = 2 ∘ 10 = 210`,
  - `a[1] ∘ a[1] = 2 ∘ 2 = 22`.

  So the sum is equal to `1010 + 102 + 210 + 22 = 1344`.

- For `a = [8]`, the output should be `concatenationsSum(a) = 88`.

  There is only one number in `a`, and `a[0] ∘ a[0] = 8 ∘ 8 = 88`, so the answer is `88`.

Input/Output

- **[execution time limit] 4 seconds (py)**

- **[input] array.integer a**

  A non-empty array of positive integers.

  *Guaranteed constraints:*
  `1 ≤ a.length ≤ 105`,
  `1 ≤ a[i] ≤ 106`.

- **[output] integer64**

  - The sum of all `a[i] ∘ a[j]`s. It's guaranteed that the answer is less than `253`.



## Code

```python
def concatenationsSum(a):
    
    def calculate_digit(num):
        digit = 0
        # divisor = 10
        while num > 0:
            num = num / 10
            digit += 1
        return digit
    
    output = 0
    length = len(a)
    tensum = 0
    for num in a:
        tensum += pow(10,calculate_digit(num))
    tensum += length
        
    return tensum * sum(a)
```

