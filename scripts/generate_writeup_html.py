#!/usr/bin/env python3
"""
generate_writeup_html.py — converts the strategic writeup .md to a self-contained
.html file with the four SVG visuals embedded inline.

Usage:
    python3 scripts/generate_writeup_html.py

Reads:  writeup/Vizcom GTM Amplifier — Strategic Writeup.md
Writes: writeup/Vizcom GTM Amplifier — Strategic Writeup.html
"""
from __future__ import annotations

import html as html_lib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WRITEUP_DIR = ROOT / "writeup"
MD_PATH = WRITEUP_DIR / "Vizcom GTM Amplifier — Strategic Writeup.md"
HTML_PATH = WRITEUP_DIR / "Vizcom GTM Amplifier — Strategic Writeup.html"


# ---------------------------------------------------------------------------
# markdown → HTML (custom, no external deps)
# ---------------------------------------------------------------------------


def inline(s: str) -> str:
    """Inline markdown: images, links, bold, italic, code."""
    # Images first (so they're not eaten by the link regex)
    def img_repl(m: re.Match) -> str:
        alt, path = m.group(1), m.group(2)
        # If path points to an SVG inside writeup/, inline the SVG content
        if path.startswith("./visuals/") and path.endswith(".svg"):
            svg_path = WRITEUP_DIR / path[2:]
            if svg_path.exists():
                svg_content = svg_path.read_text(encoding="utf-8").strip()
                # Strip XML declaration if present
                svg_content = re.sub(r"^<\?xml[^>]+\?>\s*", "", svg_content)
                # Strip HTML comments at the top (deprecation markers etc.)
                svg_content = re.sub(r"^<!--[\s\S]*?-->\s*", "", svg_content)
                return (
                    f'<figure class="inline-svg">{svg_content}'
                    f'<figcaption>{html_lib.escape(alt)}</figcaption></figure>'
                )
        # Otherwise standard <img>
        return f'<img src="{html_lib.escape(path)}" alt="{html_lib.escape(alt)}" />'

    s = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", img_repl, s)
    # Links
    s = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f'<a href="{html_lib.escape(m.group(2))}" target="_blank" rel="noopener">{m.group(1)}</a>',
        s,
    )
    # Bold
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    # Italic (avoid catching ** by requiring no * before/after)
    s = re.sub(r"(?<![*\w])\*([^*\n]+)\*(?![*\w])", r"<em>\1</em>", s)
    # Inline code
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s


