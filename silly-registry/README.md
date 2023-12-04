# Silly Registry

When you connect `http://chal.tuctf.com:30003/`, only header comes, no body responses.

Hmm... how about `http://chal.tuctf.com:30003/flag`? Also nothing, but header changed.

`Docker-Distribution-Api-Version: registry/2.0`

Nah, then this might be docker registry.

Send GET to `http://chal.tuctf.com:30003/v2/_catalog`, then you will get 401 UNAUTHORIZED. `Www-Authenticate` header gives `Bearer realm=silly-blahblah`... Hmm, then just send Bearer with arbitrary token, such as `Bearer 1`.

Then you finally get `http://chal.tuctf.com:30003/v2/_catalog`. It saids there is one container, `silly-container`.

`http://chal.tuctf.com:30003/v2/silly-container/manifests/latest` will give you list of blobs, you can get the gzip-archived flag at `http://chal.tuctf.com:30003/v2/silly-container/blobs/sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4`.

Flag is **TUCTF{my_51lly_53cr37_15_54f3_w17h_y0u}**