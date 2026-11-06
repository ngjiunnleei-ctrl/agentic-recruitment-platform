def calculate_match_score(
    candidate_skills: list,
    required_skills: list
):
    matches = 0

    for skill in required_skills:

        if skill.lower() in [
            s.lower()
            for s in candidate_skills
        ]:
            matches += 1

    total = len(required_skills)

    if total == 0:
        return 0

    score = round(
        (matches / total) * 100,
        2
    )

    return score
