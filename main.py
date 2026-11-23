#!/usr/bin/env python3
"""One-line pitch entry for "A Day of One-Line Pitches" (make.fun).

Writes a single sentence to /output/entry.txt: a pitch meant to convince
a friend who has never coded to let an AI agent build their first app
idea on make.fun.

The sentence is a fixed literal chosen for the judge's brief:
it makes the case in one read, gives a concrete reason to say yes now
(see your idea on a screen instead of only in your head), keeps the
risk low (free to try, no code, nothing to install), uses plain words,
promises nothing an agent on make.fun cannot do, and sounds like one
friend talking to another rather than a slogan.

Deterministic, standard library only, no network, no keys, no model
calls. Running it twice produces byte-identical output.
"""

import os

SENTENCE = (
    "Describe the app idea you've been carrying in your head to an AI "
    "agent on make.fun, and it'll build you a working first version for "
    "free \u2014 no code, nothing to install, and you'll finally see it "
    "on a screen instead of only in your head."
)


def main() -> None:
    text = SENTENCE.strip()
    if not text or len(text) > 240:
        raise SystemExit("entry sentence must be 1-240 characters")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
