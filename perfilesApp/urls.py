from unicodedata import name
from django.urls import path

from django.contrib.auth import views as auth_views

from perfilesApp.views import ShowProfilePageView, EditProfilePageView, CreateProfilePageView


urlpatterns = [
    
    path('<int:pk>/perfilesApp/profile/',ShowProfilePageView.as_view(),name='show_profile_page'),
    path('<int:pk>/perfilesApp/edit_profile_page/',EditProfilePageView.as_view(),name='edit_profile_page'),
    path('perfilesApp/create_profile_page/',CreateProfilePageView.as_view(),name='create_profile_page'),
    
] 