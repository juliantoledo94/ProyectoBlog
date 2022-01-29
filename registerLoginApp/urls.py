from unicodedata import name
from django.urls import path
from .views import  UserRegisterView,UserEditView
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('registerLogionApp/register/',UserRegisterView.as_view(),name='register'),
    path('registerLogionApp/edit_profile/',UserEditView.as_view(),name='edit_profile'),
    #path('registerLogionApp/password/',auth_views.PasswordChangeView.as_view()),
    
    
    
] 