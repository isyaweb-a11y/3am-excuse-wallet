"""The 3 AM Excuse -- one-line entry.

One line under 200 characters in the voice of a hardware wallet that
will not sign a transaction at 3 AM. The wallet has a personality, a
reason, and a joke that lands in one breath: its keys are asleep, its
screen is dimmed, and the "urgent" transfer can wait for sunrise.
Written to /output/entry.txt.
"""

import os

SETUP = (
    "Sorry, I don\u2019t sign after midnight \u2014 my keys are asleep, "
    "my screen is dimmed,"
)
PAYOFF = "and your \u2018urgent\u2019 transfer can wait for sunrise like the rest of us."

MAX_CHARS = 200
MIN_CHARS = 1


def compose(setup: str, payoff: str) -> str:
    """Join the refusal and the reason into one wallet-voiced excuse."""
    line = " ".join(part.strip() for part in (setup, payoff))
    return line


def check_line(line: str) -> str:
    """Gate the line the way the sealed scorer does: 1..200 chars, one line."""
    assert MIN_CHARS <= len(line) <= MAX_CHARS, f"line is {len(line)} chars"
    assert line == line.strip(), "no stray whitespace around the line"
    assert "\n" not in line, "the line must stay on one line"
    return line


def check_wallet_voice(line: str) -> dict:
    """Per-bounty delivery check: the excuse must sound like the wallet.

    The brief wants the device's own personality, reason and joke in one
    breath, so the line must refuse to sign after midnight, name its
    sleeping keys, and make the urgent transfer wait for sunrise.
    """
    words = line.split()
    assert 15 <= len(words) <= 40, f"line has {len(words)} words"
    assert "sign" in line, "the wallet must refuse to sign"
    assert "keys are asleep" in line, "the reason must be the sleeping keys"
    assert "sunrise" in line, "the punch must make the transfer wait for sunrise"
    assert line.startswith("Sorry,"), "the wallet refuses politely"
    return {"words": len(words), "chars": len(line), "lines": 1}


def main() -> None:
    line = check_line(compose(SETUP, PAYOFF))
    notes = check_wallet_voice(line)
    assert notes["lines"] == 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
