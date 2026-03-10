from database import questions


def get_next_question(ability):

    q = questions.find_one(
        {"difficulty": {"$gte": ability}},
        sort=[("difficulty", 1)]
    )

    if not q:
        q = questions.find_one(
            {},
            sort=[("difficulty", -1)]
        )

    return q


def update_ability(ability, correct):

    if correct:
        ability += 0.1
    else:
        ability -= 0.1

    ability = max(0.1, min(ability, 1.0))

    return ability