## On the page "http://leak8.chal.deti:8017"
I saw 
```
Public site

Nothing interesting.
crawlers: see our rules

```

## Method
- After seeing the "crawlers: see our rules" i thought that the site might have some rules wrote for crawlers, which would reveal some pages
- So i went to "http://leak8.chal.deti:8017/robots.txt" which returned me 
```
User-agent: *
Disallow: /admin-secret/
```

- After seeing this i went to http://leak8.chal.deti:8017/admin-secret which returned
```

flag{70d7874ef9f8714a4e0745cb84f9d0d5}
```

## Reproduce
- Go to page "http://leak8.chal.deti:8017/admin-secret" or curl it
- The Flag should be there
