# resume_app/forms.py

from django import forms
from .models import Personal, Education, Experience, Skill, Project, Certification, Language


class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['name', 'phone', 'email', 'address']
class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'institution', 'graduation_year']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['job_title', 'company', 'start_date', 'end_date', 'description']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['title', 'issuing_organization', 'date_received']

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name']
