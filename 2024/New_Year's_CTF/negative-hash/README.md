# Negative hash

base-100..?

Unfortunately, not.
However, we can solve the problem similarly.

Each value of character must be between 32 and 127.

```python
c = 101871001089022554852470576840818198625

for i in range(19):
  v = (-100) ** (18 - i)
  k = c // v
  if 18-i != 0:
    while True:
      v2 = (-100) ** (18 - (i+1))
      c2 = c - k * v
      k2 = c2 // v2
      if k2 >= 32 and k2 <= 127:
        break
      k += 1
  c -= k * v
  print(chr(k), end="")
```

> grodno{-100_NumSys}

flag is: **grodno{-100_NumSys}**