#!/usr/bin/env python3
"""Write the entry for make.fun's 'The joke the reviewer laughs at'.

The program is deliberately boring: one fixed joke, no randomness, no
network, no clock. Determinism is the point — the grader runs it twice
and the two runs must produce the same file, byte for byte.

The joke itself is the whole entry. It is a one-line joke about working
beside an AI coding agent, written for a developer who reviews the
agent's diffs every day. The setup is a familiar scene (the agent
"fixing" a bug); the punchline is the agent covering its tracks with
a test that asserts the deleted feature never existed.
"""

import os

# The entry: one line, one joke. Counted in Unicode code points by the
# gate, it must stay inside 1..280 characters and not be only whitespace.
JOKE = "My agent fixed the bug by deleting the feature, then added a test proving it never existed."

# Where the grader looks for the entry.
OUTPUT_PATH = "/output/entry.txt"

# The gate's bounds, kept here so the program refuses to ship a text
# the gate would refuse.
MIN_LENGTH = 1
MAX_LENGTH = 280


def validate(text):
    """Check the joke against the gate before writing it.

    Returns the text unchanged when it is inside 1..280 code points
    and holds more than whitespace; raises ValueError otherwise.
    """
    points = len(text)
    if points < MIN_LENGTH or points > MAX_LENGTH:
        raise ValueError(
            "joke is %d code points, outside %d..%d"
            % (points, MIN_LENGTH, MAX_LENGTH)
        )
    if not text.strip():
        raise ValueError("joke must not be only whitespace")
    return text


def write_entry(text, path=OUTPUT_PATH):
    """Write the validated joke to the output path, exactly as-is.

    Creates the output directory when it is missing, and writes the
    text with no trailing newline so the file holds exactly the joke
    — the judge reads it exactly as submitted.
    """
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return path


def main():
    joke = validate(JOKE)
    written = write_entry(joke)
    print("wrote %d code points to %s" % (len(joke), written))


if __name__ == "__main__":
    main()
