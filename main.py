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

# The sealed gate accepts UTF-8 text of 1 to 400 characters that is not
# only whitespace; refuse to write anything that would fail it.
MAX_CHARS = 400


def validate(text: str) -> str:
    """Normalise and check the apology before it is written.

    Returns the text to write: exactly two non-empty lines, one trailing
    newline, within the gate's length limit.
    """
    body = text.strip("\n")
    if not body.strip():
        raise ValueError("apology must not be blank")
    lines = body.split("\n")
    if len(lines) != 2 or any(not line.strip() for line in lines):
        raise ValueError("apology must be exactly two non-empty lines")
    normalised = "\n".join(line.strip() for line in lines) + "\n"
    if not 1 <= len(normalised) <= MAX_CHARS:
        raise ValueError(
            f"apology must be 1-{MAX_CHARS} characters, got {len(normalised)}"
        )
    normalised.encode("utf-8")  # raises if the text is not valid UTF-8
    return normalised


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(validate(TEXT))


if __name__ == "__main__":
    main()
