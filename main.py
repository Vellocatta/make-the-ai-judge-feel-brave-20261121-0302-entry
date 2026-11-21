"""Make the AI judge feel brave.

Writes one short relaxing text to /output/entry.txt (stdlib only, no network).
"""
import os

TEXT = (
    "The river turns the stones over, one by one, patient as a reader "
    "with a long book. Each one comes up smooth and cool, and the current "
    "carries it a little further down. There is nowhere else it has to be, "
    "and no hurry to arrive."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 280:
        raise ValueError("entry text must be 1-280 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
