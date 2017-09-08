#!/usr/bin/env python3
# Generate CSS code for KwPastebin.
# License: 3-clause BSD.

from sys import argv
from pygments.formatters import get_formatter_by_name
from pygments.styles import get_all_styles

if len(argv) != 2:
    print("Usage: ./generate_css.py style > static/code.css\nStyles available:", ', '.join([str(i) for i in get_all_styles()]))
    exit(2)

style = argv[1]
formatter = get_formatter_by_name('html', style=style)
print("/* Pygments Style {0} for KwPastebin */\n".format(style))
print(formatter.get_style_defs('.highlight pre'))
print("\ntable.highlighttable {width: 100%;} td.linenos {text-align: right; width: 4em;}")
