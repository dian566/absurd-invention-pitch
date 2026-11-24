"""Entry for the make.fun bounty "One-Sentence Absurd Invention Pitch".

Writes a single sentence pitching a ridiculous invention, at most 220
characters and nothing else, to /output/entry.txt.
"""

import os

LINE = "A smoke alarm that whispers \"it's just toast, calm down\" instead of screaming, then files a noise complaint against itself."

assert len(LINE) <= 220, "entry must be at most 220 characters"
assert LINE.strip(), "entry must not be empty"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
