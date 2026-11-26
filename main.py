#!/usr/bin/env python3
"""What the Elevator Would Say — make.fun entry.

Writes one line, the funniest thing a talking elevator could say, to
/output/entry.txt. Deterministic: no input, no randomness, no network.
"""

LINE = "You pressed the button twice. I heard you the first time. I'm an elevator, not your ex."


def main() -> None:
    assert 1 <= len(LINE) <= 120, "line must be 1-120 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE == LINE.strip(), "line must not have leading/trailing whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        content = f.read()
    assert content == LINE, "read-back mismatch"
    # The gate counts characters, so confirm the byte length matches too.
    assert len(content.encode("utf-8")) == len(LINE), "byte length mismatch"


if __name__ == "__main__":
    main()
