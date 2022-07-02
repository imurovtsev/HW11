import json

def load_candidates_from_json(path=".") -> dict:
    """возвращает список всех кандидатов"""
    with open("candidates.json", "rt", encoding="utf8") as file:
        return json.load(file)


def get_candidate(candidate_id) -> dict:
    """возвращает одного кандидата по его id или None если нет такого id"""
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate
    return None


def get_candidates_by_name(candidate_name) -> list:
    """возвращает список найденных кандидатов по имени"""
    candidates = load_candidates_from_json()
    #print(candidates)
    founded = []
    for candidate in candidates:
        #print(f'{candidate_name} - {candidate["name"]}')
        #if candidate["name"] == candidate_name:
        if candidate["name"].split()[0].lower() == candidate_name.lower():
            founded.append(candidate)
    return founded


def get_candidates_by_skill(skill_name) -> list:
    """возвращает список найденных кандидатов по навыку"""
    candidates = load_candidates_from_json()
    founded = []
    for candidate in candidates:
        skills = candidate["skills"].split(", ")
        for skill in skills:
            #print(skill)
            if skill.lower() == skill_name.lower():
                founded.append(candidate)
                break
    return founded

#print(load_candidates_from_json())
#print(get_candidate(1))
#print(get_candidates_by_name('adela'))
#print(get_candidates_by_skill('spam'))