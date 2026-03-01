# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This is a Sphinx documentation site — a collection of copy-paste Python library examples organized as a reference/tutorial book. Each library lives in its own subdirectory with a `README.rst` file and standalone `.py` example scripts.

## Build Commands

```bash
# Build HTML documentation
uv sync
uv run make html
```

The built site goes to `build/html/`. Open `build/html/index.html` to preview locally.

## Project Structure

- **`index.rst`** — top-level table of contents, controls what appears in the docs
- **`conf.py`** — Sphinx configuration (theme: furo, extensions: myst_parser, sphinx_design, sphinx_copybutton)
- **`<library>/README.rst`** — documentation page for each library (RST format)
- **`<library>/*.py`** — standalone example scripts included via `.. literalinclude::` directives
- **`<library>/*.png`** — output images referenced with `.. figure::` directives
- **`_static/`** — CSS and logo assets

## Content Conventions

Each library page follows this pattern:
1. A question as the section heading (e.g., "How to draw a bar chart?")
2. Brief description of the library
3. Install instruction in a `.. code::` block
4. One or more examples using `.. literalinclude:: script.py`
5. Optional `.. figure:: image.png` showing expected output
6. A `.. seealso::` block linking to official docs

Example scripts should be **self-contained and runnable** — no shared utilities or imports from sibling directories.

## Adding a New Library

1. Create a subdirectory `<library>/`
2. Write `<library>/README.rst` following the conventions above
3. Add standalone `.py` example scripts
4. Add the entry to `index.rst` under the appropriate section: `<library>/README.rst`
5. Run `make html` to verify it builds without warnings

## Formats

- Documentation pages use **RST** (`.rst`), not Markdown — `myst_parser` is installed but RST is the primary format used
- The `exclude_patterns` in `conf.py` excludes `README.md` (the GitHub-facing readme) and `learning_goals.md` files from the Sphinx build
