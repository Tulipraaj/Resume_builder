# resume_app/urls.py

from django.urls import path
from .views import add_education, add_experience, add_skill, add_personal, add_project, add_certification, add_language, dashboard, generate_resume_pdf

urlpatterns = [
    path('add_education/', add_education, name='add_education'),
    path('add_experience/', add_experience, name='add_experience'),
    path('add_skill/', add_skill, name='add_skill'),
    path('add_personal/', add_personal, name='add_personal'),
    path('add_project/', add_project, name='add_project'),
    path('add_certification/', add_certification, name='add_certification'),
    path('add_language/', add_language, name='add_language'),
    path('dashboard/', dashboard, name='dashboard'),
    path('generate_resume_pdf/', generate_resume_pdf, name='generate_resume_pdf'),
]
