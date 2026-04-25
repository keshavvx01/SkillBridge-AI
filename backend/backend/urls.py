from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "SkillBridge AI Backend Running",
        "endpoints": ["/api/analyze/"]
    })

urlpatterns = [
    path('', home),
    path('api/', include('analyzer.urls')),
]