#!/usr/bin/env python

import os

import minify_html

SRC_DIR = "src"
BUILD_DIR = "build"

print("Building...")

for root, dirs, files in os.walk(SRC_DIR):
    for filename in files:
        if not filename.endswith(".html"):
            continue

        src_path = os.path.join(root, filename)
        with open(src_path) as f:
            minified = minify_html.minify(
                f.read(),
                minify_js=True,
                minify_css=True,
                remove_processing_instructions=True,
            )

        relative_path = os.path.relpath(root, SRC_DIR)
        if relative_path == ".":
            relative_path = ""
        build_path = os.path.join(BUILD_DIR, relative_path)

        os.makedirs(build_path, exist_ok=True)
        new_path = os.path.join(build_path, filename)
        with open(new_path, "w") as f:
            f.write(minified)
        print(f"Built: {new_path}")

print("Done!")
