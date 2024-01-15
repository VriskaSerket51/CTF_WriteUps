import { fetch, CookieJar } from "node-fetch-cookies";

async function main() {
  const cookieJar = new CookieJar();
  let resp = await fetch(cookieJar, "https://hacker-typer.tuctf.com/", {
    method: "GET",
    headers: {
      accept: "*/*",
    },
  });

  let text = await resp.text();
  let word = text.split('"word-title">')[1].split("</strong>")[0];

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
    word = JSON.parse(text).next_word;
  }
}

main();
