 	
## In the page:
### http://sqli1.chal.deti:8030

I saw this:
``` html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Staff Portal</title>
  <link rel="stylesheet" href="/static/base.css">
</head>
<body>
  <div class="shell">
    <header class="masthead">
      
      <div class="logo" aria-hidden="true">S</div>
      
      <div>
        <h1>Staff Portal</h1>
        <p class="tagline">On-shift sign-in for the IT support crew</p>
      </div>
    </header>

    

    
    <div class="card">
      <h2>Sign in</h2>
      <p>Enter your crew credentials to see the shift board.</p>

      

      <form method="post" action="/login" class="stack">
        <label class="field">Username
          <input type="text" name="username" autocomplete="username" required>
        </label>
        <label class="field">Password
          <input type="password" name="password" autocomplete="current-password" required>
        </label>
        <button type="submit" class="btn">Sign in</button>
      </form>
    </div>
    

    <footer class="footer">&copy; 2026 Staff Portal &middot; prepared for the course lab</footer>
  </div>
</body>
</html>
```

It is a login page

## Method
- The first I did was to put a normal Username and Password which gave me a message **"That name and password do not match our roster"**
- Then i put a " ' " and a random password and it returned an error message **"Something went wrong on our side - please try again."** which indicated me that a SQL Injection is possible
- Then I tested the classic injection username : "asd ' or 1=1 -- //" password : "<doesnt matter>" and it worked, the login was successfull

## Reproduce
Go to the page, and on the login put on the camps:
  - Username : ads' or 1=1 -- // 
  - Password : <anything you want>
