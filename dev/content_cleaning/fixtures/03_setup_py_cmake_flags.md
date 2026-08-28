# Extension fails to build on ARM with -march=native

State: CLOSED | #9003
Labels: bug, build-system

---

The C extension refuses to build on Apple Silicon. I suspect the hardcoded flags in `setup.py`
are x86-only.

# Comments on example/repo#9003

Total: 1 comments

--- Comment 1 ---

Confirmed, `-march=native` plus a couple of SSE-specific flags were hardcoded. Here's the
relevant chunk of `setup.py` for reference, in case anyone wants to patch it locally before the
release goes out:

```python
extra_compile_args = [
    "-O3",
    "-march=native",
    "-msse4.2",
    "-mavx2",
    "-fPIC",
    "-fno-strict-aliasing",
    "-Wall",
    "-Wextra",
    "-Wno-unused-parameter",
    "-DNDEBUG",
    "-DPY_SSIZE_T_CLEAN",
]

ext_modules = [
    Extension(
        "mypkg._native",
        sources=["src/native.c", "src/simd.c"],
        extra_compile_args=extra_compile_args,
        extra_link_args=["-flto"],
        include_dirs=["include"],
    )
]
```

And the equivalent bit of `CMakeLists.txt` for the folks building outside of `pip`:

```cmake
target_compile_options(mypkg_native PRIVATE
    -O3
    -fPIC
    -fno-strict-aliasing
    -Wall
    -Wextra
    -DNDEBUG
)
if(APPLE AND CMAKE_SYSTEM_PROCESSOR MATCHES "arm64")
    target_compile_options(mypkg_native PRIVATE -mcpu=apple-m1)
else()
    target_compile_options(mypkg_native PRIVATE -march=native -msse4.2 -mavx2)
endif()
```

I'll open a PR with the arm64 branch above; feel free to test it on your M-series machine before
I merge.
