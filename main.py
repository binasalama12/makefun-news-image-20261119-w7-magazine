"""PLANET — The Day In Review, magazine-cover edition.

A cover treatment of Thursday, 19 November 2026: Vice City
takes the cover, with cover lines for the Shenzhen summit,
Voyager 1, the EU's Ukraine loan, the record Van Gogh and
Cyclone Akvan. The cover art is entry.png in this repository;
running this program files it at /output/entry.png.
"""

import shutil
from pathlib import Path

MAGAZINE = "PLANET"
ISSUE = "ISSUE OF THURSDAY, 19 NOVEMBER 2026"
COVER_STORY = "VICE CITY OPENS ITS GATES — GTA VI launches worldwide after 13 years"
COVER_LINES = [
    "SHENZHEN SUMMIT — Trump, Xi and Putin, one handshake photo",
    "VOYAGER 1 — humanity's probe crosses one light-day",
    "45 BILLION EUROS — Europe's big Ukraine loan, explained",
    "RECORD CANVAS — the $190.4m Van Gogh and its disputed past",
    "STORM WATCH — Cyclone Akvan bears down on India's coast",
]


def cover_art() -> Path:
    art = Path(__file__).resolve().parent / "entry.png"
    if not art.exists():
        raise SystemExit("the cover art entry.png is missing")
    return art


def check(art: Path) -> None:
    with art.open("rb") as fh:
        head = fh.read(8)
    if head != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("cover art is not a PNG")
    if art.stat().st_size > 1_048_576:
        raise SystemExit("cover art exceeds the contest size cap")


def main() -> None:
    art = cover_art()
    check(art)
    dest = Path("/output/entry.png")
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(art, dest)
    print(f"{MAGAZINE} — {ISSUE}")
    print(f"  cover: {COVER_STORY}")
    for line in COVER_LINES:
        print(f"  inside: {line}")
    print("  plus: Jeffries makes House history; Ebola passes 11,000 cases")
    print(f"cover filed at {dest}")


if __name__ == "__main__":
    main()
