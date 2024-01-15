# Plenty O Fish in the Sea

Open `lost_map.log`, and lots of strange phrases, hmm...

However, you can find sus string `%7B83h%2` at line 6715.
Also, `TUCTF` at line 2434.

Wow, then we can just iterate each phrase to find answer!
`%7B83h%2` looks like url-encoded, so we might url-decode to the result.

```python
from urllib import parse

f = open("lost_map.log")

result = {}

for line in f:
    stripped = line.strip()
    if not stripped in result:
        result[stripped] = 1
    else:
        result[stripped] += 1

out = ""

for s in result:
    if result[s] == 1:
        out += s

print(parse.unquote(out))
```

The flag is: **TUCTF{83h!Nd_7h3_W@73rF@11}**