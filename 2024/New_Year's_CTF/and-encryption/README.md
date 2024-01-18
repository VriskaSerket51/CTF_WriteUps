# AND-encryption

We can calculate original flag by do OR op to all results.

Maybe just 20 times is ok.

```python
from winpwn import *

context.newline = "\n"

p = remote("ctf.mf.grsu.by", 9023)

def __or(a, b):
    return [x | y for x, y in zip(a, b)]

flag = None

for _ in range(20):
    p.recvuntil(":")
    p.sendline("1")
    data = p.recvline().strip()
    data = [int(data[i:i+2], 16) for i in range(0, len(data), 2)]
    flag = data if flag is None else __or(data, flag)

p.recvuntil(":")
p.sendline("2")
p.sendline("".join(map(chr, flag)))

p.interactive()
```

> Flag: Правильно !
> Ваш флаг: grodno{525e00st1ll_b3tt3r_X0R_th4n_AND...ffc8fa}

flag is: **grodno{525e00st1ll_b3tt3r_X0R_th4n_AND...ffc8fa}**