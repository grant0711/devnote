#!/usr/bin/env python3
"""
Description:
Local executable file to capture devnote content and post content
to remote server

Within install, this file is rendered executable and copied over to /bin
"""
import os
import sys
import subprocess
import datetime
from pathlib import Path
from hashlib import md5
import urllib
from urllib import request, parse


class DevNote():
    def __init__(self, now: datetime.datetime=None):
        if now == None:
            now = datetime.datetime.now(datetime.timezone.utc)
        self.date = now.strftime('%Y-%m-%d')
        self.filepath = self.set_filepath()
        self.create()

    def set_filepath(self):
        return f"{os.environ['DEVNOTE_LOCAL']}/{self.date}.txt"

    def title(self):
        return f"# Notes for {self.date}:\n"
        
    def create(self):
        if not Path(self.filepath).is_file():
            subprocess.call(["touch", self.filepath])
            self.append(self.title(), with_update=False)

    def append(self, text: str, with_update: bool=True):
        with open(self.filepath, 'a') as file:
            file.write(text)
            file.write('\n')
        if with_update:
            self.post()

    def interactive_edit(self):
        start_hash = self.hash()
        subprocess.call(["nano", self.filepath])
        end_hash = self.hash()
        if start_hash != end_hash:
            self.post()

    def readfile(self):
        with open(self.filepath, 'r') as file:
            return file.read()

    def hash(self):
        content = self.readfile()
        return md5(content.encode()).hexdigest

    def post(self):
        data = parse.urlencode({
            'content': self.readfile(),
            'date': self.date
        }).encode()
        req =  request.Request(os.environ['DEVNOTE_URL'], data=data)
        req.add_header('Authorization', f"Token {os.environ['DEVNOTE_TOKEN']}")
        req.add_header('Content-Type', 'application/json')
        try:
            with request.urlopen(req, timeout=30) as response:
                print(response)
        except urllib.error.HTTPError as e:
            print(f'Sync failed: {e}')


if __name__ == "__main__":
    devnote = DevNote()
    if len(sys.argv) > 1:
        devnote.append(' '.join(sys.argv[1:]))
    else:
        devnote.interactive_edit()
