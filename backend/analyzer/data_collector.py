import json
import os

def fetch_job_descriptions():
    return [
        {
            "role": "DevOps Engineer",
            "description": "Looking for experience in Docker, Kubernetes, AWS, CI/CD pipelines, Linux."
        },
        {
            "role": "AI Engineer",
            "description": "Strong Python, Machine Learning, TensorFlow, NLP required."
        }
    ]

SKILL_KEYWORDS = [
    "python", "docker", "kubernetes", "aws",
    "ci/cd", "linux", "tensorflow", "ml"
]

def extract_skills(text):
    text = text.lower()
    found = []

    for skill in SKILL_KEYWORDS:
        if skill in text:
            found.append(skill)

    return found

def assign_weight(skill):
    high_priority = ["aws", "kubernetes", "tensorflow"]
    medium_priority = ["docker", "ci/cd", "ml"]

    if skill in high_priority:
        return 5
    elif skill in medium_priority:
        return 3
    else:
        return 2

def update_data():
    jobs = fetch_job_descriptions()
    data = {}

    for job in jobs:
        role = job["role"]
        skills = extract_skills(job["description"])

        # ✅ create weighted skills
        skill_weights = {
            skill.capitalize(): assign_weight(skill)
            for skill in skills
        }

        data[role] = skill_weights

    path = os.path.join(os.path.dirname(__file__), "data.json")

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    print("Data updated successfully")

if __name__ == "__main__":
    update_data()