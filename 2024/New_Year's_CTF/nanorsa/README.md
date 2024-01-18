# nanoRSA

You got a [file](rsa.txt)

```
e = 1
c = 9908255308151638808626355523286556242109836830117153917
n = 245841236512478852752909734912575581815967630033049838269083
```

c = m^e mod n... and e is 1.

Then m = c.

```python
from Crypto.Util.number import long_to_bytes

print(long_to_bytes(9908255308151638808626355523286556242109836830117153917))
```

> b'grodno{R3sTcD4gH6iJ0kL}'

flag is: **grodno{R3sTcD4gH6iJ0kL}**