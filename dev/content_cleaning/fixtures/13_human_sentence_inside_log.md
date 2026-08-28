# Build breaks halfway

State: OPEN | #1

---

Here is the full output:

```
copying src/mod_0.py -> build/lib/mod_0.py
copying src/mod_1.py -> build/lib/mod_1.py
copying src/mod_2.py -> build/lib/mod_2.py
copying src/mod_3.py -> build/lib/mod_3.py
copying src/mod_4.py -> build/lib/mod_4.py
copying src/mod_5.py -> build/lib/mod_5.py
copying src/mod_6.py -> build/lib/mod_6.py
copying src/mod_7.py -> build/lib/mod_7.py
copying src/mod_8.py -> build/lib/mod_8.py
copying src/mod_9.py -> build/lib/mod_9.py
copying src/mod_10.py -> build/lib/mod_10.py
copying src/mod_11.py -> build/lib/mod_11.py
Note that at this point I manually deleted the stale egg-info directory, which is the only reason the build got this far.
copying src/other_0.py -> build/lib/other_0.py
copying src/other_1.py -> build/lib/other_1.py
copying src/other_2.py -> build/lib/other_2.py
copying src/other_3.py -> build/lib/other_3.py
copying src/other_4.py -> build/lib/other_4.py
copying src/other_5.py -> build/lib/other_5.py
copying src/other_6.py -> build/lib/other_6.py
copying src/other_7.py -> build/lib/other_7.py
copying src/other_8.py -> build/lib/other_8.py
copying src/other_9.py -> build/lib/other_9.py
copying src/other_10.py -> build/lib/other_10.py
copying src/other_11.py -> build/lib/other_11.py
```

Any idea?
