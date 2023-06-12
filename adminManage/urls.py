from django.urls import path
from .import views

urlpatterns = [
    path('', views.adminHomePage, name='adminHomePage'),
    path('inbox/', views.inboxPage, name='inbox'),
    path('message/<uuid:message_id>/', views.messageView, name='messageView'),
    path('deleteMessage/<uuid:message_id>/', views.deleteMessage, name='deleteMessage'),
    

    path('inbox/<int:year>/<int:month>/', views.inboxPageFilter, name='inboxPageFilter'),
    path('adminProjectList/', views.adminProjectList, name='adminProjectList'),
    path('createProject/', views.createProject.as_view(), name='createProject'),
    path('createProject/<int:pk>/', views.editProject.as_view(), name='editProject'),
    path('deleteProject/<int:pk>/', views.deleteProject.as_view(), name='deleteProject'),
    
    path('createProjectBody/', views.createProjectBody.as_view(), name='createProjectBody'),
    path('projectBodyList/', views.projectBodyList, name='projectBodyList'),
    path('editProjectBody/<int:pk>/', views.editProjectBody.as_view(), name='editProjectBody'),
    path('deleteProjectBody/<int:pk>/', views.deleteProjectBody, name='deleteProjectBody'),

    path('toolsEdit/', views.toolsEdit, name='toolsEdit'),
    
    path('addFrontEndSkills/', views.addFrontEndSkills.as_view(), name='addFrontEndSkills'),
    path('editFrontEndSkills/<slug:slug>', views.editFrontEndSkills.as_view(), name='editFrontEndSkills'),
    path('deleteFrontEndSkills/<slug:slug>', views.deleteFrontEndSkills.as_view(), name='deleteFrontEndSkills'),
    
    path('addBackEndSkills/', views.addBackEndSkills.as_view(), name='addBackEndSkills'),
    path('editBackEndSkills/<slug:slug>', views.editBackEndSkills.as_view(), name='editBackEndSkills'),
    path('deleteBackEndSkills/<slug:slug>', views.deleteBackEndSkills.as_view(), name='deleteBackEndSkills'),
    
    path('addFrameWorksSkills/', views.addFrameWorksSkills.as_view(), name='addFrameWorksSkills'),
    path('editFrameWorksSkills/<slug:slug>', views.editFrameWorksSkills.as_view(), name='editFrameWorksSkills'),
    path('deleteFrameWorksSkills/<slug:slug>', views.deleteFrameWorksSkills.as_view(), name='deleteFrameWorksSkills'),
    
    path('logout/', views.logoutUser, name='logoutUser'),

]