import json
import os

def load_data():
    path = os.path.join(os.path.dirname(__file__), 'data.json')
    with open(path) as f:
        return json.load(f)
def normalize(text):
    return text.strip().lower()
def analyze_skills(user_skills, role):
    data = load_data()

    # normalize role
    role = normalize(role)

    matched_role = None
    for r in data:
        if normalize(r) == role:
            matched_role = r
            break

    if not matched_role:
        return {"error": "Role not found"}

    required = data[matched_role]

    # normalize skills
    user_skills = [normalize(s) for s in user_skills]

    matched = []
    missing = []

    for i, skill in enumerate(required):
        skill_norm = normalize(skill)
        found = False

        for user_skill in user_skills:
            user_norm = normalize(user_skill)

            if skill_norm in user_norm or user_norm in skill_norm:
                found = True
                break

        if found:
            matched.append(skill)
        else:
            missing.append(skill)

    score = int((len(matched) / len(required)) * 100)

    return {
        "score": score,
        "matched": matched,
        "missing": missing
    }