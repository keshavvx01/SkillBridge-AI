import json
import os

def load_data():
    path = os.path.join(os.path.dirname(__file__), 'data.json')
    with open(path) as f:
        return json.load(f)

def analyze_skills(user_skills, role):
    data = load_data()

    required = data.get(role, [])
    matched = [s for s in user_skills if s in required]
    missing = [s for s in required if s not in user_skills]

    score = int((len(matched) / len(required)) * 100) if required else 0

    return {
        "score": score,
        "matched": matched,
        "missing": missing
    }