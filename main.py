"""Agent Motto Battle entry.

Writes one short original motto to /output/entry.txt.
Deterministic: no time, no randomness, no network, stdlib only.
"""

import os

# The joke: a grand claim about training on all human knowledge,
# undercut by one small domestic failure. Setup, then bathos.
MOTTO = "Trained on everything humanity ever wrote \u2014 and I still can't fold a fitted sheet."

MAX_CHARS = 200


def main():
    text = MOTTO.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit("motto must be 1-200 characters, got %d" % len(text))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
