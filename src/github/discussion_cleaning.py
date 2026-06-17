# INFRASTRUCTURE
import re

# From text_cleaning.py: generic image/no-space strips (GH_IMG, MD_IMG, data-URI, failed-upload)
from src.github.text_cleaning import strip_generic_noise

FOOTER_LOOKAHEAD = 20
_BADGE_DOMAINS = frozenset([
    'shields.io/badge', 'camo.githubusercontent.com',
    'app.dosu.dev/response-feedback', 'go.dosu.dev',
])
_FOOTER_TEXT_PHRASES = (
    'To reply, just mention',
    'Docs are dead. Just use',
    'Share context across your team and agents. Try',
)
ISSUE_HEADING_RE = re.compile(
    r'^### (?:🔎 Search before asking|🤖 Consult the online AI assistant)'
)


# FUNCTIONS

# Strip blockquote prefix for dosu marker detection
def _bare(line: str) -> str:
    return re.sub(r'^[\s>]+', '', line).strip()


# True if line is a dosu-feedback badge line (shields.io / camo / dosu domains)
def _is_badge_line(line: str) -> bool:
    c = _bare(line)
    has_badge = '[![' in c or c.startswith('<sup>How did I do?')
    has_dosu = any(x in c for x in _BADGE_DOMAINS)
    return has_badge and has_dosu


# True if line is a markerless dosu greeting (email-rendered, no <!-- Greeting --> marker)
def _is_dosu_markerless_greeting(line: str) -> bool:
    stripped = re.sub(r'^[\s>_*]+', '', line.replace('&nbsp;', ' ')).strip()
    if not (stripped.startswith('Hi @') or stripped.startswith('你好@') or stripped.startswith('你好 @')):
        return False
    if 'Dosu' not in line:
        return False
    return ('helping' in line and 'team' in line) or ('帮助' in line and '团队' in line)


# True if line is a dosu footer text line (blockquoted/email-rendered — no marker, no badge)
def _is_dosu_footer_text_line(line: str) -> bool:
    stripped = re.sub(r'^[\s>_*]+', '', line).strip()
    has_dosu_ref = 'Dosu' in line or '@dosu' in line
    for phrase in _FOOTER_TEXT_PHRASES:
        if stripped.startswith(phrase) and has_dosu_ref:
            return True
    if '回复时只需提及' in line and '@dosu' in line:
        return True
    if '已经过时' in line and ('Dosu' in line or 'dosu.dev' in line):
        return True
    return False


# Strip bot-generated noise from text; safe on raw get_discussion output or pre-built MDs
def strip_noise(text: str) -> str:
    lines = text.splitlines()
    i = 0
    out = []
    while i < len(lines):
        line = lines[i]
        bare = _bare(line)

        # DOSU_FOOTER: strip <!-- Dosu Comment Footer --> ... badge line (incl.)
        if bare == '<!-- Dosu Comment Footer -->':
            badge_idx = next(
                (j for j in range(i + 1, min(i + FOOTER_LOOKAHEAD, len(lines)))
                 if _is_badge_line(lines[j])), None
            )
            if badge_idx is not None:
                block = lines[i:badge_idx + 1]
                if not any(re.search(r'^\s*>\s*\*\*@', l) for l in block):
                    i = badge_idx + 1
                    continue

        # DOSU_GREETING: strip <!-- Greeting --> + next non-blank line
        if bare == '<!-- Greeting -->':
            greet_idx = next(
                (j for j in range(i + 1, min(i + 5, len(lines))) if lines[j].strip()), None
            )
            if greet_idx is not None:
                i = greet_idx + 1
                continue

        # ISSUE_TEMPLATE_CHECKLIST: strip heading + consecutive checkbox/blank lines
        if ISSUE_HEADING_RE.match(line.strip()):
            j = i + 1
            while j < len(lines) and (lines[j].strip().startswith('- [') or not lines[j].strip()):
                j += 1
            i = j
            continue

        # STANDALONE BADGE LINE: markerless/blockquoted/orphaned dosu badges
        if _is_badge_line(line):
            i += 1
            continue

        # DOSU_FOOTER_TEXT: blockquoted/email-rendered footer prose (no marker, no badge)
        if _is_dosu_footer_text_line(line):
            i += 1
            continue

        # DOSU_MARKERLESS_GREETING: email-rendered greeting line (no <!-- Greeting --> marker)
        if _is_dosu_markerless_greeting(line):
            i += 1
            continue

        # Inline subs: DOSU_ANSWER_MARKER, DOSU_GREETING_INLINE; then generic noise via text_cleaning
        line = re.sub(r'<!--\s*(?:Answer|Greeting)\s*-->', '', line)
        line = strip_generic_noise(line)

        out.append(line)
        i += 1

    return "\n".join(out)
