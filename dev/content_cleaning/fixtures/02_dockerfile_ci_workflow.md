# Docker image is 2.1GB, way bigger than it should be

State: CLOSED | #9002
Labels: bug, docker

---

Our production image ballooned after the last release. I think it's the layer caching, but I
can't tell from the Dockerfile alone.

# Comments on example/repo#9002

Total: 1 comments

--- Comment 1 ---

Found it — you're installing build tooling in the final stage instead of a builder stage. Here's
a multi-stage version that fixes it, drop this in as your new `Dockerfile`:

```dockerfile
FROM python:3.11-slim AS builder
RUN apt-get update && apt-get install -y --no-install-recommends build-essential gcc
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt
COPY . /app

FROM python:3.11-slim
RUN groupadd -r app && useradd -r -g app app
COPY --from=builder /root/.local /home/app/.local
COPY --from=builder /app /app
ADD ./scripts/entrypoint.sh /entrypoint.sh
WORKDIR /app
USER app
ENTRYPOINT ["/entrypoint.sh"]
```

And the matching CI step, since the old one was still building single-stage:

```yaml
- name: Build image
  run: |
    docker build -t myapp:${{ github.sha }} .
    docker image inspect myapp:${{ github.sha }} --format='{{.Size}}'
```

That should get you back under 400MB.
