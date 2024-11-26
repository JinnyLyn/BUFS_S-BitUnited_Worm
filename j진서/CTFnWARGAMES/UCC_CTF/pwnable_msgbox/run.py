#!/usr/bin/env python3

import subprocess
import sys
import tempfile
import pathlib

with tempfile.NamedTemporaryFile() as f:
    try:
        print("exploit size: ")
        n = int(input())
        if n > 0x100000:
            exit()

        print("exploit: ")
        exploit = b''
        for i in range(n):
            exploit += sys.stdin.buffer.read(1)

        f.write(exploit)
        f.flush()

        subprocess.run(["timeout", "30", f"{pathlib.Path(__file__).parent}/run.sh", f.name])
    except:
        exit()