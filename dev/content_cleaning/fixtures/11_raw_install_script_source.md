# Please share the CI install script, the docs are out of date

State: CLOSED | #9011
Labels: documentation

---

The install instructions in the README don't match what CI actually does — CI clearly installs
some system packages first that aren't mentioned anywhere.

# Comments on example/repo#9011

Total: 1 comments

--- Comment 1 ---

Here's the actual script we run in CI, `scripts/bootstrap.sh` — feel free to run it locally too,
it's idempotent:

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "Installing system dependencies"
sudo apt-get update
sudo apt-get install -y libpq-dev libjpeg-dev zlib1g-dev

echo "Creating virtualenv"
python3 -m venv .venv
source .venv/bin/activate

echo "Installing python dependencies"
pip install --upgrade pip
pip install -e ".[dev]"

echo "Running database migrations"
python manage.py migrate --noinput

echo "Bootstrap complete"
```

I'll fix the README to link to this script instead of duplicating an out-of-date copy of the
steps.
