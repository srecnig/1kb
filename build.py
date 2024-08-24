#!/usr/bin/env python

import os

import minify_html

SRC_DIR = "src"
BUILD_DIR = "build"

print("Building...")
for filename in os.listdir(SRC_DIR):
    with open(os.path.join(SRC_DIR, filename)) as f:
        if not filename.endswith(".html"):
            continue
        minified = minify_html.minify(
            f.read(),
            minify_js=True,
            minify_css=True,
            remove_processing_instructions=True,
        )
    with open(os.path.join(BUILD_DIR, filename), "w") as f:
        f.write(minified)

print("Done!")
