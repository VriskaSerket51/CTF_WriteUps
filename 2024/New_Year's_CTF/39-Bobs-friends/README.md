# 39 Bob's friends

e = 39, with 39 n and c.

Use Hastad Attack.

```python
from functools import reduce
import gmpy2
from Crypto.Util.number import long_to_bytes

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)

    for n_i, a_i in zip(n, a):
        p, _ = gmpy2.t_divmod(prod, n_i)
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q, r = gmpy2.t_divmod(a, b)
        a, b = b, r
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

c = [...]
n = [...]

result = (chinese_remainder(n, c))

m, _ = gmpy2.iroot(result, 39)
print(long_to_bytes(m))
```

> 'grodno{I_s3nd_y0u_gr33t1ngs,_long-no5ed_b4rb@rian!}'

flag is: **grodno{I_s3nd_y0u_gr33t1ngs,_long-no5ed_b4rb@rian!}**