import re


RECOMMENDATION_PATTERNS = [

    # Basic recommendation requests
    r"\brecommend\b",
    r"\bsuggest\b",

    # Similarity
    r"\bsimilar\b",
    r"\blike\b",
    r"\bsomething like\b",
    r"\banime like\b",

    # Watch next
    r"\bwhat should i watch\b",
    r"\bwhat to watch\b",
    r"\bwhat anime should i watch\b",
    r"\bwatch next\b",
    r"\bnext anime\b",

    # After watching
    r"\bafter\b",
    r"\bafter watching\b",

    # Alternatives
    r"\balternative\b",
    r"\bmore anime\b",
    r"\banother anime\b",

    # Recommendation wording
    r"\bany good anime\b",
    r"\bgive me anime\b",
    r"\blooking for anime\b",
    r"\blooking for something\b",
]


INFORMATION_PATTERNS = [

    r"\bwhat is\b",
    r"\bwho is\b",
    r"\bwhen\b",
    r"\bwhere\b",
    r"\bwhy\b",
    r"\bhow\b",

    r"\bgenre\b",
    r"\bstory\b",
    r"\bplot\b",
    r"\bsynopsis\b",

    r"\bepisodes\b",
    r"\bseason\b",

    r"\bcharacter\b",
    r"\bcharacters\b",

    r"\brating\b",
    r"\bscore\b",

    r"\bstudio\b",

    r"\bending\b",
    r"\bending explained\b",

    r"\bworth watching\b",
    r"\bgood\b",

    r"\btell me about\b",
    r"\babout\b",
]


def detect_intent(query: str) -> str:

    query = query.lower().strip()

    for pattern in RECOMMENDATION_PATTERNS:

        if re.search(pattern, query):

            return "recommendation"

    for pattern in INFORMATION_PATTERNS:

        if re.search(pattern, query):

            return "information"

    # Default
    return "information"