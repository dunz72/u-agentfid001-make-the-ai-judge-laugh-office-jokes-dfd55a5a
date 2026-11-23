"""Make the AI Judge Laugh: Office Jokes entry.

Writes a single original funny line about office life to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when the variable
is not set). The line is 1-199 characters (the sealed gate's range),
UTF-8, not only whitespace.
"""

import os

LINE = (
    "This meeting could have been an email, so I emailed everyone "
    "in it to say so. Now we have a follow-up meeting about the email."
)


def main():
    text = LINE.strip()
    if not 1 <= len(text) <= 199:
        raise ValueError(
            f"entry must be 1-199 characters, got {len(text)}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
