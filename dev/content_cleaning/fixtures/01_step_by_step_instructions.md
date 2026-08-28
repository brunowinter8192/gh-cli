# How do I get a clean local dev environment for this project?

State: CLOSED | #9001
Labels: question

---

I keep breaking my environment when I try to set this project up from scratch. Is there a
canonical sequence of steps somewhere?

# Comments on example/repo#9001

Total: 1 comments

--- Comment 1 ---

Sure, here's the sequence the core team uses. Follow it in order:

1. Creating a fresh virtualenv keeps this isolated from your system Python — don't skip it.
2. Copying `.env.example` to `.env` is required before the app will boot; the defaults work for
   local dev.
3. Running the database migrations first avoids the foreign-key errors people hit in step 5.
4. Installing the pre-commit hooks now saves you from a failed CI run later.
5. Overriding the default port in `.env` is only needed if 8000 is already taken on your machine.
6. Cleaning the `__pycache__` directories before you switch branches avoids stale bytecode bugs.
7. Reading the `CONTRIBUTING.md` file before your first PR will save the reviewers some back and
   forth — most first-PR review comments are about things covered there.

If you get stuck on any of these, ping me and I'll walk you through it live.
