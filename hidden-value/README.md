# Hidden Value

Let's reverse the binary!

main function:
```c
int main(int argc, const char **argv, const char **envp)
{
  char s[112]; // [rsp+0h] [rbp-70h]

  setvbuf(stdin, 0LL, 2, 0LL);
  setvbuf(stdout, 0LL, 2, 0LL);
  printf("Enter your name: ");
  fgets(s, 100, stdin);
  greet_user(s);
  return 0;
}
```

It reads 100 bytes from input, and call greet_user.
Let's see greet_user.

greet_user:
```c
void greet_user(const char *a1)
{
  char dest[44]; // [rsp+10h] [rbp-30h]
  int v3; // [rsp+3Ch] [rbp-4h]

  v3 = 0x12345678;
  strcpy(dest, a1);
  if ( v3 == 0xDEADBEEF )
    hidden_command();
  else
    printf("Hello, %s! Nothing special happened.\n", dest);
}
```

It smells like BOF.
If the address of dest is `0x00`, the the address of v3 will be `0x44`.
Then just send `"a" * 44 + "\xEF\xBE\xAD\xDE"` to server, v3 will be overwritten and you can get the flag.

Flag is **TUCTF{pr4cti4l_buffer_overrun}**