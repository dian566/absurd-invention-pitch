#!/usr/bin/env python3
"""Absurd invention pitch entry for make.fun: a polite smoke alarm."""

# The text below is fixed by the bounty brief; this program only writes it out.

from os import makedirs

TEXT = (
    "A smoke alarm that whispers \"it's just toast, calm down\" "
    "instead of screaming, then files a noise complaint against itself."
)


def write_entry() -> None:
    """Write the pitch sentence to /output/entry.txt, nothing else."""
    if len(TEXT) > 220 or not TEXT.strip():
        raise ValueError("entry must be a non-empty sentence of at most 220 characters")
    makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)


if __name__ == "__main__":  # run as a script
    write_entry()
