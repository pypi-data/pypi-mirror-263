#!/usr/bin/env python3

import re
import subprocess
import mkdocs
import tempfile
import os
import shutil

PATTERN = r'(<iframe\s+.*?asyncapi="([^"]*)".*?src="([^"]*)".*?>)'
MARKER = re.compile(PATTERN)

class AsyncAPIPlugin(mkdocs.plugins.BasePlugin):
    def on_page_markdown(self, markdown, page, config, files):
        match = MARKER.search(markdown)
        if match is None:
            return markdown
        if not install_nodejs():
            print("Failed to install nodejs and npm")
            return markdown
        
       
        indir = "docs"
        path = match.group(2)
        html_path = os.path.splitext(path)[0] + '.html'
        newfile = os.path.join(indir, html_path)

        print(f'asyncapi path: {path}')
        print(f'src path: {html_path}')

        if os.path.isfile(newfile):
            print(f'{newfile} exists')
            return markdown
        
        markdown = re.sub(PATTERN, '', markdown)
        with tempfile.TemporaryDirectory() as outdir:
            infile = os.path.join(indir, path)
            print("Generating HTML from", infile)
            subprocess.run(
                [
                    "ag",
                    infile,
                    "@asyncapi/html-template",
                    "-p",
                    "singleFile=true"
                    "--force-write",
                    "-o",
                    outdir,
                ],
                check=True,
            )
            print ("Done generating HTML")
            outfile = os.path.join(outdir, 'index.html')
            print("Moving", outfile, "to", newfile)

            shutil.copy(outfile, newfile)

        return markdown

def install_nodejs():
    if is_installed('npm') and is_installed('nodejs'):
        print("###nodejs and npm already installed###")
        return True
    print("Installing nodejs and npm")
    try:
        subprocess.run(
            [
                "apk",
                "update"
            ],
            check=True,
        )
        subprocess.run(
            [
                "apk",
                "add",
                "--no-cache",
                "nodejs",
                "npm"
            ],
            check=True,
        )
        subprocess.run(
            [
                "npm",
                "install",
                "-g",
                "@asyncapi/generator"
            ],
            check=True,
        )
    except:
        return False
    print("###Installed nodejs and npm###")
    return True
def is_installed(command):
    try:
        subprocess.check_output([command, '--version'])
        return True
    except FileNotFoundError:
        return False