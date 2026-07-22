import re


def detect_intent(query: str):

    query = query.lower().strip()


    recommendation_patterns = [

        r"\brecommend\b",
        r"\bsuggest\b",
        r"\bsimilar\b",
        r"\blike\b",
        r"\bwhat should i watch\b",
        r"\bwhat to watch\b",
        r"\bwhat anime should i watch\b",
        r"\bnext anime\b",
        r"\banime after\b",
        r"\bafter watching\b",
        r"\bsomething similar\b",
        r"\bmore anime\b"
    ]


    for pattern in recommendation_patterns:

        if re.search(pattern, query):
            return "recommendation"


    return "information"