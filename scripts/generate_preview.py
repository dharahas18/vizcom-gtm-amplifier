#!/usr/bin/env python3
"""
generate_preview.py — produces a browser-openable preview.html for a drop folder.

Usage:
    python scripts/generate_preview.py outputs/{slug}/

Reads blog.md / linkedin.md / x_thread.md / geo_aeo.md / pr_pitch.md / summary.md
in the given folder, renders them as styled channel cards in a single HTML file,
and writes preview.html alongside them.

No external dependencies. Markdown rendering is minimal but sufficient for the
patterns Vizcom output uses (headers, bold/italic, links, images, blockquotes,
horizontal rules, paragraphs).
"""
from __future__ import annotations

import html as html_lib
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# minimal markdown → HTML (no external deps)
# ---------------------------------------------------------------------------

def md_to_html(text: str) -> str:
    """Render a small, agent-friendly subset of markdown to HTML."""
    lines = text.splitlines()
    out: list[str] = []
    in_blockquote = False
    in_paragraph = False
    in_list = False

    def close_paragraph():
        nonlocal in_paragraph
        if in_paragraph:
            out.append("</p>")
            in_paragraph = False

    def close_blockquote():
        nonlocal in_blockquote
        if in_blockquote:
            close_paragraph()
            out.append("</blockquote>")
            in_blockquote = False

    def close_list():
        nonlocal in_list
        if in_list:
            out.append("</ul>")
            in_list = False

    def inline(s: str) -> str:
        # ![alt](path) — image
        s = re.sub(
            r"!\[([^\]]*)\]\(([^)]+)\)",
            lambda m: f'<img src="{html_lib.escape(m.group(2))}" '
                      f'alt="{html_lib.escape(m.group(1))}" />',
            s,
        )
        # [text](url) — link
        s = re.sub(
            r"\[([^\]]+)\]\(([^)]+)\)",
            lambda m: f'<a href="{html_lib.escape(m.group(2))}" '
                      f'target="_blank">{html_lib.escape(m.group(1))}</a>',
            s,
        )
        # **bold**
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        # *italic*  (avoid matching **)
        s = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", s)
        # `code`
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        return s

    for raw in lines:
        line = raw.rstrip()

        # horizontal rule
        if re.match(r"^\s*---+\s*$", line):
            close_list(); close_blockquote(); close_paragraph()
            out.append("<hr/>")
            continue

        # headers
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            close_list(); close_blockquote(); close_paragraph()
            level = len(m.group(1))
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            continue

        # blockquote
        if line.startswith("> "):
            close_list(); close_paragraph()
            if not in_blockquote:
                out.append("<blockquote>")
                in_blockquote = True
            out.append(f"<p>{inline(line[2:].strip())}</p>")
            continue
        else:
            close_blockquote()

        # unordered list
        if re.match(r"^[-*]\s+", line):
            close_paragraph()
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(line[2:].strip())}</li>")
            continue
        else:
            close_list()

        # blank line → paragraph break
        if not line.strip():
            close_paragraph()
            continue

        # default: paragraph text
        if not in_paragraph:
            out.append("<p>")
            in_paragraph = True
        out.append(inline(line))
        out.append("<br/>")

    close_list(); close_blockquote(); close_paragraph()
    # trim trailing <br/> immediately before </p>
    return "\n".join(out).replace("<br/>\n</p>", "</p>")


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse a leading YAML-ish frontmatter block. Returns (fields, body)."""
    if not text.startswith("---\n"):
        return {}, text
    try:
        end = text.index("\n---\n", 4)
    except ValueError:
        return {}, text
    fm_text = text[4:end]
    body = text[end + 5:]
    fields = {}
    for raw in fm_text.splitlines():
        if ":" in raw and not raw.startswith(" "):
            k, _, v = raw.partition(":")
            fields[k.strip()] = v.strip().strip('"').strip("'")
    return fields, body


def read_md(folder: Path, name: str) -> str:
    p = folder / name
    return p.read_text(encoding="utf-8") if p.exists() else ""


def count_words(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def find_image(folder: Path) -> str | None:
    for candidate in ("hero.jpg", "hero.jpeg", "hero.png", "hero.webp"):
        p = folder / candidate
        if p.exists():
            return candidate
    return None


# ---------------------------------------------------------------------------
# template
# ---------------------------------------------------------------------------

CSS = """
* { box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
  background: #f3f2ef; color: #1d1d1f;
  max-width: 920px; margin: 0 auto; padding: 2rem 1.5rem 4rem;
  line-height: 1.55;
}
.page-header {
  margin-bottom: 2rem; padding-bottom: 1rem; border-bottom: 1px solid #d4d4d4;
}
.page-header h1 { font-size: 1.6rem; margin: 0 0 .35rem; letter-spacing: -.01em; }
.page-meta { color: #6e6e73; font-size: .82rem; }
.page-meta code { background: #fff; padding: 1px 6px; border-radius: 3px; border: 1px solid #d4d4d4; font-size: .78rem; }

.channel {
  background: #fff; border: 1px solid #d4d4d4; border-radius: 10px;
  margin-bottom: 1.25rem; overflow: hidden;
}
.channel-bar {
  display: flex; align-items: center; gap: .6rem;
  padding: .75rem 1rem; background: #fafafa; border-bottom: 1px solid #e5e5e5;
  font-size: .85rem;
}
.channel-bar .name { font-weight: 600; font-size: .95rem; }
.channel-bar .meta { margin-left: auto; color: #6e6e73; font-size: .78rem; }
.channel-body { padding: 1.25rem 1.5rem; }

/* BLOG */
.blog .channel-body h1 { font-size: 1.55rem; margin: 0 0 .25rem; letter-spacing: -.01em; }
.blog .channel-body h2 { font-size: 1.15rem; margin: 1.6rem 0 .5rem; border-bottom: 1px solid #eee; padding-bottom: .3rem; }
.blog .channel-body h3 { font-size: 1.0rem; margin: 1.2rem 0 .3rem; color: #444; }
.blog .channel-body img { max-width: 100%; height: auto; border-radius: 5px; margin: .9rem 0; display: block; }
.blog .channel-body p { margin: .65rem 0; }
.blog .channel-body em { color: #555; font-style: italic; }
.blog .channel-body blockquote { margin: 1rem 0; padding: .5rem 1rem; border-left: 3px solid #ccc; color: #555; background: #fafafa; }
.blog .channel-body hr { border: none; border-top: 1px solid #eee; margin: 1.5rem 0; }

/* LINKEDIN */
.linkedin .channel-bar .name::before { content: "in  "; color: #0a66c2; font-weight: 700; }
.linkedin .channel-body { padding: 1rem 1.5rem 1.5rem; }
.linkedin .post-text { white-space: pre-wrap; font-size: .95rem; }
.linkedin .post-image { width: 100%; max-height: 520px; object-fit: cover; border-radius: 4px; margin-top: 1rem; }
.linkedin .carousel-note { font-size: .78rem; color: #6e6e73; margin-top: .4rem; }

/* X */
.x .channel-bar .name::before { content: "𝕏  "; font-weight: 700; }
.x .tweet { padding: 1rem 1.5rem; border-bottom: 1px solid #eff3f4; }
.x .tweet:last-child { border-bottom: none; }
.x .tweet-meta { color: #536471; font-size: .82rem; margin-bottom: .35rem; }
.x .tweet-meta strong { color: #0f1419; }
.x .tweet-text { white-space: pre-wrap; font-size: .98rem; color: #0f1419; }
.x .tweet-image { width: 100%; max-height: 480px; object-fit: cover; border-radius: 12px; margin-top: .6rem; border: 1px solid #eff3f4; }

/* GEO/AEO */
.geo .channel-bar .name::before { content: "🔍  "; }
.geo .channel-body p:first-child { font-weight: 600; }

/* PR */
.pr .channel-bar .name::before { content: "📧  "; }
.pr .channel-body { font-family: ui-monospace, Menlo, monospace; font-size: .88rem; background: #fdfdfd; }

/* SUMMARY collapsible */
details.summary-block { background: #fafafa; border: 1px solid #d4d4d4; border-radius: 10px; padding: .75rem 1rem; margin-top: 1.5rem; }
details.summary-block summary { cursor: pointer; font-weight: 600; }
details.summary-block .channel-body { padding-top: .75rem; }
"""


def render_blog(folder: Path) -> str:
    body = read_md(folder, "blog.md")
    if not body:
        return ""
    words = count_words(body)
    return f"""
  <section class="channel blog">
    <div class="channel-bar">
      <span class="name">Blog</span>
      <span class="meta">vizcom.com/blog · {words} words</span>
    </div>
    <div class="channel-body">{md_to_html(body)}</div>
  </section>
"""


def render_linkedin(folder: Path) -> str:
    body = read_md(folder, "linkedin.md")
    if not body:
        return ""
    # Separate the IMAGE / CAROUSEL marker lines from the post text
    text_lines = []
    image_path = None
    carousel = None
    for line in body.splitlines():
        if line.startswith("IMAGE:"):
            image_path = line.split(":", 1)[1].strip().lstrip("./")
        elif line.startswith("CAROUSEL"):
            carousel = line.split(":", 1)[1].strip() if ":" in line else line
        else:
            text_lines.append(line)
    post_text = "\n".join(text_lines).strip()
    chars = len(post_text)
    img_html = ""
    if image_path:
        img_html = f'<img class="post-image" src="{html_lib.escape(image_path)}" alt="hero render"/>'
    carousel_html = ""
    if carousel:
        carousel_html = f'<div class="carousel-note">Carousel: {html_lib.escape(carousel)}</div>'
    return f"""
  <section class="channel linkedin">
    <div class="channel-bar">
      <span class="name">LinkedIn</span>
      <span class="meta">linkedin.com/company/vizcomhq · {chars} chars</span>
    </div>
    <div class="channel-body">
      <div class="post-text">{html_lib.escape(post_text)}</div>
      {img_html}
      {carousel_html}
    </div>
  </section>
"""


def render_x(folder: Path) -> str:
    body = read_md(folder, "x_thread.md")
    if not body:
        return ""
    # Split into tweet sections by # Tweet N markers
    tweets = []
    current_lines: list[str] = []
    current_image: str | None = None
    for line in body.splitlines():
        m = re.match(r"^#+\s*Tweet\s+\d+", line, re.IGNORECASE)
        if m:
            if current_lines:
                tweets.append((("\n".join(current_lines)).strip(), current_image))
            current_lines, current_image = [], None
            continue
        if line.startswith("IMAGE:"):
            current_image = line.split(":", 1)[1].strip().lstrip("./")
            continue
        if line.strip() == "---":
            continue
        current_lines.append(line)
    if current_lines:
        tweets.append((("\n".join(current_lines)).strip(), current_image))
    tweets_html = ""
    for text, image_path in tweets:
        chars = len(text)
        img_html = (f'<img class="tweet-image" src="{html_lib.escape(image_path)}" '
                    f'alt="tweet image"/>' if image_path else "")
        tweets_html += f"""
    <div class="tweet">
      <div class="tweet-meta"><strong>Vizcom</strong> @Vizcom_ · just now · {chars} chars</div>
      <div class="tweet-text">{html_lib.escape(text)}</div>
      {img_html}
    </div>
"""
    return f"""
  <section class="channel x">
    <div class="channel-bar">
      <span class="name">X / Twitter</span>
      <span class="meta">x.com/Vizcom_ · {len(tweets)} tweet pair</span>
    </div>
    {tweets_html}
  </section>
"""


def render_geo(folder: Path) -> str:
    body = read_md(folder, "geo_aeo.md")
    if not body:
        return ""
    words = count_words(body)
    return f"""
  <section class="channel geo">
    <div class="channel-bar">
      <span class="name">GEO / AEO</span>
      <span class="meta">answer-engine optimized · {words} words</span>
    </div>
    <div class="channel-body">{md_to_html(body)}</div>
  </section>
"""


def render_pr(folder: Path) -> str:
    body = read_md(folder, "pr_pitch.md")
    if not body:
        return ""
    sentence_count = body.count(". ") + (1 if body.strip().endswith(".") else 0)
    return f"""
  <section class="channel pr">
    <div class="channel-bar">
      <span class="name">PR pitch</span>
      <span class="meta">trade press · ~{sentence_count} sentences</span>
    </div>
    <div class="channel-body">{md_to_html(body)}</div>
  </section>
"""


def render_summary(folder: Path) -> str:
    body = read_md(folder, "summary.md")
    if not body:
        return ""
    return f"""
  <details class="summary-block">
    <summary>📋 Run summary &amp; voice self-check</summary>
    <div class="channel-body">{md_to_html(body)}</div>
  </details>
"""


def build(folder: Path) -> str:
    summary_text = read_md(folder, "summary.md")
    summary_fm, _ = parse_frontmatter(summary_text)
    title_match = re.match(r"^# Signal:\s*(.+)$", summary_text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else folder.name

    slug = folder.name
    # Try to pluck signal_type from summary body
    type_match = re.search(r"\*\*Type:\*\*\s*`?(\w+)`?", summary_text) or \
                 re.search(r"Type:\s*`(\w+)`", summary_text)
    signal_type = type_match.group(1) if type_match else "(unknown)"

    sections = [
        render_blog(folder),
        render_linkedin(folder),
        render_x(folder),
        render_geo(folder),
        render_pr(folder),
        render_summary(folder),
    ]
    body_html = "\n".join(s for s in sections if s)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Preview — {html_lib.escape(slug)}</title>
  <style>{CSS}</style>
</head>
<body>
  <header class="page-header">
    <h1>{html_lib.escape(title)}</h1>
    <div class="page-meta">
      slug <code>{html_lib.escape(slug)}</code>
      &nbsp;·&nbsp; type <code>{html_lib.escape(signal_type)}</code>
      &nbsp;·&nbsp; channels rendered below in the recommended publishing order
    </div>
  </header>
{body_html}
</body>
</html>
"""


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/generate_preview.py outputs/{slug}/",
              file=sys.stderr)
        return 1
    folder = Path(sys.argv[1])
    if not folder.is_dir():
        print(f"Not a directory: {folder}", file=sys.stderr)
        return 1
    html = build(folder)
    out = folder / "preview.html"
    out.write_text(html, encoding="utf-8")
    print(f"Wrote {out} ({out.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
