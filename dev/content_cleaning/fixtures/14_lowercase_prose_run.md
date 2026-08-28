# Documenting our release ritual

State: OPEN | #2

---

running the tests locally is step one
creating a signed tag is step two
copying the changelog into the release body is step three
writing the announcement draft is step four
reading it back out loud catches most typos
installing the release candidate in a clean venv is step five
removing the old wheels from dist/ avoids upload conflicts
generating the sdist happens automatically
skipping the smoke test is how we shipped a broken build last time
cleaning the build directory prevents stale artifacts
overriding the version in setup.cfg is never allowed
moving the tag after publishing breaks the CDN cache
deleting a published release is not possible on PyPI
byte-compiling is handled by the wheel, do not do it manually
