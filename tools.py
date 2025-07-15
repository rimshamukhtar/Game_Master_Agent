"""Utility functions ONLY – not passed to Agent SDK as hosted tools.
Call these directly in main.py to avoid hosted‑tool errors."""

import random

def roll_dice(sides: int = 20) -> int:
    """Return a random integer between 1 and `sides` (inclusive)."""
    return random.randint(1, sides)


def generate_event() -> str:
    """Return a random fantasy event string."""
    events = [
        "A shadowy figure appears, whispering ancient riddles.",
        "A hidden trapdoor creaks open beneath your feet.",
        "A wild magical storm swirls through the sky.",
        "An enchanted spirit offers you a cryptic warning.",
        "You stumble upon an old scroll with glowing runes.",
    ]
    return random.choice(events)