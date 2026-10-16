## On the page "http://leak9.chal.deti:8018"
I saw 
```

Welcome to Acme Corp

Nothing to see here. Please move along.

Edit

```

(The edit is a button)

## Method
- The first thing i did was try to click the edit button to see where it would lead, it didnt do Nothing
- The failure of the button led me to try to inspect the HTML to try to find if the button form submit should do a request to any server
- The inspect page (the HTML) looked like this 
```<!DOCTYPE html>

<html>
<head><title>Acme Corp</title></head>
<body>
  <!-- TODO: remove this debug marker before shipping -->
  <!-- FLAG: flag{f6358bb5a60fd3c52b971c7c128104a2} -->
  <h1>Welcome to Acme Corp</h1>
  <p>Nothing to see here. Please move along.</p>
  <button>edit</button>
</body>
</html>
```

- Yheah, the flag was hidden as a comment in the HTML

## Reproduce
- Go to page "http://leak9.chal.deti:8018"
- On a browser click "View Page Source"
- The Flag should be there

__Alternitibly__
- Run  curl -X GET http://leak9.chal.deti:8018
- On the ouput there will be the HTML and the flag
```
```
```
