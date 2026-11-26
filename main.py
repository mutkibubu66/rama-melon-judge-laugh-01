"""Make the AI Judge Laugh — one funny line about office life.

Pure Python stdlib. Writes exactly one line (138 characters) to
/output/entry.txt.
"""

import os

LINE = (
    "Our meeting about having too many meetings ran over, so we booked "
    "a follow-up to discuss the action items from the meeting about meetings."
)


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
