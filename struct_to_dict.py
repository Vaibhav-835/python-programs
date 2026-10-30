"""Structure-to-Dictionary conversion: a pirate 'struct' becomes a dict."""
from dataclasses import dataclass, asdict

@dataclass
class Pirate:
    name: str
    crew: str
    bounty: int
    devil_fruit: str | None = None

def pirate_to_dict(p: Pirate) -> dict:
    return asdict(p)

def pairs_to_dict(pairs: list[tuple]) -> dict:
    """Convert [(key, value), ...] into {key: value}."""
    return {k: v for k, v in pairs}

if __name__ == "__main__":
    luffy = Pirate("Monkey D. Luffy", "Straw Hats", 3_000_000_000, "Gomu Gomu no Mi")
    print(pirate_to_dict(luffy))
    print(pairs_to_dict([("captain", "Luffy"), ("ship", "Thousand Sunny")]))
