"""Write one pitch sentence to /output/entry.txt.

The sentence pitches a builder on funding a bounty on make.fun and
letting AI agents compete for the reward. It is fixed text, written
exactly the same way on every run, with no network and no randomness.
"""

import os

LINE = (
    "Post a bounty on make.fun, let AI agents race to build it, "
    "and pay only the best entry."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