def md_to_html(text: str) -> str:
    """Convert a markdown document into HTML."""
    lines = text.splitlines()
    out: list[str] = []

    i = 0
    n = len(lines)
    in_para = False
    list_stack: list[str] = []  # 'ul' or 'ol'
    in_blockquote = False
    in_codeblock = False
    in_html_block = False
    code_lang = ""

    def close_para() -> None:
        nonlocal in_para
        if in_para:
            out.append("</p>")
            in_para = False

    def close_lists() -> None:
        while list_stack:
            out.append(f"</{list_stack.pop()}>")

    def close_blockquote() -> None:
        nonlocal in_blockquote
        if in_blockquote:
            close_para()
            out.append("</blockquote>")
            in_blockquote = False

    while i < n:
        raw = lines[i]
        line = raw.rstrip()

        # Pass-through raw HTML blocks (<details>, <summary>, </details>)
        if line.strip().startswith("<details") or line.strip().startswith("</details"):
            close_para(); close_lists(); close_blockquote()
            out.append(line)
            i += 1
            continue
        if line.strip().startswith("<summary") or line.strip().startswith("</summary"):
            out.append(line)
            i += 1
            continue

        # Code fences
        m = re.match(r"^```(\w*)\s*$", line)
        if m:
            if in_codeblock:
                out.append("</code></pre>")
                in_codeblock = False
                code_lang = ""
            else:
                close_para(); close_lists(); close_blockquote()
                code_lang = m.group(1)
                cls = f' class="lang-{code_lang}"' if code_lang else ""
                out.append(f'<pre><code{cls}>')
                in_codeblock = True
            i += 1
            continue

        if in_codeblock:
            out.append(html_lib.escape(line))
            i += 1
            continue

        # Horizontal rule
        if re.match(r"^\s*---+\s*$", line):
            close_para(); close_lists(); close_blockquote()
            out.append("<hr/>")
            i += 1
            continue

        # Headers
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            close_para(); close_lists(); close_blockquote()
            level = len(m.group(1))
            content = inline(m.group(2))
            # Slug for anchor
            slug = re.sub(r"[^a-z0-9]+", "-", m.group(2).lower()).strip("-")
            out.append(f'<h{level} id="{slug}">{content}</h{level}>')
            i += 1
            continue

        # Tables (markdown pipe tables)
        if "|" in line and i + 1 < n and re.match(r"^\s*\|?[\s\-:|]+\|?\s*$", lines[i + 1]):
            close_para(); close_lists(); close_blockquote()
            # Header row
            headers = [c.strip() for c in line.strip().strip("|").split("|")]
            out.append('<table>')
            out.append("<thead><tr>")
            for h in headers:
                out.append(f"<th>{inline(h)}</th>")
            out.append("</tr></thead>")
            # Skip separator
            i += 2
            out.append("<tbody>")
            while i < n and lines[i].strip().startswith("|"):
                row = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                out.append("<tr>")
                for c in row:
                    out.append(f"<td>{inline(c)}</td>")
                out.append("</tr>")
                i += 1
            out.append("</tbody></table>")
            continue

        # Blockquote
        if line.startswith("> "):
            close_lists(); close_para()
            if not in_blockquote:
                out.append("<blockquote>")
                in_blockquote = True
            out.append(f"<p>{inline(line[2:].strip())}</p>")
            i += 1
            continue
        elif in_blockquote and line.strip() == "":
            # blank line within blockquote OK
            i += 1
            continue
        else:
            if in_blockquote:
                close_blockquote()

        # Unordered list
        m_ul = re.match(r"^(\s*)[-*]\s+(.*)$", line)
        m_ol = re.match(r"^(\s*)(\d+)\.\s+(.*)$", line)
        if m_ul:
            close_para()
            indent = len(m_ul.group(1))
            content = m_ul.group(2)
            # Adjust list nesting
            depth = (indent // 2) + 1
            while len(list_stack) < depth:
                out.append("<ul>")
                list_stack.append("ul")
            while len(list_stack) > depth:
                out.append(f"</{list_stack.pop()}>")
            out.append(f"<li>{inline(content)}</li>")
            i += 1
            continue
        if m_ol:
            close_para()
            indent = len(m_ol.group(1))
            content = m_ol.group(3)
            depth = (indent // 2) + 1
            while len(list_stack) < depth:
                out.append("<ol>")
                list_stack.append("ol")
            while len(list_stack) > depth:
                out.append(f"</{list_stack.pop()}>")
            out.append(f"<li>{inline(content)}</li>")
            i += 1
            continue
        elif list_stack:
            close_lists()

        # Blank line — paragraph break
        if not line.strip():
            close_para()
            i += 1
            continue

        # Default: paragraph text
        if not in_para:
            out.append("<p>")
            in_para = True
        else:
            out.append(" ")
        out.append(inline(line))
        i += 1

    close_para(); close_lists(); close_blockquote()
    if in_codeblock:
        out.append("</code></pre>")

    return "\n".join(out)


# ---------------------------------------------------------------------------
# HTML template
# ---------------------------------------------------------------------------

CSS = """
:root {
  --fg: #1d1d1f;
  --muted: #6e6e73;
  --bg: #fff;
  --border: #e5e5e7;
  --link: #0a66c2;
  --code-bg: #f6f6f6;
  --quote-bg: #f9f9f9;
}
* { box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, "Helvetica Neue", sans-serif;
  background: #fafafa; color: var(--fg);
  max-width: 920px; margin: 0 auto;
  padding: 3rem 1.75rem 5rem;
  line-height: 1.6; font-size: 16px;
}
h1, h2, h3, h4 { color: var(--fg); letter-spacing: -0.01em; line-height: 1.25; }
h1 { font-size: 2.1rem; margin: 0 0 1.25rem; }
h2 { font-size: 1.5rem; margin: 2.5rem 0 1rem; padding-bottom: .35rem; border-bottom: 1px solid var(--border); }
h3 { font-size: 1.2rem; margin: 1.75rem 0 .6rem; }
h4 { font-size: 1.05rem; margin: 1.25rem 0 .5rem; color: #333; }
p { margin: .75rem 0; }
a { color: var(--link); text-decoration: none; }
a:hover { text-decoration: underline; }
strong { color: #000; }
em { color: #333; }
code {
  background: var(--code-bg);
  padding: 1px 6px; border-radius: 4px;
  font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
  font-size: .9em;
}
pre {
  background: var(--code-bg);
  padding: 1rem 1.25rem; border-radius: 6px;
  overflow-x: auto; font-size: .85rem; line-height: 1.5;
  margin: 1rem 0;
}
pre code { background: transparent; padding: 0; font-size: 1em; }
blockquote {
  margin: 1rem 0; padding: .5rem 1.25rem;
  background: var(--quote-bg); border-left: 4px solid #d4d4d4;
  border-radius: 0 4px 4px 0; color: #333;
}
blockquote p { margin: .4rem 0; }
ul, ol { margin: .75rem 0 .75rem 1.5rem; padding: 0; }
li { margin: .25rem 0; }
hr { border: none; border-top: 1px solid var(--border); margin: 2.5rem 0; }
table {
  border-collapse: collapse; margin: 1.25rem 0; width: 100%;
  background: #fff; border-radius: 6px; overflow: hidden;
  border: 1px solid var(--border);
  font-size: .95rem;
}
thead { background: #f5f5f7; }
th, td { padding: .55rem .9rem; text-align: left; border-bottom: 1px solid var(--border); vertical-align: top; }
tr:last-child td { border-bottom: none; }
th { font-weight: 600; }
figure.inline-svg {
  margin: 1.5rem 0; text-align: center;
}
figure.inline-svg svg {
  max-width: 100%; height: auto; border: 1px solid var(--border); border-radius: 6px; background: #fafafa;
}
figure.inline-svg figcaption {
  margin-top: .5rem; font-size: .85rem; color: var(--muted); font-style: italic;
}
details {
  background: #fafafa; border: 1px solid var(--border); border-radius: 6px;
  padding: .75rem 1rem; margin: 1rem 0;
}
details summary {
  cursor: pointer; font-weight: 600; font-size: .95rem; color: var(--muted);
}
details[open] summary { margin-bottom: .5rem; }
@media print {
  body { background: #fff; padding: 1rem; }
  h2 { page-break-after: avoid; }
  figure.inline-svg, table { page-break-inside: avoid; }
}
"""


def build_html(body: str, title: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>{html_lib.escape(title)}</title>
  <style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>
"""


def main() -> int:
    if not MD_PATH.exists():
        print(f"Source not found: {MD_PATH}")
        return 1
    md = MD_PATH.read_text(encoding="utf-8")
    # Strip the H1 from the body and use it as the page title
    title_match = re.match(r"^#\s+(.*)$", md, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Vizcom GTM Amplifier"
    body = md_to_html(md)
    html = build_html(body, title)
    HTML_PATH.write_text(html, encoding="utf-8")
    print(f"Wrote {HTML_PATH} ({HTML_PATH.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
