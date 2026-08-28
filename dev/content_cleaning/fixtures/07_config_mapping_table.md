# What do the log-level env vars actually map to?

State: CLOSED | #9007
Labels: documentation

---

The docs mention "log level names" but never say what they map to internally. Trying to set
`LOG_LEVEL=warn` and it's not doing what I expect.

# Comments on example/repo#9007

Total: 1 comments

--- Comment 1 ---

This isn't documented anywhere, sorry — here's the actual mapping from `logging_config.py`:

```
env value      internal level
-------------  ---------------
trace          5
debug          10
info           20
warn           30
warning        30
error          40
critical       50
silent         100
```

Note `warn` and `warning` are aliases for the same level, and `silent` is not a real logging
level — it's a sentinel we check for separately to disable the handler entirely. That's probably
why `warn` "isn't doing what you expect": if you were expecting it to only show warnings and
above and instead it's showing more, check whether something else in your config is also setting
`info`, since the more verbose of the two wins.
