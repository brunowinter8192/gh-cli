04_log_ending_in_failure.md:12-43
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

12_positive_control_build_log.md:20-43
Collecting mypkg[full]
  Downloading https://files.pythonhosted.org/packages/aa/bb/mypkg-2.1.0-py3-none-any.whl (11.2 MB)
Collecting torch>=2.0.0 (from mypkg[full])
  Downloading https://files.pythonhosted.org/packages/cc/dd/torch-2.3.0-cp311-none-macosx_11_0_arm64.whl (66.5 MB)
Collecting numpy>=1.21.0 (from mypkg[full])
  Using cached numpy-2.1.1-cp311-cp311-macosx_11_0_arm64.whl (14.1 MB)
Collecting requests>=2.28.0 (from mypkg[full])
  Using cached requests-2.32.3-py3-none-any.whl (64 kB)
Collecting pyyaml>=6.0 (from mypkg[full])
  Downloading https://files.pythonhosted.org/packages/ee/ff/pyyaml-6.0.2-cp311-cp311-macosx_11_0_arm64.whl (171 kB)
Collecting tqdm>=4.65.0 (from mypkg[full])
  Using cached tqdm-4.67.1-py3-none-any.whl (78 kB)
Collecting pillow>=10.0.0 (from mypkg[full])
  Downloading https://files.pythonhosted.org/packages/11/22/pillow-11.2.1-cp311-cp311-macosx_11_0_arm64.whl (3.0 MB)
Collecting filelock (from torch>=2.0.0->mypkg[full])
  Downloading https://files.pythonhosted.org/packages/33/44/filelock-3.18.0-py3-none-any.whl (16 kB)
Collecting sympy (from torch>=2.0.0->mypkg[full])
  Downloading https://files.pythonhosted.org/packages/55/66/sympy-1.13.1-py3-none-any.whl (6.2 MB)
Collecting networkx (from torch>=2.0.0->mypkg[full])
  Downloading https://files.pythonhosted.org/packages/77/88/networkx-3.4.2-py3-none-any.whl (1.7 MB)
Collecting jinja2 (from torch>=2.0.0->mypkg[full])
  Downloading https://files.pythonhosted.org/packages/99/00/jinja2-3.1.6-py3-none-any.whl (134 kB)
Installing collected packages: filelock, tqdm, sympy, requests, pyyaml, pillow, numpy, networkx, jinja2, torch, mypkg
Successfully installed filelock-3.18.0 jinja2-3.1.6 mypkg-2.1.0 networkx-3.4.2 numpy-2.1.1 pillow-11.2.1 pyyaml-6.0.2 requests-2.32.3 sympy-1.13.1 torch-2.3.0 tqdm-4.67.1
