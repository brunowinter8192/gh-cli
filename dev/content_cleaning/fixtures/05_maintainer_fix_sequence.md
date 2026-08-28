# Fresh checkout won't build after the submodule split

State: CLOSED | #9005
Labels: documentation

---

Cloned the repo today and the build fails immediately. Did something change in the setup?

# Comments on example/repo#9005

Total: 1 comments

--- Comment 1 ---

Yeah, `vendor/` is a submodule now. This is the fix, run these three commands in order:

```
git submodule update --init --recursive
pip install -e .
python -m mypkg.selftest
```

The selftest at the end should print `OK` — if it doesn't, your submodule pin is probably stale,
run `git submodule update --remote` and try again.
