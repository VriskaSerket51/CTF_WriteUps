# Table Encryption

Open `table_encryption.xml.enc`. Sus extension... xml?!

Let's try xor decryption.

```python
head = b'<?xml version="1.0" encoding="'

f = open("table_encryption.xml.enc", "rb")
data = f.read()

key = xor(head, data[:len(head)])
print(key)
```

> output: `[69, 109, 111, 106, 105, 32, 77, 111, 114, 105, 110, 103, 32, 83, 116, 97, 69, 109, 111, 106, 105, 32, 77, 111, 114, 105, 110, 103, 32, 83]`

Well... it looks like 16 bytes are repeated. Then key is: `[69, 109, 111, 106, 105, 32, 77, 111, 114, 105, 110, 103, 32, 83, 116, 97]`

When you iterate xor decryption, you can get:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<root>
    <table name="users">
        <column name="id" type="int" />
        <column name="name" type="varchar" />
        <column name="email" type="varchar" />
        <column name="password" type="varchar" />
    </table>
    <table name="posts">
        <column name="id" type="int" />
        <column name="user_id" type="int" />
        <column name="title" type="varchar" />
        <column name="content" type="varchar" />
    </table>
    <table name="comments">
        <column name="id" type="int" />
        <column name="post_id" type="int" />
        <column name="user_id" type="int" />
        <column name="content" type="varchar" />
    </table>
    <users>
        <user>
            <id>1</id>
            <name>John Doe</name>
            <email>john@tuctf.com</email>
            <password>TUCTF{x0r_t4bl3s_R_fun!!!11!}</password>
        </user>
    </users>
</root>
```

So the flag is **TUCTF{x0r_t4bl3s_R_fun!!!11!}**