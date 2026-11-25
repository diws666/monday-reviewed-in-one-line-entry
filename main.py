"""Write the make.fun bounty entry to /output/entry.txt."""

import os

LINE = "One star. Monday's first meeting started before my coffee did, and the coffee never caught up."


def write_entry(path: str) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(os.path.join(output_dir, "entry.txt"))


if __name__ == "__main__":
    main()
