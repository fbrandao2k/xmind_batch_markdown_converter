# xmind-batch-to-markdown

Small Python script to batch-convert all `.xmind` files in a folder to Markdown, using the [xmindparser](https://github.com/tobyqin/xmindparser) CLI under the hood.[page:1]

This is just a thin convenience wrapper around `xmindparser`, which supports Xmind 8, Xmind (Zen), and Xmind 2026 files.[page:1]

## Motivation

If you have many Xmind mind maps and want them as plain Markdown (for example, to move them into a notes app, an AI model, or a Git repo), doing **Export → Markdown** one file at a time is tedious.  
This script walks a folder, finds all `.xmind` files, and converts each one to a `.md` file by calling the `xmindparser` command-line tool.

## How it works

- Uses Python’s `glob` to list all `.xmind` files under a target directory.
- For each file, calls the `xmindparser` CLI with the `-markdown` flag.
- If `xmindparser` is not installed yet, it installs the `xmindparser` package via `pip` and then retries.[page:1]

The actual parsing and Markdown generation are fully handled by `xmindparser` itself.[page:1]

## Requirements

- Python 3.7+
- `pip` available on your PATH
- `xmindparser` (installed automatically on first run if missing)[page:1]

## Installation

Clone this repository:

```bash
git clone https://github.com/fbrandao2k/xmind_batch_markdown_converter.git
cd xmind_batch_markdown_converter
```

## (Optional but recommended) Create a virtual environment:

```bash
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (cmd)
.venv\Scripts\activate.bat

# macOS/Linux
source .venv/bin/activate
```

Install `xmindparser` manually (or let the script do it on first run):

```bash
pip install xmindparser
```

Usage
* 1 - Create a folder called xmindFilesToBeConverted inside the project directory.
* 2 - Put all your .xmind files inside that folder.
* 3 - Run the script:

```bash
python convert_xmind_to_markdown.py
```

You should see output like:

```text
Converting: xmindFilesToBeConverted/example.xmind
Converting: xmindFilesToBeConverted/project-plan.xmind
```

`xmindparser` will write `.md` files next to the source `.xmind` files (following its default behavior for the command you use, e.g. `-markdown`).[web:17]

Script
The core script is:

```python
import os, sys, glob, subprocess

d = "xmindFilesToBeConverted"
files = glob.glob(os.path.join(d, "*.xmind"))

if not files:
    print("No .xmind files found in", d)
else:
    for f in files:
        print("Converting:", f)
        try:
            subprocess.run(["xmindparser", f, "-markdown"], check=True)
        except FileNotFoundError:
            print("`xmindparser` CLI not found; installing package...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "xmindparser"])
            subprocess.run(["xmindparser", f, "-markdown"], check=True)
        except subprocess.CalledProcessError as e:
            print("Conversion failed for", f, ":", e)
```

You can rename this file (for example, to convert_xmind_to_markdown.py) and adjust the d variable if you want to use a different folder name.

## Notes and limitations
All format and feature support comes from xmindparser itself, including:[web:17][web:23]
* Support for Xmind legacy (8) and Xmind Zen/Pro file types.
* Limitations such as not parsing some Pro features (Task info, audio notes), floating topics, certain relationships, summary and boundary info, and treating rich text as plain text.[web:17]
For details, see the upstream project’s README and examples.[web:17]

## Future ideas
This repo intentionally stays small and focused. Possible future improvements:
* Add command-line arguments for:
  *  Input directory
  *  Output directory
  *  Recursive folder traversal
* Add a simple GUI wrapper.
* Expose the conversion as an MCP server/tool so other clients can call it programmatically.
* Add tests that validate generated Markdown against sample Xmind files (using xmindparser’s example files).[web:20][web:30]

## Credits
All parsing and conversion logic is provided by:

tobyqin/xmindparser (MIT license)[web:17][web:23]

This repo is just a convenience wrapper for batch conversion.
