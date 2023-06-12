from django import forms
from django.forms import ModelForm
from adminManage.models import message

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder':'Username',})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder':'Password',})

class MessageForm(ModelForm):
    class Meta:
        model = message
        fields = ['name', 'subject', 'email', 'body']
        
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'formHolder', 'placeholder':'Name',})
        self.fields['subject'].widget.attrs.update({'class': 'formHolder', 'placeholder':'Subject',})
        self.fields['email'].widget.attrs.update({'class': 'formHolder',  'placeholder':'Email',})
        self.fields['body'].widget.attrs.update({'class': 'formHolder',})
  
# class CreateProjectForm(ModelForm):
#     class Meta:
#         model = project
#         fields = ['title', 'slug', 'projectLogo', 'frontPageImage', 'overview', 'status', 'category', 'tags', ]
        
#     def __init__(self, *args, **kwargs):
#         super(CreateProjectForm, self).__init__(*args, **kwargs)
#         self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder':'title',})
#         self.fields['slug'].widget.attrs.update({'class': 'form-control', 'placeholder':'slug',})
#         self.fields['projectLogo'].widget.attrs.update({'class': 'form-control', 'placeholder':'projectLogo',})
#         self.fields['frontPageImage'].widget.attrs.update({'class': 'form-control', 'placeholder':'frontPageImage',})
#         self.fields['overview'].widget.attrs.update({'class': 'form-control', 'placeholder':'overview',})
#         self.fields['publish'].widget.attrs.update({'class': 'form-control', 'placeholder':'publish',})
#         self.fields['status'].widget.attrs.update({'class': 'form-control', 'placeholder':'status',})
#         self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder':'category',})
#         self.fields['tags'].widget.attrs.update({'class': 'form-control', 'placeholder':'tags',})
        
        
# class CreateProjectBody(ModelForm):
#     class Meta:
#         model = projectBody
#         fields = ['project', 'title', 'slug', 'body', 'image', 'active',]
        
#     def __init__(self, *args, **kwargs):
#         super(CreateProjectBody, self).__init__(*args, **kwargs)
#         self.fields['project'].widget.attrs.update({'class': 'form-control', 'placeholder':'project',})
#         self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder':'title',})
#         self.fields['slug'].widget.attrs.update({'class': 'form-control', 'placeholder':'slug',})
#         self.fields['body'].widget.attrs.update({'class': 'form-control', 'placeholder':'body',})
#         self.fields['image'].widget.attrs.update({'class': 'form-control', 'placeholder':'image',})
#         self.fields['active'].widget.attrs.update({'class': 'form-control', 'placeholder':'active',})


