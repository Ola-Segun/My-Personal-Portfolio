from django.db import models
from django.utils import timezone
import uuid
from uuid import UUID
from django.utils.text import slugify
from taggit.managers import TaggableManager

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().filter(status='published')



    

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    
    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.title

class project(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    objects = models.Manager()
    title = models.CharField(max_length=250)
    slug = models.SlugField(null=True)
    projectLogo = models.ImageField(upload_to='images/', blank=True)
    frontPageImage = models.ImageField(upload_to='images/', blank=True)
    overview = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True, null = True)
    published = PublishedManager() # Our custom manager.
    status = models.CharField(max_length=10,
                            choices=STATUS_CHOICES,
                            default='draft')
    category = models.ForeignKey(Category, related_name='tag',
                                 on_delete=models.SET_NULL, null=True, blank=True)
    tags = TaggableManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(project, self).save(*args, **kwargs)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return self.title
    
class projectBody(models.Model):
    
    project = models.ForeignKey(project,
                             on_delete=models.CASCADE,
                             related_name='comments',
                             serialize=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True)
    body = models.TextField()
    image = models.ImageField(upload_to='project/pk', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return self.title
    
    
# class message(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     subject = models.CharField(max_length=200)
#     slug = models.SlugField(max_length=250, null=True)
#     body = models.TextField()
#     is_read = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)
#     id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
#     def __str__(self):
#         return self.name