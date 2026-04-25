from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import analyze_skills

@api_view(['POST'])
def analyze(request):
    skills = request.data.get("skills", [])
    role = request.data.get("role", "")

    result = analyze_skills(skills, role)

    return Response(result)