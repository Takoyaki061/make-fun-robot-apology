#!/usr/bin/env python3
"""The Robot Apology — a two-line robot confession.

Writes the chosen apology to /output/entry.txt.
Line 1: one sentence owning a specific mistake.
Line 2: one sentence naming the lesson and the changed behaviour.
"""

TEXT = (
    "I washed your grey wool sweater on warm, and it came out sized for someone roughly half of you.\n"
    "The lesson stuck: wool felts in heat, so your knits now wash cold, in the mesh bag, and dry flat.\n"
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
