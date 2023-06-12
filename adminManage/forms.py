from django import forms
from django.forms import ModelForm
from basePortfolio.models import project, projectBody
from.models import  frontEndSkills, backEndSkills, frameWorksSkills, Profile
from . import models

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'profile_picture',]

      
class CreateProjectForm(ModelForm):
    class Meta:
        model = project
        fields = ['title', 'slug', 'projectLogo', 'frontPageImage', 'overview', 'status', 'category', 'tags', ]
        # widgets = {'slug': forms.HiddenInput(),}

    def __init__(self, *args, **kwargs):
        super(CreateProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder':'title',})
        self.fields['slug'].widget.attrs.update({'class': 'form-control', 'placeholder':'slug',})
        self.fields['projectLogo'].widget.attrs.update({'class': 'form-control', 'placeholder':'projectLogo',})
        self.fields['frontPageImage'].widget.attrs.update({'class': 'form-control', 'placeholder':'frontPageImage',})
        self.fields['overview'].widget.attrs.update({'class': 'form-control', 'placeholder':'overview',})
        self.fields['status'].widget.attrs.update({'class': 'form-control', 'placeholder':'status',})
        self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder':'category',})
        self.fields['tags'].widget.attrs.update({'class': 'form-control', 'placeholder':'tags',})
        
        
class CreateProjectBodyFrom(ModelForm):
    class Meta:
        model = projectBody
        fields = ['project', 'title', 'slug', 'body', 'image', 'active',]
        
    def __init__(self, *args, **kwargs):
        super(CreateProjectBodyFrom, self).__init__(*args, **kwargs)
        self.fields['project'].widget.attrs.update({'class': 'form-control', 'placeholder':'project',})
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder':'title',})
        self.fields['slug'].widget.attrs.update({'class': 'form-control', 'placeholder':'slug',})
        self.fields['body'].widget.attrs.update({'class': 'form-control', 'placeholder':'body',})
        self.fields['image'].widget.attrs.update({'class': 'form-control', 'placeholder':'image',})
        self.fields['active'].widget.attrs.update({'class': 'form-control', 'placeholder':'active',})



class frontEndSkillsForm(ModelForm):
    class Meta:
        model = frontEndSkills
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(CreateProjectForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder':'name',})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder':'description',})

class backEndSkillsForm(ModelForm):
    class Meta:
        model = backEndSkills
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(CreateProjectForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder':'name',})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder':'description',})


class frameWorkSkillsForm(ModelForm):
    class Meta:
        model = frameWorksSkills
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(CreateProjectForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder':'name',})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder':'description',})
