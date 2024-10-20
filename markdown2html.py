#!/usr/bin/env python3

import sys
import os
import markdown

# Check if the number of arguments is less than 2
if len(sys.argv) != 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

markdown_file = sys.argv[1]
html_file = sys.argv[2]

# Check if the Markdown file exists
if not os.path.isfile(markdown_file):
    print(f"Missing {markdown_file}", file=sys.stderr)
    sys.exit(1)

# Convert Markdown to HTML
with open(markdown_file, 'r') as md_file:
    markdown_content = md_file.read()
    html_content = markdown.markdown(markdown_content)

# Write the HTML output to the output file
with open(html_file, 'w') as html_out:
    html_out.write(html_content)

sys.exit(0)
