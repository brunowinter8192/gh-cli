# 4.0.0 broke my integration, what actually changed?

State: CLOSED | #9008
Labels: question

---

Upgraded straight from 3.9 to 4.0 and half my code broke. The changelog on the releases page is
pretty terse. Can someone summarize what actually moved?

# Comments on example/repo#9008

Total: 1 comments

--- Comment 1 ---

Copying the relevant slice of the changelog here since the releases page truncates it:

```
## 4.0.0

- Removing the deprecated `Client.fetch_sync()` method — use `Client.fetch()` with `await`
  instead, it's been async-only internally since 3.6.
- Adding a required `timeout` parameter to `Client()` — previously it silently defaulted to
  never timing out, which was the source of about a third of our support tickets.
- Renaming `Response.body` to `Response.content` for consistency with the streaming API.
- Removing the `legacy_auth` flag entirely — if you were relying on it, see the migration guide
  linked below.
- Adding retry-with-backoff as the default behavior for 5xx responses; set `retries=0` to get
  the old fire-once behavior back.
- Changing the default serializer from `pickle` to `json` for anything written to the on-disk
  cache; existing pickle caches are auto-migrated on first read.
```

The `timeout` one is almost certainly what's breaking you if you're instantiating `Client()`
positionally anywhere — it shifted every positional arg after it by one.
