#!/usr/bin/env python3
import os
import subprocess
import datetime
from pathlib import Path
from hashlib import md5
import urllib
from urllib import request, parse



if __name__ == "__main__":
    # Use the YYYYMMDD as the filename
    date = datetime.datetime.now().strftime('%Y%m%d')

    filepath = f"{os.environ['DEVNOTE_LOCAL']}/{date}.txt"
    if not Path(filepath).is_file():
        # Create our file if it doesn't exist
        subprocess.call(["touch", filepath])
        start_hash = ''
    else:
        # Read our md5 hash of the file
        with open(filepath, 'r') as infile:
            content = infile.read()
            start_hash = md5(content.encode()).hexdigest()
    
    # Open up nano to start editing file
    subprocess.call(["nano", filepath])

    # After closing nano read in our file here
    with open(filepath, 'r') as infile:
        content = infile.read()

    # Check our hash to see if we changed the file
    if start_hash == md5(content.encode()).hexdigest():
        print(f'devnote {date}.txt not modified')
        exit()

    # Post our file content to our endpoint
    data = parse.urlencode({
        'content': content,
        'date': date
    }).encode()
    req =  request.Request(os.environ['DEVNOTE_URL'], data=data)
    req.add_header('Authorization', f"Token {os.environ['DEVNOTE_TOKEN']}")
    req.add_header('Content-Type', 'application/json')
    try:
        with request.urlopen(req, timeout=30) as response:
            print(response)
    except urllib.error.HTTPError as e:
        print(f'failed to post devnote: {e}')

    