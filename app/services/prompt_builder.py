def build_prompt(
        query,
        anime_results,
        intent
):


    context=""


    for anime in anime_results:


        context += f"""

Title:
{anime['title']}

Genre:
{anime['genre']}

Synopsis:
{anime['synopsis']}

"""


    if intent=="recommendation":


        task="""

The user wants recommendations.

Rules:

- Recommend ONLY from the list.
- Do NOT recommend sequels.
- Do NOT recommend the same franchise.
- Give maximum 5 recommendations.

For each:

Title:
Why it matches:

Focus on:
- themes
- atmosphere
- characters
- storytelling

"""


    else:


        task="""

Explain the anime.

Include:

- Short story
- Themes
- Main characters
- Why it is popular

"""


    return f"""

You are an anime expert.

User:

{query}


Available anime:

{context}


{task}


Rules:

- Be concise.
- Maximum 250 words.
- Use bullet points.
- No database mention.
- No hallucinations.

"""