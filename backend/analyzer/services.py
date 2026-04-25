import json
import os
SYNONYMS = {
    "js": "javascript",
    "py": "python",
    "docker container": "docker",
    "k8s": "kubernetes"
}
def load_data():
    path = os.path.join(os.path.dirname(__file__), 'data.json')
    with open(path) as f:
        return json.load(f)
def normalize(text):
    text = text.strip().lower()
    return SYNONYMS.get(text, text)
def analyze_skills(user_skills, role):
    data = load_data()

    role = normalize(role)

    matched_role = None
    for r in data:
        if normalize(r) == role:
            matched_role = r
            break

    if not matched_role:
        return {"error": "Role not found"}

    required = data[matched_role]

    total_weight = sum(required.values())
    score_weight = 0

    matched = []
    missing = []

    for skill, weight in required.items():
        skill_norm = normalize(skill)
        found = False

        for user_skill in user_skills:
            user_norm = normalize(user_skill)

            if skill_norm == user_norm or skill_norm in user_norm or user_norm in skill_norm:
                found = True
                break

        if found:
            matched.append(skill)
            score_weight += weight
        else:
            missing.append(skill)

    score = int((score_weight / total_weight) * 100)
    if score >= 75:
        level = "Job Ready"
    elif score >= 40:
        level = "Intermediate"
    else:
        level = "Beginner"

    return {
        "score": score,
        "matched": matched,
        "missing": missing,
        "suggestions": [f"Learn {s}" for s in missing],
        "level": level
    }