from django.shortcuts import render, redirect
from django.shortcuts import render,get_object_or_404
from adminManage. models import frontEndSkills, backEndSkills, frameWorksSkills, Profile
from .models import  project, projectBody
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
from . forms import MessageForm
from . forms import LoginForm
from django.contrib import messages
from datetime import datetime
from django.db.models.functions import TruncMonth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def portfolioPage(request):
    front_skills = frontEndSkills.objects.all()
    back_skills = backEndSkills.objects.all()
    frames = frameWorksSkills.objects.all()
    project_list = project.objects.all()
    form = MessageForm()
    login_form = LoginForm()
    profile = None
    default_profile_picture_url = 'static\images\joshua-oyebanji-LEB4O4n0IdQ-unsplash_cropped1.jpg'
    
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        if 'subject' in request.POST:
            handle_message_submission(request, form)
        elif 'password' in request.POST:
            handle_login_submission(request, login_form)

    projects = paginate_project_list(request, project_list)

    context = {
        'frontSkills': front_skills,
        'backSkills': back_skills,
        'frames': frames,
        'projects': projects,
        'page': request.GET.get('page'),
        'form': form,
        'login_form': login_form,
        'profile': profile,
        'default_profile_picture_url': default_profile_picture_url,
        
    }
    return render(request, 'base/portfolioPage.html', context)

def handle_message_submission(request, form):
    form = MessageForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Message sent.')
    return redirect('portfolioPage')

def handle_login_submission(request, login_form):
    login_form = LoginForm(request.POST)
    if login_form.is_valid():
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
        else:
            messages.error(request, 'Invalid login credentials.')
    return redirect('portfolioPage')

def paginate_project_list(request, project_list):
    paginator = Paginator(project_list, 2)
    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages) 
    return projects


def projectPage(request, slug):
    project_object = get_object_or_404(project, slug=slug)
    Project_body = projectBody.objects.filter(project = project_object).order_by('created')
    context = {'project_object' : project_object,
               'Project_body':Project_body,}
    return render(request, 'base/project.html', context)



