#!/usr/bin/env python3
"""What the Elevator Would Say — make.fun entry.

Writes one line, the funniest thing a talking elevator could say, to
/output/entry.txt. Deterministic: no input, no randomness, no network.
"""

LINE = "You pressed the button twice. I heard you the first time. I'm an elevator, not your ex."


def main() -> None:
    assert 1 <= len(LINE) <= 120, "line must be 1-120 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == LINE, "read-back mismatch"


if __name__ == "__main__":
    main()
