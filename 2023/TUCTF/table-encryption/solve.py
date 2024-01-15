def xor(lhs, rhs):
  return [x ^ y for (x, y) in zip(lhs, rhs)]

head = b'<?xml version="1.0" encoding="'

f = open("table_encryption.xml.enc", "rb")
data = f.read()

key = xor(head, data[:len(head)])[:16]

for i in range(0, len(data), len(key)):
  chunk = data[i:i+len(key)]
  dec = xor(chunk, key)
  print(bytes(dec).decode(), end="")