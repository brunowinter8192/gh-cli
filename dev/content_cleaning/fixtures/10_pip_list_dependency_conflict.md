# scikit-image and opencv pin conflict, install fails silently downgrading numpy

State: CLOSED | #9010
Labels: bug, dependencies

---

Installing this package downgrades `numpy` to 1.23 without telling me, and then a bunch of
unrelated stuff breaks. I think two of the pinned sub-dependencies disagree with each other.

# Comments on example/repo#9010

Total: 2 comments

--- Comment 1 ---

Can you post your `pip list` output so I can see the exact versions that got resolved?

--- Comment 2 ---

Sure, here it is:

```
Package                Version
----------------------  ----------------
certifi                 2024.7.4
charset-normalizer      3.3.2
contourpy               1.2.1
cycler                  0.12.1
fonttools               4.53.1
idna                    3.7
imageio                 2.34.2
kiwisolver              1.4.5
lazy_loader             0.4
matplotlib              3.9.1
mypkg                   2.1.0
networkx                3.3
numpy                   1.23.5
opencv-python            4.6.0.66
packaging               24.1
pillow                  10.4.0
pyparsing               3.1.2
python-dateutil         2.9.0.post0
requests                2.32.3
scikit-image            0.24.0
scipy                   1.14.0
six                     1.16.0
tifffile                2024.7.2
tzdata                  2024.1
urllib3                 2.2.2
```

`opencv-python==4.6.0.66` is pinned by our OCR extra and it caps `numpy<1.24`, but
`scikit-image==0.24.0` wants `numpy>=1.24`. Pip silently resolves to the older `numpy` because
the OCR extra's constraint is stricter, and nothing warns you about it. Loosening the OCR
extra's opencv pin to `>=4.8` should let both resolve to a current numpy — I'll put up a PR for
that pin change.
