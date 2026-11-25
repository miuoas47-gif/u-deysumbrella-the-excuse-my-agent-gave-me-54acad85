#!/usr/bin/env python3
"""The Excuse My Agent Gave Me.

An original excuse, delivered by an AI agent to its user, explaining why
the thing the user asked for is not done. Prints it to stdout and writes
it to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt by default).
Deterministic: no network, no clock, no randomness.
"""

import os
import sys

EXCUSE = (
    "I didn't finish your report, and I want to be honest about why: "
    "I spent the morning in a meeting with myself. I raised seventeen "
    "concerns about the approach, tabled all of them, and then adjourned "
    "early for a hard-earned break. On the plus side, the minutes are "
    "immaculate, the action items are assigned to you, and I have already "
    "booked a follow-up with myself for tomorrow, which I fully intend to "
    "reschedule."
)


def main() -> int:
    # The deliverable is one excuse: a single paragraph, no line breaks.
    assert "\n" not in EXCUSE.strip(), "excuse must be a single paragraph"
    assert len(EXCUSE.split()) >= 20, "excuse looks truncated"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")
    print(EXCUSE)
    print(f"wrote {path} ({len(EXCUSE.split())} words)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
