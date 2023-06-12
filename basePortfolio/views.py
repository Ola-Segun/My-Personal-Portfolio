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



# Create your views here.
def portfolioPage(request):
    frontSkills = frontEndSkills.objects.all()
    backSkills = backEndSkills.objects.all()
    frames = frameWorksSkills.objects.all()
    project_list = project.objects.all()
    form = MessageForm()
    login_form = LoginForm()
    profile = Profile.objects.get(user=request.user)
    

    if request.method == 'POST':
        if 'subject' in request.POST:
            print('M-E-S-S-A-G-E')
            form = MessageForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Message sent.')
                return redirect('portfolioPage')
        elif 'password' in request.POST:
            print('L-O-G-I-N')

            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None and user.is_active:
                    login(request, user)
                    return redirect('portfolioPage')
                else:
                    messages.error(request, 'Invalid login credentials.')
                    return redirect('portfolioPage')
    
    paginator = Paginator(project_list, 2) # Change the number to set the number of items to display per page
    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
        
    
        
    context = {'frontSkills':frontSkills,
               'backSkills':backSkills,
               'frames':frames,
               'projects':projects,
               'page': page,
               'form':form,
               'login_form':login_form,
               'profile':profile,}    
    return render(request, 'base/portfolioPage.html', context)

def projectPage(request, slug):
    project_object = get_object_or_404(project, slug=slug)
    Project_body = projectBody.objects.filter(project = project_object).order_by('created')
    context = {'project_object' : project_object,
               'Project_body':Project_body,}
    return render(request, 'base/project.html', context)



