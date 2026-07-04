# AGENTS.md — Ninja Urban Farming

## Project Overview

A comprehensive Indonesian-language guidebook on organic urban farming (*Ninja Urban Farming*). This is a **writing/editorial project**, not a software project.

## File Structure

- **`Ninja-Urban-Farming.md`** — Main manuscript. Very large single-file markdown. Source of truth.
- **`BluePrint.md`** — Condensed summary/outline of the book. Useful as a quick reference.
- **`inject_visuals.py`** — Replaces placeholder comments in the manuscript with mermaid diagrams and image references. Run after significant structure changes.
- **`drafts/content/`** — Content drafts by domain (aquaculture, entomology, horticulture, soil biochemistry, integrated systems). These feed into the main manuscript.
- **`drafts/editorial/`** — Editorial pipeline: gap analysis, structured draft, copy-edited version, review reports.
- **`drafts/prompts/`** — AI prompt templates for each writing/editing stage (cartographer, copy editor, technical reviewer, layout designer, etc.).
- **`drafts/publishing/`** — Final staged outputs: layout draft, final manuscript.
- **`obsidian/urban_farming/`** — Obsidian vault for note-taking and knowledge management. Separate from the manuscript pipeline.
- **`roblox/`** — Empty directory. Reserved for future game-related content.

## Key Conventions

### Language
All content is in **Indonesian** (Bahasa Indonesia). Do not translate to English.

### Visual Injection Syntax
`inject_visuals.py` matches lines starting with specific prefix patterns, e.g.:
- `**[Diagram X.X:` → replaced with mermaid code blocks
- `**[Gambar X.X:` → replaced with image markdown referencing paths under `/Users/satyaadidharma/.gemini/...`

When adding new diagrams or images, follow these placeholder patterns. Run `python inject_visuals.py` after editing placeholders.

### Editorial Pipeline
Content flows: `drafts/content/` → `drafts/editorial/` → `drafts/publishing/` → `Ninja-Urban-Farming.md`

The prompts directory contains the exact AI agent instructions used for each stage. When editing content through similar AI-assisted workflows, refer to these prompts for consistency.

## Commands

```bash
python inject_visuals.py
```

No build, test, lint, or typecheck exists. This is a pure markdown project.
