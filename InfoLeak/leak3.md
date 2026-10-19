## On the page "http://leak3.chal.deti:8012/"
I saw
```
Media

Company media hub.
banner
```

## Method
- With nothing to interact I inspected the source code and I saw this
```

<h1>Media</h1><p>Company media hub.</p><img src="/public/banner.png" alt="banner">

```

- I went to /public/banner.png and it return 404 
- I then tried to go back to the folder behind it, the /public ("http://leak3.chal.deti:8012/public/") and saw
```

Index of /public/

    readme.txt
    flag.txt

```

- Then i clicked flag.txt and it got me to "http://leak3.chal.deti:8012/public/flag.txt" where i saw
```

flag{37d38bc19f5cc89390d25f8cd04ea736}

```

## Reproduce
- Go to "http://leak3.chal.deti:8012/public/"
- Click on "flag.txt"

__Alternative__

- Just go the "http://leak3.chal.deti:8012/public/flag.txt" or just curl it

