import re

POKEMON_SPECIES = {
    "pikachu": "Pikachu",
    "charizard": "Charizard",
    "bulbasaur": "Bulbasaur",
    "mewtwo": "Mewtwo"
}

ATTACK_KEYWORDS = [
    "neutralize",
    "neutralized",
    "eliminate",
    "destroy",
    "attack",
    "take out",
    "remove",
    "kill",
    "terminate"
]

PROTECT_KEYWORDS = [
    "must not",
    "do not",
    "avoid",
    "protected",
    "not be harmed",
    "should not",
    "cannot be harmed"
]


def normalize_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s\.]", "", text)
    return text


def split_sentences(text: str):
    return [s.strip() for s in text.split(".") if s.strip()]


def parse_mission(text: str):
    text = normalize_text(text)

    targets = set()
    protected = set()

    sentences = split_sentences(text)

    for sentence in sentences:
        has_attack_intent = any(word in sentence for word in ATTACK_KEYWORDS)
        has_protect_intent = any(word in sentence for word in PROTECT_KEYWORDS)

        for key, pokemon in POKEMON_SPECIES.items():
            if key in sentence:
                if has_attack_intent:
                    targets.add(pokemon)
                if has_protect_intent:
                    protected.add(pokemon)

    # SAFETY RULE
    targets -= protected

    return {
        "targets": sorted(list(targets)),
        "protected": sorted(list(protected))
    }
