#!/usr/bin/env python3
"""PLANET - The Day In Review (wallet w7, news-image-20261119).

A magazine-cover take on 19 November 2026. The bundled cover art is
checked for a valid PNG header and a sane file size, then delivered
to /output/entry.png for the make.fun program runner.
"""

import os
import shutil
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
ART = os.path.join(ROOT, "entry.png")
OUT_DIR = "/output"
OUT_FILE = os.path.join(OUT_DIR, "entry.png")
SIGNATURE = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
LIMIT = 1024 * 1024

COVER_LINES = [
    "APEC Shenzhen: Trump, Xi and Putin in the same room",
    "GTA VI finally launches, thirteen years after its predecessor",
    "Cyclone Akvan closes in on the Andhra and Odisha coasts",
    "Democrats nominate Hakeem Jeffries for Speaker",
    "US and Iran trade fire over the Gulf",
]


def validate(path):
    """Return the byte size of a good PNG, or raise ValueError."""
    if not os.path.isfile(path):
        raise ValueError("entry.png was not found next to main.py")
    size = os.path.getsize(path)
    if size > LIMIT:
        raise ValueError("entry.png exceeds the 1 MiB ceiling: %d bytes" % size)
    if size < len(SIGNATURE):
        raise ValueError("entry.png is too small to be a PNG")
    with open(path, "rb") as fh:
        if fh.read(len(SIGNATURE)) != SIGNATURE:
            raise ValueError("entry.png header is not a PNG signature")
    return size


def publish():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copy2(ART, OUT_FILE)
    return OUT_FILE


def main():
    try:
        nbytes = validate(ART)
    except ValueError as err:
        print("PLANET: %s" % err, file=sys.stderr)
        return 1
    target = publish()
    if os.path.getsize(target) != nbytes:
        print("PLANET: copy size mismatch after publish", file=sys.stderr)
        return 1
    print("PLANET - The Day In Review - 19 November 2026")
    print("cover validated: %d bytes, delivered to %s" % (nbytes, target))
    print("On the cover:")
    for line in COVER_LINES:
        print(" * " + line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
