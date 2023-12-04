# Hacker Typer

> I use Typescript/Javascript for WEB challenges; that's why the solve script is written with Javascript.

When you connect to `https://hacker-typer.tuctf.com/`, guid will be add to your cookie.

Page shows a word, and you have to type it and post as fast as you can.

You can get first word by this.
```js
let word = text.split('"word-title">')[1].split("</strong>")[0];
```

Next words can be found at POST results, so just looping around.
```js
while (true) {
  resp = await fetch(cookieJar, "https://hacker-typer.tuctf.com/check_word", {
    method: "POST",
    body: `word=${word}`,
    headers: {
      accept: "*/*",
      "content-type": "application/x-www-form-urlencoded",
    },
  });
  text = await resp.text();
  console.log(text);
}
```

When you get 150 streaks, you can get the flag: **TUCTF{SuP3R_Typ3R}**.

See detailed script at [solve.mjs](solve.mjs).