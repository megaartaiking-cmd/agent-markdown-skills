# agent-markdown-skills

> **Agent Skills for Markdown — convert to HTML, build a table of contents, check links, and count words. Offline, stdlib-only Python.**

**1 skill · 1 CLI · 0 dependencies · 100% offline**

[![GitHub stars](https://img.shields.io/github/stars/megaartaiking-cmd/agent-markdown-skills?style=social)](https://github.com/megaartaiking-cmd/agent-markdown-skills/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](tools/mdtool.py)

AI agents are great at code, but Markdown documents still mean opening a notes app or a docs editor to do the simplest jobs — convert to HTML, list the links, or count the words. This repo fixes that gap: a small Agent Skill (SKILL.md) plus a tiny Python CLI that works with Markdown files — in the terminal, on the user's own PC.

Works with Claude Code, Cursor, GitHub Copilot, Codex, Gemini CLI, and any agent that reads SKILL.md files.

## Why this exists

Agent Skills are the fastest-growing category on GitHub — small, composable skill bundles, one job per skill, install in one step. Markdown is the format agents write in most, and there is no small, offline, agent-native way to publish it, navigate it, or measure it.

This one is:

- **Agent-native** — a skill in the open SKILL.md format, one job, clear rules
- **Offline** — no upload, no cloud, files never leave the PC
- **Lightweight** — stdlib-only Python, no pip install, no heavy app
- **Safe** — it never overwrites the input file; the HTML is a copy, the `.md` stays the source of truth

## Skills

| Skill | What it does | Command |
|---|---|---|
| `markdown-docs` | Convert to HTML, TOC, links, word count | `mdtool.py` |

The skill lives in `skills/markdown-docs/SKILL.md` — copy that folder into your agent's skills folder, or point your agent at this repo.

## Quick start

```sh
git clone https://github.com/megaartaiking-cmd/agent-markdown-skills.git
cd agent-markdown-skills

# 1. Word count, headings, links, reading time
python tools/mdtool.py stats examples/sample.md

# 2. Build a table of contents
python tools/mdtool.py toc examples/sample.md

# 3. Convert to a standalone HTML page
python tools/mdtool.py to-html examples/sample.md sample.html
```

No installation needed — Python 3.9+ is the only requirement.

## Usage

```sh
# Word count, headings, links, reading time
python tools/mdtool.py stats doc.md

# Print a table of contents from headings
python tools/mdtool.py toc doc.md

# List all links in the document
python tools/mdtool.py links doc.md

# Convert Markdown to a standalone HTML page
python tools/mdtool.py to-html doc.md doc.html
```

See [examples/commands.md](examples/commands.md) for all commands, and [examples/sample.md](examples/sample.md) for a small file to try them on.

## How it works

1. You (or your agent) describe the job in plain words: "convert this to HTML and list the links".
2. The skill in `skills/markdown-docs/` tells the agent the exact workflow, the command to run, and the rules — never overwrite the original, always write to a new file.
3. `tools/mdtool.py` (stdlib-only Python) does the work locally and reports the output path.
4. Nothing is uploaded. The work happens on your PC.

## Works with

- Claude Code
- Cursor
- GitHub Copilot
- Codex
- Gemini CLI
- Any agent that reads Agent Skills (SKILL.md)

Copy `skills/markdown-docs/` into your agent's skills directory, or ask your agent to read the SKILL.md file in this repo directly.

## FAQ

**Does it need the internet?**
No. After `git clone`, everything runs offline.

**What Markdown does the HTML converter handle?**
Headings, bold, italic, code, lists, and links. It is not a full Markdown renderer — tables and footnotes are not converted, and the skill says so.

**Does converting change my words?**
No. Formatting only — the text stays exactly as written.

**What if my document has no headings?**
The table of contents would be empty, and the tool says so instead of inventing one.

**Will it run on an old PC?**
Yes — that is the point. It is a small Python script with no dependencies.

**Can I add a skill?**
Yes — copy `skills/markdown-docs/` as a template, write a SKILL.md with a clear name, description, workflow, and rules, and open a pull request.

## Contributing

Issues and pull requests are welcome. Keep skills small, one job per skill, with a tested command in `tools/mdtool.py`. Please do not add dependencies — stdlib only.

## License

MIT — see [LICENSE](LICENSE).

## More Agent Skills

More offline Agent Skills by the same author — one focused skill per repo:

- [agent-audio-skills](https://github.com/megaartaiking-cmd/agent-audio-skills) — Trim podcasts, normalize volume, extract audio from video
- [agent-csv-skills](https://github.com/megaartaiking-cmd/agent-csv-skills) — Clean, filter, summarize CSVs; convert to JSON and Markdown
- [agent-json-skills](https://github.com/megaartaiking-cmd/agent-json-skills) — Validate, format, flatten, query, and diff JSON
- [agent-git-skills](https://github.com/megaartaiking-cmd/agent-git-skills) — Commit messages, changelogs, repo health, branch cleanup
- [agent-text-skills](https://github.com/megaartaiking-cmd/agent-text-skills) — Summarize text, extract keywords, readability, dedupe
- [agent-file-skills](https://github.com/megaartaiking-cmd/agent-file-skills) — Organize folders, find duplicates, batch rename
- [agent-sql-skills](https://github.com/megaartaiking-cmd/agent-sql-skills) — Explore SQLite, run queries, export to CSV
- [agent-video-skills](https://github.com/megaartaiking-cmd/agent-video-skills) — Edit video offline — trim, make Shorts, add titles, colour-grade
- [LiteCut Pro](https://github.com/megaartaiking-cmd/LIGHT-CUT-VIDEO-EDITOR) — lightweight offline video editor for Windows 10

---

**Keywords:** agent skills, AI agent Markdown, Markdown to HTML, table of contents, Markdown word count, Claude Code skills, Cursor skills, offline Markdown tool, Python Markdown CLI
