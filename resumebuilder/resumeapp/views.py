# resume_app/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from .forms import PersonalForm, EducationForm, ExperienceForm, SkillForm, ProjectForm, CertificationForm, LanguageForm

def delete_existing_entries(user, model_set):
    if model_set.exists():
        model_set.all().delete()

@login_required
def add_view(request, form_class, template_name):
    model_set = form_class.Meta.model.objects.filter(user=request.user)
    delete_existing_entries(request.user, model_set)

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('dashboard')
    else:
        form = form_class()
    return render(request, template_name, {'form': form})

@login_required
def add_personal(request):
    return add_view(request, PersonalForm, 'add_personal.html')

@login_required
def add_education(request):
    return add_view(request, EducationForm, 'add_education.html')

@login_required
def add_experience(request):
    return add_view(request, ExperienceForm, 'add_experience.html')

@login_required
def add_skill(request):
    return add_view(request, SkillForm, 'add_skill.html')

@login_required
def add_project(request):
    return add_view(request, ProjectForm, 'add_project.html')

@login_required
def add_certification(request):
    return add_view(request, CertificationForm, 'add_certification.html')

@login_required
def add_language(request):
    return add_view(request, LanguageForm, 'add_language.html')

@login_required
def dashboard(request):
    context = {
        'personals': request.user.personal_set.all(),
        'educations': request.user.education_set.all(),
        'experiences': request.user.experience_set.all(),
        'skills': request.user.skill_set.all(),
        'projects': request.user.project_set.all(),
        'certifications': request.user.certification_set.all(),
        'languages': request.user.language_set.all(),
    }
    return render(request, 'dashboard.html', context)

def generate_resume_pdf(request):
    template_path = 'pdf_template.html'
    context = {
        'user': request.user,
        'personals': request.user.personal_set.all(),
        'educations': request.user.education_set.all(),
        'experiences': request.user.experience_set.all(),
        'skills': request.user.skill_set.all(),
        'projects': request.user.project_set.all(),
        'certifications': request.user.certification_set.all(),
        'languages': request.user.language_set.all(),
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="resume.pdf"'

    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Error generating PDF')
    return response

