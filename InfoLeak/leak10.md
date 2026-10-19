## On the page "http://leak10.chal.deti:8019"
I saw
```

Error LAB 
[Input Text] [send]
```

## Method
- After going to the page i saw the text and tested a random input "a" and clicked send to test the behaviour
- It redirected me to "http://leak10.chal.deti:8019/crash?msg=a" where it showed
```

Traceback (most recent call last):
  File "/usr/local/lib/python3.12/site-packages/flask/app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
    e = RuntimeError('boom in /crash')
    rv = None
    self = 
  File "/usr/local/lib/python3.12/site-packages/flask/app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    req = 
    rule =  crash>
    self = 
    view_args = {}
  File "/app/app.py", line 43, in crash
    raise RuntimeError(f"boom in {request.path}")
    secret = 'flag{bfa756a60a9d27a4344c5633e2d50ac3}'
RuntimeError: boom in /crash
```

- As you can see, in the second line counting from the bottom ,the flag is there
- This is a stack trace that shouldn't happen, giving too much information about the inner working of the system

## Reproduce
- Go to "http://leak10.chal.deti:8019" and in the text input put anything and hit send
- In the next page it just shows the flag

__Alternative__

- Just go to "http://leak10.chal.deti:8019/crash?msg=adsfdss" or curl it
- It shows the flag
