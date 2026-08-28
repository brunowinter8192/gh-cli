# Regression: throughput dropped ~15% since 2.3.0

State: CLOSED | #9006
Labels: performance

---

Ran the standard benchmark suite before and after upgrading and something got slower. Numbers
below, all runs are the median of 5 on the same machine.

# Comments on example/repo#9006

Total: 1 comments

--- Comment 1 ---

Reproduced. Here's the full table, requests/sec by endpoint:

```
endpoint                  2.2.0        2.3.0
------------------------  -----------  -----------
GET /health                 42000        41800
GET /users/:id               8100         6900
POST /users                  3200         3150
GET /users/:id/orders        5400         4300
POST /orders                 1800         1790
GET /search                  2100         1050
PATCH /users/:id             4700         4650
DELETE /users/:id            5100         5050
```

`GET /search` and `GET /users/:id/orders` are the two that actually regressed — both go through
the new query planner. Everything else is within noise. I'd start looking at the planner's join
order for those two first.
