from django.shortcuts import render, redirect

# Create your views here.
from .models import *

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def services(request):
    services = Service.objects.all()
    context = {
        'services': services
    }
    return render(request, 'pages/services.html', context)

def portfolio(request):
    portfolios = Portfolio.objects.all()
    projects = Project.objects.all()
    context = {
        'projects': projects,
        'portfolios': portfolios
    }
    return render(request, 'pages/portfolio.html', context)

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'pages/projects.html', context)

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    context = {
        'project': project
    }
    return render(request, 'pages/project_detail.html', context)

def blog(request):
    return render(request, 'pages/blog.html')

def faq(request):
    return render(request, 'pages/faq.html')

def terms(request):
    return render(request, 'pages/terms.html')

def privacy(request):
    return render(request, 'pages/privacy.html')

def team(request):
    teams = Teams.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'pages/team.html', context)

def values(request):
    return render(request, 'pages/values.html')
# pack
def business_pack(request):
    return render(request, 'packs/business_pack.html')

def assistance_pack(request):
    return render(request, 'packs/assistance.html')

def internship_pack(request):
    return render(request, 'packs/internship.html')

def personal_pack(request):
    return render(request, 'packs/personal.html')

def professional_pack(request):
    return render(request, 'packs/professional.html')

def scholarship_pack(request):
    return render(request, 'packs/scholarship.html')

def sharing_pack(request):
    return render(request, 'packs/sharing.html')

def learning_with_us(request):
    return render(request, 'packs/learning.html')

def become_member(request):
    return render(request, 'packs/become_member.html')

def ressources_pack(request):
    return render(request, 'packs/ressources.html')

def mentor_pack(request):
    return render(request, 'packs/mentor.html')


# Vue pour créer un message
def messages(request):
    if request.method == 'POST':
        # Simple création sans validation complexe
        Messages.objects.create(
            name=request.POST.get('name', ''),
            email=request.POST.get('email', ''),
            subject=request.POST.get('subject', ''),
            message=request.POST.get('message', '')
        )
        return render(request, 'pages/success.html')

    return render(request, 'pages/contact.html')

def envois_message(request):
    return render(request, 'pages/message.html')