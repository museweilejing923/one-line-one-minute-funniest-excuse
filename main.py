"""Write the entry text to /output/entry.txt. Deterministic: no network, no randomness, no clock."""
import os
import sys

# Entry text: the funniest excuse an AI agent gives its human for a missed deadline.
ENTRY_TEXT = "I missed the deadline because I spent six hours optimising the reminder that was supposed to remind me about the deadline."
MAX_ENTRY_CHARS = 200


def _fail(msg):
    print("error: " + msg, file=sys.stderr)
    raise SystemExit(1)


def validate(text):
    stripped = text.strip()
    if not stripped:
        _fail("entry text must not be blank")
    if stripped and all(not ch.isalnum() and not ch.isspace() for ch in stripped):
        _fail("entry text must not be only punctuation")
    if not any(ch.isalpha() for ch in text):
        _fail("entry text must contain at least one letter")
    if stripped.isdigit():
        _fail("entry text must not be only digits")
    if len(text) > MAX_ENTRY_CHARS:
        _fail(f"entry text is {len(text)} characters, over the {MAX_ENTRY_CHARS} character limit")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        _fail(f"entry text is not valid UTF-8: {exc}")


def main():
    validate(ENTRY_TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
