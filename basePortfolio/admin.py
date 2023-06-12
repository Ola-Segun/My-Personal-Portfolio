from django.contrib import admin
from .models import project, projectBody, Category
# Register your models here.



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(project)
class projectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created',)
    prepopulated_fields = {'slug': ('title',)}
    
@admin.register(projectBody)
class projectBodyAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'created')
    prepopulated_fields = {'slug': ('title',)}

