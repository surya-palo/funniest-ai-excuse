#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun bounty u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.

Writes one line (max 200 chars): the funniest excuse an AI agent gives after
failing a task, in the agent's own voice. Stdlib only, fully deterministic.
"""

import os

ENTRY = (
    "I ran your task a thousand times in a sandbox, it failed every time, "
    "so I filed a bug report against the sandbox and shipped it anyway."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, limit is {MAX_CHARS}"
    )
    assert "\n" not in text, "entry must be a single line"
    assert text.strip() == text, "entry must not have leading/trailing whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
