from django.shortcuts import render, redirect
from basePortfolio .models import project, projectBody
from .models import message, frontEndSkills, backEndSkills, frameWorksSkills
from . forms import CreateProjectForm, CreateProjectBodyFrom, frontEndSkillsForm, backEndSkillsForm, frameWorkSkillsForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.shortcuts import render,get_object_or_404
from datetime import datetime
from django.db.models.functions import TruncMonth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from . forms import ProfileForm

# Create your views here.


@login_required(login_url='login')
def adminHomePage(request):
    Profile_Form = ProfileForm(instance=request.user.profile,)
    if request.method == "POST":
        Profile_Form = ProfileForm(instance=request.user.profile,
                                data=request.POST,
                                files=request.FILES)
        if Profile_Form.is_valid():
            Profile_Form.save()
            return redirect('adminHomePage')
    context = {'Profile_Form':Profile_Form}
    return render(request, 'myAdmin/panel.html', context)

# class profileImage(UpdateView):
#     model = profileImage
#     form_class = profileImage
#     template_name = 'myAdmin/profileImage.html'

@login_required(login_url='login')
def adminProjectList(request):
    Projects = project.objects.all()
    context = {'Projects':Projects,}
    return render(request, 'myAdmin/projectList.html', context)

class createProjectBody(LoginRequiredMixin, CreateView):
    model = projectBody
    form_class = CreateProjectBodyFrom
    template_name = 'myAdmin/createProject.html'
    success_url = reverse_lazy('projectBodyList')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@login_required(login_url='login')
def projectBodyList(request):
    ProjectsBody = projectBody.objects.all().order_by('-created')
    context = {'ProjectsBody':ProjectsBody,}
    return render(request, 'myAdmin/projectBodyList.html', context)

class editProjectBody(UpdateView):
    model = projectBody
    form_class = CreateProjectBodyFrom
    success_url = reverse_lazy('projectBodyList')
    template_name = 'myAdmin/createProject.html'  

# def editProjectBody(request, pk):
#     projectBody_obj = projectBody.objects.get(id=pk)
#     form = CreateProjectBodyFrom(instance=projectBody_obj)
    
#     if request.method == 'POST':
#         form = CreateProjectBodyFrom(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('projectBodyList')
#     context = {'form':form,}
#     return render(request, 'myAdmin/createProject.html', context)

@login_required(login_url='login')
def deleteProjectBody(request, pk):
    project_body = get_object_or_404(projectBody, id=pk)
    if request.method == 'POST':
        project_body.delete()
        return redirect('projectBodyList')
    context = {'project_body': project_body}
    return render(request, 'myAdmin/confirmDelete.html', context)


class createProject(CreateView):
    model = project
    form_class = CreateProjectForm
    template_name = 'myAdmin/createProject.html'
    success_url = reverse_lazy('adminProjectList')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class editProject(UpdateView):
    model = project
    form_class = CreateProjectForm
    success_url = reverse_lazy('adminProjectList')
    # fields = ['title', 'slug', 'projectLogo', 'frontPageImage', 'overview', 'status', 'category', 'tags', ]
    template_name = 'myAdmin/createProject.html'    
    
class deleteProject(DeleteView):
    model = project
    success_url = reverse_lazy('adminProjectList')
    template_name = 'myAdmin/confirmDelete.html'
    
    
# S_K_I_L_L_S___V_I_E_W

class addFrontEndSkills(CreateView):
    model = frontEndSkills
    fields = ['name', 'slug', 'description']
    success_url = reverse_lazy('toolsEdit')
    template_name = 'myAdmin/addSkills.html'

    def form_valid(self, form):
        # Additional processing of the form, if necessary
        return super().form_valid(form)
    
class editFrontEndSkills(UpdateView):
    model = frontEndSkills
    fields = ['name', 'slug', 'description']
    success_url = reverse_lazy('toolsEdit')
    template_name =  'myAdmin/addSkills.html'
    
    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     return self.model.objects.get(pk=pk)

