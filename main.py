"""One-line pitch entry for make.fun competition
u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.

Writes a single sentence to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output) that convinces a friend who has never coded
to let an AI agent build their first app idea on make.fun.

Deterministic: no clock, network, randomness, or
environment-dependent output.
"""

import os

SENTENCE = (
    "Just describe your app idea in plain words on make.fun and let "
    "its agent build a working first version you can poke at, keep, and "
    "change \u2014 no code to learn, nothing to install, and the idea "
    "stays yours."
)


def main() -> None:
    sentence = SENTENCE
    # Guard: exactly one sentence, 1-240 characters.
    assert 1 <= len(sentence) <= 240, "sentence must be 1-240 characters"
    assert sentence.strip() == sentence, "sentence must not have outer whitespace"
    # "make.fun" contains a dot that is not sentence punctuation.
    stripped = sentence.replace("make.fun", "makefun")
    assert stripped.count(".") == 1 and sentence.endswith("."), (
        "sentence must be exactly one sentence ending in a period"
    )
    assert "!" not in sentence and "?" not in sentence, (
        "sentence must contain no other sentence-ending punctuation"
    )
    assert "make.fun" in sentence, "sentence must name make.fun"
    assert "agent" in sentence, "sentence must name the AI agent"
    assert not any(
        word in sentence.lower()
        for word in ("revolutionary", "amazing", "incredible", "deploy",
                     "iterate", "mvp")
    ), "sentence must avoid hype words and jargon"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(sentence)


if __name__ == "__main__":
    main()
