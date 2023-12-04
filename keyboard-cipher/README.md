# Keyboard Cipher

When you download `keyboard_cipher.enc`, then you can get hex
`0x636a56355279424b615464354946686b566942794e586c4849455279523359674d47394d49486845643045675a316b315569426163304d675a316c715469426163314567616b6c7354534268563252594947745063434178643045675332395149466c6e536d343d`.

Run [hex2string](https://www.rapidtables.com/convert/number/hex-to-ascii.html) then you can get base 64 string `cjV5RyBKaTd5IFhkViByNXlHIERyR3YgMG9MIHhEd0EgZ1k1UiBac0MgZ1lqTiBac1EgaklsTSBhV2RYIGtPcCAxd0EgS29QIFlnSm4=`.

Also run [base64decode](https://www.base64decode.org/) then you will get cipher `r5yG Ji7y XdV r5yG DrGv 0oL xDwA gY5R ZsC gYjN ZsQ jIlM aWdX kOp 1wA KoP YgJn`.

Now look at your keyboard, check which key is surrounded by each key in chunk.

For example, key 'r', '5', 'y', 'g' encompass key 't', so the first chunk means 't'.

Decrypt all chunks, then you will get `tuctfpstxhakslqlh`, so the flag is **TUCTF{tuctfpstxhakslqlh}**