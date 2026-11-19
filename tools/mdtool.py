#!/usr/bin/env python3
"""mdtool.py — tiny offline Markdown CLI for agent-markdown-skills.

Stdlib only. No dependencies, no network, no cloud.
Converts Markdown to HTML, builds a table of contents,
lists links, and counts words.

Usage:
  python tools/mdtool.py to-html doc.md doc.html
  python tools/mdtool.py toc doc.md
  python tools/mdtool.py links doc.md
  python tools/mdtool.py stats doc.md
"""
import argparse
import html
import os
import re
import sys


def fail(msg):
    print(f"mdtool: error: {msg}", file=sys.stderr)
    return 2


def read_md(path):
    if not os.path.isfile(path):
        print(f"mdtool: error: file not found: {path}", file=sys.stderr)
        return None
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError as e:
        print(f"mdtool: error: cannot read {path}: {e}", file=sys.stderr)
        return None


def inline(text):
    """Convert inline Markdown (bold, italic, code, links) to HTML."""
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def to_html_body(text):
    out, in_list = [], False
    for line in text.splitlines():
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            if in_list:
                out.append("</ul>")
                in_list = False
            level = len(m.group(1))
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
        elif line.startswith("- ") or line.startswith("* "):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(line[2:].strip())}</li>")
        elif line.strip() == "":
            if in_list:
                out.append("</ul>")
                in_list = False
        elif line.strip().startswith("```"):
            out.append("<pre><code>code block</code></pre>")
        else:
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f"<p>{inline(line.strip())}</p>")
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def headings(text):
    found = []
    for line in text.splitlines():
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            found.append((len(m.group(1)), m.group(2).strip()))
    return found


def cmd_to_html(a):
    text = read_md(a.input)
    if text is None:
        return 2
    body = to_html_body(text)
    page = ("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
            f"<title>{html.escape(os.path.basename(a.input))}</title>\n</head>\n<body>\n"
            f"{body}\n</body>\n</html>\n")
    parent = os.path.dirname(os.path.abspath(a.output))
    os.makedirs(parent, exist_ok=True)
    with open(a.output, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"Converted: {a.input} -> {a.output}")
    return 0


def cmd_toc(a):
    text = read_md(a.input)
    if text is None:
        return 2
    found = headings(text)
    if not found:
        print("No headings found.")
        return 0
    for level, title in found:
        indent = "  " * (level - 1)
        anchor = re.sub(r"[^a-z0-9 ]", "", title.lower()).replace(" ", "-")
        print(f"{indent}- [{title}](#{anchor})")
    return 0


def cmd_links(a):
    text = read_md(a.input)
    if text is None:
        return 2
    links = re.findall(r"\[([^\]]*)\]\(([^)]+)\)", text)
    bare = re.findall(r"(?<!\]\()(?<!href=\")https?://[^\s)>\"]+", text)
    if not links and not bare:
        print("No links found.")
        return 0
    for label, url in links:
        print(f"{url}  ({label or 'no text'})")
    for url in bare:
        if url not in [u for _, u in links]:
            print(f"{url}  (bare URL)")
    print(f"\nTotal: {len(links) + len(bare)} link(s)")
    return 0


def cmd_stats(a):
    text = read_md(a.input)
    if text is None:
        return 2
    words = re.findall(r"[A-Za-z0-9']+", text)
    found = headings(text)
    links = re.findall(r"\[([^\]]*)\]\(([^)]+)\)", text)
    code_blocks = text.count("```") // 2
    minutes = max(1, round(len(words) / 200))
    print(f"File: {a.input}")
    print(f"Words: {len(words)}")
    print(f"Characters: {len(text)}")
    print(f"Headings: {len(found)}")
    print(f"Links: {len(links)}")
    print(f"Code blocks: {code_blocks}")
    print(f"Reading time: about {minutes} minute(s) at 200 words/minute")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(prog="mdtool", description="Tiny offline Markdown CLI (stdlib only).")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("to-html", help="Convert Markdown to a standalone HTML page")
    s.add_argument("input"); s.add_argument("output")
    s.set_defaults(fn=cmd_to_html)

    s = sub.add_parser("toc", help="Print a table of contents from headings")
    s.add_argument("input")
    s.set_defaults(fn=cmd_toc)

    s = sub.add_parser("links", help="List all links in the document")
    s.add_argument("input")
    s.set_defaults(fn=cmd_links)

    s = sub.add_parser("stats", help="Word count, headings, links, reading time")
    s.add_argument("input")
    s.set_defaults(fn=cmd_stats)

    a = p.parse_args(argv)
    return a.fn(a)


if __name__ == "__main__":
    raise SystemExit(main())
