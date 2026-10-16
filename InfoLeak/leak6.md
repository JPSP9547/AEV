## On page "http://leak6.chal.deti:8015/" i saw
```
Auth service
 [guest] [login]
```

[guest] is a text input with the placeholder "guest"
[login] is a button

## Method
- I just clicked on login in the placeholder user and it redirected to "http://leak6.chal.deti:8015/login" where it returned 
```
{"token":"eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJzdWIiOiAiZ3Vlc3QiLCAicm9sZSI6ICJ1c2VyIiwgImZlYXR1cmVfZmxhZ3MiOiB7InNob3dfYWRtaW4iOiB0cnVlfSwgImZsYWciOiAiZmxhZ3s3NGUwNWUwMDg1MzNmNDI0MmQxZGJlNTM0ZjVkMmQ0ZH0ifQ.oFSLwM6URcbJJHWJUCIRAeJOsXWzAR2v2vllXsORriI"}
```

- I assumed it was a JWT token so i went to decode it at the "https://www.jwt.io/" website
- I was right, it was a JWT Token and these were the decrypted contents:
```
{
  "sub": "guest",
  "role": "user",
  "feature_flags": {
    "show_admin": true
  },
  "flag": "flag{811a2155d58d0f182ec57761eeec9f5c}"
}
```
```
```

- The flag is right there

## Reproduce
- Go to "http://leak6.chal.deti:8015"
- Write any user on the text camp and click login
- Decode the returned token
- Flag is there
```
