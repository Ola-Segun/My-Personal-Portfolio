from django.db import models
import uuid
from django.conf import settings
from uuid import UUID
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    
    profile_picture = models.ImageField(upload_to = 'users/%Y/%m/%d/',
                                        blank=True)

    def __str__(self):
        return f'Profile for {self.user.username}'

class frontEndSkills(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    
class backEndSkills(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)


    
class frameWorksSkills(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)



class message(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, null=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.name
    
    
