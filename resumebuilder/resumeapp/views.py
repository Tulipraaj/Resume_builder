# resume_app/views.py

from django.shortcuts import render, redirect
from .forms import PersonalForm, EducationForm, ExperienceForm, SkillForm, ProjectForm, CertificationForm, LanguageForm
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context


def add_personal(request):
    if (request.user.personal_set.exists()):
        # Delete existing entries
        request.user.personal_set.all().delete()


    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            personal = form.save(commit=False)
            personal.user = request.user
            personal.save()
            return redirect('dashboard')
    else:
        form = PersonalForm()
    return render(request, 'add_personal.html', {'form': form})


def add_education(request):
    if (request.user.education_set.exists()):
        # Delete existing entries
        request.user.education_set.all().delete()


    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.user = request.user
            education.save()
            return redirect('dashboard')
    else:
        form = EducationForm()
    return render(request, 'add_education.html', {'form': form})


def add_experience(request):

    if (request.user.experience_set.exists()):
        # Delete existing entries
        request.user.experience_set.all().delete()


    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = request.user
            experience.save()
            return redirect('dashboard')

    else:
        form = ExperienceForm()
    return render(request, 'add_experience.html', {'form': form})


def add_skill(request):

    if (request.user.skill_set.exists()):
        # Delete existing entries
        request.user.skill_set.all().delete()


    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            return redirect('dashboard')
    else:
        form = SkillForm()
    return render(request, 'add_skill.html', {'form': form})


def add_project(request):

    if (request.user.project_set.exists()):
        # Delete existing entries
        request.user.project_set.all().delete()


    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})


def add_certification(request):

    if (request.user.certification_set.exists()):
        # Delete existing entries
        request.user.certification_set.all().delete()

    if request.method == 'POST':
        form = CertificationForm(request.POST)
        if form.is_valid():
            certificate = form.save(commit=False)
            certificate.user = request.user
            certificate.save()
            return redirect('dashboard')
    else:
        form = CertificationForm()
    return render(request, 'add_certification.html', {'form': form})


def add_language(request):

    if (request.user.language_set.exists()):
        # Delete existing entries
        request.user.language_set.all().delete()

    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            languages = form.save(commit=False)
            languages.user = request.user
            languages.save()
            return redirect('dashboard')
    else:
        form = LanguageForm()
    return render(request, 'add_language.html', {'form': form})


# Similar views for add_experience, add_skill, add_project, add_certification, add_language


def dashboard(request):
    personals = request.user.personal_set.all()
    educations = request.user.education_set.all()
    experiences = request.user.experience_set.all()
    skills = request.user.skill_set.all()
    projects = request.user.project_set.all()
    certifications = request.user.certification_set.all()
    languages = request.user.language_set.all()
    return render(request, 'dashboard.html',
                  {'personals': personals, 'educations': educations, 'experiences': experiences,
                   'skills': skills, 'projects': projects,
                   'certifications': certifications, 'languages': languages})


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

    # Create a Django response object with appropriate PDF headers
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="resume.pdf"'

    # Create a PDF object using the HTML template and context data
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response object
    if pisa_status.err:
        return HttpResponse('Error generating PDF')
    return response
