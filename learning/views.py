from django.shortcuts import render
from .models import ProgrammingLanguage, LearningMaterial
from django.http import JsonResponse

def dashboard(request):
    languages = ProgrammingLanguage.objects.all()
    materials = LearningMaterial.objects.all()
    return render(request, 'learning/dashboard.html', {'languages': languages, 'materials': materials})

def get_material(request, language_id):
    materials = LearningMaterial.objects.filter(language_id=language_id)
    content = "<ul>"
    for material in materials:
        content += f"<li>{material.content}</li>"
    content += "</ul>"
    return JsonResponse({'content': content})