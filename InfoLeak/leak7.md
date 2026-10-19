## On the page "http://leak7.chal.deti:8016" i saw
```
Oracle

[Text input] [check]
```

Check is a button

## Method
- I wrote something random ("abc") and it redirected to "http://leak7.chal.deti:8016/oracle?prefix=abc" which return 
```
Forbidden

You don't have the permission to access the requested resource. It is either read-protected or not readable by the server.
```

- I found 2 things from this, that my input goes to in the parameter "prefix" and that i had to put the right stuff in there to get any clue
- With this information I decided to fuzz to get some clue
- I fuzzed like this 
```
24@s24:~$ ffuf -u http://leak7.chal.deti:8016/oracle?prefix=FUZZ -w /usr/share/dirb/wordlists/common.txt -ac

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://leak7.chal.deti:8016/oracle?prefix=FUZZ
 :: Wordlist         : FUZZ: /usr/share/dirb/wordlists/common.txt
 :: Follow redirects : false
 :: Calibration      : true
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

                        [Status: 200, Size: 3, Words: 1, Lines: 1, Duration: 15ms]
f                       [Status: 200, Size: 3, Words: 1, Lines: 1, Duration: 18ms]
flag                    [Status: 200, Size: 3, Words: 1, Lines: 1, Duration: 68ms]
fla                     [Status: 200, Size: 3, Words: 1, Lines: 1, Duration: 68ms]
:: Progress: [4614/4614] :: Job [1/1] :: 1449 req/sec :: Duration: [0:00:03] :: Errors: 0 ::
```

- It returned good on "f", "fla" and "flag", so I tought it might test caracter by caracter, I tested with "flau" which returned an error and then with "flag{" which returned yes, so it confirmed my suspicion

- From there I only had to go caracter by caracter to find the flag, I did a script in python to do it

- Run the script python3 leak7.py and it gave me the flag

## Reproduce
- Setup a venv, install requests package in there, run python3 leak7.py
- It gives the flag
