---
name: markdown-docs
description: Convert Markdown to HTML, build a table of contents, list links, and count words, offline, with Python. Use when the user or agent wants to publish, navigate, or measure a Markdown document.
---

# Markdown Docs

Work with Markdown documents without a heavy app. Convert to a standalone
HTML page, build a table of contents, list every link, or get word counts
and reading time. No cloud, no upload. Files stay local.

## When to use

- "Convert this Markdown to HTML"
- "Build a table of contents for this doc"
- "List all the links in this file"
- "How long is this document?"

## Workflow

1. Check the file is Markdown. If it is not, say so and stop.
2. Get the shape of the document first:
   ```sh
   python tools/mdtool.py stats doc.md
   python tools/mdtool.py toc doc.md
   ```
   Report word count, headings, links, and reading time.
3. Convert to HTML when asked:
   ```sh
   python tools/mdtool.py to-html doc.md doc.html
   ```
   The output is a single standalone HTML file — open it in any browser.
4. List links when asked:
   ```sh
   python tools/mdtool.py links doc.md
   ```
   Report every link and its text. Do not follow the links unless asked.
5. Confirm the output file exists and report its path.

## Examples

**How long is this document?**
```sh
python tools/mdtool.py stats README.md
# Words: 1240 — Headings: 8 — Links: 5 — Reading time: about 6 minute(s)
```

**Publish a doc as a web page**
```sh
python tools/mdtool.py to-html guide.md guide.html
# Converted: guide.md -> guide.html
```

**Find every link before sharing the doc**
```sh
python tools/mdtool.py links guide.md
# https://example.com/guide  (full guide)
```

## Rules

- Never overwrite the input file. Always write to a new output file.
- The HTML converter handles headings, bold, italic, code, lists, and links. It is not a full Markdown renderer — say so if the document uses tables or footnotes.
- Do not rewrite the document's words when converting; formatting only.
- If the document has no headings, say the table of contents would be empty instead of inventing one.
- Keep the original `.md` file as the source of truth; the HTML is a copy.
