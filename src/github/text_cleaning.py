# INFRASTRUCTURE
import re

# GitHub user-attachment screenshot <img> tag
GH_IMG_RE = re.compile(
    r'<img\s+width="\d+"\s+height="\d+"\s+alt="[^"]*"\s+'
    r'src="https://github\.com/user-attachments/assets/[a-f0-9-]+"[^>]*/?>',
    re.IGNORECASE,
)
# Markdown image by file extension: ![alt](url.png|jpg|jpeg|gif|svg|webp[?params])
MD_IMG_RE = re.compile(
    r'!\[[^\]]*\]\([^)]*\.(?:png|jpe?g|gif|svg|webp)(?:\?[^)]*)?\)',
    re.IGNORECASE,
)
# Markdown image whose src is a base64 data-URI: ![alt](data:image/...;base64,...)
MD_DATA_URI_RE = re.compile(
    r'!\[[^\]]*\]\(data:image/[^;]+;base64,[A-Za-z0-9+/=]+\)',
    re.IGNORECASE,
)
# Bare base64 data-URI (inline, not inside markdown image syntax)
DATA_URI_RE = re.compile(
    r'data:image/[^;]+;base64,[A-Za-z0-9+/=]+',
    re.IGNORECASE,
)


# FUNCTIONS

# Apply all generic noise subs to a single line; used by strip_generic_noise and per-line callers
def _strip_line(line: str) -> str:
    line = re.sub(GH_IMG_RE, '', line)
    line = re.sub(MD_DATA_URI_RE, '', line)
    line = re.sub(DATA_URI_RE, '', line)
    line = re.sub(r'!\[Uploading[^\]]*\]\(\)', '', line)
    line = re.sub(MD_IMG_RE, '', line)
    line = re.sub(r'\S{1000,}', '', line)
    return line


# Strip generic image noise and long no-space runs from text
def strip_generic_noise(text: str) -> str:
    return '\n'.join(_strip_line(line) for line in text.splitlines())
