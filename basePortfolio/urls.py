from django.urls import path
from . views import portfolioPage, projectPage

urlpatterns = [
    path('', portfolioPage, name='portfolioPage'),
    path('project/<slug:slug>/', projectPage, name='projectPage'),
]