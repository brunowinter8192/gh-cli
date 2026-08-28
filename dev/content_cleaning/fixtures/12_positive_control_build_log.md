# Just a slow install, not actually a bug

State: CLOSED | #9012
Labels: question

---

Install takes forever on my machine, is this normal? Pasting the full log in case it's useful,
but it did finish successfully in the end.

# Comments on example/repo#9012

Total: 1 comments

--- Comment 1 ---

Yeah that's normal, torch and its CUDA deps are just big. Nothing wrong here:

```
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
```

Took about 6 minutes here, mostly the torch wheel download. Nothing to fix.
