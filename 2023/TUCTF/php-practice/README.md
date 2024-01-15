# PHP Practice

It looks like website is kind of crawler or something.
When you send `link=https://google.com`, then the site prints html of google.

Then how about `localhost`? Unfortunately, the site block either `localhost` and `127.0.0.1`

Then, we can use `file://` protocol. Server might use Linux, so send `link=file:///etc/passwd`.

Wow, we got user list!
Now we can read arbitrary files.
Just for fun, I uploaded server code [display.php](display.php).

However, as we don't know the flag file's name, we can't read flag.
Site's html contains comment such like "TODO: Hide secret file".
So how about getting `.htaccess` file?

In `.htaccess`, there is flag file name; and you also can read flag file with `file://var/www/html/{filename}`.

Flag is **TUCTF{th1s_i5_my_secr3t_l0c@l_f1le!}**