# Polynomial hash

Chall code:
```python
def PolynomialHash(s, a):
    return sum([ord(s[i]) * pow(a, len(s)-i-1) for i in range(len(s))])
 
flag = "***********"
flag = "grodno{aaa}"
PolynomialHash(flag, 256)

#35201194166317999524907401661096042001277
```

Then it might be base256?

```python
c = 35201194166317999524907401661096042001277

for i in range(17):
  v = 256 ** (16 - i)
  print(chr(c // v), end ="")
  c -= c // v * v
```

> grodno{256NumSys}

flag is: **grodno{256NumSys}**