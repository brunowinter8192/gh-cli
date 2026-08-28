MinerU__1418.md:77-237
Looking in indexes: https://mirrors.aliyun.com/pypi/simple, https://wheels.myhloli.com
Requirement already satisfied: magic-pdf[full] in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (0.6.1)
Collecting magic-pdf[full]
  Using cached https://mirrors.aliyun.com/pypi/packages/c2/71/dd8ef0c351663872fac973fafac5aaf8b6b09f21fba7e8f11cd9562a3e39/magic_pdf-0.10.6-py3-none-any.whl (1.0 MB)
Requirement already satisfied: boto3>=1.28.43 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from magic-pdf[full]) (1.35.92)
Requirement already satisfied: Brotli>=1.1.0 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from magic-pdf[full]) (1.1.0)
Requirement already satisfied: click>=8.1.7 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from magic-pdf[full]) (8.1.8)
Collecting fast-langdetect==0.2.0 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/d0/99/9cb2230dbdc5697b7d6cce86eec3397a80a2c877c400059fb49a79c48546/fast_langdetect-0.2.0-py3-none-any.whl (6.4 kB)
Requirement already satisfied: loguru>=0.6.0 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from magic-pdf[full]) (0.7.3)
Requirement already satisfied: numpy<2.0.0,>=1.21.6 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from magic-pdf[full]) (1.26.4)
Collecting pydantic<2.8.0,>=2.7.2 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/17/ba/1b65c9cbc49e0c7cd1be086c63209e9ad883c2a409be4746c21db4263f41/pydantic-2.7.4-py3-none-any.whl (409 kB)
Requirement already satisfied: PyMuPDF>=1.24.9 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from magic-pdf[full]) (1.25.1)
Requirement already satisfied: scikit-learn>=1.0.2 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from magic-pdf[full]) (1.6.0)
Collecting torch>=2.2.2 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/69/f0/46e74e0d145f43fa506cb336eaefb2d240547e4ce1f496e442711093ab25/torch-2.5.1-cp310-cp310-manylinux2014_aarch64.whl (91.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 91.9/91.9 MB 10.7 MB/s eta 0:00:00
Collecting transformers (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/f2/3a/8bdab26e09c5a242182b7ba9152e216d5ab4ae2d78c4298eb4872549cd35/transformers-4.47.1-py3-none-any.whl (10.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.1/10.1 MB 9.0 MB/s eta 0:00:00
Collecting pdfminer.six==20231228 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/eb/9c/e46fe7502b32d7db6af6e36a9105abb93301fa1ec475b5ddcba8b35ae23a/pdfminer.six-20231228-py3-none-any.whl (5.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.6/5.6 MB 9.7 MB/s eta 0:00:00
Collecting unimernet==0.2.2 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/4e/52/1b4213bf779b78a1bcd19acf259e653bcad99a9bb96fa1c70c407d1a0321/unimernet-0.2.2-py3-none-any.whl (2.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 8.2 MB/s eta 0:00:00
Collecting torch>=2.2.2 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/d5/67/93143534e1c1293a08fcb96cced205c199c6ae9306707b1a29f533e359f0/torch-2.3.1-cp310-cp310-manylinux2014_aarch64.whl (86.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 86.9/86.9 MB 10.1 MB/s eta 0:00:00
Collecting torchvision<=0.18.1,>=0.17.2 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/9d/7e/38b7d6689e988f23a2c07782e045abaf2d54c7b63086f164c4dbd41228b5/torchvision-0.18.1-cp310-cp310-manylinux2014_aarch64.whl (14.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 14.0/14.0 MB 10.2 MB/s eta 0:00:00
Collecting ultralytics>=8.3.48 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/99/d6/931e939060d8ff54c6f1b05f3481547a8f454fb100e517dbe7a1559f7de0/ultralytics-8.3.58-py3-none-any.whl (905 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 905.3/905.3 kB 8.1 MB/s eta 0:00:00
Collecting paddleocr==2.7.3 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/f2/55/0469ebca1d9c581a3fa740621afe96461a0ef450e489e10e278cc17a19ef/paddleocr-2.7.3-py3-none-any.whl (780 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 780.0/780.0 kB 11.1 MB/s eta 0:00:00
Collecting struct-eqtable==0.3.2 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/37/37/15c7071e838ff648aea987ad918abe23eaca7ef61c3aba38c0638f73aaad/struct_eqtable-0.3.2-py3-none-any.whl (26 kB)
Collecting einops (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/44/5a/f0b9ad6c0a9017e62d4735daaeb11ba3b6c009d69a26141b258cd37b5588/einops-0.8.0-py3-none-any.whl (43 kB)
Collecting accelerate (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/c2/60/a585c806d6c0ec5f8149d44eb202714792802f484e6e2b1bf96b23bd2b00/accelerate-1.2.1-py3-none-any.whl (336 kB)
Collecting doclayout-yolo==0.0.2 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/32/f7/b6255e19d49a216af0d98d125eeec66e91821a20f2fe3d02456abb248309/doclayout_yolo-0.0.2-py3-none-any.whl (708 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 708.2/708.2 kB 10.0 MB/s eta 0:00:00
Collecting rapidocr-paddle (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/b4/9e/bc59911e8721e87587f3e4a08923da3df1ad02a603a3978f8e5f4184ea81/rapidocr_paddle-1.4.4-py3-none-any.whl (15.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 15.0/15.0 MB 11.0 MB/s eta 0:00:00
Collecting rapid-table (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/4a/cb/def6329492bd5ff5265a79043fea612c2218ce0ece3c700525d5b47abd29/rapid_table-0.3.0-py3-none-any.whl (7.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.2/7.2 MB 6.1 MB/s eta 0:00:00
Requirement already satisfied: PyYAML in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from magic-pdf[full]) (6.0.2)
Collecting detectron2 (from magic-pdf[full])
  Using cached https://gcore.jsdelivr.net/gh/myhloli/wheels@main/assets/whl/detectron2/detectron2-0.6-cp310-cp310-linux_aarch64.whl (902 kB)
Collecting paddlepaddle==3.0.0b1 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/5a/f3/6d3e19787d9784540085fabff71dc399ca840d6c1c34fcb665af2cebd9eb/paddlepaddle-3.0.0b1-cp310-cp310-manylinux2014_aarch64.whl (83.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 83.1/83.1 MB 11.1 MB/s eta 0:00:00
Collecting matplotlib (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/ed/8d/45754b4affdb8f0d1a44e4e2bcd932cdf35b256b60d5eda9f455bb293ed0/matplotlib-3.10.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (8.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.4/8.4 MB 10.6 MB/s eta 0:00:00
Collecting opencv-python>=4.6.0 (from doclayout-yolo==0.0.2->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/81/e4/7a987ebecfe5ceaf32db413b67ff18eb3092c598408862fff4d7cc3fd19b/opencv_python-4.10.0.84-cp37-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (41.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 41.7/41.7 MB 11.4 MB/s eta 0:00:00
Collecting pillow>=7.1.2 (from doclayout-yolo==0.0.2->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/81/aa/8d4ad25dc11fd10a2001d5b8a80fdc0e564ac33b293bdfe04ed387e0fd95/pillow-11.1.0-cp310-cp310-manylinux_2_28_aarch64.whl (4.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.4/4.4 MB 10.8 MB/s eta 0:00:00
Requirement already satisfied: requests>=2.23.0 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from doclayout-yolo==0.0.2->magic-pdf[full]) (2.32.3)
Requirement already satisfied: scipy>=1.4.1 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from doclayout-yolo==0.0.2->magic-pdf[full]) (1.15.0)
Requirement already satisfied: tqdm>=4.64.0 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from doclayout-yolo==0.0.2->magic-pdf[full]) (4.67.1)
Collecting psutil (from doclayout-yolo==0.0.2->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/47/da/99f4345d4ddf2845cb5b5bd0d93d554e84542d116934fde07a0c50bd4e9f/psutil-6.1.1-cp36-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (289 kB)
Collecting py-cpuinfo (from doclayout-yolo==0.0.2->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/e0/a9/023730ba63db1e494a271cb018dcd361bd2c917ba7004c3e49d5daf795a2/py_cpuinfo-9.0.0-py3-none-any.whl (22 kB)
Collecting thop>=0.1.1 (from doclayout-yolo==0.0.2->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/bb/0f/72beeab4ff5221dc47127c80f8834b4bcd0cb36f6ba91c0b1d04a1233403/thop-0.1.1.post2209072238-py3-none-any.whl (15 kB)
Collecting pandas>=1.1.4 (from doclayout-yolo==0.0.2->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/ed/12/86c1747ea27989d7a4064f806ce2bae2c6d575b950be087837bdfcabacc9/pandas-2.2.3-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.whl (66.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 66.5/66.5 MB 990.1 kB/s eta 0:00:00
Collecting seaborn>=0.11.0 (from doclayout-yolo==0.0.2->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/83/11/00d3c3dfc25ad54e731d91449895a79e4bf2384dc3ac01809010ba88f6d5/seaborn-0.13.2-py3-none-any.whl (294 kB)
Collecting albumentations>=1.4.11 (from doclayout-yolo==0.0.2->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/af/ae/904b7bf58281d2bc1f3d6d48813bbcee742d1f8e3f9c0e1c451b0f67eb5a/albumentations-1.4.24-py3-none-any.whl (274 kB)
Requirement already satisfied: fasttext-wheel>=0.9.2 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from fast-langdetect==0.2.0->magic-pdf[full]) (0.9.2)
Requirement already satisfied: robust-downloader>=0.0.2 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from fast-langdetect==0.2.0->magic-pdf[full]) (0.0.2)
Collecting langdetect>=1.0.9 (from fast-langdetect==0.2.0->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/0e/72/a3add0e4eec4eb9e2569554f7c70f4a3c27712f40e3284d483e88094cc0e/langdetect-1.0.9.tar.gz (981 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 981.5/981.5 kB 1.2 MB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting shapely (from paddleocr==2.7.3->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/af/09/6374c11cb493a9970e8c04d7be25f578a37f6494a2fecfbed3a447b16b2c/shapely-2.0.6-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (2.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.4/2.4 MB 1.0 MB/s eta 0:00:00
Collecting scikit-image (from paddleocr==2.7.3->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/9d/49/866c3acc5dce86fffbc0852c1090b4df9b36407680691b1e04a4315f4851/scikit_image-0.25.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (14.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 14.2/14.2 MB 1.4 MB/s eta 0:00:00
Collecting imgaug (from paddleocr==2.7.3->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/66/b1/af3142c4a85cba6da9f4ebb5ff4e21e2616309552caca5e8acefe9840622/imgaug-0.4.0-py2.py3-none-any.whl (948 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 948.0/948.0 kB 1.4 MB/s eta 0:00:00
Collecting pyclipper (from paddleocr==2.7.3->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/f5/6a/28ec55cc3f972368b211fca017e081cf5a71009d1b8ec3559767cda5b289/pyclipper-1.3.0.post6-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (929 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 929.5/929.5 kB 1.3 MB/s eta 0:00:00
Collecting lmdb (from paddleocr==2.7.3->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/e9/a6/f46e761bbb90b06d855a57a55de302c7adedc2a87eea5af99f793c6bc81a/lmdb-1.6.2-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (293 kB)
Collecting visualdl (from paddleocr==2.7.3->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/ea/b5/37726c750a4f4598660998327c3566b2d2ed5a1a5f44e9f0dde875602447/visualdl-2.5.3-py3-none-any.whl (6.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.3/6.3 MB 1.6 MB/s eta 0:00:00
Collecting rapidfuzz (from paddleocr==2.7.3->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/b6/2d/19b8e5d80257b13d73ba994552b78a69ac2ed70f1de716f1b02fcb84d09c/rapidfuzz-3.11.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (1.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.4/1.4 MB 1.5 MB/s eta 0:00:00
Collecting opencv-python>=4.6.0 (from doclayout-yolo==0.0.2->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/12/5d/1527327b9f7ea13bef31377f8bf399f03dc5f4f1c9f1fb69bc56b6e24cd4/opencv_python-4.6.0.66-cp36-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (39.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 39.5/39.5 MB 1.9 MB/s eta 0:00:00
Collecting opencv-contrib-python<=4.6.0.66 (from paddleocr==2.7.3->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/13/2d/e8580e089200a8fe84f9befca59ba2d4c92e174dc17dc37a4574ab113db0/opencv_contrib_python-4.6.0.66-cp36-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (45.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 45.3/45.3 MB 2.4 MB/s eta 0:00:00
Collecting cython (from paddleocr==2.7.3->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/d8/3b/67480e609537e9fc899864847910ded481b82d033fea1b7fcf85893a2fc4/Cython-3.0.11-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (3.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.5/3.5 MB 3.2 MB/s eta 0:00:00
Collecting lxml (from paddleocr==2.7.3->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/69/c1/5ea46b2d4c98f5bf5c83fffab8a0ad293c9bc74df9ecfbafef10f77f7201/lxml-5.3.0-cp310-cp310-manylinux_2_28_aarch64.whl (4.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.8/4.8 MB 2.5 MB/s eta 0:00:00
Collecting premailer (from paddleocr==2.7.3->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/b1/07/4e8d94f94c7d41ca5ddf8a9695ad87b888104e2fd41a35546c1dc9ca74ac/premailer-3.10.0-py2.py3-none-any.whl (19 kB)
Collecting openpyxl (from paddleocr==2.7.3->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/c0/da/977ded879c29cbd04de313843e76868e6e13408a94ed6b987245dc7c8506/openpyxl-3.1.5-py2.py3-none-any.whl (250 kB)
Collecting attrdict (from paddleocr==2.7.3->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/ef/97/28fe7e68bc7adfce67d4339756e85e9fcf3c6fd7f0c0781695352b70472c/attrdict-2.0.1-py2.py3-none-any.whl (9.9 kB)
Collecting python-docx (from paddleocr==2.7.3->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/3e/3d/330d9efbdb816d3f60bf2ad92f05e1708e4a1b9abe80461ac3444c83f749/python_docx-1.1.2-py3-none-any.whl (244 kB)
Collecting beautifulsoup4 (from paddleocr==2.7.3->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/b1/fe/e8c672695b37eecc5cbf43e1d0638d88d66ba3a44c4d321c796f4e59167f/beautifulsoup4-4.12.3-py3-none-any.whl (147 kB)
Collecting fonttools>=4.24.0 (from paddleocr==2.7.3->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/f8/9e/e1ba20bd3b71870207fd45ca3b90208a7edd8ae3b001081dc31c45adb017/fonttools-4.55.3-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (4.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.6/4.6 MB 3.2 MB/s eta 0:00:00
Collecting fire>=0.3.0 (from paddleocr==2.7.3->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/6b/b6/82c7e601d6d3c3278c40b7bd35e17e82aa227f050aa9f66cb7b7fce29471/fire-0.7.0.tar.gz (87 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting pdf2docx (from paddleocr==2.7.3->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/b5/f9/6d567df395c0409baf2b4dd9cd30d1e977c70672fe7ec2a684af1e6aa41c/pdf2docx-0.5.8-py3-none-any.whl (132 kB)
Collecting httpx (from paddlepaddle==3.0.0b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/2a/39/e50c7c3a983047577ee07d2a9e53faf5a69493943ec3f6a384bdc792deb2/httpx-0.28.1-py3-none-any.whl (73 kB)
Collecting protobuf>=3.20.2 (from paddlepaddle==3.0.0b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/e4/20/38fc33b60dcfb380507b99494aebe8c34b68b8ac7d32808c4cebda3f6f6b/protobuf-5.29.2-cp38-abi3-manylinux2014_aarch64.whl (319 kB)
Collecting decorator (from paddlepaddle==3.0.0b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/d5/50/83c593b07763e1161326b3b8c6686f0f4b0f24d5526546bee538c89837d6/decorator-5.1.1-py3-none-any.whl (9.1 kB)
Collecting astor (from paddlepaddle==3.0.0b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/c3/88/97eef84f48fa04fbd6750e62dcceafba6c63c81b7ac1420856c8dcc0a3f9/astor-0.8.1-py2.py3-none-any.whl (27 kB)
Collecting opt-einsum==3.3.0 (from paddlepaddle==3.0.0b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/bc/19/404708a7e54ad2798907210462fd950c3442ea51acc8790f3da48d2bee8b/opt_einsum-3.3.0-py3-none-any.whl (65 kB)
Collecting networkx (from paddlepaddle==3.0.0b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/b9/54/dd730b32ea14ea797530a4479b2ed46a6fb250f682a9cfb997e968bf0261/networkx-3.4.2-py3-none-any.whl (1.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 3.2 MB/s eta 0:00:00
Requirement already satisfied: typing-extensions in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from paddlepaddle==3.0.0b1->magic-pdf[full]) (4.12.2)
Requirement already satisfied: charset-normalizer>=2.0.0 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from pdfminer.six==20231228->magic-pdf[full]) (3.4.1)
Requirement already satisfied: cryptography>=36.0.0 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from pdfminer.six==20231228->magic-pdf[full]) (44.0.0)

MinerU__1418.md:239-257
Collecting magic-pdf[full]
  Downloading https://mirrors.aliyun.com/pypi/packages/0a/e3/25a46b44ae93baaf9e76e1410b78a49d9596e603ff6dd134c6edaa9ee0f6/magic_pdf-0.10.5-py3-none-any.whl (994 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 994.9/994.9 kB 2.7 MB/s eta 0:00:00
Collecting unimernet==0.2.1 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/99/db/f32a6f9c5ca2647bd94287dce4ddd4732ef01879029fab3ce99d41e8f44b/unimernet-0.2.1-py3-none-any.whl (2.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 3.3 MB/s eta 0:00:00
Collecting magic-pdf[full]
  Downloading https://mirrors.aliyun.com/pypi/packages/80/d8/87092b4da6534b757807814f0c1b13690dfc7ecf7193f38ac045f4003929/magic_pdf-0.10.4-py3-none-any.whl (994 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 994.9/994.9 kB 3.1 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/89/58/a888f8008cec7d83818e029f2d53265829b4f712c07e93afd78c9ba930c2/magic_pdf-0.10.3-py3-none-any.whl (994 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 994.7/994.7 kB 3.0 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/d2/c6/19c493b8f470dc3c3ef34ba3a7a1c76067174c6abf09624aad69c8401fc7/magic_pdf-0.10.2-py3-none-any.whl (993 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 993.7/993.7 kB 2.7 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/85/2c/ae81baa12b04304c3defba4629fb32de75e807c4078f6c68ad59a2b2e29c/magic_pdf-0.10.1-py3-none-any.whl (1.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 2.9 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/87/e0/4c394c3fdd73035b0aad2c4a0c1c2fba93611bd6f7b2a807dcdd7f5b58de/magic_pdf-0.10.0-py3-none-any.whl (1.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 2.6 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/ef/cb/10f4125092900f5726a38df493ab3917adc82f3162360feffaf7db19cd41/magic_pdf-0.9.3-py3-none-any.whl (1.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 2.5 MB/s eta 0:00:00

MinerU__1418.md:259-278
  Downloading https://mirrors.aliyun.com/pypi/packages/1e/7a/52c976ce12e0794c3fde3d7fc0668066e3f4469ca8c2c09efb68abfa1d9e/magic_pdf-0.9.2-py3-none-any.whl (1.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 3.1 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/0b/c6/01cbb164174e6833e3133c11ea43fe7919ce414a42e46405c102b9594dbd/magic_pdf-0.9.1-py3-none-any.whl (1.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 1.3 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/2d/8d/db5b345e0b14b50d0026e3f079413f765ec678377e79994704d8c7330a68/magic_pdf-0.9.0-py3-none-any.whl (1.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 2.1 MB/s eta 0:00:00
Collecting pypandoc (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/ff/bd/cf1dd70b95f3366f3c457c5259ed8f032122210441407b6ed281d7fcbb8c/pypandoc-1.14-py3-none-any.whl (21 kB)
Collecting struct-eqtable==0.1.0 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/a4/25/d1e91b2ad2727c9ecb332607729a03c2f0f345afd2547f4100e543330f0e/struct_eqtable-0.1.0-py3-none-any.whl (8.5 kB)
Collecting magic-pdf[full]
  Downloading https://mirrors.aliyun.com/pypi/packages/00/5b/5157586376edf6bed6dd0f234423f89ecb01ce10adc6cc608e2e1a935280/magic_pdf-0.8.1-py3-none-any.whl (1.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 2.8 MB/s eta 0:00:00
Requirement already satisfied: wordninja>=2.0.0 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from magic-pdf[full]) (2.0.0)
Collecting unimernet==0.1.6 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/0c/1d/5847f9237c695efae828fea23b4db8bc51419804f116c9156ab0f557377a/unimernet-0.1.6-py3-none-any.whl (2.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.2/2.2 MB 1.9 MB/s eta 0:00:00
Collecting magic-pdf[full]
  Downloading https://mirrors.aliyun.com/pypi/packages/4d/d0/2b4eeeb024161b4158df66f49ad39490dcb87337b2f1b35de89ab6e1e4ee/magic_pdf-0.8.0-py3-none-any.whl (1.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 3.0 MB/s eta 0:00:00

MinerU__1418.md:283-299
Requirement already satisfied: fast-langdetect>=0.2.1 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from magic-pdf[full]) (0.2.2)
Requirement already satisfied: pdfminer.six>=20231228 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from magic-pdf[full]) (20240706)
Requirement already satisfied: botocore<1.36.0,>=1.35.92 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from boto3>=1.28.43->magic-pdf[full]) (1.35.92)
Requirement already satisfied: jmespath<2.0.0,>=0.7.1 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from boto3>=1.28.43->magic-pdf[full]) (1.0.1)
Requirement already satisfied: s3transfer<0.11.0,>=0.10.0 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from boto3>=1.28.43->magic-pdf[full]) (0.10.4)
Requirement already satisfied: joblib>=1.2.0 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from scikit-learn>=1.0.2->magic-pdf[full]) (1.4.2)
Requirement already satisfied: threadpoolctl>=3.1.0 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from scikit-learn>=1.0.2->magic-pdf[full]) (3.5.0)
Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from botocore<1.36.0,>=1.35.92->boto3>=1.28.43->magic-pdf[full]) (2.9.0.post0)
Requirement already satisfied: urllib3!=2.2.0,<3,>=1.25.4 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from botocore<1.36.0,>=1.35.92->boto3>=1.28.43->magic-pdf[full]) (2.3.0)
Requirement already satisfied: cffi>=1.12 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from cryptography>=36.0.0->pdfminer.six==20231228->magic-pdf[full]) (1.17.1)
Requirement already satisfied: pybind11>=2.2 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from fasttext-wheel>=0.9.2->fast-langdetect==0.2.0->magic-pdf[full]) (2.13.6)
Requirement already satisfied: setuptools>=0.7.0 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from fasttext-wheel>=0.9.2->fast-langdetect==0.2.0->magic-pdf[full]) (68.0.0)
Requirement already satisfied: idna<4,>=2.5 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from requests>=2.23.0->doclayout-yolo==0.0.2->magic-pdf[full]) (3.10)
Requirement already satisfied: certifi>=2017.4.17 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from requests>=2.23.0->doclayout-yolo==0.0.2->magic-pdf[full]) (2024.12.14)
Requirement already satisfied: colorlog in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from robust-downloader>=0.0.2->fast-langdetect==0.2.0->magic-pdf[full]) (6.9.0)
Requirement already satisfied: pycparser in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from cffi>=1.12->cryptography>=36.0.0->pdfminer.six==20231228->magic-pdf[full]) (2.22)
Requirement already satisfied: six>=1.5 in ./.local/share/uv/python/cpython-3.10.12-linux-aarch64-gnu/lib/python3.10/site-packages (from python-dateutil<3.0.0,>=2.1->botocore<1.36.0,>=1.35.92->boto3>=1.28.43->magic-pdf[full]) (1.17.0)

MinerU__2262.md:106-131
The following NEW packages will be INSTALLED:

  bzip2              conda-forge/osx-arm64::bzip2-1.0.8-h99b78c6_7 
  ca-certificates    conda-forge/osx-arm64::ca-certificates-2025.1.31-hf0a4a13_0 
  libexpat           conda-forge/osx-arm64::libexpat-2.7.0-h286801f_0 
  libffi             conda-forge/osx-arm64::libffi-3.4.6-h1da3d7d_1 
  liblzma            conda-forge/osx-arm64::liblzma-5.8.1-h39f12f2_0 
  libmpdec           conda-forge/osx-arm64::libmpdec-4.0.0-h99b78c6_0 
  libsqlite          conda-forge/osx-arm64::libsqlite-3.49.1-h3f77e49_2 
  libzlib            conda-forge/osx-arm64::libzlib-1.3.1-h8359307_2 
  ncurses            conda-forge/osx-arm64::ncurses-6.5-h5e97a16_3 
  openssl            conda-forge/osx-arm64::openssl-3.5.0-h81ee809_0 
  pip                conda-forge/noarch::pip-25.0.1-pyh145f28c_0 
  python             conda-forge/osx-arm64::python-3.13.3-h81fe080_101_cp313 
  python_abi         conda-forge/osx-arm64::python_abi-3.13-6_cp313 
  readline           conda-forge/osx-arm64::readline-8.2-h1d1bf99_2 
  tk                 conda-forge/osx-arm64::tk-8.6.13-h5083fa2_1 
  tzdata             conda-forge/noarch::tzdata-2025b-h78e105d_0 



Downloading and Extracting Packages:
                                                                                
Preparing transaction: done                                                     
Verifying transaction: done                                                     
Executing transaction: done                                                     

MinerU__2262.md:143-372
Looking in indexes: https://mirrors.aliyun.com/pypi/simple
Collecting magic-pdf[full]
  Using cached https://mirrors.aliyun.com/pypi/packages/34/24/1e95d3d37415cbcb768f680c09099fbc111bc77c0ddc219c093206c94ab0/magic_pdf-1.3.4-py3-none-any.whl (11.2 MB)
Collecting Brotli>=1.1.0 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/0a/9f/fb37bb8ffc52a8da37b1c03c459a8cd55df7a57bdccd8831d500e994a0ca/Brotli-1.1.0-cp313-cp313-macosx_10_13_universal2.whl (815 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 815.7/815.7 kB 2.4 MB/s eta 0:00:00
Collecting PyMuPDF<1.25.0,>=1.24.9 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/2c/11/8d6f4c8fca86b93759e430c4b0b7b66f8067d58893d6fe0a193420d14453/PyMuPDF-1.24.14-cp39-abi3-macosx_11_0_arm64.whl (18.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 18.4/18.4 MB 2.4 MB/s eta 0:00:00
Collecting boto3>=1.28.43 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/f6/e4/00958f65ac74ab0a76af33f16c8fdf5726a5c6f0d3c0d0c058ff0dd00fd7/boto3-1.37.35-py3-none-any.whl (139 kB)
Collecting click>=8.1.7 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/7e/d4/7ebdbd03970677812aac39c869717059dbb71a4cfc033ca6e5221787892c/click-8.1.8-py3-none-any.whl (98 kB)
Collecting fast-langdetect<0.3.0,>=0.2.3 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/27/da/c621e64d4bc23f485468295bb7d4a5f2290ebb4d342c8dc448ab66808071/fast_langdetect-0.2.5-py3-none-any.whl (786 kB)
Collecting loguru>=0.6.0 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/0c/29/0348de65b8cc732daa3e33e67806420b2ae89bdce2b04af740289c5c6c8c/loguru-0.7.3-py3-none-any.whl (61 kB)
Collecting numpy>=1.21.6 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/6a/70/67b24d68a56551d43a6ec9fe8c5f91b526d4c1a46a6387b956bf2d64744e/numpy-2.2.4-cp313-cp313-macosx_14_0_arm64.whl (5.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.1/5.1 MB 2.4 MB/s eta 0:00:00
Collecting pdfminer.six==20231228 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/eb/9c/e46fe7502b32d7db6af6e36a9105abb93301fa1ec475b5ddcba8b35ae23a/pdfminer.six-20231228-py3-none-any.whl (5.6 MB)
Collecting pydantic<2.11,>=2.7.2 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/f4/3c/8cc1cc84deffa6e25d2d0c688ebb80635dfdbf1dbea3e30c541c8cf4d860/pydantic-2.10.6-py3-none-any.whl (431 kB)
Collecting scikit-learn>=1.0.2 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/9d/05/f2fc4effc5b32e525408524c982c468c29d22f828834f0625c5ef3d601be/scikit_learn-1.6.1-cp313-cp313-macosx_12_0_arm64.whl (11.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.1/11.1 MB 2.4 MB/s eta 0:00:00
Collecting torch!=2.5.0,!=2.5.1,>=2.2.2 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/88/8b/d60c0491ab63634763be1537ad488694d316ddc4a20eaadd639cedc53971/torch-2.6.0-cp313-none-macosx_11_0_arm64.whl (66.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 66.5/66.5 MB 2.4 MB/s eta 0:00:00
Collecting torchvision (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/f9/56/47d456b61c3bbce7bed4af3925c83d405bb87468e659fd3cf3d9840c3b51/torchvision-0.21.0-cp313-cp313-macosx_11_0_arm64.whl (1.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 2.3 MB/s eta 0:00:00
Collecting tqdm>=4.67.1 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/d0/30/dc54f88dd4a2b5dc8a0279bdd7270e735851848b762aeb1c1184ed1f6b14/tqdm-4.67.1-py3-none-any.whl (78 kB)
Collecting transformers!=4.51.0,<5.0.0,>=4.49.0 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/a9/b6/5257d04ae327b44db31f15cce39e6020cc986333c715660b1315a9724d82/transformers-4.51.3-py3-none-any.whl (10.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.4/10.4 MB 2.4 MB/s eta 0:00:00
Collecting PyYAML<7,>=6.0.2 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/45/9f/3b1c20a0b7a3200524eb0076cc027a970d320bd3a6592873c85c92a08731/PyYAML-6.0.2-cp313-cp313-macosx_11_0_arm64.whl (171 kB)
Collecting dill<1,>=0.3.8 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/50/3d/9373ad9c56321fdab5b41197068e1d8c25883b3fea29dd361f9b55116869/dill-0.4.0-py3-none-any.whl (119 kB)
Collecting doclayout-yolo==0.0.2b1 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/3e/f8/bab8c287088276b26b68dd07de9b355b0ca0582a0d32d7a26b08a56e18e8/doclayout_yolo-0.0.2b1-py3-none-any.whl (711 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 711.2/711.2 kB 2.3 MB/s eta 0:00:00
Collecting ftfy<7,>=6.3.1 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/ab/6e/81d47999aebc1b155f81eca4477a616a70f238a2549848c38983f3c22a82/ftfy-6.3.1-py3-none-any.whl (44 kB)
Collecting matplotlib<4,>=3.10 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/08/97/b0ca5da0ed54a3f6599c3ab568bdda65269bc27c21a2c97868c1625e4554/matplotlib-3.10.1-cp313-cp313-macosx_11_0_arm64.whl (8.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.0/8.0 MB 2.4 MB/s eta 0:00:00
Collecting omegaconf<3,>=2.3.0 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/e3/94/1843518e420fa3ed6919835845df698c7e27e183cb997394e4a670973a65/omegaconf-2.3.0-py3-none-any.whl (79 kB)
Collecting openai<2,>=1.70.0 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/80/9a/f34f163294345f123673ed03e77c33dee2534f3ac1f9d18120384457304d/openai-1.75.0-py3-none-any.whl (646 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 647.0/647.0 kB 2.3 MB/s eta 0:00:00
Collecting pyclipper<2,>=1.3.0 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/8c/b3/75232906bd13f869600d23bdb8fe6903cc899fa7e96981ae4c9b7d9c409e/pyclipper-1.3.0.post6-cp313-cp313-macosx_10_13_universal2.whl (268 kB)
Collecting rapid-table<2.0.0,>=1.0.5 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/4a/cf/a86d2cae2a80bc0c3ce7961b908c61ccbf72e0d882ccb62169c1623135c6/rapid_table-1.0.5-py3-none-any.whl (33 kB)
Collecting shapely<3,>=2.0.7 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/71/3c/d888597bda680e4de987316b05ca9db07416fa29523beff64f846503302f/shapely-2.1.0-cp313-cp313-macosx_11_0_arm64.whl (1.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 2.4 MB/s eta 0:00:00
Collecting ultralytics<9,>=8.3.48 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/03/d1/5aac637e50f7cad9ee6428105a2fd4436922fd40ca587ae4e0393a923e1a/ultralytics-8.3.109-py3-none-any.whl (974 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 974.8/974.8 kB 2.3 MB/s eta 0:00:00
Collecting opencv-python>=4.6.0 (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/05/4d/53b30a2a3ac1f75f65a59eb29cf2ee7207ce64867db47036ad61743d5a23/opencv_python-4.11.0.86-cp37-abi3-macosx_13_0_arm64.whl (37.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 37.3/37.3 MB 2.4 MB/s eta 0:00:00
Collecting pillow>=7.1.2 (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/b5/09/29d5cd052f7566a63e5b506fac9c60526e9ecc553825551333e1e18a4858/pillow-11.2.1-cp313-cp313-macosx_11_0_arm64.whl (3.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 2.4 MB/s eta 0:00:00
Collecting requests>=2.23.0 (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/f9/9b/335f9764261e915ed497fcdeb11df5dfd6f7bf257d4a6a2a686d80da4d54/requests-2.32.3-py3-none-any.whl (64 kB)
Collecting scipy>=1.4.1 (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/dd/b1/f9fe6e3c828cb5930b5fe74cb479de5f3d66d682fa8adb77249acaf545b8/scipy-1.15.2-cp313-cp313-macosx_14_0_arm64.whl (22.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 22.4/22.4 MB 2.4 MB/s eta 0:00:00
Collecting psutil (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/04/8b/30f930733afe425e3cbfc0e1468a30a18942350c1a8816acfade80c005c4/psutil-7.0.0-cp36-abi3-macosx_11_0_arm64.whl (239 kB)
Collecting py-cpuinfo (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/e0/a9/023730ba63db1e494a271cb018dcd361bd2c917ba7004c3e49d5daf795a2/py_cpuinfo-9.0.0-py3-none-any.whl (22 kB)
Collecting thop>=0.1.1 (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/bb/0f/72beeab4ff5221dc47127c80f8834b4bcd0cb36f6ba91c0b1d04a1233403/thop-0.1.1.post2209072238-py3-none-any.whl (15 kB)
Collecting pandas>=1.1.4 (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/e4/93/b3f5d1838500e22c8d793625da672f3eec046b1a99257666c94446969282/pandas-2.2.3-cp313-cp313-macosx_11_0_arm64.whl (11.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.3/11.3 MB 2.4 MB/s eta 0:00:00
Collecting seaborn>=0.11.0 (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/83/11/00d3c3dfc25ad54e731d91449895a79e4bf2384dc3ac01809010ba88f6d5/seaborn-0.13.2-py3-none-any.whl (294 kB)
Collecting albumentations>=1.4.11 (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/97/d3/cf3aab593209d1be5e4bca54aeea297225708bd25f06426d6b8ec3630a76/albumentations-2.0.5-py3-none-any.whl (290 kB)
Collecting charset-normalizer>=2.0.0 (from pdfminer.six==20231228->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/38/94/ce8e6f63d18049672c76d07d119304e1e2d7c6098f0841b51c666e9f44a0/charset_normalizer-3.4.1-cp313-cp313-macosx_10_13_universal2.whl (195 kB)
Collecting cryptography>=36.0.0 (from pdfminer.six==20231228->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/9e/be/7a26142e6d0f7683d8a382dd963745e65db895a79a280a30525ec92be890/cryptography-44.0.2-cp39-abi3-macosx_10_9_universal2.whl (6.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.7/6.7 MB 2.4 MB/s eta 0:00:00
Collecting botocore<1.38.0,>=1.37.35 (from boto3>=1.28.43->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/22/00/bf9c894f5af8e35b06ecf757d4a95883408e71c48642dc7f8760580584fd/botocore-1.37.35-py3-none-any.whl (13.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.5/13.5 MB 2.4 MB/s eta 0:00:00
Collecting jmespath<2.0.0,>=0.7.1 (from boto3>=1.28.43->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/31/b4/b9b800c45527aadd64d5b442f9b932b00648617eb5d63d2c7a6587b7cafc/jmespath-1.0.1-py3-none-any.whl (20 kB)
Collecting s3transfer<0.12.0,>=0.11.0 (from boto3>=1.28.43->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/86/62/8d3fc3ec6640161a5649b2cddbbf2b9fa39c92541225b33f117c37c5a2eb/s3transfer-0.11.4-py3-none-any.whl (84 kB)
Collecting robust-downloader>=0.0.2 (from fast-langdetect<0.3.0,>=0.2.3->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/56/a1/779e9d0ebbdc704411ce30915a1105eb01aeaa9e402d7e446613ff8fb121/robust_downloader-0.0.2-py3-none-any.whl (15 kB)
Collecting fasttext-predict>=0.9.2.4 (from fast-langdetect<0.3.0,>=0.2.3->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/d9/53/8d542773e32c9d98dd8c680e390fe7e6d4fc92ab3439dc1bb8e70c46c7ad/fasttext_predict-0.9.2.4-cp313-cp313-macosx_11_0_arm64.whl (97 kB)
Collecting wcwidth (from ftfy<7,>=6.3.1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/fd/84/fd2ba7aafacbad3c4201d395674fc6348826569da3c0937e75505ead3528/wcwidth-0.2.13-py2.py3-none-any.whl (34 kB)
Collecting contourpy>=1.0.1 (from matplotlib<4,>=3.10->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/ff/66/a40badddd1223822c95798c55292844b7e871e50f6bfd9f158cb25e0bd39/contourpy-1.3.2-cp313-cp313-macosx_11_0_arm64.whl (255 kB)
Collecting cycler>=0.10 (from matplotlib<4,>=3.10->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/e7/05/c19819d5e3d95294a6f5947fb9b9629efb316b96de511b418c53d245aae6/cycler-0.12.1-py3-none-any.whl (8.3 kB)
Collecting fonttools>=4.22.0 (from matplotlib<4,>=3.10->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/e9/2f/11439f3af51e4bb75ac9598c29f8601aa501902dcedf034bdc41f47dd799/fonttools-4.57.0-cp313-cp313-macosx_10_13_universal2.whl (2.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.7/2.7 MB 2.4 MB/s eta 0:00:00
Collecting kiwisolver>=1.3.1 (from matplotlib<4,>=3.10->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/59/e3/b8bd14b0a54998a9fd1e8da591c60998dc003618cb19a3f94cb233ec1511/kiwisolver-1.4.8-cp313-cp313-macosx_11_0_arm64.whl (65 kB)
Collecting packaging>=20.0 (from matplotlib<4,>=3.10->magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/88/ef/eb23f262cca3c0c4eb7ab1933c3b1f03d021f2c48f54763065b6f0e321be/packaging-24.2-py3-none-any.whl (65 kB)
Collecting pyparsing>=2.3.1 (from matplotlib<4,>=3.10->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/05/e7/df2285f3d08fee213f2d041540fa4fc9ca6c2d44cf36d3a035bf2a8d2bcc/pyparsing-3.2.3-py3-none-any.whl (111 kB)
Collecting python-dateutil>=2.7 (from matplotlib<4,>=3.10->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/ec/57/56b9bcc3c9c6a792fcbaf139543cee77261f3651ca9da0c93f5c1221264b/python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Collecting antlr4-python3-runtime==4.9.* (from omegaconf<3,>=2.3.0->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/3e/38/7859ff46355f76f8d19459005ca000b6e7012f2f1ca597746cbcd1fbfe5e/antlr4-python3-runtime-4.9.3.tar.gz (117 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting anyio<5,>=3.5.0 (from openai<2,>=1.70.0->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/a1/ee/48ca1a7c89ffec8b6a0c5d02b89c305671d5ffd8d3c94acf8b8c408575bb/anyio-4.9.0-py3-none-any.whl (100 kB)
Collecting distro<2,>=1.7.0 (from openai<2,>=1.70.0->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/12/b3/231ffd4ab1fc9d679809f356cebee130ac7daa00d6d6f3206dd4fd137e9e/distro-1.9.0-py3-none-any.whl (20 kB)
Collecting httpx<1,>=0.23.0 (from openai<2,>=1.70.0->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/2a/39/e50c7c3a983047577ee07d2a9e53faf5a69493943ec3f6a384bdc792deb2/httpx-0.28.1-py3-none-any.whl (73 kB)
Collecting jiter<1,>=0.4.0 (from openai<2,>=1.70.0->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/13/aa/7a890dfe29c84c9a82064a9fe36079c7c0309c91b70c380dc138f9bea44a/jiter-0.9.0-cp313-cp313-macosx_11_0_arm64.whl (318 kB)
Collecting sniffio (from openai<2,>=1.70.0->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/e9/44/75a9c9421471a6c4805dbf2356f7c181a29c1879239abab1ea2cc8f38b40/sniffio-1.3.1-py3-none-any.whl (10 kB)
Collecting typing-extensions<5,>=4.11 (from openai<2,>=1.70.0->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/8b/54/b1ae86c0973cc6f0210b53d508ca3641fb6d0c56823f288d108bc7ab3cc8/typing_extensions-4.13.2-py3-none-any.whl (45 kB)
Collecting annotated-types>=0.6.0 (from pydantic<2.11,>=2.7.2->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/78/b6/6307fbef88d9b5ee7421e68d78a9f162e0da4900bc5f5793f6d3d0e34fb8/annotated_types-0.7.0-py3-none-any.whl (13 kB)
Collecting pydantic-core==2.27.2 (from pydantic<2.11,>=2.7.2->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/10/6c/e62b8657b834f3eb2961b49ec8e301eb99946245e70bf42c8817350cbefc/pydantic_core-2.27.2-cp313-cp313-macosx_11_0_arm64.whl (1.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 2.4 MB/s eta 0:00:00
Collecting onnxruntime>1.17.0 (from rapid-table<2.0.0,>=1.0.5->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/f2/25/93f65617b06c741a58eeac9e373c99df443b02a774f4cb6511889757c0da/onnxruntime-1.21.0-cp313-cp313-macosx_13_0_universal2.whl (33.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 33.7/33.7 MB 2.4 MB/s eta 0:00:00
Collecting colorlog (from rapid-table<2.0.0,>=1.0.5->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/e3/51/9b208e85196941db2f0654ad0357ca6388ab3ed67efdbfc799f35d1f83aa/colorlog-6.9.0-py3-none-any.whl (11 kB)
Collecting joblib>=1.2.0 (from scikit-learn>=1.0.2->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/91/29/df4b9b42f2be0b623cbd5e2140cafcaa2bef0759a00b7b70104dcfe2fb51/joblib-1.4.2-py3-none-any.whl (301 kB)
Collecting threadpoolctl>=3.1.0 (from scikit-learn>=1.0.2->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/32/d5/f9a850d79b0851d1d4ef6456097579a9005b31fea68726a4ae5f2d82ddd9/threadpoolctl-3.6.0-py3-none-any.whl (18 kB)
Collecting filelock (from torch!=2.5.0,!=2.5.1,>=2.2.2->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/4d/36/2a115987e2d8c300a974597416d9de88f2444426de9571f4b59b2cca3acc/filelock-3.18.0-py3-none-any.whl (16 kB)
Collecting networkx (from torch!=2.5.0,!=2.5.1,>=2.2.2->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/b9/54/dd730b32ea14ea797530a4479b2ed46a6fb250f682a9cfb997e968bf0261/networkx-3.4.2-py3-none-any.whl (1.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 2.4 MB/s eta 0:00:00
Collecting jinja2 (from torch!=2.5.0,!=2.5.1,>=2.2.2->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/62/a1/3d680cbfd5f4b8f15abc1d571870c5fc3e594bb582bc3b64ea099db13e56/jinja2-3.1.6-py3-none-any.whl (134 kB)
Collecting fsspec (from torch!=2.5.0,!=2.5.1,>=2.2.2->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/44/4b/e0cfc1a6f17e990f3e64b7d941ddc4acdc7b19d6edd51abf495f32b1a9e4/fsspec-2025.3.2-py3-none-any.whl (194 kB)
Collecting setuptools (from torch!=2.5.0,!=2.5.1,>=2.2.2->magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/54/21/f43f0a1fa8b06b32812e0975981f4677d28e0f3271601dc88ac5a5b83220/setuptools-78.1.0-py3-none-any.whl (1.3 MB)
Collecting sympy==1.13.1 (from torch!=2.5.0,!=2.5.1,>=2.2.2->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/b2/fe/81695a1aa331a842b582453b605175f419fe8540355886031328089d840a/sympy-1.13.1-py3-none-any.whl (6.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.2/6.2 MB 2.4 MB/s eta 0:00:00
Collecting mpmath<1.4,>=1.1.0 (from sympy==1.13.1->torch!=2.5.0,!=2.5.1,>=2.2.2->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/43/e3/7d92a15f894aa0c9c4b49b8ee9ac9850d6e63b03c9c32c0367a13ae62209/mpmath-1.3.0-py3-none-any.whl (536 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 536.2/536.2 kB 2.2 MB/s eta 0:00:00
Collecting huggingface-hub<1.0,>=0.30.0 (from transformers!=4.51.0,<5.0.0,>=4.49.0->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/93/27/1fb384a841e9661faad1c31cbfa62864f59632e876df5d795234da51c395/huggingface_hub-0.30.2-py3-none-any.whl (481 kB)
Collecting regex!=2019.12.17 (from transformers!=4.51.0,<5.0.0,>=4.49.0->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/09/c9/4e68181a4a652fb3ef5099e077faf4fd2a694ea6e0f806a7737aff9e758a/regex-2024.11.6-cp313-cp313-macosx_11_0_arm64.whl (284 kB)
Collecting tokenizers<0.22,>=0.21 (from transformers!=4.51.0,<5.0.0,>=4.49.0->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/ae/1a/4526797f3719b0287853f12c5ad563a9be09d446c44ac784cdd7c50f76ab/tokenizers-0.21.1-cp39-abi3-macosx_11_0_arm64.whl (2.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.7/2.7 MB 2.4 MB/s eta 0:00:00
Collecting safetensors>=0.4.3 (from transformers!=4.51.0,<5.0.0,>=4.49.0->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/b8/3b/11f1b4a2f5d2ab7da34ecc062b0bc301f2be024d110a6466726bec8c055c/safetensors-0.5.3-cp38-abi3-macosx_11_0_arm64.whl (418 kB)
Collecting numpy>=1.21.6 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/25/18/c732d7dd9896d11e4afcd487ac65e62f9fa0495563b7614eb850765361fa/numpy-2.1.1-cp313-cp313-macosx_14_0_arm64.whl (5.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.1/5.1 MB 2.4 MB/s eta 0:00:00
Collecting ultralytics-thop>=2.0.0 (from ultralytics<9,>=8.3.48->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/a6/10/251f036b4c5d77249f9a119cc89dafe8745dc1ad1f1a5f06b6a3988ca454/ultralytics_thop-2.0.14-py3-none-any.whl (26 kB)
Collecting albucore==0.0.23 (from albumentations>=1.4.11->doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/3d/de/4d9298befa6ae0f21230378f55100dca364816e3734028ca2766f2eca263/albucore-0.0.23-py3-none-any.whl (14 kB)
Collecting opencv-python-headless>=4.9.0.80 (from albumentations>=1.4.11->doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/dc/53/2c50afa0b1e05ecdb4603818e85f7d174e683d874ef63a6abe3ac92220c8/opencv_python_headless-4.11.0.86-cp37-abi3-macosx_13_0_arm64.whl (37.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 37.3/37.3 MB 2.4 MB/s eta 0:00:00
Collecting stringzilla>=3.10.4 (from albucore==0.0.23->albumentations>=1.4.11->doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/16/7d/519e655db076726b3490c4f9e248ede85c491bcb64dc16bc24e736f5142f/stringzilla-3.12.4-cp313-cp313-macosx_11_0_arm64.whl (79 kB)
Collecting simsimd>=5.9.2 (from albucore==0.0.23->albumentations>=1.4.11->doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/cf/86/816050f0fd0767e960c6b900e3c97fd6a4ae54a6aa5b8ef24846757a3f7d/simsimd-6.2.1-cp313-cp313-macosx_11_0_arm64.whl (93 kB)
Collecting idna>=2.8 (from anyio<5,>=3.5.0->openai<2,>=1.70.0->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/76/c6/c88e154df9c4e1a2a66ccf0005a88dfb2650c1dffb6f5ce603dfbd452ce3/idna-3.10-py3-none-any.whl (70 kB)
Collecting urllib3!=2.2.0,<3,>=1.25.4 (from botocore<1.38.0,>=1.37.35->boto3>=1.28.43->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/6b/11/cc635220681e93a0183390e26485430ca2c7b5f9d33b15c74c2861cb8091/urllib3-2.4.0-py3-none-any.whl (128 kB)
Collecting cffi>=1.12 (from cryptography>=36.0.0->pdfminer.six==20231228->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/8b/f1/672d303ddf17c24fc83afd712316fda78dc6fce1cd53011b839483e1ecc8/cffi-1.17.1-cp313-cp313-macosx_11_0_arm64.whl (178 kB)
Collecting certifi (from httpx<1,>=0.23.0->openai<2,>=1.70.0->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/38/fc/bce832fd4fd99766c04d1ee0eead6b0ec6486fb100ae5e74c1d91292b982/certifi-2025.1.31-py3-none-any.whl (166 kB)
Collecting httpcore==1.* (from httpx<1,>=0.23.0->openai<2,>=1.70.0->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/18/8d/f052b1e336bb2c1fc7ed1aaed898aa570c0b61a09707b108979d9fc6e308/httpcore-1.0.8-py3-none-any.whl (78 kB)
Collecting h11<0.15,>=0.13 (from httpcore==1.*->httpx<1,>=0.23.0->openai<2,>=1.70.0->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/95/04/ff642e65ad6b90db43e668d70ffb6736436c7ce41fcc549f4e9472234127/h11-0.14.0-py3-none-any.whl (58 kB)
Collecting coloredlogs (from onnxruntime>1.17.0->rapid-table<2.0.0,>=1.0.5->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/a7/06/3d6badcf13db419e25b07041d9c7b4a2c331d3f4e7134445ec5df57714cd/coloredlogs-15.0.1-py2.py3-none-any.whl (46 kB)
Collecting flatbuffers (from onnxruntime>1.17.0->rapid-table<2.0.0,>=1.0.5->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/b8/25/155f9f080d5e4bc0082edfda032ea2bc2b8fab3f4d25d46c1e9dd22a1a89/flatbuffers-25.2.10-py2.py3-none-any.whl (30 kB)
Collecting protobuf (from onnxruntime>1.17.0->rapid-table<2.0.0,>=1.0.5->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/8e/66/7f3b121f59097c93267e7f497f10e52ced7161b38295137a12a266b6c149/protobuf-6.30.2-cp39-abi3-macosx_10_9_universal2.whl (417 kB)
Collecting pytz>=2020.1 (from pandas>=1.1.4->doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/81/c4/34e93fe5f5429d7570ec1fa436f1986fb1f00c3e0f43a589fe2bbcd22c3f/pytz-2025.2-py2.py3-none-any.whl (509 kB)
Collecting tzdata>=2022.7 (from pandas>=1.1.4->doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/5c/23/c7abc0ca0a1526a0774eca151daeb8de62ec457e77262b66b359c3c7679e/tzdata-2025.2-py2.py3-none-any.whl (347 kB)
Collecting six>=1.5 (from python-dateutil>=2.7->matplotlib<4,>=3.10->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/b7/ce/149a00dd41f10bc29e5921b496af8b574d8413afcd5e30dfa0ed46c2cc5e/six-1.17.0-py2.py3-none-any.whl (11 kB)
Collecting MarkupSafe>=2.0 (from jinja2->torch!=2.5.0,!=2.5.1,>=2.2.2->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/2b/6d/9409f3684d3335375d04e5f05744dfe7e9f120062c9857df4ab490a1031a/MarkupSafe-3.0.2-cp313-cp313-macosx_11_0_arm64.whl (12 kB)
Collecting pycparser (from cffi>=1.12->cryptography>=36.0.0->pdfminer.six==20231228->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/13/a3/a812df4e2dd5696d1f351d58b8fe16a405b234ad2886a0dab9183fb78109/pycparser-2.22-py3-none-any.whl (117 kB)
Collecting humanfriendly>=9.1 (from coloredlogs->onnxruntime>1.17.0->rapid-table<2.0.0,>=1.0.5->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/f0/0f/310fb31e39e2d734ccaa2c0fb981ee41f7bd5056ce9bc29b2248bd569169/humanfriendly-10.0-py2.py3-none-any.whl (86 kB)
Building wheels for collected packages: antlr4-python3-runtime
  Building wheel for antlr4-python3-runtime (pyproject.toml) ... done
  Created wheel for antlr4-python3-runtime: filename=antlr4_python3_runtime-4.9.3-py3-none-any.whl size=144592 sha256=2efa33f1f0c8fbbb630ed5ca19f2efd070283feb7166f49acf979904cdacacfd
  Stored in directory: /Users/myhloli/Library/Caches/pip/wheels/46/a7/6e/18ba4163eeda4c44351868050fa916ee725680b4c1bb5af8d2
Successfully built antlr4-python3-runtime
Installing collected packages: wcwidth, stringzilla, simsimd, pytz, pyclipper, py-cpuinfo, mpmath, flatbuffers, fasttext-predict, Brotli, antlr4-python3-runtime, urllib3, tzdata, typing-extensions, tqdm, threadpoolctl, sympy, sniffio, six, setuptools, safetensors, regex, PyYAML, pyparsing, PyMuPDF, pycparser, psutil, protobuf, pillow, packaging, numpy, networkx, MarkupSafe, loguru, kiwisolver, joblib, jmespath, jiter, idna, humanfriendly, h11, ftfy, fsspec, fonttools, filelock, distro, dill, cycler, colorlog, click, charset-normalizer, certifi, annotated-types, shapely, scipy, requests, python-dateutil, pydantic-core, opencv-python-headless, opencv-python, omegaconf, jinja2, httpcore, contourpy, coloredlogs, cffi, anyio, torch, scikit-learn, robust-downloader, pydantic, pandas, onnxruntime, matplotlib, huggingface-hub, httpx, cryptography, botocore, albucore, ultralytics-thop, torchvision, tokenizers, thop, seaborn, s3transfer, rapid-table, pdfminer.six, openai, fast-langdetect, albumentations, ultralytics, transformers, doclayout-yolo, boto3, magic-pdf
Successfully installed Brotli-1.1.0 MarkupSafe-3.0.2 PyMuPDF-1.24.14 PyYAML-6.0.2 albucore-0.0.23 albumentations-2.0.5 annotated-types-0.7.0 antlr4-python3-runtime-4.9.3 anyio-4.9.0 boto3-1.37.35 botocore-1.37.35 certifi-2025.1.31 cffi-1.17.1 charset-normalizer-3.4.1 click-8.1.8 coloredlogs-15.0.1 colorlog-6.9.0 contourpy-1.3.2 cryptography-44.0.2 cycler-0.12.1 dill-0.4.0 distro-1.9.0 doclayout-yolo-0.0.2b1 fast-langdetect-0.2.5 fasttext-predict-0.9.2.4 filelock-3.18.0 flatbuffers-25.2.10 fonttools-4.57.0 fsspec-2025.3.2 ftfy-6.3.1 h11-0.14.0 httpcore-1.0.8 httpx-0.28.1 huggingface-hub-0.30.2 humanfriendly-10.0 idna-3.10 jinja2-3.1.6 jiter-0.9.0 jmespath-1.0.1 joblib-1.4.2 kiwisolver-1.4.8 loguru-0.7.3 magic-pdf-1.3.4 matplotlib-3.10.1 mpmath-1.3.0 networkx-3.4.2 numpy-2.1.1 omegaconf-2.3.0 onnxruntime-1.21.0 openai-1.75.0 opencv-python-4.11.0.86 opencv-python-headless-4.11.0.86 packaging-24.2 pandas-2.2.3 pdfminer.six-20231228 pillow-11.2.1 protobuf-6.30.2 psutil-7.0.0 py-cpuinfo-9.0.0 pyclipper-1.3.0.post6 pycparser-2.22 pydantic-2.10.6 pydantic-core-2.27.2 pyparsing-3.2.3 python-dateutil-2.9.0.post0 pytz-2025.2 rapid-table-1.0.5 regex-2024.11.6 requests-2.32.3 robust-downloader-0.0.2 s3transfer-0.11.4 safetensors-0.5.3 scikit-learn-1.6.1 scipy-1.15.2 seaborn-0.13.2 setuptools-78.1.0 shapely-2.1.0 simsimd-6.2.1 six-1.17.0 sniffio-1.3.1 stringzilla-3.12.4 sympy-1.13.1 thop-0.1.1.post2209072238 threadpoolctl-3.6.0 tokenizers-0.21.1 torch-2.6.0 torchvision-0.21.0 tqdm-4.67.1 transformers-4.51.3 typing-extensions-4.13.2 tzdata-2025.2 ultralytics-8.3.109 ultralytics-thop-2.0.14 urllib3-2.4.0 wcwidth-0.2.13

MinerU__2262.md:505-533
The following NEW packages will be INSTALLED:

  bzip2              pkgs/main/osx-arm64::bzip2-1.0.8-h80987f9_6 
  ca-certificates    pkgs/main/osx-arm64::ca-certificates-2025.2.25-hca03da5_0 
  expat              pkgs/main/osx-arm64::expat-2.7.1-h313beb8_0 
  libcxx             pkgs/main/osx-arm64::libcxx-14.0.6-h848a8c0_0 
  libffi             pkgs/main/osx-arm64::libffi-3.4.4-hca03da5_1 
  libmpdec           pkgs/main/osx-arm64::libmpdec-4.0.0-h80987f9_0 
  ncurses            pkgs/main/osx-arm64::ncurses-6.4-h313beb8_0 
  openssl            pkgs/main/osx-arm64::openssl-3.0.16-h02f6b3c_0 
  pip                pkgs/main/osx-arm64::pip-25.0-py313hca03da5_0 
  python             pkgs/main/osx-arm64::python-3.13.2-h4862095_100_cp313 
  python_abi         pkgs/main/osx-arm64::python_abi-3.13-0_cp313 
  readline           pkgs/main/osx-arm64::readline-8.2-h1a28f6b_0 
  setuptools         pkgs/main/osx-arm64::setuptools-75.8.0-py313hca03da5_0 
  sqlite             pkgs/main/osx-arm64::sqlite-3.45.3-h80987f9_0 
  tk                 pkgs/main/osx-arm64::tk-8.6.14-h6ba3021_0 
  tzdata             pkgs/main/noarch::tzdata-2025a-h04d1e81_0 
  wheel              pkgs/main/osx-arm64::wheel-0.45.1-py313hca03da5_0 
  xz                 pkgs/main/osx-arm64::xz-5.6.4-h80987f9_1 
  zlib               pkgs/main/osx-arm64::zlib-1.2.13-h18a0788_1 



Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done

MinerU__2262.md:545-641
Looking in indexes: https://mirrors.aliyun.com/pypi/simple
Collecting magic-pdf[full]
  Using cached https://mirrors.aliyun.com/pypi/packages/34/24/1e95d3d37415cbcb768f680c09099fbc111bc77c0ddc219c093206c94ab0/magic_pdf-1.3.4-py3-none-any.whl (11.2 MB)
Collecting Brotli>=1.1.0 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/0a/9f/fb37bb8ffc52a8da37b1c03c459a8cd55df7a57bdccd8831d500e994a0ca/Brotli-1.1.0-cp313-cp313-macosx_10_13_universal2.whl (815 kB)
Collecting PyMuPDF<1.25.0,>=1.24.9 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/2c/11/8d6f4c8fca86b93759e430c4b0b7b66f8067d58893d6fe0a193420d14453/PyMuPDF-1.24.14-cp39-abi3-macosx_11_0_arm64.whl (18.4 MB)
Collecting boto3>=1.28.43 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/f6/e4/00958f65ac74ab0a76af33f16c8fdf5726a5c6f0d3c0d0c058ff0dd00fd7/boto3-1.37.35-py3-none-any.whl (139 kB)
Collecting click>=8.1.7 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/7e/d4/7ebdbd03970677812aac39c869717059dbb71a4cfc033ca6e5221787892c/click-8.1.8-py3-none-any.whl (98 kB)
Collecting fast-langdetect<0.3.0,>=0.2.3 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/27/da/c621e64d4bc23f485468295bb7d4a5f2290ebb4d342c8dc448ab66808071/fast_langdetect-0.2.5-py3-none-any.whl (786 kB)
Collecting loguru>=0.6.0 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/0c/29/0348de65b8cc732daa3e33e67806420b2ae89bdce2b04af740289c5c6c8c/loguru-0.7.3-py3-none-any.whl (61 kB)
Collecting numpy>=1.21.6 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/c3/bc/2b3545766337b95409868f8e62053135bdc7fa2ce630aba983a2aa60b559/numpy-2.2.4-cp313-cp313-macosx_11_0_arm64.whl (14.1 MB)
Collecting pdfminer.six==20231228 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/eb/9c/e46fe7502b32d7db6af6e36a9105abb93301fa1ec475b5ddcba8b35ae23a/pdfminer.six-20231228-py3-none-any.whl (5.6 MB)
Collecting pydantic<2.11,>=2.7.2 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/f4/3c/8cc1cc84deffa6e25d2d0c688ebb80635dfdbf1dbea3e30c541c8cf4d860/pydantic-2.10.6-py3-none-any.whl (431 kB)
Collecting scikit-learn>=1.0.2 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/9d/05/f2fc4effc5b32e525408524c982c468c29d22f828834f0625c5ef3d601be/scikit_learn-1.6.1-cp313-cp313-macosx_12_0_arm64.whl (11.1 MB)
Collecting torch!=2.5.0,!=2.5.1,>=2.2.2 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/88/8b/d60c0491ab63634763be1537ad488694d316ddc4a20eaadd639cedc53971/torch-2.6.0-cp313-none-macosx_11_0_arm64.whl (66.5 MB)
Collecting torchvision (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/f9/56/47d456b61c3bbce7bed4af3925c83d405bb87468e659fd3cf3d9840c3b51/torchvision-0.21.0-cp313-cp313-macosx_11_0_arm64.whl (1.8 MB)
Collecting tqdm>=4.67.1 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/d0/30/dc54f88dd4a2b5dc8a0279bdd7270e735851848b762aeb1c1184ed1f6b14/tqdm-4.67.1-py3-none-any.whl (78 kB)
Collecting transformers!=4.51.0,<5.0.0,>=4.49.0 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/a9/b6/5257d04ae327b44db31f15cce39e6020cc986333c715660b1315a9724d82/transformers-4.51.3-py3-none-any.whl (10.4 MB)
Collecting PyYAML<7,>=6.0.2 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/45/9f/3b1c20a0b7a3200524eb0076cc027a970d320bd3a6592873c85c92a08731/PyYAML-6.0.2-cp313-cp313-macosx_11_0_arm64.whl (171 kB)
Collecting dill<1,>=0.3.8 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/50/3d/9373ad9c56321fdab5b41197068e1d8c25883b3fea29dd361f9b55116869/dill-0.4.0-py3-none-any.whl (119 kB)
Collecting doclayout-yolo==0.0.2b1 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/3e/f8/bab8c287088276b26b68dd07de9b355b0ca0582a0d32d7a26b08a56e18e8/doclayout_yolo-0.0.2b1-py3-none-any.whl (711 kB)
Collecting ftfy<7,>=6.3.1 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/ab/6e/81d47999aebc1b155f81eca4477a616a70f238a2549848c38983f3c22a82/ftfy-6.3.1-py3-none-any.whl (44 kB)
Collecting matplotlib<4,>=3.10 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/08/97/b0ca5da0ed54a3f6599c3ab568bdda65269bc27c21a2c97868c1625e4554/matplotlib-3.10.1-cp313-cp313-macosx_11_0_arm64.whl (8.0 MB)
Collecting omegaconf<3,>=2.3.0 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/e3/94/1843518e420fa3ed6919835845df698c7e27e183cb997394e4a670973a65/omegaconf-2.3.0-py3-none-any.whl (79 kB)
Collecting openai<2,>=1.70.0 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/80/9a/f34f163294345f123673ed03e77c33dee2534f3ac1f9d18120384457304d/openai-1.75.0-py3-none-any.whl (646 kB)
Collecting pyclipper<2,>=1.3.0 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/8c/b3/75232906bd13f869600d23bdb8fe6903cc899fa7e96981ae4c9b7d9c409e/pyclipper-1.3.0.post6-cp313-cp313-macosx_10_13_universal2.whl (268 kB)
Collecting rapid-table<2.0.0,>=1.0.5 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/4a/cf/a86d2cae2a80bc0c3ce7961b908c61ccbf72e0d882ccb62169c1623135c6/rapid_table-1.0.5-py3-none-any.whl (33 kB)
Collecting shapely<3,>=2.0.7 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/71/3c/d888597bda680e4de987316b05ca9db07416fa29523beff64f846503302f/shapely-2.1.0-cp313-cp313-macosx_11_0_arm64.whl (1.6 MB)
Collecting ultralytics<9,>=8.3.48 (from magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/03/d1/5aac637e50f7cad9ee6428105a2fd4436922fd40ca587ae4e0393a923e1a/ultralytics-8.3.109-py3-none-any.whl (974 kB)
Collecting opencv-python>=4.6.0 (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/17/06/68c27a523103dad5837dc5b87e71285280c4f098c60e4fe8a8db6486ab09/opencv-python-4.11.0.86.tar.gz (95.2 MB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
Collecting pillow>=7.1.2 (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/b5/09/29d5cd052f7566a63e5b506fac9c60526e9ecc553825551333e1e18a4858/pillow-11.2.1-cp313-cp313-macosx_11_0_arm64.whl (3.0 MB)
Collecting requests>=2.23.0 (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/f9/9b/335f9764261e915ed497fcdeb11df5dfd6f7bf257d4a6a2a686d80da4d54/requests-2.32.3-py3-none-any.whl (64 kB)
Collecting scipy>=1.4.1 (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/fe/c3/2854f40ecd19585d65afaef601e5e1f8dbf6758b2f95b5ea93d38655a2c6/scipy-1.15.2-cp313-cp313-macosx_12_0_arm64.whl (30.1 MB)
Collecting psutil (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/04/8b/30f930733afe425e3cbfc0e1468a30a18942350c1a8816acfade80c005c4/psutil-7.0.0-cp36-abi3-macosx_11_0_arm64.whl (239 kB)
Collecting py-cpuinfo (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/e0/a9/023730ba63db1e494a271cb018dcd361bd2c917ba7004c3e49d5daf795a2/py_cpuinfo-9.0.0-py3-none-any.whl (22 kB)
Collecting thop>=0.1.1 (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/bb/0f/72beeab4ff5221dc47127c80f8834b4bcd0cb36f6ba91c0b1d04a1233403/thop-0.1.1.post2209072238-py3-none-any.whl (15 kB)
Collecting pandas>=1.1.4 (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/e4/93/b3f5d1838500e22c8d793625da672f3eec046b1a99257666c94446969282/pandas-2.2.3-cp313-cp313-macosx_11_0_arm64.whl (11.3 MB)
Collecting seaborn>=0.11.0 (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/83/11/00d3c3dfc25ad54e731d91449895a79e4bf2384dc3ac01809010ba88f6d5/seaborn-0.13.2-py3-none-any.whl (294 kB)
Collecting albumentations>=1.4.11 (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/97/d3/cf3aab593209d1be5e4bca54aeea297225708bd25f06426d6b8ec3630a76/albumentations-2.0.5-py3-none-any.whl (290 kB)
Collecting charset-normalizer>=2.0.0 (from pdfminer.six==20231228->magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/38/94/ce8e6f63d18049672c76d07d119304e1e2d7c6098f0841b51c666e9f44a0/charset_normalizer-3.4.1-cp313-cp313-macosx_10_13_universal2.whl (195 kB)
Collecting cryptography>=36.0.0 (from pdfminer.six==20231228->magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/9e/be/7a26142e6d0f7683d8a382dd963745e65db895a79a280a30525ec92be890/cryptography-44.0.2-cp39-abi3-macosx_10_9_universal2.whl (6.7 MB)
Collecting botocore<1.38.0,>=1.37.35 (from boto3>=1.28.43->magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/22/00/bf9c894f5af8e35b06ecf757d4a95883408e71c48642dc7f8760580584fd/botocore-1.37.35-py3-none-any.whl (13.5 MB)
Collecting jmespath<2.0.0,>=0.7.1 (from boto3>=1.28.43->magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/31/b4/b9b800c45527aadd64d5b442f9b932b00648617eb5d63d2c7a6587b7cafc/jmespath-1.0.1-py3-none-any.whl (20 kB)
Collecting s3transfer<0.12.0,>=0.11.0 (from boto3>=1.28.43->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/86/62/8d3fc3ec6640161a5649b2cddbbf2b9fa39c92541225b33f117c37c5a2eb/s3transfer-0.11.4-py3-none-any.whl (84 kB)
Collecting robust-downloader>=0.0.2 (from fast-langdetect<0.3.0,>=0.2.3->magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/56/a1/779e9d0ebbdc704411ce30915a1105eb01aeaa9e402d7e446613ff8fb121/robust_downloader-0.0.2-py3-none-any.whl (15 kB)
Collecting fasttext-predict>=0.9.2.4 (from fast-langdetect<0.3.0,>=0.2.3->magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/d9/53/8d542773e32c9d98dd8c680e390fe7e6d4fc92ab3439dc1bb8e70c46c7ad/fasttext_predict-0.9.2.4-cp313-cp313-macosx_11_0_arm64.whl (97 kB)
Collecting wcwidth (from ftfy<7,>=6.3.1->magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/fd/84/fd2ba7aafacbad3c4201d395674fc6348826569da3c0937e75505ead3528/wcwidth-0.2.13-py2.py3-none-any.whl (34 kB)
Collecting contourpy>=1.0.1 (from matplotlib<4,>=3.10->magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/ff/66/a40badddd1223822c95798c55292844b7e871e50f6bfd9f158cb25e0bd39/contourpy-1.3.2-cp313-cp313-macosx_11_0_arm64.whl (255 kB)
Collecting cycler>=0.10 (from matplotlib<4,>=3.10->magic-pdf[full])
  Using cached https://mirrors.aliyun.com/pypi/packages/e7/05/c19819d5e3d95294a6f5947fb9b9629efb316b96de511b418c53d245aae6/cycler-0.12.1-py3-none-any.whl (8.3 kB)

MinerU__2262.md:645-793
Looking in indexes: https://mirrors.aliyun.com/pypi/simple
Collecting magic-pdf[full]
  Downloading https://mirrors.aliyun.com/pypi/packages/34/24/1e95d3d37415cbcb768f680c09099fbc111bc77c0ddc219c093206c94ab0/magic_pdf-1.3.4-py3-none-any.whl (11.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.2/11.2 MB 4.3 MB/s eta 0:00:00
Collecting Brotli>=1.1.0 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/0a/9f/fb37bb8ffc52a8da37b1c03c459a8cd55df7a57bdccd8831d500e994a0ca/Brotli-1.1.0-cp313-cp313-macosx_10_13_universal2.whl (815 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 815.7/815.7 kB 4.3 MB/s eta 0:00:00
Collecting PyMuPDF<1.25.0,>=1.24.9 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/2c/11/8d6f4c8fca86b93759e430c4b0b7b66f8067d58893d6fe0a193420d14453/PyMuPDF-1.24.14-cp39-abi3-macosx_11_0_arm64.whl (18.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 18.4/18.4 MB 4.4 MB/s eta 0:00:00
Collecting boto3>=1.28.43 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/f6/e4/00958f65ac74ab0a76af33f16c8fdf5726a5c6f0d3c0d0c058ff0dd00fd7/boto3-1.37.35-py3-none-any.whl (139 kB)
Collecting click>=8.1.7 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/7e/d4/7ebdbd03970677812aac39c869717059dbb71a4cfc033ca6e5221787892c/click-8.1.8-py3-none-any.whl (98 kB)
Collecting fast-langdetect<0.3.0,>=0.2.3 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/27/da/c621e64d4bc23f485468295bb7d4a5f2290ebb4d342c8dc448ab66808071/fast_langdetect-0.2.5-py3-none-any.whl (786 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 786.6/786.6 kB 4.7 MB/s eta 0:00:00
Collecting loguru>=0.6.0 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/0c/29/0348de65b8cc732daa3e33e67806420b2ae89bdce2b04af740289c5c6c8c/loguru-0.7.3-py3-none-any.whl (61 kB)
Collecting numpy>=1.21.6 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/c3/bc/2b3545766337b95409868f8e62053135bdc7fa2ce630aba983a2aa60b559/numpy-2.2.4-cp313-cp313-macosx_11_0_arm64.whl (14.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 14.1/14.1 MB 4.4 MB/s eta 0:00:00
Collecting pdfminer.six==20231228 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/eb/9c/e46fe7502b32d7db6af6e36a9105abb93301fa1ec475b5ddcba8b35ae23a/pdfminer.six-20231228-py3-none-any.whl (5.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.6/5.6 MB 4.5 MB/s eta 0:00:00
Collecting pydantic<2.11,>=2.7.2 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/f4/3c/8cc1cc84deffa6e25d2d0c688ebb80635dfdbf1dbea3e30c541c8cf4d860/pydantic-2.10.6-py3-none-any.whl (431 kB)
Collecting scikit-learn>=1.0.2 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/9d/05/f2fc4effc5b32e525408524c982c468c29d22f828834f0625c5ef3d601be/scikit_learn-1.6.1-cp313-cp313-macosx_12_0_arm64.whl (11.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.1/11.1 MB 4.4 MB/s eta 0:00:00
Collecting torch!=2.5.0,!=2.5.1,>=2.2.2 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/88/8b/d60c0491ab63634763be1537ad488694d316ddc4a20eaadd639cedc53971/torch-2.6.0-cp313-none-macosx_11_0_arm64.whl (66.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 66.5/66.5 MB 4.4 MB/s eta 0:00:00
Collecting torchvision (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/f9/56/47d456b61c3bbce7bed4af3925c83d405bb87468e659fd3cf3d9840c3b51/torchvision-0.21.0-cp313-cp313-macosx_11_0_arm64.whl (1.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 4.9 MB/s eta 0:00:00
Collecting tqdm>=4.67.1 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/d0/30/dc54f88dd4a2b5dc8a0279bdd7270e735851848b762aeb1c1184ed1f6b14/tqdm-4.67.1-py3-none-any.whl (78 kB)
Collecting transformers!=4.51.0,<5.0.0,>=4.49.0 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/a9/b6/5257d04ae327b44db31f15cce39e6020cc986333c715660b1315a9724d82/transformers-4.51.3-py3-none-any.whl (10.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.4/10.4 MB 5.0 MB/s eta 0:00:00
Collecting PyYAML<7,>=6.0.2 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/45/9f/3b1c20a0b7a3200524eb0076cc027a970d320bd3a6592873c85c92a08731/PyYAML-6.0.2-cp313-cp313-macosx_11_0_arm64.whl (171 kB)
Collecting dill<1,>=0.3.8 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/50/3d/9373ad9c56321fdab5b41197068e1d8c25883b3fea29dd361f9b55116869/dill-0.4.0-py3-none-any.whl (119 kB)
Collecting doclayout-yolo==0.0.2b1 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/3e/f8/bab8c287088276b26b68dd07de9b355b0ca0582a0d32d7a26b08a56e18e8/doclayout_yolo-0.0.2b1-py3-none-any.whl (711 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 711.2/711.2 kB 5.7 MB/s eta 0:00:00
Collecting ftfy<7,>=6.3.1 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/ab/6e/81d47999aebc1b155f81eca4477a616a70f238a2549848c38983f3c22a82/ftfy-6.3.1-py3-none-any.whl (44 kB)
Collecting matplotlib<4,>=3.10 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/08/97/b0ca5da0ed54a3f6599c3ab568bdda65269bc27c21a2c97868c1625e4554/matplotlib-3.10.1-cp313-cp313-macosx_11_0_arm64.whl (8.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.0/8.0 MB 4.9 MB/s eta 0:00:00
Collecting omegaconf<3,>=2.3.0 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/e3/94/1843518e420fa3ed6919835845df698c7e27e183cb997394e4a670973a65/omegaconf-2.3.0-py3-none-any.whl (79 kB)
Collecting openai<2,>=1.70.0 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/80/9a/f34f163294345f123673ed03e77c33dee2534f3ac1f9d18120384457304d/openai-1.75.0-py3-none-any.whl (646 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 647.0/647.0 kB 6.1 MB/s eta 0:00:00
Collecting pyclipper<2,>=1.3.0 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/8c/b3/75232906bd13f869600d23bdb8fe6903cc899fa7e96981ae4c9b7d9c409e/pyclipper-1.3.0.post6-cp313-cp313-macosx_10_13_universal2.whl (268 kB)
Collecting rapid-table<2.0.0,>=1.0.5 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/4a/cf/a86d2cae2a80bc0c3ce7961b908c61ccbf72e0d882ccb62169c1623135c6/rapid_table-1.0.5-py3-none-any.whl (33 kB)
Collecting shapely<3,>=2.0.7 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/71/3c/d888597bda680e4de987316b05ca9db07416fa29523beff64f846503302f/shapely-2.1.0-cp313-cp313-macosx_11_0_arm64.whl (1.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 5.2 MB/s eta 0:00:00
Collecting ultralytics<9,>=8.3.48 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/03/d1/5aac637e50f7cad9ee6428105a2fd4436922fd40ca587ae4e0393a923e1a/ultralytics-8.3.109-py3-none-any.whl (974 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 974.8/974.8 kB 5.8 MB/s eta 0:00:00
Collecting opencv-python>=4.6.0 (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/17/06/68c27a523103dad5837dc5b87e71285280c4f098c60e4fe8a8db6486ab09/opencv-python-4.11.0.86.tar.gz (95.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 95.2/95.2 MB 4.8 MB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
Collecting pillow>=7.1.2 (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/b5/09/29d5cd052f7566a63e5b506fac9c60526e9ecc553825551333e1e18a4858/pillow-11.2.1-cp313-cp313-macosx_11_0_arm64.whl (3.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 5.1 MB/s eta 0:00:00
Collecting requests>=2.23.0 (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/f9/9b/335f9764261e915ed497fcdeb11df5dfd6f7bf257d4a6a2a686d80da4d54/requests-2.32.3-py3-none-any.whl (64 kB)
Collecting scipy>=1.4.1 (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/fe/c3/2854f40ecd19585d65afaef601e5e1f8dbf6758b2f95b5ea93d38655a2c6/scipy-1.15.2-cp313-cp313-macosx_12_0_arm64.whl (30.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 30.1/30.1 MB 5.1 MB/s eta 0:00:00
Collecting psutil (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/04/8b/30f930733afe425e3cbfc0e1468a30a18942350c1a8816acfade80c005c4/psutil-7.0.0-cp36-abi3-macosx_11_0_arm64.whl (239 kB)
Collecting py-cpuinfo (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/e0/a9/023730ba63db1e494a271cb018dcd361bd2c917ba7004c3e49d5daf795a2/py_cpuinfo-9.0.0-py3-none-any.whl (22 kB)
Collecting thop>=0.1.1 (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/bb/0f/72beeab4ff5221dc47127c80f8834b4bcd0cb36f6ba91c0b1d04a1233403/thop-0.1.1.post2209072238-py3-none-any.whl (15 kB)
Collecting pandas>=1.1.4 (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/e4/93/b3f5d1838500e22c8d793625da672f3eec046b1a99257666c94446969282/pandas-2.2.3-cp313-cp313-macosx_11_0_arm64.whl (11.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.3/11.3 MB 5.6 MB/s eta 0:00:00
Collecting seaborn>=0.11.0 (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/83/11/00d3c3dfc25ad54e731d91449895a79e4bf2384dc3ac01809010ba88f6d5/seaborn-0.13.2-py3-none-any.whl (294 kB)
Collecting albumentations>=1.4.11 (from doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/97/d3/cf3aab593209d1be5e4bca54aeea297225708bd25f06426d6b8ec3630a76/albumentations-2.0.5-py3-none-any.whl (290 kB)
Collecting charset-normalizer>=2.0.0 (from pdfminer.six==20231228->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/38/94/ce8e6f63d18049672c76d07d119304e1e2d7c6098f0841b51c666e9f44a0/charset_normalizer-3.4.1-cp313-cp313-macosx_10_13_universal2.whl (195 kB)
Collecting cryptography>=36.0.0 (from pdfminer.six==20231228->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/9e/be/7a26142e6d0f7683d8a382dd963745e65db895a79a280a30525ec92be890/cryptography-44.0.2-cp39-abi3-macosx_10_9_universal2.whl (6.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.7/6.7 MB 5.4 MB/s eta 0:00:00
Collecting botocore<1.38.0,>=1.37.35 (from boto3>=1.28.43->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/22/00/bf9c894f5af8e35b06ecf757d4a95883408e71c48642dc7f8760580584fd/botocore-1.37.35-py3-none-any.whl (13.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.5/13.5 MB 5.2 MB/s eta 0:00:00
Collecting jmespath<2.0.0,>=0.7.1 (from boto3>=1.28.43->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/31/b4/b9b800c45527aadd64d5b442f9b932b00648617eb5d63d2c7a6587b7cafc/jmespath-1.0.1-py3-none-any.whl (20 kB)
Collecting s3transfer<0.12.0,>=0.11.0 (from boto3>=1.28.43->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/86/62/8d3fc3ec6640161a5649b2cddbbf2b9fa39c92541225b33f117c37c5a2eb/s3transfer-0.11.4-py3-none-any.whl (84 kB)
Collecting robust-downloader>=0.0.2 (from fast-langdetect<0.3.0,>=0.2.3->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/56/a1/779e9d0ebbdc704411ce30915a1105eb01aeaa9e402d7e446613ff8fb121/robust_downloader-0.0.2-py3-none-any.whl (15 kB)
Collecting fasttext-predict>=0.9.2.4 (from fast-langdetect<0.3.0,>=0.2.3->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/d9/53/8d542773e32c9d98dd8c680e390fe7e6d4fc92ab3439dc1bb8e70c46c7ad/fasttext_predict-0.9.2.4-cp313-cp313-macosx_11_0_arm64.whl (97 kB)
Collecting wcwidth (from ftfy<7,>=6.3.1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/fd/84/fd2ba7aafacbad3c4201d395674fc6348826569da3c0937e75505ead3528/wcwidth-0.2.13-py2.py3-none-any.whl (34 kB)
Collecting contourpy>=1.0.1 (from matplotlib<4,>=3.10->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/ff/66/a40badddd1223822c95798c55292844b7e871e50f6bfd9f158cb25e0bd39/contourpy-1.3.2-cp313-cp313-macosx_11_0_arm64.whl (255 kB)
Collecting cycler>=0.10 (from matplotlib<4,>=3.10->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/e7/05/c19819d5e3d95294a6f5947fb9b9629efb316b96de511b418c53d245aae6/cycler-0.12.1-py3-none-any.whl (8.3 kB)
Collecting fonttools>=4.22.0 (from matplotlib<4,>=3.10->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/e9/2f/11439f3af51e4bb75ac9598c29f8601aa501902dcedf034bdc41f47dd799/fonttools-4.57.0-cp313-cp313-macosx_10_13_universal2.whl (2.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.7/2.7 MB 5.6 MB/s eta 0:00:00
Collecting kiwisolver>=1.3.1 (from matplotlib<4,>=3.10->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/59/e3/b8bd14b0a54998a9fd1e8da591c60998dc003618cb19a3f94cb233ec1511/kiwisolver-1.4.8-cp313-cp313-macosx_11_0_arm64.whl (65 kB)
Collecting packaging>=20.0 (from matplotlib<4,>=3.10->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/88/ef/eb23f262cca3c0c4eb7ab1933c3b1f03d021f2c48f54763065b6f0e321be/packaging-24.2-py3-none-any.whl (65 kB)
Collecting pyparsing>=2.3.1 (from matplotlib<4,>=3.10->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/05/e7/df2285f3d08fee213f2d041540fa4fc9ca6c2d44cf36d3a035bf2a8d2bcc/pyparsing-3.2.3-py3-none-any.whl (111 kB)
Collecting python-dateutil>=2.7 (from matplotlib<4,>=3.10->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/ec/57/56b9bcc3c9c6a792fcbaf139543cee77261f3651ca9da0c93f5c1221264b/python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Collecting antlr4-python3-runtime==4.9.* (from omegaconf<3,>=2.3.0->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/3e/38/7859ff46355f76f8d19459005ca000b6e7012f2f1ca597746cbcd1fbfe5e/antlr4-python3-runtime-4.9.3.tar.gz (117 kB)
  Preparing metadata (setup.py) ... done
Collecting anyio<5,>=3.5.0 (from openai<2,>=1.70.0->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/a1/ee/48ca1a7c89ffec8b6a0c5d02b89c305671d5ffd8d3c94acf8b8c408575bb/anyio-4.9.0-py3-none-any.whl (100 kB)
Collecting distro<2,>=1.7.0 (from openai<2,>=1.70.0->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/12/b3/231ffd4ab1fc9d679809f356cebee130ac7daa00d6d6f3206dd4fd137e9e/distro-1.9.0-py3-none-any.whl (20 kB)
Collecting httpx<1,>=0.23.0 (from openai<2,>=1.70.0->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/2a/39/e50c7c3a983047577ee07d2a9e53faf5a69493943ec3f6a384bdc792deb2/httpx-0.28.1-py3-none-any.whl (73 kB)
Collecting jiter<1,>=0.4.0 (from openai<2,>=1.70.0->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/13/aa/7a890dfe29c84c9a82064a9fe36079c7c0309c91b70c380dc138f9bea44a/jiter-0.9.0-cp313-cp313-macosx_11_0_arm64.whl (318 kB)
Collecting sniffio (from openai<2,>=1.70.0->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/e9/44/75a9c9421471a6c4805dbf2356f7c181a29c1879239abab1ea2cc8f38b40/sniffio-1.3.1-py3-none-any.whl (10 kB)
Collecting typing-extensions<5,>=4.11 (from openai<2,>=1.70.0->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/8b/54/b1ae86c0973cc6f0210b53d508ca3641fb6d0c56823f288d108bc7ab3cc8/typing_extensions-4.13.2-py3-none-any.whl (45 kB)
Collecting annotated-types>=0.6.0 (from pydantic<2.11,>=2.7.2->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/78/b6/6307fbef88d9b5ee7421e68d78a9f162e0da4900bc5f5793f6d3d0e34fb8/annotated_types-0.7.0-py3-none-any.whl (13 kB)
Collecting pydantic-core==2.27.2 (from pydantic<2.11,>=2.7.2->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/10/6c/e62b8657b834f3eb2961b49ec8e301eb99946245e70bf42c8817350cbefc/pydantic_core-2.27.2-cp313-cp313-macosx_11_0_arm64.whl (1.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 5.6 MB/s eta 0:00:00

MinerU__2262.md:795-817
Collecting magic-pdf[full]
  Downloading https://mirrors.aliyun.com/pypi/packages/b4/e9/a66311a9ffed1d4c2dcff2267fe9d7ff38980c8767494069ecd34143359c/magic_pdf-1.3.3-py3-none-any.whl (11.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.2/11.2 MB 5.5 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/79/3d/58e52dd51fb9c683c775d829edf136d37573cbc4aa83b39c491ad2fe38d5/magic_pdf-1.3.2-py3-none-any.whl (11.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.2/11.2 MB 5.5 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/71/b9/91a9f9ba59b67ce58906f9eea5a287cf6b5e87968eb3a500a852056d2bc3/magic_pdf-1.3.1-py3-none-any.whl (11.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.2/11.2 MB 5.2 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/74/c2/8b794190a2273ff3f7293bca7ce18cbd3ac0f2cedef94dca9debe8a3e508/magic_pdf-1.3.0-py3-none-any.whl (4.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.1/4.1 MB 5.2 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/b3/9c/ffb90814ea62f6f566a2b9365ec46b791c4cbec6d28aeb2ad44eb0846add/magic_pdf-1.2.2-py3-none-any.whl (3.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.9/3.9 MB 5.1 MB/s eta 0:00:00
Collecting numpy<2.0.0,>=1.21.6 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/65/6e/09db70a523a96d25e115e71cc56a6f9031e7b8cd166c1ac8438307c14058/numpy-1.26.4.tar.gz (15.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 15.8/15.8 MB 5.2 MB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
Collecting pydantic>=2.7.2 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/b0/1d/407b29780a289868ed696d1616f4aad49d6388e5a77f567dcd2629dcd7b8/pydantic-2.11.3-py3-none-any.whl (443 kB)
Collecting unimernet==0.2.3 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/31/40/7b604dd088fe7b49081729e5136538a145e33a949cc35f5602b497961cd0/unimernet-0.2.3-py3-none-any.whl (2.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 4.6 MB/s eta 0:00:00

MinerU__2262.md:819-841
Collecting magic-pdf[full]
  Downloading https://mirrors.aliyun.com/pypi/packages/c2/05/560efe202c6fb6588ccf93ea9333f121630fc47c70fae0408dd19728e1e0/magic_pdf-1.2.1-py3-none-any.whl (3.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.9/3.9 MB 4.6 MB/s eta 0:00:00
Collecting fast-langdetect>=0.2.3 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/30/71/0e6da751ef4a9afae2903f76fb8e43c612e3d288a7b01a74ccc20e81b68f/fast_langdetect-0.3.2-py3-none-any.whl (788 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 788.1/788.1 kB 3.7 MB/s eta 0:00:00
Collecting magic-pdf[full]
  Downloading https://mirrors.aliyun.com/pypi/packages/f5/1b/22e8586e6f9f24fe4f73ede44f6e3d0fdfe40849fb2c4aae43cf26120ca4/magic_pdf-1.2.0-py3-none-any.whl (3.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.9/3.9 MB 5.0 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/97/05/bcdb5a8e449236c132867350ef8f98b43b09d26e124ab48ec24d614407ee/magic_pdf-1.1.0-py3-none-any.whl (3.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.9/3.9 MB 5.1 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/26/e4/dba99555b624c9b5d729eda84a94f36f2f6c2e416f81c1b31d5bf2d2379f/magic_pdf-1.0.1-py3-none-any.whl (3.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.9/3.9 MB 4.7 MB/s eta 0:00:00
Collecting PyMuPDF>=1.24.9 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/4e/55/43b64fa6cd048d2ea4574c045b5ac05d023254b91c2c703185f6f8a77b30/pymupdf-1.25.5-cp39-abi3-macosx_11_0_arm64.whl (18.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 18.6/18.6 MB 4.6 MB/s eta 0:00:00
Collecting magic-pdf[full]
  Downloading https://mirrors.aliyun.com/pypi/packages/c2/71/dd8ef0c351663872fac973fafac5aaf8b6b09f21fba7e8f11cd9562a3e39/magic_pdf-0.10.6-py3-none-any.whl (1.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.0/1.0 MB 4.4 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/0a/e3/25a46b44ae93baaf9e76e1410b78a49d9596e603ff6dd134c6edaa9ee0f6/magic_pdf-0.10.5-py3-none-any.whl (994 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 994.9/994.9 kB 4.3 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/80/d8/87092b4da6534b757807814f0c1b13690dfc7ecf7193f38ac045f4003929/magic_pdf-0.10.4-py3-none-any.whl (994 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 994.9/994.9 kB 4.2 MB/s eta 0:00:00

MinerU__2262.md:843-852
  Downloading https://mirrors.aliyun.com/pypi/packages/89/58/a888f8008cec7d83818e029f2d53265829b4f712c07e93afd78c9ba930c2/magic_pdf-0.10.3-py3-none-any.whl (994 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 994.7/994.7 kB 1.5 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/d2/c6/19c493b8f470dc3c3ef34ba3a7a1c76067174c6abf09624aad69c8401fc7/magic_pdf-0.10.2-py3-none-any.whl (993 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 993.7/993.7 kB 3.8 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/85/2c/ae81baa12b04304c3defba4629fb32de75e807c4078f6c68ad59a2b2e29c/magic_pdf-0.10.1-py3-none-any.whl (1.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 3.9 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/87/e0/4c394c3fdd73035b0aad2c4a0c1c2fba93611bd6f7b2a807dcdd7f5b58de/magic_pdf-0.10.0-py3-none-any.whl (1.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 4.4 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/ef/cb/10f4125092900f5726a38df493ab3917adc82f3162360feffaf7db19cd41/magic_pdf-0.9.3-py3-none-any.whl (1.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 4.0 MB/s eta 0:00:00

MinerU__2262.md:854-866
  Downloading https://mirrors.aliyun.com/pypi/packages/1e/7a/52c976ce12e0794c3fde3d7fc0668066e3f4469ca8c2c09efb68abfa1d9e/magic_pdf-0.9.2-py3-none-any.whl (1.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 4.3 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/0b/c6/01cbb164174e6833e3133c11ea43fe7919ce414a42e46405c102b9594dbd/magic_pdf-0.9.1-py3-none-any.whl (1.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 2.7 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/2d/8d/db5b345e0b14b50d0026e3f079413f765ec678377e79994704d8c7330a68/magic_pdf-0.9.0-py3-none-any.whl (1.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 2.6 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/00/5b/5157586376edf6bed6dd0f234423f89ecb01ce10adc6cc608e2e1a935280/magic_pdf-0.8.1-py3-none-any.whl (1.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 4.2 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/4d/d0/2b4eeeb024161b4158df66f49ad39490dcb87337b2f1b35de89ab6e1e4ee/magic_pdf-0.8.0-py3-none-any.whl (1.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 4.3 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/93/3d/6127d46701e60b3ab1a9621fe9c99c84f7e46939a8744013b2367651ad27/magic_pdf-0.7.1-py3-none-any.whl (1.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 4.7 MB/s eta 0:00:00
  Downloading https://mirrors.aliyun.com/pypi/packages/f6/e5/3a96d48b487c74727009ee3c128c065ab36b2c64bada36225b7bfe07d2e1/magic_pdf-0.6.1-py3-none-any.whl (330 kB)

MinerU__2262.md:868-899
Collecting wordninja>=2.0.0 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/30/15/abe4af50f4be92b60c25e43c1c64d08453b51e46c32981d80b3aebec0260/wordninja-2.0.0.tar.gz (541 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 541.6/541.6 kB 4.5 MB/s eta 0:00:00
  Preparing metadata (setup.py) ... done
Collecting pdfminer.six>=20231228 (from magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/77/32/89749ba23e5020e89fb584c1b39d7da6d7c56a9048307de8a88eec79e2d3/pdfminer_six-20250416-py3-none-any.whl (5.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.6/5.6 MB 4.5 MB/s eta 0:00:00
Collecting joblib>=1.2.0 (from scikit-learn>=1.0.2->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/91/29/df4b9b42f2be0b623cbd5e2140cafcaa2bef0759a00b7b70104dcfe2fb51/joblib-1.4.2-py3-none-any.whl (301 kB)
Collecting threadpoolctl>=3.1.0 (from scikit-learn>=1.0.2->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/32/d5/f9a850d79b0851d1d4ef6456097579a9005b31fea68726a4ae5f2d82ddd9/threadpoolctl-3.6.0-py3-none-any.whl (18 kB)
Collecting urllib3!=2.2.0,<3,>=1.25.4 (from botocore<1.38.0,>=1.37.35->boto3>=1.28.43->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/6b/11/cc635220681e93a0183390e26485430ca2c7b5f9d33b15c74c2861cb8091/urllib3-2.4.0-py3-none-any.whl (128 kB)
Collecting cffi>=1.12 (from cryptography>=36.0.0->pdfminer.six==20231228->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/8b/f1/672d303ddf17c24fc83afd712316fda78dc6fce1cd53011b839483e1ecc8/cffi-1.17.1-cp313-cp313-macosx_11_0_arm64.whl (178 kB)
Collecting idna<4,>=2.5 (from requests>=2.23.0->doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/76/c6/c88e154df9c4e1a2a66ccf0005a88dfb2650c1dffb6f5ce603dfbd452ce3/idna-3.10-py3-none-any.whl (70 kB)
Collecting certifi>=2017.4.17 (from requests>=2.23.0->doclayout-yolo==0.0.2b1->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/38/fc/bce832fd4fd99766c04d1ee0eead6b0ec6486fb100ae5e74c1d91292b982/certifi-2025.1.31-py3-none-any.whl (166 kB)
Collecting colorlog (from robust-downloader>=0.0.2->fast-langdetect<0.3.0,>=0.2.3->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/e3/51/9b208e85196941db2f0654ad0357ca6388ab3ed67efdbfc799f35d1f83aa/colorlog-6.9.0-py3-none-any.whl (11 kB)
Collecting pycparser (from cffi>=1.12->cryptography>=36.0.0->pdfminer.six==20231228->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/13/a3/a812df4e2dd5696d1f351d58b8fe16a405b234ad2886a0dab9183fb78109/pycparser-2.22-py3-none-any.whl (117 kB)
Collecting six>=1.5 (from python-dateutil>=2.7->matplotlib<4,>=3.10->magic-pdf[full])
  Downloading https://mirrors.aliyun.com/pypi/packages/b7/ce/149a00dd41f10bc29e5921b496af8b574d8413afcd5e30dfa0ed46c2cc5e/six-1.17.0-py2.py3-none-any.whl (11 kB)
Building wheels for collected packages: wordninja
  Building wheel for wordninja (setup.py) ... done
  Created wheel for wordninja: filename=wordninja-2.0.0-py3-none-any.whl size=541551 sha256=b158de314f0b7e9e477e801d35716aa5583744dec4c93d71ea3e08340bacba58
  Stored in directory: /private/var/folders/qq/h6nmcjm114j06f05fgv203hh0000gn/T/pip-ephem-wheel-cache-mhlpvq2f/wheels/42/a3/d0/2bd47f82f5dcd5efd2d9b43b7f29e8049d75e53cf3448d1352
Successfully built wordninja
Installing collected packages: wordninja, fasttext-predict, Brotli, urllib3, tqdm, threadpoolctl, six, PyMuPDF, pycparser, numpy, loguru, joblib, jmespath, idna, colorlog, click, charset-normalizer, certifi, scipy, requests, python-dateutil, cffi, scikit-learn, robust-downloader, cryptography, botocore, s3transfer, pdfminer.six, fast-langdetect, boto3, magic-pdf
Successfully installed Brotli-1.1.0 PyMuPDF-1.25.5 boto3-1.37.35 botocore-1.37.35 certifi-2025.1.31 cffi-1.17.1 charset-normalizer-3.4.1 click-8.1.8 colorlog-6.9.0 cryptography-44.0.2 fast-langdetect-0.3.2 fasttext-predict-0.9.2.4 idna-3.10 jmespath-1.0.1 joblib-1.4.2 loguru-0.7.3 magic-pdf-0.6.1 numpy-2.2.4 pdfminer.six-20250416 pycparser-2.22 python-dateutil-2.9.0.post0 requests-2.32.3 robust-downloader-0.0.2 s3transfer-0.11.4 scikit-learn-1.6.1 scipy-1.15.2 six-1.17.0 threadpoolctl-3.6.0 tqdm-4.67.1 urllib3-2.4.0 wordninja-2.0.0

MinerU__826.md:127-143
The following NEW packages will be INSTALLED:

  bzip2              pkgs/main/win-64::bzip2-1.0.8-h2bbff1b_6
  ca-certificates    pkgs/main/win-64::ca-certificates-2024.9.24-haa95532_0
  libffi             pkgs/main/win-64::libffi-3.4.4-hd77b12b_1
  openssl            pkgs/main/win-64::openssl-3.0.15-h827c3e9_0
  pip                pkgs/main/win-64::pip-24.2-py310haa95532_0
  python             pkgs/main/win-64::python-3.10.15-h4607a30_1
  setuptools         pkgs/main/win-64::setuptools-75.1.0-py310haa95532_0
  sqlite             pkgs/main/win-64::sqlite-3.45.3-h2bbff1b_0
  tk                 pkgs/main/win-64::tk-8.6.14-h0416ee5_0
  tzdata             pkgs/main/noarch::tzdata-2024b-h04d1e81_0
  vc                 pkgs/main/win-64::vc-14.40-h2eaa2aa_1
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.40.33807-h98bb1dd_1
  wheel              pkgs/main/win-64::wheel-0.44.0-py310haa95532_0
  xz                 pkgs/main/win-64::xz-5.4.6-h8cc25b3_1
  zlib               pkgs/main/win-64::zlib-1.2.13-h8cc25b3_1

MinerU__826.md:165-194
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple, https://wheels.myhloli.com
Requirement already satisfied: magic-pdf[full] in c:\users\maple\anaconda3\lib\site-packages (0.6.1)
Collecting magic-pdf[full]
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/00/5b/5157586376edf6bed6dd0f234423f89ecb01ce10adc6cc608e2e1a935280/magic_pdf-0.8.1-py3-none-any.whl (1.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 1.7 MB/s eta 0:00:00
Requirement already satisfied: boto3>=1.28.43 in c:\users\maple\anaconda3\lib\site-packages (from magic-pdf[full]) (1.35.52)
Requirement already satisfied: Brotli>=1.1.0 in c:\users\maple\anaconda3\lib\site-packages (from magic-pdf[full]) (1.1.0)
Requirement already satisfied: click>=8.1.7 in c:\users\maple\anaconda3\lib\site-packages (from magic-pdf[full]) (8.1.7)
Collecting fast-langdetect==0.2.0 (from magic-pdf[full])
  Using cached https://pypi.tuna.tsinghua.edu.cn/packages/d0/99/9cb2230dbdc5697b7d6cce86eec3397a80a2c877c400059fb49a79c48546/fast_langdetect-0.2.0-py3-none-any.whl (6.4 kB)
Requirement already satisfied: loguru>=0.6.0 in c:\users\maple\anaconda3\lib\site-packages (from magic-pdf[full]) (0.7.2)
Requirement already satisfied: numpy<2.0.0,>=1.21.6 in c:\users\maple\anaconda3\lib\site-packages (from magic-pdf[full]) (1.26.4)
Collecting pdfminer.six==20231228 (from magic-pdf[full])
  Using cached https://pypi.tuna.tsinghua.edu.cn/packages/eb/9c/e46fe7502b32d7db6af6e36a9105abb93301fa1ec475b5ddcba8b35ae23a/pdfminer.six-20231228-py3-none-any.whl (5.6 MB)
Collecting pydantic<2.8.0,>=2.7.2 (from magic-pdf[full])
  Using cached https://pypi.tuna.tsinghua.edu.cn/packages/17/ba/1b65c9cbc49e0c7cd1be086c63209e9ad883c2a409be4746c21db4263f41/pydantic-2.7.4-py3-none-any.whl (409 kB)
Requirement already satisfied: PyMuPDF>=1.24.9 in c:\users\maple\anaconda3\lib\site-packages (from magic-pdf[full]) (1.24.13)
Requirement already satisfied: scikit-learn>=1.0.2 in c:\users\maple\anaconda3\lib\site-packages (from magic-pdf[full]) (1.4.2)
Requirement already satisfied: wordninja>=2.0.0 in c:\users\maple\anaconda3\lib\site-packages (from magic-pdf[full]) (2.0.0)
Collecting unimernet==0.1.6 (from magic-pdf[full])
  Using cached https://pypi.tuna.tsinghua.edu.cn/packages/0c/1d/5847f9237c695efae828fea23b4db8bc51419804f116c9156ab0f557377a/unimernet-0.1.6-py3-none-any.whl (2.2 MB)
Collecting ultralytics (from magic-pdf[full])
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/e7/5c/9168bef8044e5119e0314e903622b1f195aa30f3b5fab9146e3684a4222a/ultralytics-8.3.26-py3-none-any.whl (878 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 879.0/879.0 kB 4.3 MB/s eta 0:00:00
Collecting paddleocr==2.7.3 (from magic-pdf[full])
  Using cached https://pypi.tuna.tsinghua.edu.cn/packages/f2/55/0469ebca1d9c581a3fa740621afe96461a0ef450e489e10e278cc17a19ef/paddleocr-2.7.3-py3-none-any.whl (780 kB)
Collecting pypandoc (from magic-pdf[full])
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/ff/bd/cf1dd70b95f3366f3c457c5259ed8f032122210441407b6ed281d7fcbb8c/pypandoc-1.14-py3-none-any.whl (21 kB)
Collecting struct-eqtable==0.1.0 (from magic-pdf[full])
  Using cached https://pypi.tuna.tsinghua.edu.cn/packages/a4/25/d1e91b2ad2727c9ecb332607729a03c2f0f345afd2547f4100e543330f0e/struct_eqtable-0.1.0-py3-none-any.whl (8.5 kB)

MinerU__826.md:202-227
Requirement already satisfied: fast-langdetect>=0.2.1 in c:\users\maple\anaconda3\lib\site-packages (from magic-pdf[full]) (0.2.2)
Requirement already satisfied: pdfminer.six>=20231228 in c:\users\maple\anaconda3\lib\site-packages (from magic-pdf[full]) (20240706)
Requirement already satisfied: botocore<1.36.0,>=1.35.52 in c:\users\maple\anaconda3\lib\site-packages (from boto3>=1.28.43->magic-pdf[full]) (1.35.52)
Requirement already satisfied: jmespath<2.0.0,>=0.7.1 in c:\users\maple\anaconda3\lib\site-packages (from boto3>=1.28.43->magic-pdf[full]) (1.0.1)
Requirement already satisfied: s3transfer<0.11.0,>=0.10.0 in c:\users\maple\anaconda3\lib\site-packages (from boto3>=1.28.43->magic-pdf[full]) (0.10.3)
Requirement already satisfied: colorama in c:\users\maple\anaconda3\lib\site-packages (from click>=8.1.7->magic-pdf[full]) (0.4.6)
Requirement already satisfied: fasttext-wheel>=0.9.2 in c:\users\maple\anaconda3\lib\site-packages (from fast-langdetect>=0.2.1->magic-pdf[full]) (0.9.2)
Requirement already satisfied: robust-downloader>=0.0.2 in c:\users\maple\anaconda3\lib\site-packages (from fast-langdetect>=0.2.1->magic-pdf[full]) (0.0.2)
Requirement already satisfied: requests>=2.32.3 in c:\users\maple\anaconda3\lib\site-packages (from fast-langdetect>=0.2.1->magic-pdf[full]) (2.32.3)
Requirement already satisfied: win32-setctime>=1.0.0 in c:\users\maple\anaconda3\lib\site-packages (from loguru>=0.6.0->magic-pdf[full]) (1.1.0)
Requirement already satisfied: charset-normalizer>=2.0.0 in c:\users\maple\anaconda3\lib\site-packages (from pdfminer.six>=20231228->magic-pdf[full]) (2.0.4)
Requirement already satisfied: cryptography>=36.0.0 in c:\users\maple\anaconda3\lib\site-packages (from pdfminer.six>=20231228->magic-pdf[full]) (42.0.5)
Requirement already satisfied: scipy>=1.6.0 in c:\users\maple\anaconda3\lib\site-packages (from scikit-learn>=1.0.2->magic-pdf[full]) (1.13.1)
Requirement already satisfied: joblib>=1.2.0 in c:\users\maple\anaconda3\lib\site-packages (from scikit-learn>=1.0.2->magic-pdf[full]) (1.4.2)
Requirement already satisfied: threadpoolctl>=2.0.0 in c:\users\maple\anaconda3\lib\site-packages (from scikit-learn>=1.0.2->magic-pdf[full]) (2.2.0)
Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in c:\users\maple\anaconda3\lib\site-packages (from botocore<1.36.0,>=1.35.52->boto3>=1.28.43->magic-pdf[full]) (2.9.0.post0)
Requirement already satisfied: urllib3!=2.2.0,<3,>=1.25.4 in c:\users\maple\anaconda3\lib\site-packages (from botocore<1.36.0,>=1.35.52->boto3>=1.28.43->magic-pdf[full]) (2.2.2)
Requirement already satisfied: cffi>=1.12 in c:\users\maple\anaconda3\lib\site-packages (from cryptography>=36.0.0->pdfminer.six>=20231228->magic-pdf[full]) (1.16.0)
Requirement already satisfied: pybind11>=2.2 in c:\users\maple\anaconda3\lib\site-packages (from fasttext-wheel>=0.9.2->fast-langdetect>=0.2.1->magic-pdf[full]) (2.13.6)
Requirement already satisfied: setuptools>=0.7.0 in c:\users\maple\anaconda3\lib\site-packages (from fasttext-wheel>=0.9.2->fast-langdetect>=0.2.1->magic-pdf[full]) (69.5.1)
Requirement already satisfied: idna<4,>=2.5 in c:\users\maple\anaconda3\lib\site-packages (from requests>=2.32.3->fast-langdetect>=0.2.1->magic-pdf[full]) (3.7)
Requirement already satisfied: certifi>=2017.4.17 in c:\users\maple\anaconda3\lib\site-packages (from requests>=2.32.3->fast-langdetect>=0.2.1->magic-pdf[full]) (2024.6.2)
Requirement already satisfied: tqdm in c:\users\maple\anaconda3\lib\site-packages (from robust-downloader>=0.0.2->fast-langdetect>=0.2.1->magic-pdf[full]) (4.66.4)
Requirement already satisfied: colorlog in c:\users\maple\anaconda3\lib\site-packages (from robust-downloader>=0.0.2->fast-langdetect>=0.2.1->magic-pdf[full]) (6.9.0)
Requirement already satisfied: pycparser in c:\users\maple\anaconda3\lib\site-packages (from cffi>=1.12->cryptography>=36.0.0->pdfminer.six>=20231228->magic-pdf[full]) (2.21)
Requirement already satisfied: six>=1.5 in c:\users\maple\anaconda3\lib\site-packages (from python-dateutil<3.0.0,>=2.1->botocore<1.36.0,>=1.35.52->boto3>=1.28.43->magic-pdf[full]) (1.16.0)

MinerU__826.md:288-329
Requirement already satisfied: Pillow>=7.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from detectron2==0.6) (11.0.0)
Requirement already satisfied: matplotlib in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from detectron2==0.6) (3.9.0)
Requirement already satisfied: pycocotools>=2.0.2 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from detectron2==0.6) (2.0.8)
Requirement already satisfied: termcolor>=1.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from detectron2==0.6) (2.5.0)
Requirement already satisfied: yacs>=0.1.8 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from detectron2==0.6) (0.1.8)
Requirement already satisfied: tabulate in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from detectron2==0.6) (0.9.0)
Requirement already satisfied: cloudpickle in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from detectron2==0.6) (3.1.0)
Requirement already satisfied: tqdm>4.29.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from detectron2==0.6) (4.67.1)
Requirement already satisfied: tensorboard in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from detectron2==0.6) (2.18.0)
Requirement already satisfied: fvcore<0.1.6,>=0.1.5 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from detectron2==0.6) (0.1.5.post20221221)
Requirement already satisfied: iopath<0.1.10,>=0.1.7 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from detectron2==0.6) (0.1.9)
Requirement already satisfied: omegaconf<2.4,>=2.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from detectron2==0.6) (2.3.0)
Requirement already satisfied: hydra-core>=1.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from detectron2==0.6) (1.3.2)
Requirement already satisfied: black in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from detectron2==0.6) (24.10.0)
Requirement already satisfied: packaging in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from detectron2==0.6) (24.2)
Requirement already satisfied: numpy in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from fvcore<0.1.6,>=0.1.5->detectron2==0.6) (1.26.4)
Requirement already satisfied: pyyaml>=5.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from fvcore<0.1.6,>=0.1.5->detectron2==0.6) (6.0.2)
Requirement already satisfied: antlr4-python3-runtime==4.9.* in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from hydra-core>=1.1->detectron2==0.6) (4.9.3)
Requirement already satisfied: portalocker in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from iopath<0.1.10,>=0.1.7->detectron2==0.6) (3.0.0)
Requirement already satisfied: contourpy>=1.0.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from matplotlib->detectron2==0.6) (1.3.1)
Requirement already satisfied: cycler>=0.10 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from matplotlib->detectron2==0.6) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from matplotlib->detectron2==0.6) (4.55.3)
Requirement already satisfied: kiwisolver>=1.3.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from matplotlib->detectron2==0.6) (1.4.7)
Requirement already satisfied: pyparsing>=2.3.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from matplotlib->detectron2==0.6) (3.2.0)
Requirement already satisfied: python-dateutil>=2.7 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from matplotlib->detectron2==0.6) (2.9.0.post0)
Requirement already satisfied: colorama in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from tqdm>4.29.0->detectron2==0.6) (0.4.6)
Requirement already satisfied: click>=8.0.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from black->detectron2==0.6) (8.1.7)
Requirement already satisfied: mypy-extensions>=0.4.3 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from black->detectron2==0.6) (1.0.0)
Requirement already satisfied: pathspec>=0.9.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from black->detectron2==0.6) (0.12.1)
Requirement already satisfied: platformdirs>=2 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from black->detectron2==0.6) (4.3.6)
Requirement already satisfied: tomli>=1.1.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from black->detectron2==0.6) (2.2.1)
Requirement already satisfied: typing-extensions>=4.0.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from black->detectron2==0.6) (4.12.2)
Requirement already satisfied: absl-py>=0.4 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from tensorboard->detectron2==0.6) (2.1.0)
Requirement already satisfied: grpcio>=1.48.2 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from tensorboard->detectron2==0.6) (1.68.1)
Requirement already satisfied: markdown>=2.6.8 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from tensorboard->detectron2==0.6) (3.7)
Requirement already satisfied: protobuf!=4.24.0,>=3.19.6 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from tensorboard->detectron2==0.6) (3.20.2)
Requirement already satisfied: setuptools>=41.0.0 in d:\ruanjian2\anaconda\envs\mineru\lib\site-packages (from tensorboard->detectron2==0.6) (75.1.0)
Requirement already satisfied: six>1.9 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from tensorboard->detectron2==0.6) (1.17.0)
Requirement already satisfied: tensorboard-data-server<0.8.0,>=0.7.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from tensorboard->detectron2==0.6) (0.7.2)
Requirement already satisfied: werkzeug>=1.0.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from tensorboard->detectron2==0.6) (3.1.3)
Requirement already satisfied: MarkupSafe>=2.1.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from werkzeug>=1.0.1->tensorboard->detectron2==0.6) (3.0.2)
Requirement already satisfied: pywin32>=226 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from portalocker->iopath<0.1.10,>=0.1.7->detectron2==0.6) (308)

MinerU__826.md:334-498
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple, https://wheels.myhloli.com
Requirement already satisfied: magic-pdf==0.8.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from magic-pdf[full]==0.8.1) (0.8.1)
Requirement already satisfied: boto3>=1.28.43 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (1.35.83)
Requirement already satisfied: Brotli>=1.1.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (1.1.0)
Requirement already satisfied: click>=8.1.7 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (8.1.7)
Requirement already satisfied: fast-langdetect==0.2.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (0.2.0)
Requirement already satisfied: loguru>=0.6.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (0.7.3)
Requirement already satisfied: numpy<2.0.0,>=1.21.6 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (1.26.4)
Requirement already satisfied: pdfminer.six==20231228 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (20231228)
Requirement already satisfied: pydantic<2.8.0,>=2.7.2 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (2.7.4)
Requirement already satisfied: PyMuPDF>=1.24.9 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (1.25.1)
Requirement already satisfied: scikit-learn>=1.0.2 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (1.6.0)
Requirement already satisfied: wordninja>=2.0.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (2.0.0)
Requirement already satisfied: unimernet==0.1.6 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from magic-pdf[full]==0.8.1) (0.1.6)
Requirement already satisfied: ultralytics in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from magic-pdf[full]==0.8.1) (8.3.51)
Requirement already satisfied: paddleocr==2.7.3 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from magic-pdf[full]==0.8.1) (2.7.3)
Requirement already satisfied: pypandoc in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from magic-pdf[full]==0.8.1) (1.14)
Requirement already satisfied: struct-eqtable==0.1.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from magic-pdf[full]==0.8.1) (0.1.0)
Requirement already satisfied: detectron2 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from magic-pdf[full]==0.8.1) (0.6)
Requirement already satisfied: matplotlib<=3.9.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from magic-pdf[full]==0.8.1) (3.9.0)
Requirement already satisfied: paddlepaddle==2.6.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from magic-pdf[full]==0.8.1) (2.6.1)
Requirement already satisfied: fasttext-wheel>=0.9.2 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from fast-langdetect==0.2.0->magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (0.9.2)
Requirement already satisfied: robust-downloader>=0.0.2 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from fast-langdetect==0.2.0->magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (0.0.2)
Requirement already satisfied: langdetect>=1.0.9 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from fast-langdetect==0.2.0->magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (1.0.9)
Requirement already satisfied: shapely in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddleocr==2.7.3->magic-pdf[full]==0.8.1) (2.0.6)
Requirement already satisfied: scikit-image in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddleocr==2.7.3->magic-pdf[full]==0.8.1) (0.25.0)
Requirement already satisfied: imgaug in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddleocr==2.7.3->magic-pdf[full]==0.8.1) (0.4.0)
Requirement already satisfied: pyclipper in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddleocr==2.7.3->magic-pdf[full]==0.8.1) (1.3.0.post6)
Requirement already satisfied: lmdb in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddleocr==2.7.3->magic-pdf[full]==0.8.1) (1.5.1)
Requirement already satisfied: tqdm in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddleocr==2.7.3->magic-pdf[full]==0.8.1) (4.67.1)
Requirement already satisfied: visualdl in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddleocr==2.7.3->magic-pdf[full]==0.8.1) (2.5.3)
Requirement already satisfied: rapidfuzz in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddleocr==2.7.3->magic-pdf[full]==0.8.1) (3.11.0)
Requirement already satisfied: opencv-python<=4.6.0.66 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddleocr==2.7.3->magic-pdf[full]==0.8.1) (4.6.0.66)
Requirement already satisfied: opencv-contrib-python<=4.6.0.66 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddleocr==2.7.3->magic-pdf[full]==0.8.1) (4.6.0.66)
Requirement already satisfied: cython in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddleocr==2.7.3->magic-pdf[full]==0.8.1) (3.0.11)
Requirement already satisfied: lxml in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddleocr==2.7.3->magic-pdf[full]==0.8.1) (5.3.0)
Requirement already satisfied: premailer in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddleocr==2.7.3->magic-pdf[full]==0.8.1) (3.10.0)
Requirement already satisfied: openpyxl in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddleocr==2.7.3->magic-pdf[full]==0.8.1) (3.1.5)
Requirement already satisfied: attrdict in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddleocr==2.7.3->magic-pdf[full]==0.8.1) (2.0.1)
Requirement already satisfied: Pillow>=10.0.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddleocr==2.7.3->magic-pdf[full]==0.8.1) (11.0.0)
Requirement already satisfied: pyyaml in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddleocr==2.7.3->magic-pdf[full]==0.8.1) (6.0.2)
Requirement already satisfied: python-docx in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddleocr==2.7.3->magic-pdf[full]==0.8.1) (1.1.2)
Requirement already satisfied: beautifulsoup4 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddleocr==2.7.3->magic-pdf[full]==0.8.1) (4.12.3)
Requirement already satisfied: fonttools>=4.24.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddleocr==2.7.3->magic-pdf[full]==0.8.1) (4.55.3)
Requirement already satisfied: fire>=0.3.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddleocr==2.7.3->magic-pdf[full]==0.8.1) (0.7.0)
Requirement already satisfied: pdf2docx in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddleocr==2.7.3->magic-pdf[full]==0.8.1) (0.5.8)
Requirement already satisfied: httpx in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddlepaddle==2.6.1->magic-pdf[full]==0.8.1) (0.28.1)
Requirement already satisfied: decorator in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddlepaddle==2.6.1->magic-pdf[full]==0.8.1) (5.1.1)
Requirement already satisfied: astor in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddlepaddle==2.6.1->magic-pdf[full]==0.8.1) (0.8.1)
Requirement already satisfied: opt-einsum==3.3.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddlepaddle==2.6.1->magic-pdf[full]==0.8.1) (3.3.0)
Requirement already satisfied: protobuf<=3.20.2,>=3.1.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from paddlepaddle==2.6.1->magic-pdf[full]==0.8.1) (3.20.2)
Requirement already satisfied: charset-normalizer>=2.0.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from pdfminer.six==20231228->magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (3.4.0)
Requirement already satisfied: cryptography>=36.0.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from pdfminer.six==20231228->magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (44.0.0)
Requirement already satisfied: torch in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from struct-eqtable==0.1.0->magic-pdf[full]==0.8.1) (2.3.1)
Requirement already satisfied: transformers in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from struct-eqtable==0.1.0->magic-pdf[full]==0.8.1) (4.40.0)
Requirement already satisfied: albumentations<2.0.0,>=1.4.4 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from unimernet==0.1.6->magic-pdf[full]==0.8.1) (1.4.21)
Requirement already satisfied: eva-decord<0.7.0,>=0.6.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from unimernet==0.1.6->magic-pdf[full]==0.8.1) (0.6.1)
Requirement already satisfied: evaluate<0.5.0,>=0.4.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from unimernet==0.1.6->magic-pdf[full]==0.8.1) (0.4.3)
Requirement already satisfied: fairscale<0.5.0,>=0.4.13 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from unimernet==0.1.6->magic-pdf[full]==0.8.1) (0.4.13)
Requirement already satisfied: ftfy<7.0.0,>=6.2.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from unimernet==0.1.6->magic-pdf[full]==0.8.1) (6.3.1)
Requirement already satisfied: iopath<0.2.0,>=0.1.9 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from unimernet==0.1.6->magic-pdf[full]==0.8.1) (0.1.9)
Requirement already satisfied: omegaconf<3.0.0,>=2.3.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from unimernet==0.1.6->magic-pdf[full]==0.8.1) (2.3.0)
Requirement already satisfied: timm<0.10.0,>=0.9.16 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from unimernet==0.1.6->magic-pdf[full]==0.8.1) (0.9.16)
Requirement already satisfied: torchtext<=0.18.0,>=0.17.2 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from unimernet==0.1.6->magic-pdf[full]==0.8.1) (0.18.0)
Requirement already satisfied: torchvision<=0.18.1,>=0.17.2 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from unimernet==0.1.6->magic-pdf[full]==0.8.1) (0.18.1)
Requirement already satisfied: wand<0.7.0,>=0.6.13 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from unimernet==0.1.6->magic-pdf[full]==0.8.1) (0.6.13)
Requirement already satisfied: webdataset<0.3.0,>=0.2.86 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from unimernet==0.1.6->magic-pdf[full]==0.8.1) (0.2.100)
Requirement already satisfied: filelock in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from transformers->struct-eqtable==0.1.0->magic-pdf[full]==0.8.1) (3.16.1)
Requirement already satisfied: huggingface-hub<1.0,>=0.19.3 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from transformers->struct-eqtable==0.1.0->magic-pdf[full]==0.8.1) (0.27.0)
Requirement already satisfied: packaging>=20.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from transformers->struct-eqtable==0.1.0->magic-pdf[full]==0.8.1) (24.2)
Requirement already satisfied: regex!=2019.12.17 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from transformers->struct-eqtable==0.1.0->magic-pdf[full]==0.8.1) (2024.11.6)
Requirement already satisfied: requests in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from transformers->struct-eqtable==0.1.0->magic-pdf[full]==0.8.1) (2.32.3)
Requirement already satisfied: tokenizers<0.20,>=0.19 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from transformers->struct-eqtable==0.1.0->magic-pdf[full]==0.8.1) (0.19.1)
Requirement already satisfied: safetensors>=0.4.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from transformers->struct-eqtable==0.1.0->magic-pdf[full]==0.8.1) (0.4.5)
Requirement already satisfied: botocore<1.36.0,>=1.35.83 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from boto3>=1.28.43->magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (1.35.83)
Requirement already satisfied: jmespath<2.0.0,>=0.7.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from boto3>=1.28.43->magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (1.0.1)
Requirement already satisfied: s3transfer<0.11.0,>=0.10.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from boto3>=1.28.43->magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (0.10.4)
Requirement already satisfied: colorama in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from click>=8.1.7->magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (0.4.6)
Requirement already satisfied: win32-setctime>=1.0.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from loguru>=0.6.0->magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (1.2.0)
Requirement already satisfied: contourpy>=1.0.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from matplotlib<=3.9.0->magic-pdf[full]==0.8.1) (1.3.1)
Requirement already satisfied: cycler>=0.10 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from matplotlib<=3.9.0->magic-pdf[full]==0.8.1) (0.12.1)
Requirement already satisfied: kiwisolver>=1.3.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from matplotlib<=3.9.0->magic-pdf[full]==0.8.1) (1.4.7)
Requirement already satisfied: pyparsing>=2.3.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from matplotlib<=3.9.0->magic-pdf[full]==0.8.1) (3.2.0)
Requirement already satisfied: python-dateutil>=2.7 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from matplotlib<=3.9.0->magic-pdf[full]==0.8.1) (2.9.0.post0)
Requirement already satisfied: annotated-types>=0.4.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from pydantic<2.8.0,>=2.7.2->magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (0.7.0)
Requirement already satisfied: pydantic-core==2.18.4 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from pydantic<2.8.0,>=2.7.2->magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (2.18.4)
Requirement already satisfied: typing-extensions>=4.6.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from pydantic<2.8.0,>=2.7.2->magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (4.12.2)
Requirement already satisfied: scipy>=1.6.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from scikit-learn>=1.0.2->magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (1.14.1)
Requirement already satisfied: joblib>=1.2.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from scikit-learn>=1.0.2->magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (1.4.2)
Requirement already satisfied: threadpoolctl>=3.1.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from scikit-learn>=1.0.2->magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (3.5.0)
Requirement already satisfied: pycocotools>=2.0.2 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from detectron2->magic-pdf[full]==0.8.1) (2.0.8)
Requirement already satisfied: termcolor>=1.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from detectron2->magic-pdf[full]==0.8.1) (2.5.0)
Requirement already satisfied: yacs>=0.1.8 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from detectron2->magic-pdf[full]==0.8.1) (0.1.8)
Requirement already satisfied: tabulate in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from detectron2->magic-pdf[full]==0.8.1) (0.9.0)
Requirement already satisfied: cloudpickle in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from detectron2->magic-pdf[full]==0.8.1) (3.1.0)
Requirement already satisfied: tensorboard in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from detectron2->magic-pdf[full]==0.8.1) (2.18.0)
Requirement already satisfied: fvcore<0.1.6,>=0.1.5 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from detectron2->magic-pdf[full]==0.8.1) (0.1.5.post20221221)
Requirement already satisfied: hydra-core>=1.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from detectron2->magic-pdf[full]==0.8.1) (1.3.2)
Requirement already satisfied: black in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from detectron2->magic-pdf[full]==0.8.1) (24.10.0)
Requirement already satisfied: psutil in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from ultralytics->magic-pdf[full]==0.8.1) (6.1.0)
Requirement already satisfied: py-cpuinfo in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from ultralytics->magic-pdf[full]==0.8.1) (9.0.0)
Requirement already satisfied: pandas>=1.1.4 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from ultralytics->magic-pdf[full]==0.8.1) (2.2.3)
Requirement already satisfied: seaborn>=0.11.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from ultralytics->magic-pdf[full]==0.8.1) (0.13.2)
Requirement already satisfied: ultralytics-thop>=2.0.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from ultralytics->magic-pdf[full]==0.8.1) (2.0.13)
Requirement already satisfied: albucore==0.0.20 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from albumentations<2.0.0,>=1.4.4->unimernet==0.1.6->magic-pdf[full]==0.8.1) (0.0.20)
Requirement already satisfied: eval-type-backport in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from albumentations<2.0.0,>=1.4.4->unimernet==0.1.6->magic-pdf[full]==0.8.1) (0.2.0)
Requirement already satisfied: opencv-python-headless>=4.9.0.80 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from albumentations<2.0.0,>=1.4.4->unimernet==0.1.6->magic-pdf[full]==0.8.1) (4.10.0.84)
Requirement already satisfied: stringzilla>=3.10.4 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from albucore==0.0.20->albumentations<2.0.0,>=1.4.4->unimernet==0.1.6->magic-pdf[full]==0.8.1) (3.11.1)
Requirement already satisfied: simsimd>=5.9.2 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from albucore==0.0.20->albumentations<2.0.0,>=1.4.4->unimernet==0.1.6->magic-pdf[full]==0.8.1) (6.2.1)
Requirement already satisfied: urllib3!=2.2.0,<3,>=1.25.4 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from botocore<1.36.0,>=1.35.83->boto3>=1.28.43->magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (2.2.3)
Requirement already satisfied: cffi>=1.12 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from cryptography>=36.0.0->pdfminer.six==20231228->magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (1.17.1)
Requirement already satisfied: datasets>=2.0.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from evaluate<0.5.0,>=0.4.1->unimernet==0.1.6->magic-pdf[full]==0.8.1) (3.2.0)
Requirement already satisfied: dill in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from evaluate<0.5.0,>=0.4.1->unimernet==0.1.6->magic-pdf[full]==0.8.1) (0.3.8)
Requirement already satisfied: xxhash in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from evaluate<0.5.0,>=0.4.1->unimernet==0.1.6->magic-pdf[full]==0.8.1) (3.5.0)
Requirement already satisfied: multiprocess in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from evaluate<0.5.0,>=0.4.1->unimernet==0.1.6->magic-pdf[full]==0.8.1) (0.70.16)
Requirement already satisfied: fsspec>=2021.05.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from fsspec[http]>=2021.05.0->evaluate<0.5.0,>=0.4.1->unimernet==0.1.6->magic-pdf[full]==0.8.1) (2024.9.0)
Requirement already satisfied: pybind11>=2.2 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from fasttext-wheel>=0.9.2->fast-langdetect==0.2.0->magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (2.13.6)
Requirement already satisfied: setuptools>=0.7.0 in d:\ruanjian2\anaconda\envs\mineru\lib\site-packages (from fasttext-wheel>=0.9.2->fast-langdetect==0.2.0->magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (75.1.0)
Requirement already satisfied: wcwidth in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from ftfy<7.0.0,>=6.2.0->unimernet==0.1.6->magic-pdf[full]==0.8.1) (0.2.13)
Requirement already satisfied: antlr4-python3-runtime==4.9.* in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from hydra-core>=1.1->detectron2->magic-pdf[full]==0.8.1) (4.9.3)
Requirement already satisfied: portalocker in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from iopath<0.2.0,>=0.1.9->unimernet==0.1.6->magic-pdf[full]==0.8.1) (3.0.0)
Requirement already satisfied: six in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from langdetect>=1.0.9->fast-langdetect==0.2.0->magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (1.17.0)
Requirement already satisfied: pytz>=2020.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from pandas>=1.1.4->ultralytics->magic-pdf[full]==0.8.1) (2024.2)
Requirement already satisfied: tzdata>=2022.7 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from pandas>=1.1.4->ultralytics->magic-pdf[full]==0.8.1) (2024.2)
Requirement already satisfied: idna<4,>=2.5 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from requests->transformers->struct-eqtable==0.1.0->magic-pdf[full]==0.8.1) (3.10)
Requirement already satisfied: certifi>=2017.4.17 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from requests->transformers->struct-eqtable==0.1.0->magic-pdf[full]==0.8.1) (2024.12.14)
Requirement already satisfied: colorlog in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from robust-downloader>=0.0.2->fast-langdetect==0.2.0->magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (6.9.0)
Requirement already satisfied: sympy in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from torch->struct-eqtable==0.1.0->magic-pdf[full]==0.8.1) (1.13.3)
Requirement already satisfied: networkx in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from torch->struct-eqtable==0.1.0->magic-pdf[full]==0.8.1) (3.4.2)
Requirement already satisfied: jinja2 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from torch->struct-eqtable==0.1.0->magic-pdf[full]==0.8.1) (3.1.4)
Requirement already satisfied: mkl<=2021.4.0,>=2021.1.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from torch->struct-eqtable==0.1.0->magic-pdf[full]==0.8.1) (2021.4.0)
Requirement already satisfied: braceexpand in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from webdataset<0.3.0,>=0.2.86->unimernet==0.1.6->magic-pdf[full]==0.8.1) (0.1.7)
Requirement already satisfied: soupsieve>1.2 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from beautifulsoup4->paddleocr==2.7.3->magic-pdf[full]==0.8.1) (2.6)
Requirement already satisfied: mypy-extensions>=0.4.3 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from black->detectron2->magic-pdf[full]==0.8.1) (1.0.0)
Requirement already satisfied: pathspec>=0.9.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from black->detectron2->magic-pdf[full]==0.8.1) (0.12.1)
Requirement already satisfied: platformdirs>=2 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from black->detectron2->magic-pdf[full]==0.8.1) (4.3.6)
Requirement already satisfied: tomli>=1.1.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from black->detectron2->magic-pdf[full]==0.8.1) (2.2.1)
Requirement already satisfied: anyio in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from httpx->paddlepaddle==2.6.1->magic-pdf[full]==0.8.1) (4.7.0)
Requirement already satisfied: httpcore==1.* in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from httpx->paddlepaddle==2.6.1->magic-pdf[full]==0.8.1) (1.0.7)
Requirement already satisfied: h11<0.15,>=0.13 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from httpcore==1.*->httpx->paddlepaddle==2.6.1->magic-pdf[full]==0.8.1) (0.14.0)
Requirement already satisfied: imageio in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from imgaug->paddleocr==2.7.3->magic-pdf[full]==0.8.1) (2.36.1)
Requirement already satisfied: tifffile>=2022.8.12 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from scikit-image->paddleocr==2.7.3->magic-pdf[full]==0.8.1) (2024.12.12)
Requirement already satisfied: lazy-loader>=0.4 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from scikit-image->paddleocr==2.7.3->magic-pdf[full]==0.8.1) (0.4)
Requirement already satisfied: et-xmlfile in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from openpyxl->paddleocr==2.7.3->magic-pdf[full]==0.8.1) (2.0.0)
Requirement already satisfied: cssselect in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from premailer->paddleocr==2.7.3->magic-pdf[full]==0.8.1) (1.2.0)
Requirement already satisfied: cssutils in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from premailer->paddleocr==2.7.3->magic-pdf[full]==0.8.1) (2.11.1)
Requirement already satisfied: cachetools in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from premailer->paddleocr==2.7.3->magic-pdf[full]==0.8.1) (5.5.0)
Requirement already satisfied: absl-py>=0.4 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from tensorboard->detectron2->magic-pdf[full]==0.8.1) (2.1.0)
Requirement already satisfied: grpcio>=1.48.2 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from tensorboard->detectron2->magic-pdf[full]==0.8.1) (1.68.1)
Requirement already satisfied: markdown>=2.6.8 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from tensorboard->detectron2->magic-pdf[full]==0.8.1) (3.7)
Requirement already satisfied: tensorboard-data-server<0.8.0,>=0.7.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from tensorboard->detectron2->magic-pdf[full]==0.8.1) (0.7.2)
Requirement already satisfied: werkzeug>=1.0.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from tensorboard->detectron2->magic-pdf[full]==0.8.1) (3.1.3)
Requirement already satisfied: bce-python-sdk in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from visualdl->paddleocr==2.7.3->magic-pdf[full]==0.8.1) (0.9.23)
Requirement already satisfied: flask>=1.1.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from visualdl->paddleocr==2.7.3->magic-pdf[full]==0.8.1) (3.1.0)
Requirement already satisfied: Flask-Babel>=3.0.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from visualdl->paddleocr==2.7.3->magic-pdf[full]==0.8.1) (4.0.0)
Requirement already satisfied: rarfile in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from visualdl->paddleocr==2.7.3->magic-pdf[full]==0.8.1) (4.2)
Requirement already satisfied: pycparser in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from cffi>=1.12->cryptography>=36.0.0->pdfminer.six==20231228->magic-pdf==0.8.1->magic-pdf[full]==0.8.1) (2.22)
Requirement already satisfied: pyarrow>=15.0.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from datasets>=2.0.0->evaluate<0.5.0,>=0.4.1->unimernet==0.1.6->magic-pdf[full]==0.8.1) (18.1.0)
Requirement already satisfied: aiohttp in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from datasets>=2.0.0->evaluate<0.5.0,>=0.4.1->unimernet==0.1.6->magic-pdf[full]==0.8.1) (3.11.10)
Requirement already satisfied: itsdangerous>=2.2 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from flask>=1.1.1->visualdl->paddleocr==2.7.3->magic-pdf[full]==0.8.1) (2.2.0)
Requirement already satisfied: blinker>=1.9 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from flask>=1.1.1->visualdl->paddleocr==2.7.3->magic-pdf[full]==0.8.1) (1.9.0)
Requirement already satisfied: Babel>=2.12 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from Flask-Babel>=3.0.0->visualdl->paddleocr==2.7.3->magic-pdf[full]==0.8.1) (2.16.0)
Requirement already satisfied: MarkupSafe>=2.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from jinja2->torch->struct-eqtable==0.1.0->magic-pdf[full]==0.8.1) (3.0.2)
Requirement already satisfied: intel-openmp==2021.* in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from mkl<=2021.4.0,>=2021.1.1->torch->struct-eqtable==0.1.0->magic-pdf[full]==0.8.1) (2021.4.0)
Requirement already satisfied: tbb==2021.* in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from mkl<=2021.4.0,>=2021.1.1->torch->struct-eqtable==0.1.0->magic-pdf[full]==0.8.1) (2021.13.1)

MinerU__826.md:500-513
Requirement already satisfied: sniffio>=1.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from anyio->httpx->paddlepaddle==2.6.1->magic-pdf[full]==0.8.1) (1.3.1)
Requirement already satisfied: pycryptodome>=3.8.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from bce-python-sdk->visualdl->paddleocr==2.7.3->magic-pdf[full]==0.8.1) (3.21.0)
Requirement already satisfied: future>=0.6.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from bce-python-sdk->visualdl->paddleocr==2.7.3->magic-pdf[full]==0.8.1) (1.0.0)
Requirement already satisfied: more-itertools in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from cssutils->premailer->paddleocr==2.7.3->magic-pdf[full]==0.8.1) (10.5.0)
Requirement already satisfied: pywin32>=226 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from portalocker->iopath<0.2.0,>=0.1.9->unimernet==0.1.6->magic-pdf[full]==0.8.1) (308)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from sympy->torch->struct-eqtable==0.1.0->magic-pdf[full]==0.8.1) (1.3.0)
Requirement already satisfied: aiohappyeyeballs>=2.3.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from aiohttp->datasets>=2.0.0->evaluate<0.5.0,>=0.4.1->unimernet==0.1.6->magic-pdf[full]==0.8.1) (2.4.4)
Requirement already satisfied: aiosignal>=1.1.2 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from aiohttp->datasets>=2.0.0->evaluate<0.5.0,>=0.4.1->unimernet==0.1.6->magic-pdf[full]==0.8.1) (1.3.2)
Requirement already satisfied: async-timeout<6.0,>=4.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from aiohttp->datasets>=2.0.0->evaluate<0.5.0,>=0.4.1->unimernet==0.1.6->magic-pdf[full]==0.8.1) (5.0.1)
Requirement already satisfied: attrs>=17.3.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from aiohttp->datasets>=2.0.0->evaluate<0.5.0,>=0.4.1->unimernet==0.1.6->magic-pdf[full]==0.8.1) (24.3.0)
Requirement already satisfied: frozenlist>=1.1.1 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from aiohttp->datasets>=2.0.0->evaluate<0.5.0,>=0.4.1->unimernet==0.1.6->magic-pdf[full]==0.8.1) (1.5.0)
Requirement already satisfied: multidict<7.0,>=4.5 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from aiohttp->datasets>=2.0.0->evaluate<0.5.0,>=0.4.1->unimernet==0.1.6->magic-pdf[full]==0.8.1) (6.1.0)
Requirement already satisfied: propcache>=0.2.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from aiohttp->datasets>=2.0.0->evaluate<0.5.0,>=0.4.1->unimernet==0.1.6->magic-pdf[full]==0.8.1) (0.2.1)
Requirement already satisfied: yarl<2.0,>=1.17.0 in c:\users\lenovo\appdata\roaming\python\python310\site-packages (from aiohttp->datasets>=2.0.0->evaluate<0.5.0,>=0.4.1->unimernet==0.1.6->magic-pdf[full]==0.8.1) (1.18.3)

curl_cffi__74.md:1521-1532
Collecting git+https://github.com/lexiforest/curl_cffi
  Cloning https://github.com/lexiforest/curl_cffi to /data/data/com.termux/files/usr/tmp/pip-req-build-4flb_xq0
  Running command git clone --filter=blob:none --quiet https://github.com/lexiforest/curl_cffi /data/data/com.termux/files/usr/tmp/pip-req-build-4flb_xq0
  Resolved https://github.com/lexiforest/curl_cffi to commit 7182af65a6f49ecac7c6149addf38c26a018c5a5
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting cffi>=2.0.0 (from curl_cffi==0.15.0b2)
  Using cached cffi-2.0.0-cp312-cp312-linux_aarch64.whl
Requirement already satisfied: certifi>=2024.2.2 in /data/data/com.termux/files/usr/lib/python3.12/site-packages (from curl_cffi==0.15.0b2) (2026.1.4)
Requirement already satisfied: pycparser in /data/data/com.termux/files/usr/lib/python3.12/site-packages (from cffi>=2.0.0->curl_cffi==0.15.0b2) (2.22)
Building wheels for collected packages: curl_cffi

curl_cffi__74.md:1548-1562
      running bdist_wheel
      running build
      running build_py
      creating build/lib.linux-aarch64-cpython-312/curl_cffi
      copying curl_cffi/__init__.py -> build/lib.linux-aarch64-cpython-312/curl_cffi
      copying curl_cffi/__version__.py -> build/lib.linux-aarch64-cpython-312/curl_cffi
      copying curl_cffi/_asyncio_selector.py -> build/lib.linux-aarch64-cpython-312/curl_cffi
      copying curl_cffi/aio.py -> build/lib.linux-aarch64-cpython-312/curl_cffi
      copying curl_cffi/cli.py -> build/lib.linux-aarch64-cpython-312/curl_cffi
      copying curl_cffi/const.py -> build/lib.linux-aarch64-cpython-312/curl_cffi
      copying curl_cffi/curl.py -> build/lib.linux-aarch64-cpython-312/curl_cffi
      copying curl_cffi/utils.py -> build/lib.linux-aarch64-cpython-312/curl_cffi
      creating build/lib.linux-aarch64-cpython-312/curl_cffi/requests
      copying curl_cffi/requests/__init__.py -> build/lib.linux-aarch64-cpython-312/curl_cffi/requests
      copying curl_cffi/requests/cookies.py -> build/lib.linux-aarch64-cpython-312/curl_cffi/requests

curl_cffi__74.md:1565-1589
      copying curl_cffi/requests/headers.py -> build/lib.linux-aarch64-cpython-312/curl_cffi/requests
      copying curl_cffi/requests/impersonate.py -> build/lib.linux-aarch64-cpython-312/curl_cffi/requests
      copying curl_cffi/requests/models.py -> build/lib.linux-aarch64-cpython-312/curl_cffi/requests
      copying curl_cffi/requests/session.py -> build/lib.linux-aarch64-cpython-312/curl_cffi/requests
      copying curl_cffi/requests/utils.py -> build/lib.linux-aarch64-cpython-312/curl_cffi/requests
      copying curl_cffi/requests/websockets.py -> build/lib.linux-aarch64-cpython-312/curl_cffi/requests
      running egg_info
      writing curl_cffi.egg-info/PKG-INFO
      writing dependency_links to curl_cffi.egg-info/dependency_links.txt
      writing entry points to curl_cffi.egg-info/entry_points.txt
      writing requirements to curl_cffi.egg-info/requires.txt
      writing top-level names to curl_cffi.egg-info/top_level.txt
      reading manifest file 'curl_cffi.egg-info/SOURCES.txt'
      reading manifest template 'MANIFEST.in'
      warning: no files found matching 'include/curl/*'
      adding license file 'LICENSE'
      writing manifest file 'curl_cffi.egg-info/SOURCES.txt'
      copying curl_cffi/py.typed -> build/lib.linux-aarch64-cpython-312/curl_cffi
      running build_ext
      generating cffi module 'build/temp.linux-aarch64-cpython-312/curl_cffi._wrapper.c'
      creating build/temp.linux-aarch64-cpython-312
      building 'curl_cffi._wrapper' extension
      creating build/temp.linux-aarch64-cpython-312/build/temp.linux-aarch64-cpython-312
      creating build/temp.linux-aarch64-cpython-312/ffi
      aarch64-linux-android-clang -fno-strict-overflow -Wsign-compare -Wunreachable-code -DNDEBUG -g -O3 -Wall -fstack-protector-strong -O3 -fstack-protector-strong -O3 -fPIC -Iinclude -Iffi -I/data/data/com.termux/files/usr/tmp/tmpmku0rr6s/include -I/data/data/com.termux/files/usr/include/python3.12 -c build/temp.linux-aarch64-cpython-312/curl_cffi._wrapper.c -o build/temp.linux-aarch64-cpython-312/build/temp.linux-aarch64-cpython-312/curl_cffi._wrapper.o

ghostty__2210.md:573-584
Downloading separate debug info for /usr/lib/libEGL_nvidia.so.0...
Downloading separate debug info for /usr/lib/libnvidia-glsi.so.560.35.03...
Downloading separate debug info for /usr/lib/libnvidia-eglcore.so.560.35.03...
Downloading separate debug info for /usr/lib/libnvidia-gpucomp.so.560.35.03...
Downloading separate debug info for /usr/lib/libnvidia-egl-gbm.so.1...
Downloading separate debug info for /usr/lib/libnvidia-egl-xcb.so.1...
Downloading separate debug info for /usr/lib/libnvidia-egl-xlib.so.1...
Downloading separate debug info for /usr/lib/libnvidia-allocator.so.1...
Downloading separate debug info for system-supplied DSO at 0x707506d86000...
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/usr/lib/libthread_db.so.1".
Downloading source file /usr/src/debug/glib2/build/../glib/glib/gthread-posix.c...

pyobjc__175.md:19-66
Collecting pyobjc
  Using cached pyobjc-3.1.1.tar.gz
Requirement already satisfied: py2app>=0.10 in /anaconda/envs/opencv/lib/python2.7/site-packages (from pyobjc)
Requirement already satisfied: pyobjc-core==3.1.1 in /anaconda/envs/opencv/lib/python2.7/site-packages (from pyobjc)
Collecting pyobjc_framework-AVKit==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-AVKit-3.1.1.tar.gz
Collecting pyobjc_framework-AVFoundation==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-AVFoundation-3.1.1.tar.gz
Collecting pyobjc_framework-Accounts==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-Accounts-3.1.1.tar.gz
Collecting pyobjc_framework-AddressBook==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-AddressBook-3.1.1.tar.gz
Collecting pyobjc_framework-AppleScriptKit==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-AppleScriptKit-3.1.1.tar.gz
Collecting pyobjc_framework-AppleScriptObjC==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-AppleScriptObjC-3.1.1.tar.gz
Collecting pyobjc_framework-ApplicationServices==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-ApplicationServices-3.1.1.tar.gz
Collecting pyobjc_framework-Automator==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-Automator-3.1.1.tar.gz
Collecting pyobjc_framework-CFNetwork==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-CFNetwork-3.1.1.tar.gz
Collecting pyobjc_framework-CalendarStore==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-CalendarStore-3.1.1.tar.gz
Collecting pyobjc_framework-CloudKit==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-CloudKit-3.1.1.tar.gz
Collecting pyobjc_framework-Cocoa==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-Cocoa-3.1.1.tar.gz
Collecting pyobjc_framework-Collaboration==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-Collaboration-3.1.1.tar.gz
Collecting pyobjc_framework-CoreBluetooth==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-CoreBluetooth-3.1.1.tar.gz
Collecting pyobjc_framework-CoreData==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-CoreData-3.1.1.tar.gz
Collecting pyobjc_framework-CoreLocation==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-CoreLocation-3.1.1.tar.gz
Collecting pyobjc_framework-CoreText==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-CoreText-3.1.1.tar.gz
Collecting pyobjc_framework-CoreWLAN==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-CoreWLAN-3.1.1.tar.gz
Collecting pyobjc_framework-CryptoTokenKit==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-CryptoTokenKit-3.1.1.tar.gz
Collecting pyobjc_framework-DictionaryServices==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-DictionaryServices-3.1.1.tar.gz
Collecting pyobjc_framework-DiskArbitration==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-DiskArbitration-3.1.1.tar.gz
Collecting pyobjc_framework-EventKit==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-EventKit-3.1.1.tar.gz

pyobjc__175.md:69-139
Collecting pyobjc_framework-FSEvents==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-FSEvents-3.1.1.tar.gz
Collecting pyobjc_framework-FinderSync==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-FinderSync-3.1.1.tar.gz
Collecting pyobjc_framework-GameCenter==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-GameCenter-3.1.1.tar.gz
Collecting pyobjc_framework-GameController==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-GameController-3.1.1.tar.gz
Collecting pyobjc_framework-IMServicePlugIn==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-IMServicePlugIn-3.1.1.tar.gz
Collecting pyobjc_framework-InputMethodKit==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-InputMethodKit-3.1.1.tar.gz
Collecting pyobjc_framework-ImageCaptureCore==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-ImageCaptureCore-3.1.1.tar.gz
Collecting pyobjc_framework-InstallerPlugins==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-InstallerPlugins-3.1.1.tar.gz
Collecting pyobjc_framework-InstantMessage==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-InstantMessage-3.1.1.tar.gz
Collecting pyobjc_framework-LatentSemanticMapping==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-LatentSemanticMapping-3.1.1.tar.gz
Collecting pyobjc_framework-LaunchServices==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-LaunchServices-3.1.1.tar.gz
Collecting pyobjc_framework-LocalAuthentication==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-LocalAuthentication-3.1.1.tar.gz
Collecting pyobjc_framework-MapKit==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-MapKit-3.1.1.tar.gz
Collecting pyobjc_framework-MediaAccessibility==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-MediaAccessibility-3.1.1.tar.gz
Collecting pyobjc_framework-MediaLibrary==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-MediaLibrary-3.1.1.tar.gz
Collecting pyobjc_framework-MultipeerConnectivity==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-MultipeerConnectivity-3.1.1.tar.gz
Collecting pyobjc_framework-NetFS==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-NetFS-3.1.1.tar.gz
Collecting pyobjc_framework-NotificationCenter==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-NotificationCenter-3.1.1.tar.gz
Collecting pyobjc_framework-OpenDirectory==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-OpenDirectory-3.1.1.tar.gz
Collecting pyobjc_framework-PreferencePanes==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-PreferencePanes-3.1.1.tar.gz
Collecting pyobjc_framework-PubSub==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-PubSub-3.1.1.tar.gz
Collecting pyobjc_framework-QTKit==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-QTKit-3.1.1.tar.gz
Collecting pyobjc_framework-Quartz==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-Quartz-3.1.1.tar.gz
Collecting pyobjc_framework-ScreenSaver==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-ScreenSaver-3.1.1.tar.gz
Collecting pyobjc_framework-ScriptingBridge==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-ScriptingBridge-3.1.1.tar.gz
Collecting pyobjc_framework-SearchKit==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-SearchKit-3.1.1.tar.gz
Collecting pyobjc_framework-ServiceManagement==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-ServiceManagement-3.1.1.tar.gz
Collecting pyobjc_framework-Social==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-Social-3.1.1.tar.gz
Collecting pyobjc_framework-SpriteKit==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-SpriteKit-3.1.1.tar.gz
Collecting pyobjc_framework-StoreKit==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-StoreKit-3.1.1.tar.gz
Collecting pyobjc_framework-SyncServices==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-SyncServices-3.1.1.tar.gz
Collecting pyobjc_framework-SystemConfiguration==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-SystemConfiguration-3.1.1.tar.gz
Collecting pyobjc_framework-WebKit==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-WebKit-3.1.1.tar.gz
Collecting pyobjc_framework-SceneKit==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-SceneKit-3.1.1.tar.gz
Requirement already satisfied: altgraph>=0.12 in /anaconda/envs/opencv/lib/python2.7/site-packages (from py2app>=0.10->pyobjc)
Requirement already satisfied: modulegraph>=0.12 in /anaconda/envs/opencv/lib/python2.7/site-packages (from py2app>=0.10->pyobjc)
Requirement already satisfied: macholib>=1.5 in /anaconda/envs/opencv/lib/python2.7/site-packages (from py2app>=0.10->pyobjc)

pyobjc__175.md:203-236
    running install
    running build
    running build_py
    overriding build_packages to copy PyObjCTest
    creating build
    creating build/lib.macosx-10.6-x86_64-2.7
    creating build/lib.macosx-10.6-x86_64-2.7/Cocoa
    copying Lib/Cocoa/__init__.py -> build/lib.macosx-10.6-x86_64-2.7/Cocoa
    creating build/lib.macosx-10.6-x86_64-2.7/CoreFoundation
    copying Lib/CoreFoundation/__init__.py -> build/lib.macosx-10.6-x86_64-2.7/CoreFoundation
    copying Lib/CoreFoundation/_metadata.py -> build/lib.macosx-10.6-x86_64-2.7/CoreFoundation
    copying Lib/CoreFoundation/_static.py -> build/lib.macosx-10.6-x86_64-2.7/CoreFoundation
    creating build/lib.macosx-10.6-x86_64-2.7/Foundation
    copying Lib/Foundation/__init__.py -> build/lib.macosx-10.6-x86_64-2.7/Foundation
    copying Lib/Foundation/_context.py -> build/lib.macosx-10.6-x86_64-2.7/Foundation
    copying Lib/Foundation/_functiondefines.py -> build/lib.macosx-10.6-x86_64-2.7/Foundation
    copying Lib/Foundation/_metadata.py -> build/lib.macosx-10.6-x86_64-2.7/Foundation
    copying Lib/Foundation/_nsindexset.py -> build/lib.macosx-10.6-x86_64-2.7/Foundation
    copying Lib/Foundation/_nsobject.py -> build/lib.macosx-10.6-x86_64-2.7/Foundation
    creating build/lib.macosx-10.6-x86_64-2.7/AppKit
    copying Lib/AppKit/__init__.py -> build/lib.macosx-10.6-x86_64-2.7/AppKit
    copying Lib/AppKit/_metadata.py -> build/lib.macosx-10.6-x86_64-2.7/AppKit
    copying Lib/AppKit/_nsapp.py -> build/lib.macosx-10.6-x86_64-2.7/AppKit
    creating build/lib.macosx-10.6-x86_64-2.7/PyObjCTools
    copying Lib/PyObjCTools/__init__.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTools
    copying Lib/PyObjCTools/AppCategories.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTools
    copying Lib/PyObjCTools/AppHelper.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTools
    copying Lib/PyObjCTools/Conversion.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTools
    copying Lib/PyObjCTools/FndCategories.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTools
    creating build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/__init__.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/guitest_graphics.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/guitest_nsalert.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_appkit_protocols.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest

pyobjc__175.md:238-251
    copying PyObjCTest/test_cfarray.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfattributedstring.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfbag.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfbase.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfbinaryheap.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfbitvector.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfbundle.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfbyteorder.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfcalendar.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfcharacterset.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfdata.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfdate.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfdateformatter.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfdictionary.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest

pyobjc__175.md:253-282
    copying PyObjCTest/test_cffiledescriptor.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cffilesecurity.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cflocale.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfmachport.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfmessageport.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfnotificationcenter.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfnumber.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfnumberformatter.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfplugin.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfpreferences.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfpropertylist.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfrunloop.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfset.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfsocket.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfstream.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfstring.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfstringtokenizer.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cftimezone.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cftree.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfurl.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfurlaccess.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfurlenumerator.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfusernotification.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfuuid.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfxmlnode.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_cfxmlparser.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_constants.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_convenience.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_corefoundation.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_foundation.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest

pyobjc__175.md:284-369
    copying PyObjCTest/test_globals.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_keyvalue.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsaccessibility.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsaccessibilityprotocols.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsactioncell.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsaffinetransform.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsalert.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsalignmentfeedbackfilter.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsanimation.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsanimationcontext.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsappearance.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsappleeventdescriptor.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsappleeventmanager.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsapplescript.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsapplication.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsapplicationscripting.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsarchiver.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsarray.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsarraycontroller.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsatstypesetter.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsattributedstring.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsattributedstring_appkit.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsautoreleasepool.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsbackgroundactivityscheduler.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsbezierpath.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsbitmap.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsbitmapimagerep.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsbox.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsbrowser.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsbrowsercell.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsbundle.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsbutton.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsbuttoncell.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsbytecountformatter.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsbyteorder.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscache.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscachedimagerep.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscalendar.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscalendardate.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscell.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscharacterset.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsclassdescription.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsclipview.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscoder.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscollectionview.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscollectionviewflowlayout.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscollectionviewlayout.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscolor.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscolorlist.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscolorpanel.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscolorpicking.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscolorspace.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscolorwell.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscombobox.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscomboboxcell.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscomparisonpredicate.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscompoundpredicate.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsconnection.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscontrol.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscontroller.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscredentialstorage.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscursor.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nscustomimagerep.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsdata.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsdate.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsdatecomponentsformatter.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsdateformatter.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsdateintervalformatter.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsdatepicker.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsdatepickercell.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsdebug.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsdecimal.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsdecimalnumber.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsdictionary.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsdictionarycontroller.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsdistributedlock.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsdistributednotificationcenter.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsdocktile.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsdocument.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsdocumentcontroller.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsdragging.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsdraggingitem.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsdraggingsession.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsdrawer.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsenergyformatter.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsenumerator.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest

pyobjc__175.md:374-591
    copying PyObjCTest/test_nsexpression.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsextensioncontext.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsextensionitem.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsextensionrequesthandling.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsfilecoordinator.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsfilehandle.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsfilemanager.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsfilepresenter.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsfileversion.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsfilewrapper.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsfont.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsfontcollection.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsfontdescriptor.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsfontmanager.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsfontpanel.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsform.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsformatter.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsformcell.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsgarbagecollector.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsgeometry.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsgesturerecognizer.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsglyphgenerator.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsglyphinfo.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsgradient.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsgraphics.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsgraphicscontext.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nshapticfeedback.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nshashtable.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nshelpmanager.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nshfsfiletypes.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nshost.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nshttpcookie.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nshttpcookiestorage.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsimage.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsimagecell.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsimagerep.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsimageview.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsindexpath.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsindexset.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsinputmanager.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsinputserver.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsinterfacestyle.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsinvocation.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsitemprovider.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsjavasetup.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsjsonserialization.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nskeyedarchiver.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nskeyvaluebinding.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nskeyvaluecoding.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nskeyvalueobservering.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nslayoutconstraint.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nslayoutmanager.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nslengthformatter.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nslevelindicatorcell.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nslinguistictagger.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nslocale.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nslocalizedstring.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nslock.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nslog.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsmachport.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsmaptable.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsmassformatter.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsmatrix.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsmedialibrarybrowsercontroller.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsmenu.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsmenuitem.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsmenuitemcell.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsmenuview.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsmetadata.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsmetadataattributes.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsmethodsignature.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsmovie.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsmovieview.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsnetservices.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsnib.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsnibloading.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsnotification.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsnotificationqueue.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsnull.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsnumber.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsnumberformatter.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsobjcruntime.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsobject.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsobject_additions.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsobjectcontroller.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsopengl.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsopengllayer.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsopenglview.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsopenpanel.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsoperation.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsorderedset.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsoutlineview.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nspagecontroller.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nspagelayout.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nspanel.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsparagraphstyle.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nspasteboard.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nspasteboarditem.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nspathcell.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nspathcontrol.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nspathutilties.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nspdfinfo.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nspdfpanel.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nspersistentdocument.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nspersonnamecomponentsformatter.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nspointerarray.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nspointerfunctions.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nspopover.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nspopupbutton.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nspopupbuttoncell.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsport.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsportcoder.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsportmessage.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsportnameserver.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nspredicate.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsprinter.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsprintinfo.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsprintoperation.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsprintpanel.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsprocessinfo.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsprogress.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsprogressindicator.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nspropertylist.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsproxy.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsrange.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsregularexpression.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsresponder.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsruleeditor.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsrulermarker.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsrulerview.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsrunloop.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsrunningapplication.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nssavepanel.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsscanner.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsscreen.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsscriptclassdescription.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsscriptcoercionhandler.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsscriptcommand.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsscriptcommanddescription.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsscriptkeyvaluecoding.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsscriptobjectspecifier.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsscriptstandardsuitecommands.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsscriptwhosetests.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsscroller.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsscrollview.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nssearchfield.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nssearchfieldcell.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nssecuretextfield.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nssegmentedcell.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nssegmentedcontrol.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsset.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nssharingservice.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nssimplehorizontaltypesetter.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsslider.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsslidercell.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nssortdescriptor.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nssound.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsspeechrecognizer.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsspeechsynthesizer.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsspellchecker.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsspellprotocol.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsspellserver.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nssplitview.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nssplitviewcontroller.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsstackview.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsstatusbar.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsstatusbarbutton.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsstatusitem.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsstepper.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nssteppercell.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsstoryboardsegue.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsstream.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsstring.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsstringdrawing.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstablecolumn.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstableheadercell.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstablerowview.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/tesT_nstableview.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstableviewrowaction.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstabview.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstabviewcontroller.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstabviewitem.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstask.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstext.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstextalternatives.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstextattachment.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstextcheckingresult.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstextcontainer.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstextfield.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstextfieldcell.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstextfinder.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstextinputclient.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstextinputcontext.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstextlist.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstextstorage.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstexttable.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstextview.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsthread.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstimer.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstimezone.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstokenfield.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstokenfieldcell.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstoolbar.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstoolbaritem.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstouch.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstrackingarea.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstreecontroller.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstreenode.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nstypesetter.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsubiquitouskeyvaluestore.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsundomanager.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsurl.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsurlauthenticationchallenge.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsurlcache.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsurlconnection.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsurlcredential.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsurlcredentialstorage.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsurldownload.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest

pyobjc__175.md:593-646
    copying PyObjCTest/test_nsurlhandle.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsurlprotectionspace.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsurlprotocol.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsurlrequest.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsurlresponse.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsurlsession.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsuseractivity.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsuserdefaults.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsuserdefaultscontroller.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsuserinterfaceitemidentification.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsuserinterfaceitemsearching.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsuserinterfacelayout.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsuserinterfacevalidation.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsusernotification.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsuserscripttask.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsuuid.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsvalue.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsvaluetransformer.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsview.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsviewcontroller.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsvisualeffectview.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nswindow.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nswindowcontroller.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nswindowrestoration.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nswindowscripting.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsworkspace.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsxmldocument.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsxmldtd.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsxmldtdnode.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsxmlelement.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsxmlnode.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsxmlnodeoptions.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsxmlparser.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nsxpcconnection.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_nszone.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_osxcasts.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_regr.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_structs.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_subclassing.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_threading.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    copying PyObjCTest/test_weirdness.py -> build/lib.macosx-10.6-x86_64-2.7/PyObjCTest
    running build_ext
    building 'CoreFoundation._inlines' extension
    creating build/temp.macosx-10.6-x86_64-2.7/Modules
    gcc -fno-strict-aliasing -I//anaconda/envs/opencv/include -arch x86_64 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -Ibuild/temp.macosx-10.6-x86_64-2.7/pyobjc-include -I//anaconda/envs/opencv/include/python2.7 -c Modules/_CoreFoundation_inlines.m -o build/temp.macosx-10.6-x86_64-2.7/Modules/_CoreFoundation_inlines.o -DPyObjC_BUILD_RELEASE=1010 -isysroot /
    gcc -bundle -undefined dynamic_lookup -L//anaconda/envs/opencv/lib -arch x86_64 -arch x86_64 build/temp.macosx-10.6-x86_64-2.7/Modules/_CoreFoundation_inlines.o -L//anaconda/envs/opencv/lib -o build/lib.macosx-10.6-x86_64-2.7/CoreFoundation/_inlines.so -framework CoreFoundation -isysroot /
    building 'CoreFoundation._CoreFoundation' extension
    gcc -fno-strict-aliasing -I//anaconda/envs/opencv/include -arch x86_64 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -Ibuild/temp.macosx-10.6-x86_64-2.7/pyobjc-include -I//anaconda/envs/opencv/include/python2.7 -c Modules/_CoreFoundation.m -o build/temp.macosx-10.6-x86_64-2.7/Modules/_CoreFoundation.o -DPyObjC_BUILD_RELEASE=1010 -isysroot /
    gcc -bundle -undefined dynamic_lookup -L//anaconda/envs/opencv/lib -arch x86_64 -arch x86_64 build/temp.macosx-10.6-x86_64-2.7/Modules/_CoreFoundation.o -L//anaconda/envs/opencv/lib -o build/lib.macosx-10.6-x86_64-2.7/CoreFoundation/_CoreFoundation.so -framework CoreFoundation -isysroot /
    building 'Foundation._inlines' extension
    gcc -fno-strict-aliasing -I//anaconda/envs/opencv/include -arch x86_64 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -Ibuild/temp.macosx-10.6-x86_64-2.7/pyobjc-include -I//anaconda/envs/opencv/include/python2.7 -c Modules/_Foundation_inlines.m -o build/temp.macosx-10.6-x86_64-2.7/Modules/_Foundation_inlines.o -DPyObjC_BUILD_RELEASE=1010 -isysroot /
    gcc -bundle -undefined dynamic_lookup -L//anaconda/envs/opencv/lib -arch x86_64 -arch x86_64 build/temp.macosx-10.6-x86_64-2.7/Modules/_Foundation_inlines.o -L//anaconda/envs/opencv/lib -o build/lib.macosx-10.6-x86_64-2.7/Foundation/_inlines.so -framework Foundation -isysroot /
    building 'Foundation._Foundation' extension
    gcc -fno-strict-aliasing -I//anaconda/envs/opencv/include -arch x86_64 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -Ibuild/temp.macosx-10.6-x86_64-2.7/pyobjc-include -I//anaconda/envs/opencv/include/python2.7 -c Modules/_Foundation.m -o build/temp.macosx-10.6-x86_64-2.7/Modules/_Foundation.o -DPyObjC_BUILD_RELEASE=1010 -isysroot /

pyobjc__176.md:22-31
Collecting pyobjc
Collecting pyobjc-framework-QTKit==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-QTKit-3.1.1.tar.gz
Collecting pyobjc-framework-PreferencePanes==3.1.1 (from pyobjc)
Collecting pyobjc-framework-CalendarStore==3.1.1 (from pyobjc)
Collecting pyobjc-framework-Contacts==3.1.1 (from pyobjc)
Collecting pyobjc-framework-CloudKit==3.1.1 (from pyobjc)
Collecting pyobjc-framework-SystemConfiguration==3.1.1 (from pyobjc)
Collecting pyobjc-framework-FinderSync==3.1.1 (from pyobjc)
Collecting pyobjc-framework-AppleScriptObjC==3.1.1 (from pyobjc)

pyobjc__176.md:33-111
Collecting py2app>=0.10 (from pyobjc)
Collecting pyobjc-framework-DiskArbitration==3.1.1 (from pyobjc)
Collecting pyobjc-framework-AddressBook==3.1.1 (from pyobjc)
Collecting pyobjc-framework-SpriteKit==3.1.1 (from pyobjc)
Collecting pyobjc-framework-Accounts==3.1.1 (from pyobjc)
Collecting pyobjc-framework-SyncServices==3.1.1 (from pyobjc)
Collecting pyobjc-framework-EventKit==3.1.1 (from pyobjc)
Collecting pyobjc-framework-AVFoundation==3.1.1 (from pyobjc)
Collecting pyobjc-framework-SearchKit==3.1.1 (from pyobjc)
Collecting pyobjc-framework-ScreenSaver==3.1.1 (from pyobjc)
Collecting pyobjc-framework-ApplicationServices==3.1.1 (from pyobjc)
Collecting pyobjc-framework-MapKit==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-MapKit-3.1.1.tar.gz
Requirement already satisfied: pyobjc-core==3.1.1 in /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages (from pyobjc)
Collecting pyobjc-framework-Cocoa==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-Cocoa-3.1.1.tar.gz
Collecting pyobjc-framework-PubSub==3.1.1 (from pyobjc)
Collecting pyobjc-framework-LaunchServices==3.1.1 (from pyobjc)
Collecting pyobjc-framework-Collaboration==3.1.1 (from pyobjc)
Collecting pyobjc-framework-ImageCaptureCore==3.1.1 (from pyobjc)
Collecting pyobjc-framework-Photos==3.1.1 (from pyobjc)
Collecting pyobjc-framework-CFNetwork==3.1.1 (from pyobjc)
Collecting pyobjc-framework-MultipeerConnectivity==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-MultipeerConnectivity-3.1.1.tar.gz
Collecting pyobjc-framework-FSEvents==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-FSEvents-3.1.1.tar.gz
Collecting pyobjc-framework-LatentSemanticMapping==3.1.1 (from pyobjc)
Collecting pyobjc-framework-MediaLibrary==3.1.1 (from pyobjc)
Collecting pyobjc-framework-InstallerPlugins==3.1.1 (from pyobjc)
Collecting pyobjc-framework-OpenDirectory==3.1.1 (from pyobjc)
Collecting pyobjc-framework-LocalAuthentication==3.1.1 (from pyobjc)
Collecting pyobjc-framework-StoreKit==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-StoreKit-3.1.1.tar.gz
Collecting pyobjc-framework-AppleScriptKit==3.1.1 (from pyobjc)
Collecting pyobjc-framework-SceneKit==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-SceneKit-3.1.1.tar.gz
Collecting pyobjc-framework-ServiceManagement==3.1.1 (from pyobjc)
Collecting pyobjc-framework-ContactsUI==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-ContactsUI-3.1.1.tar.gz
Collecting pyobjc-framework-NotificationCenter==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-NotificationCenter-3.1.1.tar.gz
Collecting pyobjc-framework-Social==3.1.1 (from pyobjc)
Collecting pyobjc-framework-InstantMessage==3.1.1 (from pyobjc)
Collecting pyobjc-framework-CoreData==3.1.1 (from pyobjc)
Collecting pyobjc-framework-GameCenter==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-GameCenter-3.1.1.tar.gz
Collecting pyobjc-framework-IMServicePlugIn==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-IMServicePlugIn-3.1.1.tar.gz
Collecting pyobjc-framework-GameController==3.1.1 (from pyobjc)
Collecting pyobjc-framework-MediaAccessibility==3.1.1 (from pyobjc)
Collecting pyobjc-framework-Quartz==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-Quartz-3.1.1.tar.gz
Collecting pyobjc-framework-CryptoTokenKit==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-CryptoTokenKit-3.1.1.tar.gz
Collecting pyobjc-framework-DictionaryServices==3.1.1 (from pyobjc)
Collecting pyobjc-framework-InputMethodKit==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-InputMethodKit-3.1.1.tar.gz
Collecting pyobjc-framework-ScriptingBridge==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-ScriptingBridge-3.1.1.tar.gz
Collecting pyobjc-framework-CoreLocation==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-CoreLocation-3.1.1.tar.gz
Collecting pyobjc-framework-Automator==3.1.1 (from pyobjc)
Collecting pyobjc-framework-NetFS==3.1.1 (from pyobjc)
Collecting pyobjc-framework-AVKit==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-AVKit-3.1.1.tar.gz
Collecting pyobjc-framework-CoreWLAN==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-CoreWLAN-3.1.1.tar.gz
Collecting pyobjc-framework-CoreBluetooth==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-CoreBluetooth-3.1.1.tar.gz
Collecting pyobjc-framework-PhotosUI==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-PhotosUI-3.1.1.tar.gz
Collecting pyobjc-framework-CoreText==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-CoreText-3.1.1.tar.gz
Collecting pyobjc-framework-WebKit==3.1.1 (from pyobjc)
  Using cached pyobjc-framework-WebKit-3.1.1.tar.gz
Requirement already satisfied: macholib>=1.5 in /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/macholib-1.7-py2.7.egg (from py2app>=0.10->pyobjc)
Requirement already satisfied: altgraph>=0.12 in /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/altgraph-0.12-py2.7.egg (from py2app>=0.10->pyobjc)
Requirement already satisfied: modulegraph>=0.12 in /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/modulegraph-0.12.1-py2.7.egg (from py2app>=0.10->pyobjc)
Building wheels for collected packages: pyobjc-framework-QTKit, pyobjc-framework-MapKit, pyobjc-framework-Cocoa, pyobjc-framework-MultipeerConnectivity, pyobjc-framework-FSEvents, pyobjc-framework-StoreKit, pyobjc-framework-SceneKit, pyobjc-framework-ContactsUI, pyobjc-framework-NotificationCenter, pyobjc-framework-GameCenter, pyobjc-framework-IMServicePlugIn, pyobjc-framework-Quartz, pyobjc-framework-CryptoTokenKit, pyobjc-framework-InputMethodKit, pyobjc-framework-ScriptingBridge, pyobjc-framework-CoreLocation, pyobjc-framework-AVKit, pyobjc-framework-CoreWLAN, pyobjc-framework-CoreBluetooth, pyobjc-framework-PhotosUI, pyobjc-framework-CoreText, pyobjc-framework-WebKit

pyobjc__176.md:114-133
  running bdist_wheel
  running build
  running build_py
  overriding build_packages to copy PyObjCTest
  creating build
  creating build/lib.macosx-10.6-intel-2.7
  creating build/lib.macosx-10.6-intel-2.7/QTKit
  copying Lib/QTKit/__init__.py -> build/lib.macosx-10.6-intel-2.7/QTKit
  copying Lib/QTKit/_metadata.py -> build/lib.macosx-10.6-intel-2.7/QTKit
  creating build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/__init__.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_qtcaptureconnection.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_QTCaptureDecompressedVideoOutput.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_qtcapturedevice.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_QTCaptureFileOutput.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_QTCaptureSession.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_QTCaptureVideoPreviewOutput.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_QTCaptureView.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_QTCompressionOptions.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_qtdatareference.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest

pyobjc__176.md:135-152
  copying PyObjCTest/test_qtexportoptions.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_qtexportsession.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_qtformatdescription.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_qtkitdefines.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_qtmedia.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_qtmetadataitem.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_qtmovie.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_qtmoviemodernizer.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_QTMovieView.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_qtsamplebuffer.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_qttime.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_qttimerange.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_qttrack.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_qtutilities.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  running build_ext
  building 'QTKit._QTKit' extension
  creating build/temp.macosx-10.6-intel-2.7/Modules
  /usr/bin/clang -fno-strict-aliasing -fno-common -dynamic -arch i386 -arch x86_64 -g -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -Ibuild/temp.macosx-10.6-intel-2.7/pyobjc-include -I/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -c Modules/_QTKit.m -o build/temp.macosx-10.6-intel-2.7/Modules/_QTKit.o -DPyObjC_BUILD_RELEASE=1012 -isysroot /

pyobjc__176.md:164-215
  running bdist_wheel
  running build
  running build_py
  overriding build_packages to copy PyObjCTest
  creating build
  creating build/lib.macosx-10.6-intel-2.7
  creating build/lib.macosx-10.6-intel-2.7/MapKit
  copying Lib/MapKit/__init__.py -> build/lib.macosx-10.6-intel-2.7/MapKit
  copying Lib/MapKit/_metadata.py -> build/lib.macosx-10.6-intel-2.7/MapKit
  creating build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/__init__.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkannotation.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkannotationview.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkcircle.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkcirclerenderer.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkdirections.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkdirectionsrequest.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkdirectionsresponse.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkdirectionstypes.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkdistanceformatter.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkgeodesicpolyline.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkgeometry.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mklocalsearch.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mklocalsearchrequest.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mklocalsearchresponse.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkmapcamera.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkmapitem.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkmapsnapshot.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkmapsnapshotoptions.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkmapsnapshotter.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkmapview.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkmultipoint.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkoverlay.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkoverlaypathrenderer.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkoverlayrenderer.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkpinannotationview.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkplacemark.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkpointannotation.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkpolygon.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkpolygonrenderer.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkpolyline.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkpolylinerenderer.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkshape.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mksnapshotoptions.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mktileoverlay.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mktileoverlayrenderer.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mktypes.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_mkuserlocation.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  running build_ext
  building 'MapKit._MapKit' extension
  creating build/temp.macosx-10.6-intel-2.7/Modules
  /usr/bin/clang -fno-strict-aliasing -fno-common -dynamic -arch i386 -arch x86_64 -g -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -Ibuild/temp.macosx-10.6-intel-2.7/pyobjc-include -I/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -c Modules/_MapKit.m -o build/temp.macosx-10.6-intel-2.7/Modules/_MapKit.o -DPyObjC_BUILD_RELEASE=1012 -isysroot /

pyobjc__176.md:229-262
  running bdist_wheel
  running build
  running build_py
  overriding build_packages to copy PyObjCTest
  creating build
  creating build/lib.macosx-10.6-intel-2.7
  creating build/lib.macosx-10.6-intel-2.7/Cocoa
  copying Lib/Cocoa/__init__.py -> build/lib.macosx-10.6-intel-2.7/Cocoa
  creating build/lib.macosx-10.6-intel-2.7/CoreFoundation
  copying Lib/CoreFoundation/__init__.py -> build/lib.macosx-10.6-intel-2.7/CoreFoundation
  copying Lib/CoreFoundation/_metadata.py -> build/lib.macosx-10.6-intel-2.7/CoreFoundation
  copying Lib/CoreFoundation/_static.py -> build/lib.macosx-10.6-intel-2.7/CoreFoundation
  creating build/lib.macosx-10.6-intel-2.7/Foundation
  copying Lib/Foundation/__init__.py -> build/lib.macosx-10.6-intel-2.7/Foundation
  copying Lib/Foundation/_context.py -> build/lib.macosx-10.6-intel-2.7/Foundation
  copying Lib/Foundation/_functiondefines.py -> build/lib.macosx-10.6-intel-2.7/Foundation
  copying Lib/Foundation/_metadata.py -> build/lib.macosx-10.6-intel-2.7/Foundation
  copying Lib/Foundation/_nsindexset.py -> build/lib.macosx-10.6-intel-2.7/Foundation
  copying Lib/Foundation/_nsobject.py -> build/lib.macosx-10.6-intel-2.7/Foundation
  creating build/lib.macosx-10.6-intel-2.7/AppKit
  copying Lib/AppKit/__init__.py -> build/lib.macosx-10.6-intel-2.7/AppKit
  copying Lib/AppKit/_metadata.py -> build/lib.macosx-10.6-intel-2.7/AppKit
  copying Lib/AppKit/_nsapp.py -> build/lib.macosx-10.6-intel-2.7/AppKit
  creating build/lib.macosx-10.6-intel-2.7/PyObjCTools
  copying Lib/PyObjCTools/__init__.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTools
  copying Lib/PyObjCTools/AppCategories.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTools
  copying Lib/PyObjCTools/AppHelper.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTools
  copying Lib/PyObjCTools/Conversion.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTools
  copying Lib/PyObjCTools/FndCategories.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTools
  creating build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/__init__.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/guitest_graphics.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/guitest_nsalert.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_appkit_protocols.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest

pyobjc__176.md:264-277
  copying PyObjCTest/test_cfarray.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfattributedstring.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfbag.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfbase.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfbinaryheap.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfbitvector.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfbundle.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfbyteorder.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfcalendar.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfcharacterset.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfdata.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfdate.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfdateformatter.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfdictionary.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest

pyobjc__176.md:279-308
  copying PyObjCTest/test_cffiledescriptor.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cffilesecurity.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cflocale.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfmachport.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfmessageport.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfnotificationcenter.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfnumber.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfnumberformatter.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfplugin.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfpreferences.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfpropertylist.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfrunloop.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfset.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfsocket.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfstream.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfstring.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfstringtokenizer.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cftimezone.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cftree.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfurl.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfurlaccess.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfurlenumerator.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfusernotification.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfuuid.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfxmlnode.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_cfxmlparser.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_constants.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_convenience.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_corefoundation.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_foundation.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest

pyobjc__176.md:310-395
  copying PyObjCTest/test_globals.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_keyvalue.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsaccessibility.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsaccessibilityprotocols.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsactioncell.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsaffinetransform.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsalert.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsalignmentfeedbackfilter.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsanimation.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsanimationcontext.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsappearance.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsappleeventdescriptor.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsappleeventmanager.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsapplescript.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsapplication.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsapplicationscripting.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsarchiver.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsarray.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsarraycontroller.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsatstypesetter.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsattributedstring.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsattributedstring_appkit.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsautoreleasepool.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsbackgroundactivityscheduler.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsbezierpath.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsbitmap.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsbitmapimagerep.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsbox.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsbrowser.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsbrowsercell.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsbundle.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsbutton.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsbuttoncell.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsbytecountformatter.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsbyteorder.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscache.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscachedimagerep.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscalendar.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscalendardate.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscell.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscharacterset.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsclassdescription.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsclipview.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscoder.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscollectionview.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscollectionviewflowlayout.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscollectionviewlayout.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscolor.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscolorlist.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscolorpanel.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscolorpicking.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscolorspace.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscolorwell.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscombobox.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscomboboxcell.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscomparisonpredicate.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscompoundpredicate.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsconnection.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscontrol.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscontroller.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscredentialstorage.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscursor.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nscustomimagerep.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsdata.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsdate.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsdatecomponentsformatter.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsdateformatter.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsdateintervalformatter.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsdatepicker.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsdatepickercell.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsdebug.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsdecimal.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsdecimalnumber.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsdictionary.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsdictionarycontroller.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsdistributedlock.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsdistributednotificationcenter.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsdocktile.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsdocument.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsdocumentcontroller.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsdragging.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsdraggingitem.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsdraggingsession.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsdrawer.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsenergyformatter.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsenumerator.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest

pyobjc__176.md:400-617
  copying PyObjCTest/test_nsexpression.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsextensioncontext.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsextensionitem.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsextensionrequesthandling.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsfilecoordinator.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsfilehandle.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsfilemanager.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsfilepresenter.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsfileversion.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsfilewrapper.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsfont.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsfontcollection.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsfontdescriptor.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsfontmanager.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsfontpanel.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsform.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsformatter.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsformcell.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsgarbagecollector.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsgeometry.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsgesturerecognizer.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsglyphgenerator.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsglyphinfo.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsgradient.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsgraphics.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsgraphicscontext.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nshapticfeedback.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nshashtable.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nshelpmanager.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nshfsfiletypes.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nshost.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nshttpcookie.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nshttpcookiestorage.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsimage.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsimagecell.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsimagerep.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsimageview.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsindexpath.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsindexset.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsinputmanager.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsinputserver.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsinterfacestyle.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsinvocation.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsitemprovider.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsjavasetup.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsjsonserialization.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nskeyedarchiver.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nskeyvaluebinding.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nskeyvaluecoding.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nskeyvalueobservering.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nslayoutconstraint.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nslayoutmanager.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nslengthformatter.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nslevelindicatorcell.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nslinguistictagger.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nslocale.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nslocalizedstring.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nslock.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nslog.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsmachport.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsmaptable.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsmassformatter.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsmatrix.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsmedialibrarybrowsercontroller.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsmenu.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsmenuitem.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsmenuitemcell.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsmenuview.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsmetadata.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsmetadataattributes.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsmethodsignature.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsmovie.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsmovieview.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsnetservices.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsnib.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsnibloading.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsnotification.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsnotificationqueue.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsnull.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsnumber.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsnumberformatter.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsobjcruntime.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsobject.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsobject_additions.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsobjectcontroller.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsopengl.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsopengllayer.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsopenglview.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsopenpanel.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsoperation.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsorderedset.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsoutlineview.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nspagecontroller.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nspagelayout.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nspanel.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsparagraphstyle.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nspasteboard.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nspasteboarditem.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nspathcell.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nspathcontrol.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nspathutilties.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nspdfinfo.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nspdfpanel.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nspersistentdocument.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nspersonnamecomponentsformatter.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nspointerarray.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nspointerfunctions.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nspopover.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nspopupbutton.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nspopupbuttoncell.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsport.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsportcoder.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsportmessage.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsportnameserver.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nspredicate.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsprinter.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsprintinfo.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsprintoperation.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsprintpanel.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsprocessinfo.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsprogress.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsprogressindicator.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nspropertylist.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsproxy.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsrange.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsregularexpression.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsresponder.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsruleeditor.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsrulermarker.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsrulerview.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsrunloop.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsrunningapplication.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nssavepanel.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsscanner.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsscreen.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsscriptclassdescription.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsscriptcoercionhandler.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsscriptcommand.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsscriptcommanddescription.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsscriptkeyvaluecoding.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsscriptobjectspecifier.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsscriptstandardsuitecommands.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsscriptwhosetests.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsscroller.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsscrollview.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nssearchfield.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nssearchfieldcell.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nssecuretextfield.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nssegmentedcell.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nssegmentedcontrol.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsset.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nssharingservice.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nssimplehorizontaltypesetter.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsslider.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsslidercell.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nssortdescriptor.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nssound.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsspeechrecognizer.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsspeechsynthesizer.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsspellchecker.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsspellprotocol.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsspellserver.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nssplitview.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nssplitviewcontroller.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsstackview.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsstatusbar.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsstatusbarbutton.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsstatusitem.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsstepper.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nssteppercell.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsstoryboardsegue.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsstream.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsstring.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsstringdrawing.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstablecolumn.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstableheadercell.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstablerowview.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/tesT_nstableview.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstableviewrowaction.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstabview.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstabviewcontroller.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstabviewitem.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstask.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstext.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstextalternatives.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstextattachment.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstextcheckingresult.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstextcontainer.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstextfield.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstextfieldcell.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstextfinder.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstextinputclient.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstextinputcontext.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstextlist.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstextstorage.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstexttable.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstextview.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsthread.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstimer.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstimezone.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstokenfield.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstokenfieldcell.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstoolbar.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstoolbaritem.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstouch.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstrackingarea.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstreecontroller.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstreenode.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nstypesetter.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsubiquitouskeyvaluestore.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsundomanager.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsurl.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsurlauthenticationchallenge.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsurlcache.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsurlconnection.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsurlcredential.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsurlcredentialstorage.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsurldownload.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest

pyobjc__176.md:619-678
  copying PyObjCTest/test_nsurlhandle.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsurlprotectionspace.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsurlprotocol.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsurlrequest.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsurlresponse.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsurlsession.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsuseractivity.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsuserdefaults.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsuserdefaultscontroller.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsuserinterfaceitemidentification.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsuserinterfaceitemsearching.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsuserinterfacelayout.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsuserinterfacevalidation.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsusernotification.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsuserscripttask.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsuuid.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsvalue.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsvaluetransformer.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsview.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsviewcontroller.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsvisualeffectview.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nswindow.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nswindowcontroller.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nswindowrestoration.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nswindowscripting.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsworkspace.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsxmldocument.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsxmldtd.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsxmldtdnode.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsxmlelement.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsxmlnode.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsxmlnodeoptions.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsxmlparser.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nsxpcconnection.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_nszone.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_osxcasts.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_regr.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_structs.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_subclassing.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_threading.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  copying PyObjCTest/test_weirdness.py -> build/lib.macosx-10.6-intel-2.7/PyObjCTest
  running build_ext
  building 'CoreFoundation._inlines' extension
  creating build/temp.macosx-10.6-intel-2.7/Modules
  /usr/bin/clang -fno-strict-aliasing -fno-common -dynamic -arch i386 -arch x86_64 -g -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -Ibuild/temp.macosx-10.6-intel-2.7/pyobjc-include -I/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -c Modules/_CoreFoundation_inlines.m -o build/temp.macosx-10.6-intel-2.7/Modules/_CoreFoundation_inlines.o -DPyObjC_BUILD_RELEASE=1012 -isysroot /
  /usr/bin/clang -bundle -undefined dynamic_lookup -arch i386 -arch x86_64 -g build/temp.macosx-10.6-intel-2.7/Modules/_CoreFoundation_inlines.o -o build/lib.macosx-10.6-intel-2.7/CoreFoundation/_inlines.so -framework CoreFoundation -isysroot /
  building 'CoreFoundation._CoreFoundation' extension
  /usr/bin/clang -fno-strict-aliasing -fno-common -dynamic -arch i386 -arch x86_64 -g -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -Ibuild/temp.macosx-10.6-intel-2.7/pyobjc-include -I/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -c Modules/_CoreFoundation.m -o build/temp.macosx-10.6-intel-2.7/Modules/_CoreFoundation.o -DPyObjC_BUILD_RELEASE=1012 -isysroot /
  /usr/bin/clang -bundle -undefined dynamic_lookup -arch i386 -arch x86_64 -g build/temp.macosx-10.6-intel-2.7/Modules/_CoreFoundation.o -o build/lib.macosx-10.6-intel-2.7/CoreFoundation/_CoreFoundation.so -framework CoreFoundation -isysroot /
  building 'Foundation._inlines' extension
  /usr/bin/clang -fno-strict-aliasing -fno-common -dynamic -arch i386 -arch x86_64 -g -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -Ibuild/temp.macosx-10.6-intel-2.7/pyobjc-include -I/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -c Modules/_Foundation_inlines.m -o build/temp.macosx-10.6-intel-2.7/Modules/_Foundation_inlines.o -DPyObjC_BUILD_RELEASE=1012 -isysroot /
  /usr/bin/clang -bundle -undefined dynamic_lookup -arch i386 -arch x86_64 -g build/temp.macosx-10.6-intel-2.7/Modules/_Foundation_inlines.o -o build/lib.macosx-10.6-intel-2.7/Foundation/_inlines.so -framework Foundation -isysroot /
  building 'Foundation._Foundation' extension
  /usr/bin/clang -fno-strict-aliasing -fno-common -dynamic -arch i386 -arch x86_64 -g -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -Ibuild/temp.macosx-10.6-intel-2.7/pyobjc-include -I/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -c Modules/_Foundation.m -o build/temp.macosx-10.6-intel-2.7/Modules/_Foundation.o -DPyObjC_BUILD_RELEASE=1012 -isysroot /
  /usr/bin/clang -bundle -undefined dynamic_lookup -arch i386 -arch x86_64 -g build/temp.macosx-10.6-intel-2.7/Modules/_Foundation.o -o build/lib.macosx-10.6-intel-2.7/Foundation/_Foundation.so -framework Foundation -isysroot /
  building 'AppKit._inlines' extension
  /usr/bin/clang -fno-strict-aliasing -fno-common -dynamic -arch i386 -arch x86_64 -g -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -Ibuild/temp.macosx-10.6-intel-2.7/pyobjc-include -I/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -c Modules/_AppKit_inlines.m -o build/temp.macosx-10.6-intel-2.7/Modules/_AppKit_inlines.o -DPyObjC_BUILD_RELEASE=1012 -isysroot /
  /usr/bin/clang -bundle -undefined dynamic_lookup -arch i386 -arch x86_64 -g build/temp.macosx-10.6-intel-2.7/Modules/_AppKit_inlines.o -o build/lib.macosx-10.6-intel-2.7/AppKit/_inlines.so -framework AppKit -isysroot /
  building 'AppKit._AppKit' extension
  /usr/bin/clang -fno-strict-aliasing -fno-common -dynamic -arch i386 -arch x86_64 -g -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -Ibuild/temp.macosx-10.6-intel-2.7/pyobjc-include -I/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -c Modules/_AppKit.m -o build/temp.macosx-10.6-intel-2.7/Modules/_AppKit.o -DPyObjC_BUILD_RELEASE=1012 -isysroot /

pyobjc__176.md:691-728
  Stored in directory: /Users/public1/Library/Caches/pip/wheels/a5/bb/89/8f00e507c6085877f3c3707bc8c01505603bbe3a8cb8694d91
  Running setup.py bdist_wheel for pyobjc-framework-FSEvents ... done
  Stored in directory: /Users/public1/Library/Caches/pip/wheels/a7/37/91/f13c9975c4d9d56d2c9b816b60924ac063df16bfcf227e9b24
  Running setup.py bdist_wheel for pyobjc-framework-StoreKit ... done
  Stored in directory: /Users/public1/Library/Caches/pip/wheels/a7/50/b9/1f9e3e4e608476009899e7d18c1c82208911d2eb4917530d66
  Running setup.py bdist_wheel for pyobjc-framework-SceneKit ... done
  Stored in directory: /Users/public1/Library/Caches/pip/wheels/17/b4/75/fe9d5010ba87cb87590883d3d27d23223d716e07aebe9bf103
  Running setup.py bdist_wheel for pyobjc-framework-ContactsUI ... done
  Stored in directory: /Users/public1/Library/Caches/pip/wheels/43/e2/c0/59b409ee60cbfd971fa5bdec7ca2455d1590906ab1fca9b19f
  Running setup.py bdist_wheel for pyobjc-framework-NotificationCenter ... done
  Stored in directory: /Users/public1/Library/Caches/pip/wheels/2b/e0/30/b75564438ce601f9d02a44354140c2afa48cfeea0a4c489b9a
  Running setup.py bdist_wheel for pyobjc-framework-GameCenter ... done
  Stored in directory: /Users/public1/Library/Caches/pip/wheels/90/3c/fa/345066d087a60990682a95697da524e6f9b74f50e13539f9ab
  Running setup.py bdist_wheel for pyobjc-framework-IMServicePlugIn ... done
  Stored in directory: /Users/public1/Library/Caches/pip/wheels/9b/86/c4/d904336167f22a20d8df640aba17416e117e3d04eb7da8f008
  Running setup.py bdist_wheel for pyobjc-framework-Quartz ... done
  Stored in directory: /Users/public1/Library/Caches/pip/wheels/9f/91/da/7174ca9f4dff1ec490798ca76798aada58ec7c9ba0a9d908bb
  Running setup.py bdist_wheel for pyobjc-framework-CryptoTokenKit ... done
  Stored in directory: /Users/public1/Library/Caches/pip/wheels/15/10/d4/4cb7f83288d7a6e535c47896c0f122e5aee3c5e6d8859c7386
  Running setup.py bdist_wheel for pyobjc-framework-InputMethodKit ... done
  Stored in directory: /Users/public1/Library/Caches/pip/wheels/f4/31/c5/92f55dd9b3198e3a27339beddc1f0763e6750c948235c0126d
  Running setup.py bdist_wheel for pyobjc-framework-ScriptingBridge ... done
  Stored in directory: /Users/public1/Library/Caches/pip/wheels/1a/e9/0c/da653561c24f49ed85f314f61d8a7d706dd076932b435f003f
  Running setup.py bdist_wheel for pyobjc-framework-CoreLocation ... done
  Stored in directory: /Users/public1/Library/Caches/pip/wheels/21/e3/13/97740a6bafb6d7a61475fbbbc1a41414e74cfd06bd4a712d57
  Running setup.py bdist_wheel for pyobjc-framework-AVKit ... done
  Stored in directory: /Users/public1/Library/Caches/pip/wheels/2d/aa/fe/e684beeecd9fcd12bc0f8b6ca360ea3f70aa3d842dcc7626d9
  Running setup.py bdist_wheel for pyobjc-framework-CoreWLAN ... done
  Stored in directory: /Users/public1/Library/Caches/pip/wheels/51/1c/db/5dd22b4b1339c69354ab48409c5b6e8f98936a0d2fe2872299
  Running setup.py bdist_wheel for pyobjc-framework-CoreBluetooth ... done
  Stored in directory: /Users/public1/Library/Caches/pip/wheels/7a/2b/c7/e12a9aa584a753a8916e6b51d54f88c88e5cbc70d23497a76e
  Running setup.py bdist_wheel for pyobjc-framework-PhotosUI ... done
  Stored in directory: /Users/public1/Library/Caches/pip/wheels/77/7d/15/ad7606e4925742232374f473c53c4e5a34f2d2300da52a096e
  Running setup.py bdist_wheel for pyobjc-framework-CoreText ... done
  Stored in directory: /Users/public1/Library/Caches/pip/wheels/84/7a/b1/9123b4da819ce38d75f9b7b213fc66c43677faa83ac013ea3f
  Running setup.py bdist_wheel for pyobjc-framework-WebKit ... done
  Stored in directory: /Users/public1/Library/Caches/pip/wheels/61/63/e1/5f62236fa431f194af8abea882b02d445c3d23381eec079d88
Successfully built pyobjc-framework-MultipeerConnectivity pyobjc-framework-FSEvents pyobjc-framework-StoreKit pyobjc-framework-SceneKit pyobjc-framework-ContactsUI pyobjc-framework-NotificationCenter pyobjc-framework-GameCenter pyobjc-framework-IMServicePlugIn pyobjc-framework-Quartz pyobjc-framework-CryptoTokenKit pyobjc-framework-InputMethodKit pyobjc-framework-ScriptingBridge pyobjc-framework-CoreLocation pyobjc-framework-AVKit pyobjc-framework-CoreWLAN pyobjc-framework-CoreBluetooth pyobjc-framework-PhotosUI pyobjc-framework-CoreText pyobjc-framework-WebKit

pyobjc__34.md:33-48
running clean
Installing 'pyobjc-core' using '/Users/nilesh/domains/workhere/bin/python'
running install
running bdist_egg
running egg_info
creating Lib/pyobjc_core.egg-info
writing Lib/pyobjc_core.egg-info/PKG-INFO
writing namespace_packages to Lib/pyobjc_core.egg-info/namespace_packages.txt
writing top-level names to Lib/pyobjc_core.egg-info/top_level.txt
writing dependency_links to Lib/pyobjc_core.egg-info/dependency_links.txt
writing manifest file 'Lib/pyobjc_core.egg-info/SOURCES.txt'
reading manifest file 'Lib/pyobjc_core.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
warning: no directories found matching 'Scripts'
warning: no directories found matching 'setup-lib'
warning: no directories found matching 'source-deps'

pyobjc__34.md:52-123
writing manifest file 'Lib/pyobjc_core.egg-info/SOURCES.txt'
writing include/pyobjc-compat.h to Lib/pyobjc_core.egg-info/include/pyobjc-compat.h
writing include/pyobjc-api.h to Lib/pyobjc_core.egg-info/include/pyobjc-api.h
installing library code to build/bdist.macosx-10.8-intel/egg
running install_lib
running build_py
Overriding build_packages to copy PyObjCTest
creating build
creating build/lib.macosx-10.8-intel-2.7
creating build/lib.macosx-10.8-intel-2.7/objc
copying Lib/objc/__init__.py -> build/lib.macosx-10.8-intel-2.7/objc
copying Lib/objc/_bridges.py -> build/lib.macosx-10.8-intel-2.7/objc
copying Lib/objc/_bridgesupport.py -> build/lib.macosx-10.8-intel-2.7/objc
copying Lib/objc/_category.py -> build/lib.macosx-10.8-intel-2.7/objc
copying Lib/objc/_compat.py -> build/lib.macosx-10.8-intel-2.7/objc
copying Lib/objc/_context.py -> build/lib.macosx-10.8-intel-2.7/objc
copying Lib/objc/_convenience.py -> build/lib.macosx-10.8-intel-2.7/objc
copying Lib/objc/_descriptors.py -> build/lib.macosx-10.8-intel-2.7/objc
copying Lib/objc/_dyld.py -> build/lib.macosx-10.8-intel-2.7/objc
copying Lib/objc/_framework.py -> build/lib.macosx-10.8-intel-2.7/objc
copying Lib/objc/_gnustep.py -> build/lib.macosx-10.8-intel-2.7/objc
copying Lib/objc/_lazyimport.py -> build/lib.macosx-10.8-intel-2.7/objc
copying Lib/objc/_locking.py -> build/lib.macosx-10.8-intel-2.7/objc
copying Lib/objc/_properties.py -> build/lib.macosx-10.8-intel-2.7/objc
copying Lib/objc/_protocols.py -> build/lib.macosx-10.8-intel-2.7/objc
copying Lib/objc/_pycoder.py -> build/lib.macosx-10.8-intel-2.7/objc
copying Lib/objc/_pythonify.py -> build/lib.macosx-10.8-intel-2.7/objc
copying Lib/objc/_setup.py -> build/lib.macosx-10.8-intel-2.7/objc
creating build/lib.macosx-10.8-intel-2.7/PyObjCTools
copying Lib/PyObjCTools/__init__.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTools
copying Lib/PyObjCTools/KeyValueCoding.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTools
copying Lib/PyObjCTools/MachSignals.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTools
copying Lib/PyObjCTools/Signals.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTools
copying Lib/PyObjCTools/TestSupport.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTools
creating build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/__init__.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/dejagnu.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/fnd.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/helper_bridgesupport.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/keyvaluehelper.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/loader.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test2_dict_interface.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test2_dictviews.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test2_filepointer.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test3_dict_interface.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test3_protocol.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test3_typecheck.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_allocatebuffer.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_archive_python.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_array_interface.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_array_property.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_arrays.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_assocations.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_blocks.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_bridges.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_bridgesupport.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_bundleFunctions.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_bundleVariables.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_callbacks.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_classandinst.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_classhooks.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_clinmeth.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_context.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_convenience.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_conversion.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_copying.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_corefoundation.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_ctests.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_descriptors.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_dict_property.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_dict_proxy.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_dyld.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest

pyobjc__34.md:125-193
copying PyObjCTest/test_framework.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_fsref.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_hidden_selector.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_identity.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_imp.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_initialized.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_ivar.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_keyvalue.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_keyvalue_prop.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_keyvaluecoding.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_leaks.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_list_proxy.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_locking.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_metadata.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_metadata_function.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_metadata_imp.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_metadata_inheritance.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_metadata_py.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_metadata_py2py.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_method_prototypes.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_methodaccess.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_methodedits.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_methods.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_methods2.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsdate_proxy.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_NULL.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_number_proxy.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_objc.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_object_property.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_opaque.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_outputinitializer.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_pickle.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_pickling_objc.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_posing.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_propertiesforclass.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_protected.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_protocol.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_protocolNamed.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_regr.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_set_interface.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_set_property.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_set_proxy.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_signatures.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_sockaddr.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_specialtypecodes_charbyte.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_specialtypecodes_charint.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_specialtypecodes_methdef.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_specialtypecodes_nsbool.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_specialtypecodes_struct.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_specialtypecodes_unichar.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_splitsig.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_structpointer.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_structs.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_subclass.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_synthesize.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_testsupport.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_usekvo.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_varargs.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_voidpointer.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_weakref.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
running build_ext
Use '/usr/bin/clang' instead of 'clang' as the compiler
building 'objc._objc' extension
creating build/temp.macosx-10.8-intel-2.7
creating build/temp.macosx-10.8-intel-2.7/libffi-src
creating build/temp.macosx-10.8-intel-2.7/libffi-src/powerpc
creating build/temp.macosx-10.8-intel-2.7/libffi-src/x86
creating build/temp.macosx-10.8-intel-2.7/Modules
creating build/temp.macosx-10.8-intel-2.7/Modules/objc

pyobjc__34.md:211-220
clang: warning: argument unused during compilation: '-mno-fused-madd'
libffi-src/x86/x86-ffi64.c:164:27: warning: implicit conversion loses integer
      precision: 'unsigned long' to 'int' [-Wshorten-64-to-32]
                        int size = byte_offset + type->size;
                            ~~~~   ~~~~~~~~~~~~^~~~~~~~~~~~
libffi-src/x86/x86-ffi64.c:216:39: warning: implicit conversion loses integer
      precision: 'unsigned long' to 'int' [-Wshorten-64-to-32]
  ...(type->size + UNITS_PER_WORD - 1) / UNITS_PER_WORD;
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~
libffi-src/x86/x86-ffi64.c:423:15: warning: implicit conversion loses integer

pyobjc__34.md:238-272
clang: warning: argument unused during compilation: '-mno-fused-madd'
Modules/objc/block_support.m:260:47: warning: implicit conversion loses integer
      precision: 'long' to 'int' [-Wshorten-64-to-32]
  ...if (PyObjCFFI_AllocByRef(Py_SIZE(signature) + PyTuple_Size(args), ...
         ~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~
Modules/objc/block_support.m:264:28: warning: implicit conversion loses integer
      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
                if (PyObjCFFI_AllocByRef(Py_SIZE(signature), &byref, ...
                    ~~~~~~~~~~~~~~~~~~~~ ^~~~~~~~~~~~~~~~~~
Modules/objc/pyobjc-compat.h:153:56: note: expanded from macro 'Py_SIZE'
#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)
                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~
Modules/objc/block_support.m:301:45: warning: implicit conversion loses integer
      precision: 'long' to 'int' [-Wshorten-64-to-32]
  ...if (PyObjCFFI_FreeByRef(Py_SIZE(signature)+PyTuple_Size(args), byref, ...
         ~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~
Modules/objc/block_support.m:306:27: warning: implicit conversion loses integer
      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
                if (PyObjCFFI_FreeByRef(Py_SIZE(signature), byref, ...
                    ~~~~~~~~~~~~~~~~~~~ ^~~~~~~~~~~~~~~~~~
Modules/objc/pyobjc-compat.h:153:56: note: expanded from macro 'Py_SIZE'
#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)
                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~
Modules/objc/block_support.m:316:41: warning: implicit conversion loses integer
      precision: 'long' to 'int' [-Wshorten-64-to-32]
                PyObjCFFI_FreeByRef(Py_SIZE(signature)+PyTuple_Size(args)...
                ~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~
Modules/objc/block_support.m:318:23: warning: implicit conversion loses integer
      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
                PyObjCFFI_FreeByRef(Py_SIZE(signature), byref, byref_attr);
                ~~~~~~~~~~~~~~~~~~~ ^~~~~~~~~~~~~~~~~~
Modules/objc/pyobjc-compat.h:153:56: note: expanded from macro 'Py_SIZE'
#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)
                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~
6 warnings generated.

pyobjc__34.md:292-326
clang: warning: argument unused during compilation: '-mno-fused-madd'
Modules/objc/function.m:189:51: warning: implicit conversion loses integer
      precision: 'long' to 'int' [-Wshorten-64-to-32]
  ...if (PyObjCFFI_AllocByRef(Py_SIZE(self->methinfo)+PyTuple_Size(args), ...
         ~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~
Modules/objc/function.m:193:28: warning: implicit conversion loses integer
      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
                if (PyObjCFFI_AllocByRef(Py_SIZE(self->methinfo), ...
                    ~~~~~~~~~~~~~~~~~~~~ ^~~~~~~~~~~~~~~~~~~~~~~
Modules/objc/pyobjc-compat.h:153:56: note: expanded from macro 'Py_SIZE'
#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)
                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~
Modules/objc/function.m:234:50: warning: implicit conversion loses integer
      precision: 'long' to 'int' [-Wshorten-64-to-32]
  ...if (PyObjCFFI_FreeByRef(Py_SIZE(self->methinfo)+PyTuple_Size(args), ...
         ~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~
Modules/objc/function.m:239:27: warning: implicit conversion loses integer
      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
                if (PyObjCFFI_FreeByRef(Py_SIZE(self->methinfo), byref, ...
                    ~~~~~~~~~~~~~~~~~~~ ^~~~~~~~~~~~~~~~~~~~~~~
Modules/objc/pyobjc-compat.h:153:56: note: expanded from macro 'Py_SIZE'
#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)
                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~
Modules/objc/function.m:249:27: warning: implicit conversion loses integer
      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
                if (PyObjCFFI_FreeByRef(PyTuple_Size(args), byref, ...
                    ~~~~~~~~~~~~~~~~~~~ ^~~~~~~~~~~~~~~~~~
Modules/objc/function.m:254:27: warning: implicit conversion loses integer
      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
                if (PyObjCFFI_FreeByRef(Py_SIZE(self->methinfo), byref, ...
                    ~~~~~~~~~~~~~~~~~~~ ^~~~~~~~~~~~~~~~~~~~~~~
Modules/objc/pyobjc-compat.h:153:56: note: expanded from macro 'Py_SIZE'
#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)
                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~
6 warnings generated.

pyobjc__34.md:370-394
Modules/objc/objc-object.h:41:90: note: expanded from macro
      'PyObjCObject_SET_BLOCK'
  ...value) (((PyObjCBlockObject*)(object))->signature = (value))
                                                       ^ ~~~~~~~
7 warnings generated.
Modules/objc/libffi_support.m:936:9: warning: implicit conversion loses integer
      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
        return curarg;
        ~~~~~~ ^~~~~~
Modules/objc/libffi_support.m:988:15: warning: implicit conversion loses integer
      precision: 'long' to 'int' [-Wshorten-64-to-32]
        return curarg+1;
        ~~~~~~ ~~~~~~^~
Modules/objc/libffi_support.m:1823:30: warning: implicit conversion loses
      integer precision: 'long' to 'int' [-Wshorten-64-to-32]
                 int result = Py_SIZE(sig) - 1;
                     ~~~~~~   ~~~~~~~~~~~~~^~~
Modules/objc/libffi_support.m:3143:9: warning: implicit conversion loses integer
      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
        return Py_SIZE(methinfo);
        ~~~~~~ ^~~~~~~~~~~~~~~~~
Modules/objc/pyobjc-compat.h:153:56: note: expanded from macro 'Py_SIZE'
#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)
                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~
Modules/objc/libffi_support.m:3326:13: warning: initializing 'char *' with an

pyobjc__34.md:411-448
Modules/objc/objc-object.h:41:90: note: expanded from macro
      'PyObjCObject_SET_BLOCK'
  ...value) (((PyObjCBlockObject*)(object))->signature = (value))
                                                       ^ ~~~~~~~
Modules/objc/libffi_support.m:3732:45: warning: implicit conversion loses
      integer precision: 'long' to 'int' [-Wshorten-64-to-32]
                if (PyObjCFFI_AllocByRef(Py_SIZE(methinfo)+PyTuple_Size(args), 
                    ~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~
Modules/objc/libffi_support.m:3737:28: warning: implicit conversion loses
      integer precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
                if (PyObjCFFI_AllocByRef(Py_SIZE(methinfo), &byref, ...
                    ~~~~~~~~~~~~~~~~~~~~ ^~~~~~~~~~~~~~~~~
Modules/objc/pyobjc-compat.h:153:56: note: expanded from macro 'Py_SIZE'
#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)
                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~
Modules/objc/libffi_support.m:3905:44: warning: implicit conversion loses
      integer precision: 'long' to 'int' [-Wshorten-64-to-32]
                if (PyObjCFFI_FreeByRef(Py_SIZE(methinfo)+PyTuple_Size(args)...
                    ~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~
Modules/objc/libffi_support.m:3910:27: warning: implicit conversion loses
      integer precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
                if (PyObjCFFI_FreeByRef(Py_SIZE(methinfo), byref, ...
                    ~~~~~~~~~~~~~~~~~~~ ^~~~~~~~~~~~~~~~~
Modules/objc/pyobjc-compat.h:153:56: note: expanded from macro 'Py_SIZE'
#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)
                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~
Modules/objc/libffi_support.m:3931:27: warning: implicit conversion loses
      integer precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
                if (PyObjCFFI_FreeByRef(PyTuple_Size(args), byref, ...
                    ~~~~~~~~~~~~~~~~~~~ ^~~~~~~~~~~~~~~~~~
Modules/objc/libffi_support.m:3936:27: warning: implicit conversion loses
      integer precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
                if (PyObjCFFI_FreeByRef(Py_SIZE(methinfo), byref, ...
                    ~~~~~~~~~~~~~~~~~~~ ^~~~~~~~~~~~~~~~~
Modules/objc/pyobjc-compat.h:153:56: note: expanded from macro 'Py_SIZE'
#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)
                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~
Modules/objc/libffi_support.m:3997:42: warning: implicit conversion loses

pyobjc__34.md:480-504
clang: warning: argument unused during compilation: '-mno-fused-madd'
Modules/objc/objc-class.m:49:6: warning: implicit conversion loses integer
      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
        n = PyTuple_GET_SIZE(mro);
          ~ ^~~~~~~~~~~~~~~~~~~~~
/System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7/tupleobject.h:51:33: note: 
      expanded from macro 'PyTuple_GET_SIZE'
#define PyTuple_GET_SIZE(op)    Py_SIZE(op)
                                ^
Modules/objc/pyobjc-compat.h:153:56: note: expanded from macro 'Py_SIZE'
#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)
                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~
Modules/objc/objc-class.m:983:23: warning: implicit conversion loses integer
      precision: 'size_t' (aka 'unsigned long') to 'int' [-Wshorten-64-to-32]
        info->method_magic = PyObjC_methodlist_magic(objc_class);
                           ~ ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Modules/objc/objc-class.m:1085:14: warning: implicit conversion loses integer
      precision: 'size_t' (aka 'unsigned long') to 'int' [-Wshorten-64-to-32]
  ...(magic = PyObjC_methodlist_magic(info->class))) || (info->generation != ...
            ~ ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Modules/objc/objc-class.m:1100:23: warning: implicit conversion loses integer
      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
                        info->generation = PyObjC_MappingCount;
                                         ~ ^~~~~~~~~~~~~~~~~~~
Modules/objc/objc-class.m:2634:50: warning: implicit conversion loses integer

pyobjc__34.md:524-578
clang: warning: argument unused during compilation: '-mno-fused-madd'
Modules/objc/objc_support.m:2119:19: warning: implicit conversion loses integer
      precision: 'long long' to 'int' [-Wshorten-64-to-32]
                        *(int*)datum = temp;
                                     ~ ^~~~
Modules/objc/objc_support.m:2154:19: warning: implicit conversion loses integer
      precision: 'long long' to 'int' [-Wshorten-64-to-32]
                        *(int*)datum = temp;
                                     ~ ^~~~
Modules/objc/objc_support.m:2190:28: warning: implicit conversion loses integer
      precision: 'unsigned long long' to 'unsigned int' [-Wshorten-64-to-32]
                        *(unsigned int*)datum = utemp;
                                              ~ ^~~~~
Modules/objc/objc_support.m:2198:19: warning: implicit conversion loses integer
      precision: 'long long' to 'int' [-Wshorten-64-to-32]
                        *(int*)datum = temp;
                                     ~ ^~~~
Modules/objc/objc_support.m:2206:28: warning: implicit conversion loses integer
      precision: 'unsigned long long' to 'unsigned int' [-Wshorten-64-to-32]
                        *(unsigned int*)datum = utemp;
                                              ~ ^~~~~
Modules/objc/objc_support.m:2434:19: warning: implicit conversion loses integer
      precision: 'long long' to 'int' [-Wshorten-64-to-32]
                        *(int*)datum = temp;
                                     ~ ^~~~
Modules/objc/objc_support.m:2442:28: warning: implicit conversion loses integer
      precision: 'unsigned long long' to 'unsigned int' [-Wshorten-64-to-32]
                        *(unsigned int*)datum = utemp;
                                              ~ ^~~~~
Modules/objc/objc_support.m:2450:20: warning: implicit conversion loses integer
      precision: 'long long' to 'long' [-Wshorten-64-to-32]
                        *(long*)datum = temp;
                                      ~ ^~~~
Modules/objc/objc_support.m:2458:29: warning: implicit conversion loses integer
      precision: 'unsigned long long' to 'unsigned long' [-Wshorten-64-to-32]
                        *(unsigned long*)datum = utemp;
                                               ~ ^~~~~
9 warnings generated.
Modules/objc/objc_support.m:722:21: warning: implicit conversion loses integer
      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
                        int item_align = PyObjCRT_AlignOfType(type);
                            ~~~~~~~~~~   ^~~~~~~~~~~~~~~~~~~~~~~~~~
Modules/objc/objc_support.m:901:12: warning: implicit conversion loses integer
      precision: 'long' to 'int' [-Wshorten-64-to-32]
                        int i = strtol(type+1, NULL, 10);
                            ~   ^~~~~~~~~~~~~~~~~~~~~~~~
Modules/objc/objc_support.m:2434:19: warning: implicit conversion loses integer
      precision: 'long long' to 'int' [-Wshorten-64-to-32]
                        *(int*)datum = temp;
                                     ~ ^~~~
Modules/objc/objc_support.m:2442:28: warning: implicit conversion loses integer
      precision: 'unsigned long long' to 'unsigned int' [-Wshorten-64-to-32]
                        *(unsigned int*)datum = utemp;
                                              ~ ^~~~~
4 warnings generated.

pyobjc__34.md:629-650
clang: warning: argument unused during compilation: '-mno-fused-madd'
Modules/objc/pointer-support.m:59:16: warning: implicit conversion loses integer
      precision: 'long' to 'int' [-Wshorten-64-to-32]
                        return end1 - signature;
                        ~~~~~~ ~~~~~^~~~~~~~~~~
Modules/objc/pointer-support.m:61:16: warning: implicit conversion loses integer
      precision: 'long' to 'int' [-Wshorten-64-to-32]
                        return end2 - signature;
                        ~~~~~~ ~~~~~^~~~~~~~~~~
Modules/objc/pointer-support.m:72:16: warning: implicit conversion loses integer
      precision: 'long' to 'int' [-Wshorten-64-to-32]
                        return end1 - signature;
                        ~~~~~~ ~~~~~^~~~~~~~~~~
Modules/objc/pointer-support.m:74:16: warning: implicit conversion loses integer
      precision: 'long' to 'int' [-Wshorten-64-to-32]
                        return end2 - signature;
                        ~~~~~~ ~~~~~^~~~~~~~~~~
Modules/objc/pointer-support.m:77:9: warning: implicit conversion loses integer
      precision: 'size_t' (aka 'unsigned long') to 'int' [-Wshorten-64-to-32]
        return strlen(signature);
        ~~~~~~ ^~~~~~~~~~~~~~~~~
5 warnings generated.

pyobjc__34.md:669-681
clang: warning: argument unused during compilation: '-mno-fused-madd'
Modules/objc/struct-wrapper.m:748:9: warning: implicit conversion loses integer
      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
                len = PyList_GET_SIZE(keys);
                    ~ ^~~~~~~~~~~~~~~~~~~~~
/System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7/listobject.h:63:32: note: 
      expanded from macro 'PyList_GET_SIZE'
#define PyList_GET_SIZE(op)    Py_SIZE(op)
                               ^
Modules/objc/pyobjc-compat.h:153:56: note: expanded from macro 'Py_SIZE'
#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)
                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~
1 warning generated.

pyobjc__34.md:857-872
clang: warning: argument unused during compilation: '-mno-fused-madd'
Modules/objc/test/testbndl.m:521:12: warning: implicit conversion loses integer
      precision: 'size_t' (aka 'unsigned long') to 'int' [-Wshorten-64-to-32]
        int len = strlen(arg);
            ~~~   ^~~~~~~~~~~
Modules/objc/test/testbndl.m:761:12: warning: implicit conversion loses integer
      precision: 'size_t' (aka 'unsigned long') to 'int' [-Wshorten-64-to-32]
        int len = strlen(*arg);
            ~~~   ^~~~~~~~~~~~
Modules/objc/test/testbndl.m:783:12: warning: implicit conversion loses integer
      precision: 'size_t' (aka 'unsigned long') to 'int' [-Wshorten-64-to-32]
        int len = strlen(*arg);
            ~~~   ^~~~~~~~~~~~
3 warnings generated.
/usr/bin/clang -bundle -undefined dynamic_lookup -Wl,-F. -arch i386 -arch x86_64 build/temp.macosx-10.8-intel-2.7/Modules/objc/test/testbndl.o -o build/lib.macosx-10.8-intel-2.7/PyObjCTest/testbndl.so -framework CoreFoundation -framework Foundation -framework Carbon -isysroot /
building 'PyObjCTest.testbndl2' extension

pyobjc__34.md:896-940
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/filepointer.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/fsref.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/identity.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/initialize.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/instanceVariables.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/locking.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/metadata.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/metadatafunction.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/NULL.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/opaque.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/properties.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/protected.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/protocol.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/pythonnumber.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/pythonset.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/sockaddr.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/specialtypecodes.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/structargs.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/structpointer1.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/structpointer2.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/structs.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/testbndl.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/testbndl2.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/testclassandinst.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/testoutputinitializer.so -> PyObjCTest
copying build/lib.macosx-10.8-intel-2.7/PyObjCTest/voidpointer.so -> PyObjCTest
copying objc/__init__.py -> build/bdist.macosx-10.8-intel/egg/objc
copying objc/_bridges.py -> build/bdist.macosx-10.8-intel/egg/objc
copying objc/_bridgesupport.py -> build/bdist.macosx-10.8-intel/egg/objc
copying objc/_category.py -> build/bdist.macosx-10.8-intel/egg/objc
copying objc/_compat.py -> build/bdist.macosx-10.8-intel/egg/objc
copying objc/_context.py -> build/bdist.macosx-10.8-intel/egg/objc
copying objc/_convenience.py -> build/bdist.macosx-10.8-intel/egg/objc
copying objc/_descriptors.py -> build/bdist.macosx-10.8-intel/egg/objc
copying objc/_dyld.py -> build/bdist.macosx-10.8-intel/egg/objc
copying objc/_framework.py -> build/bdist.macosx-10.8-intel/egg/objc
copying objc/_gnustep.py -> build/bdist.macosx-10.8-intel/egg/objc
copying objc/_lazyimport.py -> build/bdist.macosx-10.8-intel/egg/objc
copying objc/_locking.py -> build/bdist.macosx-10.8-intel/egg/objc
copying objc/_objc.so -> build/bdist.macosx-10.8-intel/egg/objc
copying objc/_properties.py -> build/bdist.macosx-10.8-intel/egg/objc
copying objc/_protocols.py -> build/bdist.macosx-10.8-intel/egg/objc
copying objc/_pycoder.py -> build/bdist.macosx-10.8-intel/egg/objc
copying objc/_pythonify.py -> build/bdist.macosx-10.8-intel/egg/objc
copying objc/_setup.py -> build/bdist.macosx-10.8-intel/egg/objc

pyobjc__34.md:1073-1100
copying PyObjCTools/__init__.py -> build/bdist.macosx-10.8-intel/egg/PyObjCTools
copying PyObjCTools/KeyValueCoding.py -> build/bdist.macosx-10.8-intel/egg/PyObjCTools
copying PyObjCTools/MachSignals.py -> build/bdist.macosx-10.8-intel/egg/PyObjCTools
copying PyObjCTools/Signals.py -> build/bdist.macosx-10.8-intel/egg/PyObjCTools
copying PyObjCTools/TestSupport.py -> build/bdist.macosx-10.8-intel/egg/PyObjCTools
byte-compiling build/bdist.macosx-10.8-intel/egg/objc/__init__.py to __init__.pyc
byte-compiling build/bdist.macosx-10.8-intel/egg/objc/_bridges.py to _bridges.pyc
byte-compiling build/bdist.macosx-10.8-intel/egg/objc/_bridgesupport.py to _bridgesupport.pyc
byte-compiling build/bdist.macosx-10.8-intel/egg/objc/_category.py to _category.pyc
byte-compiling build/bdist.macosx-10.8-intel/egg/objc/_compat.py to _compat.pyc
byte-compiling build/bdist.macosx-10.8-intel/egg/objc/_context.py to _context.pyc
byte-compiling build/bdist.macosx-10.8-intel/egg/objc/_convenience.py to _convenience.pyc
byte-compiling build/bdist.macosx-10.8-intel/egg/objc/_descriptors.py to _descriptors.pyc
byte-compiling build/bdist.macosx-10.8-intel/egg/objc/_dyld.py to _dyld.pyc
byte-compiling build/bdist.macosx-10.8-intel/egg/objc/_framework.py to _framework.pyc
byte-compiling build/bdist.macosx-10.8-intel/egg/objc/_gnustep.py to _gnustep.pyc
byte-compiling build/bdist.macosx-10.8-intel/egg/objc/_lazyimport.py to _lazyimport.pyc
byte-compiling build/bdist.macosx-10.8-intel/egg/objc/_locking.py to _locking.pyc
byte-compiling build/bdist.macosx-10.8-intel/egg/objc/_properties.py to _properties.pyc
byte-compiling build/bdist.macosx-10.8-intel/egg/objc/_protocols.py to _protocols.pyc
byte-compiling build/bdist.macosx-10.8-intel/egg/objc/_pycoder.py to _pycoder.pyc
byte-compiling build/bdist.macosx-10.8-intel/egg/objc/_pythonify.py to _pythonify.pyc
byte-compiling build/bdist.macosx-10.8-intel/egg/objc/_setup.py to _setup.pyc
byte-compiling build/bdist.macosx-10.8-intel/egg/PyObjCTools/__init__.py to __init__.pyc
byte-compiling build/bdist.macosx-10.8-intel/egg/PyObjCTools/KeyValueCoding.py to KeyValueCoding.pyc
byte-compiling build/bdist.macosx-10.8-intel/egg/PyObjCTools/MachSignals.py to MachSignals.pyc
byte-compiling build/bdist.macosx-10.8-intel/egg/PyObjCTools/Signals.py to Signals.pyc
byte-compiling build/bdist.macosx-10.8-intel/egg/PyObjCTools/TestSupport.py to TestSupport.pyc

pyobjc__34.md:1102-1111
byte-compiling build/bdist.macosx-10.8-intel/egg/objc/_objc.py to _objc.pyc
creating build/bdist.macosx-10.8-intel/egg/EGG-INFO
copying Lib/pyobjc_core.egg-info/PKG-INFO -> build/bdist.macosx-10.8-intel/egg/EGG-INFO
copying Lib/pyobjc_core.egg-info/SOURCES.txt -> build/bdist.macosx-10.8-intel/egg/EGG-INFO
copying Lib/pyobjc_core.egg-info/dependency_links.txt -> build/bdist.macosx-10.8-intel/egg/EGG-INFO
copying Lib/pyobjc_core.egg-info/namespace_packages.txt -> build/bdist.macosx-10.8-intel/egg/EGG-INFO
copying Lib/pyobjc_core.egg-info/not-zip-safe -> build/bdist.macosx-10.8-intel/egg/EGG-INFO
copying Lib/pyobjc_core.egg-info/top_level.txt -> build/bdist.macosx-10.8-intel/egg/EGG-INFO
writing build/bdist.macosx-10.8-intel/egg/EGG-INFO/native_libs.txt
creating dist

pyobjc__34.md:1123-1137
running clean
Installing 'pyobjc-framework-Cocoa' using '/Users/nilesh/domains/workhere/bin/python'
running install
running bdist_egg
running egg_info
creating Lib/pyobjc_framework_Cocoa.egg-info
writing requirements to Lib/pyobjc_framework_Cocoa.egg-info/requires.txt
writing Lib/pyobjc_framework_Cocoa.egg-info/PKG-INFO
writing namespace_packages to Lib/pyobjc_framework_Cocoa.egg-info/namespace_packages.txt
writing top-level names to Lib/pyobjc_framework_Cocoa.egg-info/top_level.txt
writing dependency_links to Lib/pyobjc_framework_Cocoa.egg-info/dependency_links.txt
writing manifest file 'Lib/pyobjc_framework_Cocoa.egg-info/SOURCES.txt'
reading manifest file 'Lib/pyobjc_framework_Cocoa.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
warning: no directories found matching 'source-deps'

pyobjc__34.md:1141-1175
writing manifest file 'Lib/pyobjc_framework_Cocoa.egg-info/SOURCES.txt'
installing library code to build/bdist.macosx-10.8-intel/egg
running install_lib
running build_py
overriding build_packages to copy PyObjCTest
creating build
creating build/lib.macosx-10.8-intel-2.7
creating build/lib.macosx-10.8-intel-2.7/Cocoa
copying Lib/Cocoa/__init__.py -> build/lib.macosx-10.8-intel-2.7/Cocoa
creating build/lib.macosx-10.8-intel-2.7/CoreFoundation
copying Lib/CoreFoundation/__init__.py -> build/lib.macosx-10.8-intel-2.7/CoreFoundation
copying Lib/CoreFoundation/_metadata.py -> build/lib.macosx-10.8-intel-2.7/CoreFoundation
copying Lib/CoreFoundation/_static.py -> build/lib.macosx-10.8-intel-2.7/CoreFoundation
creating build/lib.macosx-10.8-intel-2.7/Foundation
copying Lib/Foundation/__init__.py -> build/lib.macosx-10.8-intel-2.7/Foundation
copying Lib/Foundation/_context.py -> build/lib.macosx-10.8-intel-2.7/Foundation
copying Lib/Foundation/_functiondefines.py -> build/lib.macosx-10.8-intel-2.7/Foundation
copying Lib/Foundation/_metadata.py -> build/lib.macosx-10.8-intel-2.7/Foundation
copying Lib/Foundation/_nsindexset.py -> build/lib.macosx-10.8-intel-2.7/Foundation
copying Lib/Foundation/_nsobject.py -> build/lib.macosx-10.8-intel-2.7/Foundation
creating build/lib.macosx-10.8-intel-2.7/AppKit
copying Lib/AppKit/__init__.py -> build/lib.macosx-10.8-intel-2.7/AppKit
copying Lib/AppKit/_metadata.py -> build/lib.macosx-10.8-intel-2.7/AppKit
copying Lib/AppKit/_nsapp.py -> build/lib.macosx-10.8-intel-2.7/AppKit
creating build/lib.macosx-10.8-intel-2.7/PyObjCTools
copying Lib/PyObjCTools/__init__.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTools
copying Lib/PyObjCTools/AppCategories.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTools
copying Lib/PyObjCTools/AppHelper.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTools
copying Lib/PyObjCTools/Conversion.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTools
copying Lib/PyObjCTools/FndCategories.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTools
copying Lib/PyObjCTools/NibClassBuilder.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTools
creating build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/__init__.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/guitest_graphics.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/guitest_nsalert.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest

pyobjc__34.md:1177-1190
copying PyObjCTest/test_cfarray.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfattributedstring.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfbag.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfbase.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfbinaryheap.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfbitvector.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfbundle.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfbyteorder.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfcalendar.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfcharacterset.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfdata.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfdate.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfdateformatter.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfdictionary.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest

pyobjc__34.md:1192-1221
copying PyObjCTest/test_cffiledescriptor.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cffilesecurity.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cflocale.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfmachport.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfmessageport.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfnotificationcenter.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfnumber.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfnumberformatter.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfplugin.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfpreferences.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfpropertylist.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfrunloop.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfset.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfsocket.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfstream.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfstring.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfstringtokenizer.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cftimezone.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cftree.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfurl.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfurlaccess.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfurlenumerator.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfusernotification.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfuuid.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfxmlnode.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_cfxmlparser.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_constants.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_convenience.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_corefoundation.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_foundation.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest

pyobjc__34.md:1223-1299
copying PyObjCTest/test_globals.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_keyvalue.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsaccessibility.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsactioncell.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsaffinetransform.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsalert.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsanimation.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsanimationcontext.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsappleeventdescriptor.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsappleeventmanager.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsapplescript.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsapplication.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsapplicationscripting.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsarchiver.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsarray.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsarraycontroller.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsatstypesetter.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsattributedstring.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsattributedstring_appkit.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsautoreleasepool.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsbezierpath.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsbitmap.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsbitmapimagerep.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsbox.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsbrowser.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsbrowsercell.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsbundle.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsbutton.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsbuttoncell.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsbytecountformatter.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsbyteorder.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nscache.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nscachedimagerep.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nscalendar.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nscalendardate.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nscell.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nscharacterset.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsclassdescription.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsclipview.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nscoder.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nscollectionview.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nscolor.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nscolorlist.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nscolorpanel.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nscolorpicking.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nscolorspace.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nscolorwell.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nscombobox.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nscomboboxcell.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nscomparisonpredicate.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nscompoundpredicate.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsconnection.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nscontrol.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nscontroller.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nscredentialstorage.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nscursor.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nscustomimagerep.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsdata.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsdate.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsdateformatter.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsdatepicker.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsdatepickercell.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsdebug.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsdecimal.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsdecimalnumber.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsdictionary.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsdictionarycontroller.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsdistributedlock.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsdistributednotificationcenter.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsdocktile.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsdocument.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsdocumentcontroller.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsdragging.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsdraggingitem.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsdraggingsession.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsdrawer.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsenumerator.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest

pyobjc__34.md:1304-1498
copying PyObjCTest/test_nsexpression.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsfilecoordinator.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsfilehandle.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsfilemanager.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsfilepresenter.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsfileversion.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsfilewrapper.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsfont.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsfontcollection.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsfontdescriptor.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsfontmanager.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsfontpanel.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsform.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsformatter.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsformcell.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsgarbagecollector.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsgeometry.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsglyphgenerator.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsglyphinfo.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsgradient.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsgraphics.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsgraphicscontext.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nshashtable.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nshelpmanager.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nshfsfiletypes.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nshost.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nshttpcookie.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nshttpcookiestorage.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsimage.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsimagecell.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsimagerep.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsimageview.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsindexpath.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsindexset.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsinputmanager.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsinputserver.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsinterfacestyle.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsinvocation.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsjavasetup.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsjsonserialization.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nskeyedarchiver.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nskeyvaluebinding.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nskeyvaluecoding.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nskeyvalueobservering.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nslayoutconstraint.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nslayoutmanager.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nslevelindicatorcell.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nslinguistictagger.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nslocale.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nslocalizedstring.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nslock.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nslog.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsmachport.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsmaptable.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsmatrix.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsmenu.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsmenuitem.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsmenuitemcell.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsmenuview.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsmetadata.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsmethodsignature.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsmovie.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsmovieview.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsnetservices.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsnib.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsnibloading.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsnotification.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsnotificationqueue.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsnull.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsnumber.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsnumberformatter.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsobjcruntime.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsobject.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsobject_additions.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsobjectcontroller.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsopengl.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsopengllayer.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsopenglview.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsopenpanel.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsoperation.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsorderedset.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsoutlineview.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nspagecontroller.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nspagelayout.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nspanel.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsparagraphstyle.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nspasteboard.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nspasteboarditem.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nspathcell.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nspathcontrol.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nspathutilties.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nspersistentdocument.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nspointerarray.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nspointerfunctions.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nspopover.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nspopupbutton.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nspopupbuttoncell.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsport.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsportcoder.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsportmessage.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsportnameserver.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nspredicate.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsprinter.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsprintinfo.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsprintoperation.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsprintpanel.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsprocessinfo.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsprogressindicator.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nspropertylist.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsproxy.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsrange.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsregularexpression.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsresponder.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsruleeditor.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsrulermarker.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsrulerview.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsrunloop.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsrunningapplication.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nssavepanel.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsscanner.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsscreen.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsscriptclassdescription.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsscriptcoercionhandler.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsscriptcommand.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsscriptcommanddescription.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsscriptkeyvaluecoding.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsscriptobjectspecifier.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsscriptstandardsuitecommands.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsscriptwhosetests.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsscroller.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsscrollview.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nssearchfieldcell.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nssecuretextfield.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nssegmentedcell.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nssegmentedcontrol.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsset.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nssharingservice.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nssimplehorizontaltypesetter.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsslider.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsslidercell.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nssortdescriptor.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nssound.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsspeechrecognizer.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsspeechsynthesizer.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsspellchecker.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsspellserver.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nssplitview.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsstatusbar.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsstatusitem.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsstepper.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nssteppercell.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsstream.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsstring.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsstringdrawing.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstablecolumn.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstableheadercell.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstablerowview.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstableview.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstabview.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstabviewitem.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstask.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstext.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstextalternatives.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstextattachment.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstextcheckingresult.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstextcontainer.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstextfield.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstextfieldcell.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstextfinder.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstextinputclient.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstextinputcontext.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstextlist.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstextstorage.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstexttable.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstextview.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsthread.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstimer.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstimezone.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstokenfield.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstokenfieldcell.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstoolbar.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstoolbaritem.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstouch.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstrackingarea.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstreecontroller.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstreenode.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nstypesetter.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsubiquitouskeyvaluestore.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsundomanager.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsurl.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsurlcache.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsurlconnection.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsurlcredential.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsurlcredentialstorage.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsurldownload.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest

pyobjc__34.md:1500-1541
copying PyObjCTest/test_nsurlhandle.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsurlprotectionspace.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsurlprotocol.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsurlrequest.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsurlresponse.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsuserdefaults.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsuserdefaultscontroller.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsuserinterfaceitemsearching.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsuserinterfacevalidation.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsusernotification.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsuserscripttask.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsuuid.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsvalue.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsvaluetransformer.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsview.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsviewcontroller.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nswindow.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nswindowcontroller.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nswindowrestoration.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nswindowscripting.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsworkspace.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsxmldocument.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsxmldtd.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsxmldtdnode.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsxmlelement.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsxmlnode.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsxmlnodeoptions.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsxmlparser.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nsxpcconnection.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_nszone.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_osxcasts.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_regr.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_structs.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_subclassing.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_threading.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
copying PyObjCTest/test_weirdness.py -> build/lib.macosx-10.8-intel-2.7/PyObjCTest
running build_ext
Use '/usr/bin/clang' instead of 'clang' as the compiler
building 'CoreFoundation._inlines' extension
creating build/temp.macosx-10.8-intel-2.7/Modules
/usr/bin/clang -fno-strict-aliasing -fno-common -dynamic -g -Os -pipe -fno-common -fno-strict-aliasing -fwrapv -mno-fused-madd -DENABLE_DTRACE -DMACOSX -DNDEBUG -Wall -Wstrict-prototypes -Wshorten-64-to-32 -DNDEBUG -g -Os -Wall -Wstrict-prototypes -DENABLE_DTRACE -arch i386 -arch x86_64 -pipe -Ibuild/temp.macosx-10.8-intel-2.7/pyobjc-include -I/System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -c Modules/_CoreFoundation_inlines.m -o build/temp.macosx-10.8-intel-2.7/Modules/_CoreFoundation_inlines.o -DPyObjC_BUILD_RELEASE=1008 -isysroot /
clang: warning: argument unused during compilation: '-mno-fused-madd'
