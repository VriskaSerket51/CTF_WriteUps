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