# INFRASTRUCTURE
import re

# Any HTML <img> tag (any attribute order/presence)
IMG_RE = re.compile(r'<img\b[^>]*>', re.IGNORECASE)
# Any markdown image with non-empty URL: ![alt](url) — subsumes extension-specific and data-URI forms.
# Requires non-empty URL ([^)]+) to avoid matching ![]() used as literal code examples in prose.
MD_IMG_RE = re.compile(r'!\[[^\]]*\]\([^)]+\)', re.IGNORECASE)
# Bare base64 data-URI not inside markdown image syntax
DATA_URI_RE = re.compile(
    r'data:image/[^;]+;base64,[A-Za-z0-9+/=]+',
    re.IGNORECASE,
)


# FUNCTIONS

# Apply all generic noise subs to a single line; used by strip_generic_noise and per-line callers
def _strip_line(line: str) -> str:
    line = re.sub(IMG_RE, '', line)
    line = re.sub(MD_IMG_RE, '', line)
    line = re.sub(DATA_URI_RE, '', line)
    line = re.sub(r'!\[Uploading[^\]]*\]\(\)', '', line)
    line = re.sub(r'\S{1000,}', '', line)
    return line


# Strip generic image noise and long no-space runs from text
def strip_generic_noise(text: str) -> str:
    return '\n'.join(_strip_line(line) for line in text.splitlines())
