from django.contrib import admin
from .models import Adminmessage, frameWorksSkills, frontEndSkills, backEndSkills, Profile

# Register your models here.

@admin.register(Profile)
class profile(admin.ModelAdmin):
    list_display = ('user', 'profile_picture')



@admin.register(frontEndSkills)
class frontEndSkillsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

    
@admin.register(backEndSkills)
class backEndSkillsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

    
@admin.register(frameWorksSkills)
class frameWorksAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Adminmessage)
class messageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')
    prepopulated_fields = {'slug': ('subject',)}
