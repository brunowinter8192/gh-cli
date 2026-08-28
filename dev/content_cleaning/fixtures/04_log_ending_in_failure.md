# pip install fails at link stage with undefined symbol

State: CLOSED | #9004
Labels: bug

---

Building from source fails right at the end, after chewing through the whole compile step. Full
output below.

```
Collecting mypkg
  Using cached mypkg-1.4.0.tar.gz
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: mypkg
  Building wheel for mypkg (pyproject.toml) ... -
  running bdist_wheel
  running build
  running build_ext
  building 'mypkg._native' extension
  creating build
  creating build/temp.linux-x86_64-cpython-311
  creating build/temp.linux-x86_64-cpython-311/src
  gcc -pthread -B /usr/lib -Wno-unused-result -DNDEBUG -fwrapv -O2 -Wall -fPIC -Iinclude -c src/native.c -o build/temp.linux-x86_64-cpython-311/src/native.o
  gcc -pthread -B /usr/lib -Wno-unused-result -DNDEBUG -fwrapv -O2 -Wall -fPIC -Iinclude -c src/simd.c -o build/temp.linux-x86_64-cpython-311/src/simd.o
  creating build/lib.linux-x86_64-cpython-311
  gcc -pthread -shared -Wl,-O1 build/temp.linux-x86_64-cpython-311/src/native.o build/temp.linux-x86_64-cpython-311/src/simd.o -L/usr/lib -o build/lib.linux-x86_64-cpython-311/mypkg/_native.cpython-311-x86_64-linux-gnu.so
  running install_lib
  copying build/lib.linux-x86_64-cpython-311/mypkg/_native.cpython-311-x86_64-linux-gnu.so -> build/bdist.linux-x86_64/wheel/mypkg
  running egg_info
  writing mypkg.egg-info/PKG-INFO
  writing dependency_links to mypkg.egg-info/dependency_links.txt
  writing requirements to mypkg.egg-info/requires.txt
  writing top-level names to mypkg.egg-info/top_level.txt
  reading manifest file 'mypkg.egg-info/SOURCES.txt'
  reading manifest template 'MANIFEST.in'
  writing manifest file 'mypkg.egg-info/SOURCES.txt'
  creating build/bdist.linux-x86_64/wheel/mypkg-1.4.0.dist-info/WHEEL
  running install_egg_info
  copying mypkg.egg-info to build/bdist.linux-x86_64/wheel/mypkg-1.4.0-py3.11.egg-info
  running install_scripts
  /usr/bin/ld: build/temp.linux-x86_64-cpython-311/src/simd.o: undefined reference to symbol '__vfma_avx2'
  /usr/bin/ld: /lib/x86_64-linux-gnu/libmvec.so.1: error adding symbols: DSO missing from command line
  collect2: error: ld returned 1 exit status
  error: command '/usr/bin/gcc' failed with exit code 1
ERROR: Failed building wheel for mypkg
Failed to build mypkg
ERROR: Could not build wheels for mypkg, which is required to install pyproject.toml-based projects
```

That final `undefined reference to symbol '__vfma_avx2'` is the actual bug — looks like `simd.c`
needs `-lmvec` on the link line and nobody added it. Everything above that line is just the
normal build marching along.
