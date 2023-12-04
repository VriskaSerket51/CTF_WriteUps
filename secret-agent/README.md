# Secret Agent

You can see detailed solution script at [solve.py](solve.py)

When you connect to server, you will get messages REALLY SLOWLY.

Door keeper will block you at first. However, when you miss the password a lot, he will give you some hints. Uh... longer one? You can pass the door by sending very long password, such as `11111111111111111111111`.

Mission 1 is finding lowest-cost path within weight graph. You can use dijkstra algorithm(or brute force 💀💀). When you send answer to server, you can get key `good_job_agent1089`.

> Lowest cost is 20, Charity-Emell-Iyona-Kepliker-Osiros-Rhenora-Shariot.

By sending key from Mission 1, you can start Mission 2. Mission 2 is decoding UTF-8, and when you decode it you will get braille. Translate it to English, and reverse each chunks and make it UPPER case. It's for Mission 3.

> As the bytes doen't arrive at once, so you have to wait until every bytes come, then decode it.

When you send the key to Mission 3, then you can get the flag.

Flag: **TUCTF{CONTINUE_THE_GOOD_WORK_2023}**