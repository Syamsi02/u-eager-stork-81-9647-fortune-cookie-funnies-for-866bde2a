"""Fortune Cookie Funnies for Engineers.

Writes one fortune cookie message for a software engineer to
/output/entry.txt (and prints it). Pure standard library, deterministic:
the same line on every run.
"""

from pathlib import Path

FORTUNE = "You will find the bug the moment you explain your code to the rubber duck."

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(path=OUTPUT_PATH):
    """Write the fortune to path, creating parent dirs as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(FORTUNE + "\n", encoding="utf-8")
    return FORTUNE


def main():
    """Write the fortune and print it, so a local run shows the entry."""
    fortune = write_entry()
    print(fortune)


if __name__ == "__main__":
    main()