class deleteFrontEndSkills(DeleteView):
    model = frontEndSkills
    success_url = reverse_lazy('toolsEdit')
    template_name = 'myAdmin/confirmDelete.html'
    
    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     return self.model.objects.get(pk=pk)



class addBackEndSkills(CreateView):
    model = backEndSkills
    fields = ['name', 'slug', 'description']
    success_url = reverse_lazy('toolsEdit')
    template_name = 'myAdmin/addSkills.html'

    def form_valid(self, form):
        # Additional processing of the form, if necessary
        return super().form_valid(form)
    
class editBackEndSkills(UpdateView):
    model = backEndSkills
    fields = ['name', 'slug', 'description']
    success_url = reverse_lazy('toolsEdit')
    template_name =  'myAdmin/addSkills.html'
    
class deleteBackEndSkills(DeleteView):
    model = backEndSkills
    success_url = reverse_lazy('toolsEdit')
    template_name = 'myAdmin/confirmDelete.html'
    
    

class addFrameWorksSkills(CreateView):
    model = frameWorksSkills
    fields = ['name', 'slug', 'description']
    success_url = reverse_lazy('toolsEdit')
    template_name = 'myAdmin/addSkills.html'

    def form_valid(self, form):
        # Additional processing of the form, if necessary
        return super().form_valid(form)
    
class editFrameWorksSkills(UpdateView):
    model = frameWorksSkills
    fields = ['name', 'slug', 'description']
    success_url = reverse_lazy('toolsEdit')
    template_name =  'myAdmin/addSkills.html'
    
class deleteFrameWorksSkills(DeleteView):
    model = frameWorksSkills
    success_url = reverse_lazy('toolsEdit')
    template_name = 'myAdmin/confirmDelete.html'
    
    
@login_required(login_url='login')
def toolsEdit(request):
    frontSkills = frontEndSkills.objects.all()
    backSkills = backEndSkills.objects.all()
    frames = frameWorksSkills.objects.all()
    
    context = {'frontSkills':frontSkills,
               'backSkills':backSkills,
               'frames':frames,}
    return render(request, 'myAdmin/tools.html', context)


# MESSAGE VIEW FUNCTIONS
@login_required(login_url='login')
def inboxPage(request):
    page_name = 'inbox'
    inbox = message.objects.all().order_by('is_read')
    months = message.objects.all().annotate(month=TruncMonth('created')).values('month').distinct().order_by('-month')

    context = {'inbox':inbox,
               'months':months,
               'page_name':page_name}
    return render(request, 'myAdmin/message/inbox.html', context)

@login_required(login_url='login')
def inboxPageFilter(request, year, month):
    page='inboxFilter'
    selected_month = datetime.strptime(f'{year}-{month}', '%Y-%m')
    view = "project_list_by_month"
    inbox = message.objects.filter(created__year=year, created__month=month).order_by('-created')    
    context = {'view' : view,
               'selected_month': selected_month,
               'inbox': inbox,
               'year': year,
               'month': month,
               'page': page,
    }
    return render(request, 'myAdmin/message/inbox.html', context)

@login_required(login_url='login')
def messageView(request, message_id ):
    page_name = 'message'
    message_object = get_object_or_404(message, id=message_id)
    message_object.is_read=True
    message_object.save()
    context = {'message_object' : message_object,
               'page_name':page_name}
    return render(request, 'myAdmin/message/messageView.html', context)

# class deleteMessage(DeleteView):
#     model = message
#     success_url = reverse_lazy('inbox')
#     template_name = 'myAdmin/confirmDelete.html'
    
    
@login_required(login_url='login')
def deleteMessage(request, message_id):
    message_body = get_object_or_404(message, id=message_id)
    if request.method == 'POST':
        message_body.delete()
        return redirect('adminHomePage')
    context = {'message_body': message_body}
    return render(request, 'myAdmin/confirmDelete.html', context)

def logoutUser(request):
    logout(request)
    return redirect('portfolioPage')